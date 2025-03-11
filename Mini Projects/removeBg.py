'''
# Remove Background from Image using rembg

Requirements : python: >=3.10, <3.14

Installation:
pip install rembg # for library
pip install "rembg[cli]" # for library + cli

pip install rembg[cpu] # for library
pip install "rembg[cpu,cli]" # for library + cli

pip install "rembg[gpu]" # for library
pip install "rembg[gpu,cli]" # for library + cli    

pip install onnxruntime

'''
from rembg import remove
from PIL import Image

input_path = "mango.jpg"
output_path = "output.png"

def remove_bg(input_path, output_path):
    try:
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
        
        print(f"Background removed and saved as {output_path}")
        output_image.show()
    except Exception as e:
        print(f"Error: {e}")

remove_bg(input_path, output_path)
