# -*- coding: utf-8 -*-

# import epd as epd7in5
# import time
# from PIL import Image,ImageDraw,ImageFont
# import traceback

ursula = "It exists... It's real. I can call it a misunderstanding, but I can't pretend that it doesn't exist, or will ever cease to exist. Suffering is the condition on which we live. And when it comes, you know it. You know it as the truth. Of course it's right to cure diseases, to prevent hunger and injustice, as the social organism does. But no society can change the nature of existence. We can't prevent suffering. This pain and that pain, yes, but not Pain. A society can only relieve social suffering, unnecessary suffering. The rest remains. The root, the reality. All of us here are going to know grief; if we live fifty years, we'll have known pain for fifty years... And yet, I wonder if it isn't all a misunderstanding - this grasping after happiness, this fear of pain... If instead of fearing it and running from it, one could... get through it, go beyond it. There is something beyond it. It's the self that suffers, and there's a place where the self-ceases. I don't know how to say it. But I believe that the reality - the truth that I recognize in suffering as I don't in comfort and happiness - that the reality of pain is not pain. If you can get through it. If you can endure it all the way."

# 45 - not courier new bold (lato probs)
# limit = 45

# 31 - Courier_New_Bold
limit = 31

# row limit = 25
row_limit = 24

# split = [ursula[i:i+limit] for i in range(0, len(ursula), limit)]
#
# print('split')
# print(split)
line_height = 25
line_height_base = line_height

def split_into_pages(input):
    output = []
    # split into array of dicts, with word prop and length
    # words = input.split()
    words = []
    for word in input.split():
        words.append({
            "word": word,
            "length": len(word)
        })
    print(words)

    # for i in range(0, len(input), limit):
    #     print(i, input[i:i+limit])

split_into_pages(ursula)

# try:
#     epd = epd7in5.EPD()
#     epd.init()
#     print("Clear")
#     epd.Clear(0xFF)
#
#     print("Drawing")
#     # print("read bmp file on window")
#     Himage = Image.new('1', (epd7in5.EPD_HEIGHT, epd7in5.EPD_WIDTH), 255)  # 255: clear the frame
#
#     # font24 = ImageFont.truetype('/usr/share/fonts/truetype/lato/Lato-Regular.ttf', 24)
#     # font24 = ImageFont.truetype('/usr/share/fonts/truetype/courier/cour.ttf', 24)
#     font_base = '/usr/share/fonts/treutype/msttcorefonts/{file}'
#     font_file = 'Courier_New_Bold.ttf'
#     # font24 = ImageFont.truetype('/usr/share/fonts/truetype/msttcorefonts/cour.ttf', 24)
#     font24 = ImageFont.truetype(font_base.format(file=font_file), 24)
#     draw = ImageDraw.Draw(Himage)
#
#     # write
#     for line in split:
#         draw.text((10, line_height), line, font = font24, fill = 0)
#         line_height = line_height_base + line_height
#         print(line_height)
#
#
#     # write to display
#     epd.display(epd.getbuffer(Himage))
#
#     print('sleeping')
#     epd.sleep()
#
# except:
#     print('traceback.format_exc():\n%s', traceback.format_exc())
#     exit()
