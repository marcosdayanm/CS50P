import sys
from PIL import Image, ImageOps


def check_ext(inp, out):
    if out[-4:] not in ['.png', '.jpg'] and out[-5:] != '.jpeg':
        sys.exit('Invalid output')
    elif inp[-4:] != out[-4:]:
        sys.exit('Input and output have different extensions')

    try:
        with Image.open(inp) as img:
            pass
        img.close()
    except FileNotFoundError:
        sys.exit('Input does not exist')


if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

inp, out = sys.argv[1], sys.argv[2]

check_ext(inp, out)

with Image.open(inp) as img1:
    img1 = ImageOps.fit(img1, (600,600), method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    shirt = Image.open("shirt.png")

    img1.paste(shirt, (0,0), shirt)
    img1.save(out)

