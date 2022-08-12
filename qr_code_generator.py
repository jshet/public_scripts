import qrcode
import qrcode.image.svg

url = "https://www.google.com/maps/place/24+Greenway+Plaza+Suite+1800,+Houston,+TX+77046/@29.7563981,-95.5627019,11.13z/data=!4m5!3m4!1s0x8640c103f0eaaaab:0xf7fcc222e922d806!8m2!3d29.7302941!4d-95.440683"
urls = ['']

def make_survey_urls(urls, sep_str=""):
    for url in urls:
        output = url.replace(' ','%20')
        name = url.split("=")[1].replace(" ","-").replace("/","") + ".png"

def make_qr_code(contents, fill_color="#000000", back_color="#FFFFFF", box_size=10, border=2):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(contents)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    return img


def make_qr_code_from_url(url, fn):
    img = qrcode.make(url, image_factory=qrcode.image.svg.SvgImage)
    img.save(fn)

def with_colors(url, fn):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="green")

    img.save(fn)

make_qr_code_from_url(url, "qr.svg")
# with_colors(url, "qr2.png")