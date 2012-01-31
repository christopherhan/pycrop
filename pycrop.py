import math
from PIL import Image

def prepare_image(image, thumbnail_size):
    x,y = image.size
    th_x, th_y = thumbnail_size
    
    #the image is smaller than the minimum thumbnail dimensions
    if x < th_x and y < th_y:
        return image 
    
    if x > y: #wide image
        im = square_wide_image(image)
    elif x < y: #tall image
        im = square_tall_image(image)
    else: #it's already square
        im = image  
    
    if im.mode != "RGB":
        im = im.convert('RGB')

    im.thumbnail(thumbnail_size, Image.ANTIALIAS)
    
    return im

def image_entropy(img):
    """calculate the entropy of an image"""
    hist = img.histogram()
    hist_size = sum(hist)
    hist = [float(h) / hist_size for h in hist]
    return -sum([p * math.log(p, 2) for p in hist if p != 0])

def square_wide_image(img):
    x,y = img.size
    while x > y:
        #slice 10px at a time until square
        slice_width = min(x - y, 10)
        right = img.crop((x-slice_width, 0, x, y))
        left = img.crop((0, 0, slice_width, y))

        #remove the slice with the least entropy
        if image_entropy(left) < image_entropy(right):
            img = img.crop((slice_width, 0, x, y)) #crop the left side
        else:
            img = img.crop((0,0,x-slice_width, y)) #crop the right side

        x,y = img.size

    return img
    
def square_tall_image(img):
    """if the image is taller than it is wide, square it off. determine
    which pieces to cut off based on the entropy pieces."""
    x,y = img.size
    while y > x:
        #slice 10px at a time until square
        slice_height = min(y - x, 10)

        bottom = img.crop((0, y - slice_height, x, y))
        top = img.crop((0, 0, x, slice_height))

        #remove the slice with the least entropy
        if image_entropy(bottom) < image_entropy(top):
            img = img.crop((0, 0, x, y - slice_height))
        else:
            img = img.crop((0, slice_height, x, y))

        x,y = img.size

    return img
