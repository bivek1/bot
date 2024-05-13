import cv2
import pickle
import pytesseract

# Load the trained Random Forest Classifier from the .pkl file
with open('/Users/bibekdhakal/Python/Bot/Mathematical-Handwriting-recognition/Model/random_forest_classifier.pkl', 'rb') as file:
    classifier = pickle.load(file)

# Function to preprocess the input image
def preprocess_image(img):
    # Implement any necessary preprocessing steps here
    # (e.g., resizing, normalization, etc.)
    # Ensure that the preprocessed image has the correct shape and format expected by the classifier
    # Example:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    img = cv2.resize(img, (28, 28))  # Resize to match the input size expected by the classifier
    img = img.flatten()  # Flatten the image into a 1D array
    return img

# Function to predict digit using the loaded classifier
def predict_digit(img):
    # Preprocess the input image
    img = preprocess_image(img)
    # Perform prediction using the classifier
    prediction = classifier.predict([img])
    return prediction[0]  # Return the predicted digit

# Function to extract digits from the input image and predict using the loaded classifier
def extract_and_predict_digits(image_path):
    # Read the input image
    img = cv2.imread(image_path)
    
    cv2.imshow("Enhanced Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.destroyAllWindows()
    text = pytesseract.image_to_string(img)
    print(text)
    nume = ''.join(x for x in text if x.isdigit())
    print(nume)

# Example usage
image_path = '/Users/bibekdhakal/Python/Bot/rgb_image.jpg'
extract_and_predict_digits(image_path)
