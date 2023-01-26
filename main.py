import pytesseract
from PIL import Image

def extract_text_from_image(image_path):
    # Open image and convert to grayscale
    image = Image.open(image_path).convert('L')

    # Use Tesseract to extract text from image
    text = pytesseract.image_to_string(image)

    return text

# Example usage
image_path = "example.jpg"
text = extract_text_from_image(image_path)
print(text)
