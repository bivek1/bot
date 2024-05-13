from PIL import Image
import time
def extract_black_region(image_path):
    img = Image.open(image_path)
    width, height = img.size
    black_region = []

    # Iterate over each pixel
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            # Check if RGB values are all zeros (black)
            if pixel == (0, 0, 0):
                black_region.append((x, y))

    # Find bounding box coordinates of black region
    min_x = min(black_region, key=lambda item: item[0])[0]
    max_x = max(black_region, key=lambda item: item[0])[0]
    min_y = min(black_region, key=lambda item: item[1])[1]
    max_y = max(black_region, key=lambda item: item[1])[1]

    # Crop the image to the bounding box
    black_box = img.crop((min_x, min_y, max_x, max_y))
    black_box.show()  # Display the cropped black region
    black_box.save('/Users/bibekdhakal/Python/Bot/rgb_image.jpg')
  
    


