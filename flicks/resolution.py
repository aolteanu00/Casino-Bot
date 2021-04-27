from PIL import Image

# Open the image by specifying the image path.
image_path = "test3.png"
image_file = Image.open(image_path)

# the default
image_file.save("test4.png", dpi=(500,500))
