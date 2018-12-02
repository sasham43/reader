import epd
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

try:
    epd = epd7in5.EPD()
    epd.init()
    print("Clear")
    epd.Clear(0xFF)

    print("Drawing")
    print("read bmp file on window")
    Himage2 = Image.new('1', (epd7in5.EPD_HEIGHT, epd7in5.EPD_WIDTH), 255)  # 255: clear the frame
    bmp = Image.open('/home/pi/14.bmp')
    Himage2.paste(bmp, (50,10))
    epd.display(epd.getbuffer(Himage2))

    epd.sleep()

except:
    print('traceback.format_exc():\n%s', traceback.format_exc())
    exit()
