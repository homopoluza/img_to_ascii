import cv2
import PIL.Image
from  img_to_ascii import resize_image, image_to_ascii

def main():
    cap = cv2.VideoCapture(0)
    _, imageCV = cap.read()
    cap.release() 
    imageCV = cv2.cvtColor(imageCV, cv2.COLOR_BGR2RGB)
    imagePIL = PIL.Image.fromarray(imageCV)
    resized_image = resize_image(imagePIL, 200)
    grayscale_image = resized_image.convert("L")
    ascii_image = image_to_ascii(grayscale_image, 200)
    print(ascii_image)

while True:
    main() 
