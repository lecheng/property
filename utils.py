import re
from pyquery import PyQuery as pq

def mkdir(path):
    import os
 
    path=path.strip()
    path=path.rstrip("\\")
 
    isExists=os.path.exists(path)
 
    if not isExists:
        print path+' create success!'
        os.makedirs(path)
        return True
    else:
        print path+' folder exists!'
        return False
DISCOVER_NONPHONE_RATIO = 1200.0/695
DISCOVER_PHONE_RATIO = 480.0/695
def voffset_on_phone(width, height):
    ratio = width/height
    if ratio >= DISCOVER_NONPHONE_RATIO:
        height_phone = 480/ratio
    elif ratio <= DISCOVER_PHONE_RATIO:
        height_phone = 695
    else:
        height_phone = 480/ratio
    screen_height = 695
    base_offset = 20
    return base_offset+(screen_height/2)-(height_phone/2)

def currentConvert(amount,f,t):
    url = "https://www.google.com/finance/converter?a=" + str(amount) + "&from=" + f + "&to=" + t
    dom = pq(url)
    convert = dom('.bld').text()[0:7]
    return convert