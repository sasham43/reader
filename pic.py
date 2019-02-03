# -*- coding: utf-8 -*-

import epd as epd7in5
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import sys
print "This is the name of the script: ", sys.argv[0]

if len(sys.argv) > 1:
    pic = sys.argv[1]
else:
    pic = '/home/pi/cover.bmp'

try:
    epd = epd7in5.EPD()
    epd.init()
    print("Clear")
    epd.Clear(0xFF)

    print("Drawing")
    # print("read bmp file on window")
    Himage2 = Image.new('1', (epd7in5.EPD_HEIGHT, epd7in5.EPD_WIDTH), 255)  # 255: clear the frame
    bmp = Image.open(pic)
    # Himage2.paste(bmp, (50,10))
    Himage2.paste(bmp)

    # write to display
    epd.display(epd.getbuffer(Himage2))

    print('sleeping')
    epd.sleep()

except:
    print('traceback.format_exc():\n%s', traceback.format_exc())
    exit()
