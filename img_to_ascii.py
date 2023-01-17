from PIL import Image

#ASCII_CHAR = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '^', '`', "'", '.', ' ']
ASCII_CHAR = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]

def resize_image(image, new_width = 100):
    width, height = image.size
    new_hight = int((height / width) * new_width)
    resize_image = image.resize((new_width, new_hight))
    return(resize_image)

def image_to_ascii(grayscale_image, new_width = 100):
    pixels = grayscale_image.getdata()
    ascii_str = ''
    ascii_img = ''
    for pixel in pixels:
        ascii_str = ascii_str + (ASCII_CHAR[int(pixel // 23)]) #3.7 for long list; 23 for short one
    for i in range(0, len(ascii_str), new_width):
        ascii_img = ascii_img + "\n" + ascii_str[i:(i+new_width)]
    with open("ascii_img.txt", "w") as f:
        f.write(ascii_img)
    return(ascii_img)

def main():
    image = Image.open("./img.png")
    resized_image = resize_image(image)
    grayscale_image = resized_image.convert("L")
    ascii_image = image_to_ascii(grayscale_image)
    print(ascii_image)

if __name__ == "__main__":
    main()