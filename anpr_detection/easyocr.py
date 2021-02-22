# install using python -m pip install easyocr

import easyocr

# create reader
reader = easyocr.Reader(['en'])

# read characters 
img = "https://i.stack.imgur.com/2Kzu8.png"

characters = reader.readtext(img, detail=0)
print(characters)
# ['ZG', '8524AF']