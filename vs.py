# -*- coding: utf-8 -*-

import epd as epd7in5
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

ursula = 'It exists... It’s real. I can call it a misunderstanding, but I can’t pretend that it doesn’t exist, or will ever cease to exist. Suffering is the condition on which we live. And when it comes, you know it. You know it as the truth. Of course it’s right to cure diseases, to prevent hunger and injustice, as the social organism does. But no society can change the nature of existence. We can’t prevent suffering. This pain and that pain, yes, but not Pain. A society can only relieve social suffering, unnecessary suffering. The rest remains. The root, the reality. All of us here are going to know grief; if we live fifty years, we’ll have known pain for fifty years... And yet, I wonder if it isn’t all a misunderstanding — this grasping after happiness, this fear of pain... If instead of fearing it and running from it, one could... get through it, go beyond it. There is something beyond it. It’s the self that suffers, and there’s a place where the self—ceases. I don’t know how to say it. But I believe that the reality — the truth that I recognize in suffering as I don’t in comfort and happiness — that the reality of pain is not pain. If you can get through it. If you can endure it all the way.'

try:
    epd = epd7in5.EPD()
    epd.init()
    print("Clear")
    epd.Clear(0xFF)

    print("Drawing")
    # print("read bmp file on window")
    Himage = Image.new('1', (epd7in5.EPD_HEIGHT, epd7in5.EPD_WIDTH), 255)  # 255: clear the frame
    # bmp = Image.open('/home/pi/14.bmp')
    # Himage2.paste(bmp, (50,10))
    # epd.display(epd.getbuffer(Himage2))
    # font24 = ImageFont.truetype('/usr/share/fonts/truetype/lato/Lato-Regular.ttf', 24)
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 0), 'this si some text, let us see how it goes.  we go we go we go', fill = 0)
    epd.display(epd.getbuffer(Himage))

    print('sleeping')
    epd.sleep()

except:
    print('traceback.format_exc():\n%s', traceback.format_exc())
    exit()
