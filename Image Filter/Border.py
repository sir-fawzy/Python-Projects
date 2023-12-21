from PIL import Image
from image_converter import ListToImage, ImageToList

def main():
  # Open the image.
  dog_img = Image.open("dog.png")
  pixels = ImageToList(dog_img)

  # Apply the border filter.
  filtered_pixels = add_border(pixels)

  # Save an image
  filtered_image = ListToImage(filtered_pixels)
  filtered_image.save("dog_border.png")
  return


def add_border(pixels):
  new_pixels = []
  for row in range(len(pixels)):
    new_row = []
    for col in range(len(pixels[row])):
      r, g, b = pixels[row][col]
      if row <= 10 or col <= 10 or len(pixels)-(row+1) <= 10 or len(pixels[row])-(col+1) <= 10 :
        new_pixel = (0, 0, 0)
        new_row.append(new_pixel)
      else:
        new_row.append((r, g, b))
    new_pixels.append(new_row)
  return new_pixels
        
  # Convert to have a black border.


main()
