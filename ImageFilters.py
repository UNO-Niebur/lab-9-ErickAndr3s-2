# Lab 9 – Image Processing
# Name:Erick Andres
# Date:4/5/2026
# Assignment:Lab 9

from PIL import Image


def swapGreenBlue(img):
    """Swap the green and blue values for every pixel in the image."""
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue, alpha = pixels[x,y]
            pixels[x,y] = (red, blue, green, alpha)
    img.save("swapGB.png")

    # TODO: Loop through every pixel and swap green and blue values



def darken(img, amount):
    """Darken the image by reducing RGB values by the given amount."""
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue, alpha = pixels [x, y]

            red = max(0, red - amount)
            green = max(0, green - amount)
            blue = max(0, blue - amount)

            pixels[x, y] = (red, green, blue, alpha)


    # TODO: Loop through every pixel and reduce RGB values by amount
    # Make sure values do not go below 0

    img.save("darkImg.png")


def bwFilter(img):
    """Example function: converts image to grayscale."""
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue, alpha = pixels[x, y]
            avg = (red + green + blue) // 3
            pixels[x, y] = (avg, avg, avg, alpha)

    img.save("bwImg.png" )


def main():
    # Open the image file
    myImg = Image.open("durango.png").convert("RGBA")

    # Example (already completed)
    # bwFilter(myImg)

    # Uncomment each function as you complete it
    swapGreenBlue(myImg)
    darken(myImg, 70)


if __name__ == "__main__":
    main()
