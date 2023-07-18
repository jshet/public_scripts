from PIL import Image, ImageFilter, ImageOps

image_file = "image2.png"

im = Image.open(image_file)

print(im.format, im.size, im.mode)

# cut out a rectangle, rotate it, and paste it back
# box = (100,100,400,400)
# region = im.crop(box)
# region = region.transpose(Image.Transpose.ROTATE_180)
# im.paste(region, box)

# r, g, b, a = im.split()
# im = Image.merge("RGB", (b,r,g))

im = im.convert("RGB")
im = ImageOps.autocontrast(im)

im_gray = ImageOps.grayscale(im)
im = im_gray.filter(ImageFilter.FIND_EDGES)
im = ImageOps.invert(im)

# im_data = im.getdata()
# new_im_data = []

# for item in im_data:
#     if item[0] < 155:
#         new_im_data.append((255,255,255, 255))
#     else:
#         new_im_data.append((0,0,0, 255))  
# im.putdata(new_im_data)
# for i in range(10):
#     print(im_data[i])

im.show()
