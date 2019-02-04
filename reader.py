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
import keyboard

try:
    # Win32
    from msvcrt import getch
except ImportError:
    # UNIX
    def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

home = expanduser("~")

file = '{home}/reader.json'.format(home=home)

file_data = open(file).read()
data = json.loads(file_data)
print('current data:', data)
# current_page = data['current_page']
# current_book = data['current_book']

# fonts
font_base = '/usr/share/fonts/treutype/msttcorefonts/{file}'
font_file = 'Courier_New_Bold.ttf'
font24 = ImageFont.truetype(font_base.format(file=font_file), 24)

line_height_base = 25 # this isn't great

epd = epd7in5.EPD()

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

def update_data():
    # data['current_page'] = page
    # data['current_book'] = book
    with open(file, 'w') as outfile:
        json.dump(data, outfile)

def get_input():
    commands = ['.', ',', 'a', 'q']
    print('< >')
    key = getch()

    print(key)

    if key not in commands:
        print('command not recognized')
        get_input()

    if key == '.':
        data['current_page'] = data['current_page'] + 1
    elif key == ',':
        data['current_page'] = data['current_page'] - 1
    elif key == 'a':
        data['current_book'] = 'asimov.txt'
        data['current_page'] = 0
        print('changing current books', data)
        open_book()
        # pages = get_book_text(current_book)
        # show_page(pages[current_page])
        # get_input(current_page)
    elif key == 'q':
        exit(0)

    if data['current_page'] < 0:
        data['current_page'] = 0
    elif data['current_page'] > len(pages):
        data['current_page'] = len(pages)
    update_data()
    show_page(pages[current_page])
    get_input()

def get_book_text():
    update_data()
    book_text = open('{home}/books/{current_book}'.format(home=home, current_book=data['current_book'])).read()
    return vs.split_into_rows(book_text)

def open_book():
    pages = get_book_text()
    try:
        # print('pages', current_page, len(pages))
        show_page(pages[current_page])
        get_input()
    except:
        print('traceback.format_exc():\n%s', traceback.format_exc())
        get_input()

try:
    # book_text = open('{home}/books/{current_book}'.format(home=home, current_book=current_book)).read()
    # pages = vs.split_into_rows(book_text)
    # pages = get_book_text(current_book)
    # show_page(pages[current_page])
    # get_input(current_page)
    open_book()


except:
    print('traceback.format_exc():\n%s', traceback.format_exc())
    exit()
