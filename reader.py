# -*- coding: utf-8 -*-

import epd as epd7in5
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import sys
import pprint
import json
from os.path import expanduser
import vs, cover
import keyboard
import random
import os
import signal
import buttonshim
from subprocess import call

try:
    from evdev import uinput, UInput, ecodes as e
except ImportError:
    exit("This library requires the evdev module\nInstall with: sudo pip install evdev")

KEYCODES = [e.KEY_COMMA, e.KEY_DOT, e.KEY_C, e.KEY_R, e.KEY_Q]
BUTTONS = [buttonshim.BUTTON_A, buttonshim.BUTTON_B, buttonshim.BUTTON_C, buttonshim.BUTTON_D, buttonshim.BUTTON_E]

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

try:
    ui = UInput({e.EV_KEY: KEYCODES}, name="Button-SHIM", bustype=e.BUS_USB)

except uinput.UInputError as e:
    print(e.message)
    print("Have you tried running as root? sudo {}".format(sys.argv[0]))
    sys.exit(0)

# home = expanduser("~")
home = '/home/pi'

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
books = filter(lambda x: ('.txt' in x), os.listdir('/home/pi/books'))

line_height_base = 25 # this isn't great

epd = epd7in5.EPD()

def show_page(page=None):
    if page == None:
        page = data['pages'][data['current_page']]

    epd.init()
    Himage = Image.new('1', (epd7in5.EPD_HEIGHT, epd7in5.EPD_WIDTH), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    line_height = 0
    for line in page:
        draw.text((10, line_height), line, font = font24, fill = 0)
        line_height = line_height_base + line_height

    buffer_time = time.time()
    buffer = epd.getbuffer(Himage)
    print('buffer time', time.time() - buffer_time)
    display_time = time.time()
    epd.display(buffer)
    print('display time', time.time() - display_time)
    time.sleep(1)
    epd.sleep()

def update_data():
    # data['current_page'] = page
    # data['current_book'] = book
    print 'current data', data['current_book'], data['current_page']
    with open(file, 'w') as outfile:
        json.dump(data, outfile)

def shutdown_pi():
    cover.display_cover('random')
    call("sudo shutdown -h now", shell=True)

def get_input(input_key):
    commands = ['.', ',', 'a', 'p', 'q', 'r', 'b']
    #0de80d - green
    buttonshim.set_pixel(0x0d, 0xe8, 0x0d)
    print('< >')
    if input_key == None:
        key = getch()
    else:
        key = input_key


    print(key)

    if key not in commands:
        print('command not recognized')
        get_input(None)

    if key == '.':
        # #e8e50d - yellow
        buttonshim.set_pixel(0xe8, 0xe5, 0x0d)
        data['current_page'] = data['current_page'] + 1
    elif key == ',':
        #e80d32 - red
        buttonshim.set_pixel(0xe8, 0x0d, 0x32)
        data['current_page'] = data['current_page'] - 1
    elif key == 'a':
        data['current_book'] = 'asimov.txt'
        data['current_page'] = 0
        print('changing current books', data)
        open_book()
    elif key == 'r':
        #c00de8 - purple
        buttonshim.set_pixel(0xc0, 0x0d, 0xe8)
        cover.display_cover('random')
        return get_input(None)
    elif key == 'b':
        data['current_book'] = random.choice(books)
        data['current_page'] = 0
        open_book()
        print('random books', data)
    elif key == 'q':
        buttonshim.set_pixel(0x00, 0x00, 0x00)
        exit(0)
    elif key == 'p':
        shutdown_pi()

    if data['current_page'] < 0:
        data['current_page'] = 0
    elif data['current_page'] > len(data['pages']):
        data['current_page'] = len(data['pages'])
    update_data()
    show_page()
    get_input(None)

def get_book_text():
    update_data()
    book_text = open('{home}/books/{current_book}'.format(home=home, current_book=data['current_book'])).read()
    return vs.split_into_rows(book_text)

def open_book():
    data['pages'] = get_book_text()
    try:
        # print('pages', current_page, len(pages))
        show_page()
        get_input(None)
    except:
        print('traceback.format_exc():\n%s', traceback.format_exc())
        get_input(None)


# buttonshim
@buttonshim.on_press(BUTTONS)
def button_p_handler(button, pressed):
    print("button pressed:{0}".format(button))
    keycode = KEYCODES[button]
    print("Press: {}".format(keycode))
    input_key = ''
    if keycode == 51:
        input_key = ','
    elif keycode == 52:
        input_key = '.'
    elif keycode == 46:
        input_key = 'p'
    elif keycode == 19:
        input_key = 'r'
    get_input(input_key)


    # ui.write(e.EV_KEY, keycode, 1)
    # ui.syn()

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
