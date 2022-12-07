def lattopx(lat, height):
    adjlat = -lat + 90
    return (adjlat / 180) * height

def longtopx(long, width):
    adjlong = long + 180
    return (adjlong / 360) * width


# Gets long and lat from pixels
def pxtolong(px, width):
    adjlong = (px / width) * 360 
    return adjlong - 180

def pxtolat(px, height):
    adjlat = (px / height) * 180
    return -(adjlat -90)