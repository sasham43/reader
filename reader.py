# -*- coding: utf-8 -*-

import epd as epd7in5
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import sys
import pprint
import json
from os.path import expanduser
import vs

home = expanduser("~")

file = '{home}/reader.json'.format(home=home)

file_data = open(file).read()
data = json.loads(file_data)
print('current page:', data['current_page'])
current_page = data['current_page']
current_book = data['current_book']

line_height_base = 25 # this isn't great

epd = epd7in5.EPD()

try:
    book_text = open('{home}/books/{current_book}'.format(home=home, current_book=current_book)).read()
    pages = vs.split_into_rows(book_text)
    show_page(pages[current_page])
    key = input('< >')
    print(key)
except:
    print('traceback.format_exc():\n%s', traceback.format_exc())
    exit()



def show_page(page):
    epd.init()
    Himage = Image.new('1', (epd7in5.EPD_HEIGHT, epd7in5.EPD_WIDTH), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    line_height = 0
    for line in page:
        draw.text((10, line_height), line, font = font24, fill = 0)
        line_height = line_height_base + line_height
    epd.display(epd.getbuffer(Himage))
    time.sleep(1)
    epd.sleep()
