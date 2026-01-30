from PIL import Image
import os

def convert_image(input_file, output_format, output_dir):
    base = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(output_dir, base + "." + output_format)

    img = Image.open(input_file)

    if output_format.lower() in ["jpg", "jpeg", "pdf"]:
        img = img.convert("RGB")

    img.save(output_file)
    return output_file
