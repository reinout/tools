"""
Simple script to add the current time to a screenshot.

Pass in the filename of the screenshot as an argument and the script will
create a new file (named after the time, in the current directory) with the
time written in the lower right corner.

The location of the time string and the location of the font to use is
hardcoded.

"""
import datetime
import sys

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps


FONT = "/Users/reinout/Library/Fonts/nobile_bold.ttf"
LOCATION_IN_IMAGE = (1200, 800)  # Lower left corner where the text is placed.


def main():
    filename = sys.argv[1]
    image = Image.open(filename)
    font = ImageFont.truetype(FONT, 80)
    txt_image = Image.new('L', (800, 100))
    drawable = ImageDraw.Draw(txt_image)

    date_string = str(datetime.datetime.now().strftime('%H:%M'))
    #date_string = '10:21'

    drawable.text((0, 0), date_string,  font=font, fill=255)
    txt_image = txt_image.rotate(0, expand=2)
    image.paste(ImageOps.colorize(txt_image, (0, 0, 0), (30, 30, 30)),
                LOCATION_IN_IMAGE,
                txt_image)

    out_filename = date_string.replace(':', '_') + '.png'
    image.save(out_filename, "png")
    print("Saved %s" % out_filename)
