from rembg import remove
from PIL import Image

class foto:
    def fotoremove(inputfileimage, outputfileimage):
        input_path = inputfileimage
        output_path = outputfileimage
        input1 = Image.open(input_path)
        output = remove(input1)
        output.save(output_path)
