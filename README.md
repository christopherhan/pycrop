About
=====================
Modifies reddit's image cropping algorithm to accept an image of any dimension 
to produce a square thumbnail.

Produces an NxN-sized thumbnail of an image without distortion. For example,
a 100px x 50px image can be converted to a 25px x 25px thumbnail. First, the
100x50 will be cropped to 50x50, then reduced to 25x25. The cropping algorithm
works by calculating the entropy of an image and slicing off the side that has
the least entropy.


Dependencies
=====================
You'll need PIL installed to modify images.
http://www.pythonware.com/products/pil/

Usage
=====================
    from pycrop import pycrop as pc
    from PIL import Image
    
    im = Image.open(path_to_file)
    image = pc.prepare_image(im, (25,25))
	image.save(new_filename, 'JPEG')
	
Functions
======================
prepare_image(Image, (x, y))
----------------------
Takes a PIL Image object and a tuple of the dimensions.


