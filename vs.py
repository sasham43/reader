# -*- coding: utf-8 -*-

import epd as epd7in5
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import sys

ursula = "It exists... It's real. I can call it a misunderstanding, but I can't pretend that it doesn't exist, or will ever cease to exist. Suffering is the condition on which we live. And when it comes, you know it. You know it as the truth. Of course it's right to cure diseases, to prevent hunger and injustice, as the social organism does. But no society can change the nature of existence. We can't prevent suffering. This pain and that pain, yes, but not Pain. A society can only relieve social suffering, unnecessary suffering. The rest remains. The root, the reality. All of us here are going to know grief; if we live fifty years, we'll have known pain for fifty years... And yet, I wonder if it isn't all a misunderstanding - this grasping after happiness, this fear of pain... If instead of fearing it and running from it, one could... get through it, go beyond it. There is something beyond it. It's the self that suffers, and there's a place where the self-ceases. I don't know how to say it. But I believe that the reality - the truth that I recognize in suffering as I don't in comfort and happiness - that the reality of pain is not pain. If you can get through it. If you can endure it all the way."

# 45 - not courier new bold (lato probs)
# limit = 45

# 31 - Courier_New_Bold
limit = 31

# row limit = 25
row_limit = 22

line_height = 25
line_height_base = line_height

# class Page:


def split_into_rows(input):
    pages = [
        ['']
    ]
    row_number = 0
    page_number = 0
    page_length = 0
    for word in input.split():
        # put into pages
        if len(pages[page_number]) <= row_limit:
            rows = pages[page_number]
        else:
            page_number = page_number + 1
            row_number = 0
            pages.append([''])
            rows = pages[page_number]

        # slowly shift the words into rows
        current_row_length = len(rows[row_number])
        # print(row_number, current_row_length)
        if current_row_length + len(word) + 1 > limit:
            # too big
            row_number = row_number + 1
            rows.append(word)
        else:
            rows[row_number] = '{base} {word}'.format(base=rows[row_number], word=word)

    return pages

pages = split_into_rows(ursula)

try:
    init_time = time.time()
    epd = epd7in5.EPD()
    epd.init()
    print('initialized', time.time() - init_time)

    # fonts
    font_base = '/usr/share/fonts/treutype/msttcorefonts/{file}'
    font_file = 'Courier_New_Bold.ttf'
    font24 = ImageFont.truetype(font_base.format(file=font_file), 24)

    clear_time = time.time()
    print('clearing')
    epd.Clear(0xFF) # start off fresh
    print('cleared', time.time() - clear_time)
    # print("Drawing")

    # go page by page
    for index, page in enumerate(pages):
        print(index, page)
        # page = pages[page_number]
        print('drawing')
        image_time = time.time()
        Himage = Image.new('1', (epd7in5.EPD_HEIGHT, epd7in5.EPD_WIDTH), 255)  # 255: clear the frame
        draw = ImageDraw.Draw(Himage)
        print('done drawing', time.time() - image_time)

        # print(page)
        for line in page:
            draw.text((10, line_height), line, font = font24, fill = 0)
            line_height = line_height_base + line_height
            # print(line_height)
        # save image

        # Himage.save('/home/pi/page_{index}.png'.format(index=index), "PNG")
        # reset line height
        line_height = 0

        # buffer_time = time.time()
        # buffer = epd.getbuffer(Himage)
        # print('buffered', time.time() - buffer_time)

        # write to display
        write_time = time.time()
        print('writing')
        epd.display(epd.getbuffer(Himage))
        print('wrote', time.time() - write_time)

        del draw
        del Himage
        # del buffer

        # print('sleeping')
        # epd.sleep()

        print('new page')
        # time.sleep(60)
        epd.Clear(0xFF) # start off fresh

    # finished printing pages
    time.sleep(5)
    print('sleeping')
    epd.sleep()

except:
    print('traceback.format_exc():\n%s', traceback.format_exc())
    exit()
