import sys
from PIL import Image
import base64

if (len(sys.argv) != 2):
    print 'python base64.py filename'
    quit()

outfile = sys.argv[1] + "_16x16.png"

Image.open(sys.argv[1]).resize((16,16)).save(outfile)

with open(outfile, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    print encoded_string
