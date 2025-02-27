# Automation Project Documentation

This repository contains a range of automated testing and machine learning projects organized into two main categories: Selenium Projects and Machine Learning / AI Projects.

Selenium Projects use Selenium with Python to perform automated testing. Each sub-project is placed in its own folder with its dedicated chromedriver (or appropriate driver) for headless browsing and individual test cases. Machine Learning / AI Projects include various projects covering topics such as data anomaly detection and image recognition. Each project is self-contained and may require different runtime parameters.

Installation:  
First, clone the repository:
git clone https://github.com/sblahut/automation.git cd automation

It is recommended to create and activate a Python virtual environment:
python -m venv env source env/bin/activate # On Windows use: env\Scripts\activate

Then install the required modules:
pip install -r requirements.txt

(Ensure you have a requirements.txt file with the necessary modules.)

Requirements:  
Python 3.9 or above, Pip 19.0 or above, and ensure chromedriver.exe is placed in each Selenium project folder. Additional multi-environment variables may be needed.

Module Download Links:  
Pytest: https://pypi.org/project/pytest/#files  
Requests: https://pypi.org/project/requests/#files  
Times: https://pypi.org/project/times/  
Pip: https://pypi.org/project/pip/#files  
Selenium: https://pypi.org/project/selenium/#files  
Beautiful Soup: https://pypi.org/project/beautifulsoup4/  
Keyboard: https://pypi.org/project/keyboard/  
Pynput: https://pypi.org/project/pynput/  
OpenCV: https://pypi.org/project/opencv-python/  
Numpy: https://pypi.org/project/numpy/  
Cryptography: https://pypi.org/project/cryptography/  
Fernet: https://pypi.org/project/fernet/  
Playsound: https://pypi.org/project/playsound/  
Imutils: https://pypi.org/project/imutils/  
Dlib: https://pypi.org/project/dlib/  
Cmake: https://pypi.org/project/cmake/  
Tensorflow: https://pypi.org/project/tensorflow/  
Pandas: https://pypi.org/project/pandas/  
PIL (Pillow): https://pypi.org/project/Pillow/  
Keras: https://pypi.org/project/Keras/  
Sklearn/Scikit-Learn: https://pypi.org/project/sklearn/ and https://pypi.org/project/scikit-learn/

Projects and How to Start Them:

Selenium-Based Automation Projects:  
For each Selenium project, navigate to its folder where the chromedriver and test cases reside.

AB (Validation Scripts): Navigate to the AB folder, update any user or domain variables, and run:
python test_validation.py

(Or use pytest if tests are structured accordingly.)

ABC (Automation Test Suite): Enter the ABC folder, ensure the chromedriver is configured, then run:
pytest

ASH (Automation Test Suite): Go to the ASH folder, configure necessary environment variables, then execute:
python main_test.py

(The command may differ based on the entry script.)

Geekhive (Automation Test Suite): Enter the Geekhive folder, follow any specific instructions provided, then run:
pytest

Starr (Automation Test Suite): Enter the Starr folder, adjust user/domain parameters as needed, and start with:
python starr_main.py

Machine Learning / AI Projects:  
These projects involve processing data, training models, or running detection scripts.

anomaly_detection (Offset Data Detection / Ghost Detection): Navigate to the anomaly_detection folder, check for adjustable parameters, then run:
python anomaly_detection.py

anpr_detection (Automatic Number Plate Recognition): Enter the anpr_detection folder, verify that your webcam/video/image input is configured, then execute:
python anpr_detection.py

Follow any on-screen prompts for input selection.

drowsy_driver_detector (Drowsy Driver Detector): Go to the drowsy_driver_detector folder, adjust eye-closure time thresholds as needed, then run:
python drowsy_driver_detector.py

An alarm will trigger if drowsiness is detected.

encryption-decryption (Encryption/Decryption Script): Navigate to the encryption-decryption folder, update parameters (file paths, passwords, or CSV inputs), then run:
python encryption_decryption.py --mode encrypt --input file.csv

(Modify command options as necessary.)

facial_detection (Face Detection for Webcam/Video/Image): Enter the facial_detection folder, set up your camera or provide an image/video file, then run:
python facial_detection.py

traffic_sign_detection (Traffic Sign Recognition): Navigate to the traffic_sign_detection folder, confirm that your media input is available, then run:
python traffic_sign_detection.py

Contributors:  
Steven Blahut

For further details or questions, please refer to the project’s issue tracker on GitHub or contact the repository maintainer.









Search

Deep research
