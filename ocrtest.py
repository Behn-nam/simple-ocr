from PIL import Image
import pytesseract
from docx import Document

# Correct path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Image file
image_path = r"C:\Users\Behnam\Desktop\test\letter.jpg"
img = Image.open(image_path)

# Extract Farsi text
text = pytesseract.image_to_string(img, lang="fas")

doc = Document()
doc.add_paragraph(text)

doc.save(r"C:\Users\Behnam\Desktop\test\output.docx")

print("farsi done!!")