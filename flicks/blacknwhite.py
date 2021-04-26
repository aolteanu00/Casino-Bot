

from PIL import Image
def black_and_white(input_image_path, output_image_path):
   color_image = Image.open(input_image_path)
   bw = color_image.convert('L')
   bw.save(output_image_path)
if __name__ == '__main__':
    black_and_white('screenshot2.jpg','bw3_screenshot.jpg')
    
