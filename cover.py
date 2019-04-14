# -*- coding: utf-8 -*-

import epd as epd7in5
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import sys
import os
import random
# print "This is the name of the script: ", sys.argv[0]

# if len(sys.argv) > 1:
#     pic = sys.argv[1]
#     if len(sys.argv) > 2 and sys.argv[2] == 'white':
#         fill = 255
#     else:
#         fill = 0
# else:
#     pic = '/home/pi/cover.bmp'


def display_cover(cover):
        covers_path = '/home/pi/covers'
        covers = filter(lambda x: ('.bmp' in x), os.listdir(covers_path))
        if run_script == True:
            if sys.argv[1] == 'random':
                pic_path = random.choice(covers)
            else:
                pic_path = sys.argv[1]
        else:
            if cover == 'random':
                pic_path = random.choice(covers)
            else:
                pic_path = cover


        pic = '{dir_path}/{pic_path}'.format(dir_path=covers_path, pic_path=pic_path)


        try:
            epd = epd7in5.EPD()
            epd.init()
            # print("Clear")
            # epd.Clear(0xFF)

            print("Drawing")
            # print("read bmp file on window")
            Himage2 = Image.new('1', (epd7in5.EPD_HEIGHT, epd7in5.EPD_WIDTH), 0)  # 255: clear the frame
            bmp = Image.open(pic)
            # Himage2.paste(bmp, (50,10))
            Himage2.paste(bmp)

            # write to display
            epd.display(epd.getbuffer(Himage2))

            print('sleeping')
            epd.sleep()

        except:
            print('traceback.format_exc():\n%s', traceback.format_exc())
            if run_script == True:
                exit()

if len(sys.argv) > 1:
    run_script = True
    display_cover()
else:
    run_script = False
