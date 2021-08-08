# -*- coding: utf-8 -*-
from PIL import Image, ImageFont, ImageDraw

FONT = u'./font/out.ttf'

def DealText(text):
    text_list = list(text)
    count = 0
    i = 0
    end = len(text_list)
    while i < end:
        if text_list[i] == '\n':
            count = 0
            i += 1
        elif count == 40:
            text_list.insert(i,'\n')
            count = 0
            i += 2
        else:
            count += 1
            i += 1
        end = len(text_list)
    
    text = ''.join(text_list)
    return text


def CreateImg(text):
    result = []
    fontSize = 30
    height = 32
    font = ImageFont.truetype(FONT, fontSize)
    lines = text.split('\n')
    count = len(lines)

    for i in range(0,count-1,height):
        if  i+height >= count : 
            im = Image.new("RGB", (44*(fontSize),height *(fontSize+9)), (255, 255, 255))
            dr = ImageDraw.Draw(im)
            dr.text((45, 30), "\n".join(lines[i:]), font=font, fill="#000000", spacing=15)
            result.append(im)
            break
        elif count-i-height <= 8 :
            im = Image.new("RGB", (44*(fontSize),(count-i+1) *(fontSize+9)), (255, 255, 255))
            dr = ImageDraw.Draw(im)
            dr.text((45, 30), "\n".join(lines[i:]), font=font, fill="#000000", spacing=15)
            result.append(im)
            break
        else :
            im = Image.new("RGB", (44*(fontSize),height *(fontSize+9)), (255, 255, 255))
            dr = ImageDraw.Draw(im)
            dr.text((45, 30), "\n".join(lines[i:i+height]), font=font, fill="#000000", spacing=15)
            result.append(im)

    return result

