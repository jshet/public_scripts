from PIL import Image, ImageDraw

# bg_color = (87, 174, 261)
bg_color = (255,255,255)
line_width = 1
line_color = (150,150,150)

with Image.new("RGB", (4000,4000), bg_color) as im:


    draw = ImageDraw.Draw(im)

    draw.rectangle([100,100,3900,3900], width=line_width, outline=line_color)

    draw.line([(100,100), (3900,3900)], width=line_width, fill=line_color)
    draw.line([(100,3900), (3900,100)], width=line_width, fill=line_color)

    draw.line([(100,2000),(3900,2000)], width=line_width, fill=line_color)
    draw.line([(2000,100),(2000,3900)], width=line_width, fill=line_color)

    draw.regular_polygon((2000,2000, 1900), 6, width=line_width, outline=line_color)

    # for i in range(100):
    #     radius = 750-(i*10)
    #     base = i+10
    #     color = (base, base*2, base*3)
    #     print(color)
    #     if radius > 10:
    #         draw.regular_polygon((2000,2000, radius), 6, rotation=i*5, width=1, fill=color)

    draw.arc([(100,100), (3900,3900)], 0, 360, width=line_width, fill=line_color)

    im.show()
