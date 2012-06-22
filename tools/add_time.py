import sys
import Image
import ImageFont, ImageDraw, ImageOps
import datetime

filename = sys.argv[1]
im = Image.open(filename)

f = ImageFont.truetype("/Users/reinout/Library/Fonts/nobile_bold.ttf", 80)
txt = Image.new('L', (800,100))
d = ImageDraw.Draw(txt)
date_string = str(datetime.datetime.now().strftime('%H:%M'))
#date_string = '10:21'
d.text( (0, 0), date_string,  font=f, fill=255)
w = txt.rotate(0,  expand=2)

im.paste( ImageOps.colorize(w, (0,0,0), (30,30,30)), (1200, 800),  w)

out_filename = date_string.replace(':', '_') + '.png'
im.save(out_filename, "png")
