import numpy as np
from scipy.spatial import procrustes
from scipy.linalg import orthogonal_procrustes
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D
import argparse
import dlib
import cv2
from collections import OrderedDict

predictor_path = "drowsy_driver_detector/shape_predictor_68_face_landmarks.dat"
faces_folder_path1 = "image/jeff.jpg"
faces_folder_path2 = "image/jeff2.jpg"

FACIAL_LANDMARKS_IDXS = OrderedDict([
    ("mouth", (48,68)),
    ("right_eyebrow", (17, 22)),
    ("left_eyebrow", (22, 27)),
    ("right_eye", (36, 42)),
    ("left_eye", (42, 48)),
    ("nose", (27, 36)),
    ("jaw", (0, 17))
])

def plot_landmarks(shape, size):
    """Plot landmarks on a graph
    Args:
        shape: (68,2) numpy array reporesents facila landmarks
        size: list of image height, width, channel
    Returns:
        None
    """
    [x, y] = np.shape(shape)
    #Need to rotate (x,y) 180 degree, but not a high priority...
    #r = Affine2D().rotate_deg(180)

    for (x,y) in shape:
        plt.scatter(x,y, c='red')

    plt.show()

def rect_to_bb(rect):
    """Take a bounding predicted by dlib and convert it to the format (x, y, w, h)
    Args:
        rect:
    Returns:
        OpenCV style (x, y, width, height)
    """
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y

    return (x, y, w, h)


def shape_to_np(shape, dtype="int"):
    """Take a shape object and convert it to numpy array
    Args:
        shape: an object returned by dlib face landmark detector containing the 68 (x, y)-coordinates of the facial landmark regions
        dtype: int
    Returns:
        coords: (68,2) numpy array
    """
    coords = np.zeros((68, 2), dtype=dtype)

    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)

    return coords

def get_detections(detector, img):
    """
    Args:
        detector:
        img:
    Returns:
        dets
    """
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dets = detector(img, 1)

    return dets

def get_shape(dets, predictor, img):
    """
    Args:
        dets:
    Returns:
    """
    for i, rect in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            i, rect.left(), rect.top(), rect.right(), rect.bottom()))

        bx, by, bw, bh = rect_to_bb(rect)
        cv2.rectangle(img, (bx, by), (bx+bw, by+bh), (0, 255, 0), 1)
        # http://dlib.net/python/index.html#dlib.shape_predictor
        #shape = predictor(gray_img, rect)
        shape = predictor(img, rect)
        print(shape.num_parts)
        shape = shape_to_np(shape)
        #rect = np.matrix( [[p.x, p.y] for p in predictor(gray_img, rects[0]).parts()] )
        #print(rect)

        # plot facial landmarks on the image
        for (x, y) in shape:
            cv2.circle(img, (x, y), 1, (0, 0, 255), -1)
        return shape


def procrustes_analysys(A, B):
    """Procrustes analysis
    Basic algorithm is
        1. Recenter the points based on their mean: compute a mean and subtract it from every points in shape
        2. Normalize
        3. Rotate one of the shapes and find MSE
    Args:
        A:
        B:
    Returns:
    """
    h_A, w_A = A.shape
    h_B, w_B = B.shape

    # compute mean of each A and B
    Amu = np.mean(A, axis=0)
    Bmu = np.mean(B, axis=0)

    # subtract a mean
    A_base = A - Amu
    B_base = B - Bmu

    # normalize
    ssum_A = (A_base**2).sum()
    ssum_B = (B_base**2).sum()

    norm_A = np.sqrt(ssum_A)
    norm_B = np.sqrt(ssum_B)

    normalized_A = A_base / norm_A
    normalized_B = B_base / norm_B

    if (w_B < w_A):
        normalized_B = np.concatenate((normalized_B, np.zeros(h_A, w_A - w_B)), 0)

    A = np.dot(normalized_A.T, normalized_B)

    # SVD
    #u, s, vh = np.linalg.svd(np.dot(normalized_A, normalized_B.T))
    #u, s, vh = np.linalg.svd(np.dot(normalized_A, normalized_B.T))
    u, s, vh = np.linalg.svd(A, full_matrices=False)
    v = vh.T
    T = np.dot(v, u.T)
    #R = np.dot(vh.T, u.T)

    #scale = s.sum() * norm_A / norm_B
    scale = norm_A / norm_B
    #Z = norm_B * s.sum() * np.dot(R, normalized_A) + Bmu

    return T, scale


"""
def procrustes_analysys2(points1, points2):
    points1 = points1.astype(np.float64)
    points2 = points2.astype(np.float64)
    c1 = np.mean(points1, axis=0)
    c2 = np.mean(points2, axis=0)
    points1 -= c1
    points2 -= c2
    s1 = np.std(points1)
    s2 = np.std(points2)
    points1 /= s1
    points2 /= s2
    U, S, Vt = np.linalg.svd(np.dot(points1.T, points2))
    R = (U * Vt).T
    print("shape of c2.T is {}".format(c2.T.shape))
    print("shape of R is {}".format(R.shape))
    print("shape of c1.T is {}".format(c1.T.shape))
    print("shape of XXX is {}".format(c2.T - (s2 / s1) * R * c1.T))
    return np.vstack([np.hstack(((s2 / s1) * R,
                                       c2.T - (s2 / s1) * R * c1.T)),
                         np.matrix([0., 0., 1.])])
"""


def warp_images(img, M, dshape):
    output_image = np.zeros(dshape, dtype=img.dtype)
    cv2.warpAffine(img, M, (dshape[1], dshape[0]), dst=output_image, borderMode=cv2.BORDER_TRANSPARENT, flags=cv2.WARP_INVERSE_MAP)
    return output_image


def main():
    # initialize dlib's face detector (HOG-based) and
    # the facial landmark predictor
    # http://dlib.net/python/index.html#dlib.get_frontal_face_detector
    # http://dlib.net/python/index.html#dlib.shape_predictor
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)

    img1 = cv2.imread(faces_folder_path1)
    img2 = cv2.imread(faces_folder_path2)
    imgsize1 = img1.shape
    imgsize2 = img2.shape

    dets1 = get_detections(detector, img1)
    dets2 = get_detections(detector, img2)

    shape1 = get_shape(dets1, predictor, img1)
    shape2 = get_shape(dets2, predictor, img2)

    shapes = [shape1, shape2]

    # plot landmarks to check
    # plot_landmarks(shape1, imgsize1)
    for i, shape in enumerate(shapes):
        [x, y] = np.shape(shape)
        #Need to rotate (x,y) 180 degree, but not a high priority...
        #r = Affine2D().rotate_deg(180)
        """
        plt.figure(i)
        for (x, y) in shape:
            plt.scatter(x,y, c='red')
        plt.show()
        cv2.imshow("Detector", img1)
        cv2.waitKey(0)
        """

    # check rotation and scale using procrustes analysis
    M, scale = procrustes_analysys(shape1, shape2)
    mtx1, mtx2, disparity = procrustes(shape1, shape2)
    R, scale = orthogonal_procrustes(mtx1, mtx2, True)
    #warp_images(img2, M, img1.shape)
    theta = np.rad2deg( np.arccos(M[0][0]) )
    print("theta is {}".format(theta))

    rotation_matrix = cv2.getRotationMatrix2D((img2.shape[1]/2, img2.shape[0]/2), theta, 1)
    dst = cv2.warpAffine(img1, rotation_matrix, (img1.shape[1], img1.shape[0]))
    cv2.imshow('Rotated', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """
    # test plot
    plt.figure(i+1)
    for (x,y ) in shape2:
        plt.scatter(x, y, c='red')
    for (x, y) in mtx1:
        plt.scatter(x, y, c='blue')
    plt.show()
    """

if __name__ == "__main__":
    main()