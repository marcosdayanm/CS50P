# Expect two command line arguments of image files
import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:   # iterating over command-line arguments slicing it
    image = Image.open(arg)  # pasarle el arg a ina función de Image para abrirlas con la librería
    images.append(image)

# La librería me abre, cierra, y guarda la imagen con solo peste comando
images[0].save(
    'salto.gif', save_all=True, append_images=[images[1], images[2], images[3], images[4], images[5], images[6], images[7c]], duration=200, loop=0
)