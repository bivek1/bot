import time

import requests
from PIL import Image
from io import BytesIO
import pytesseract
import cv2
import numpy as np

def getCode(image_path):
    nume = 0
    try:
      
        img = Image.open(image_path)
        print(img)
        
        
        if img.mode == 'RGBA':

            img = img.convert('RGB')

          
            # Get the width and height of the image
            width, height = img.size

            button_width = 600  # Adjust this value as needed
            button_height = 100  # Adjust this value as needed

            # Calculate the coordinates for the bottom center position of the image
            button_center_x = width // 2
            button_bottom_y = height

            # Calculate the coordinates for cropping around the bottom center position
            left = button_center_x - button_width // 2
            upper = button_bottom_y - button_height
            right = button_center_x + button_width // 2
            lower = button_bottom_y

            # Crop the image using the calculated coordinates
            cropped_img = img.crop((left, upper, right, lower))


            # Save or display the cropped image
            cropped_img.save("/Users/bibekdhakal/Python/Bot/cropped_image.jpg")

            img = cv2.imread("/Users/bibekdhakal/Python/Bot/cropped_image.jpg")
            # Convert image to grayscale
            
            # img = cv2.imread(file)
            gamma = 1.4
            exposure_corrected = np.clip(img ** gamma, 0, 255).astype(np.uint8)

            # Enhance the shadows using histogram equalization
            gray = cv2.cvtColor(exposure_corrected, cv2.COLOR_BGR2GRAY)
            equalized = cv2.equalizeHist(gray)

            # Stack the equalized image with the original exposure-corrected image
            enhanced_img = cv2.merge((equalized, equalized, equalized))

            # Display the enhanced image
            cv2.imshow("Enhanced Image", enhanced_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.destroyAllWindows()
            text = pytesseract.image_to_string(enhanced_img)
            nume = ''.join(x for x in text if x.isdigit())
            print(nume)
           
        print("Extracted Numeric Values:", nume)
        
        return nume
    except Exception as e:
        print("An error occurred:", str(e))
        return None
    
# code = getCode('/Users/bibekdhakal/Python/Bot/div_screenshot.png')
# print(code)