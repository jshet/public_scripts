import qrcode
import qrcode.image.svg
import os

test_list = [["name1","data1"], ["name2", "data2"], ["data3"]]
destination_dir = ""
params = "?utm_source=bcard&utm_medium=qr_code_221014"

# Assign a different value here to run with your data
list_of_urls = test_list

def make_qr_urls_from_list(urls, sep_str="", add_params=""):
    for l in list_of_urls:
        '''
        Converts urls to url friendly format
        Converts names to url friendly format
        Creates qr code using url as data
        Saves qr code in destination directory with given filename
        If a parameter string is given, it will append it to the url
        '''

        # If no name provided, make the first 30 characters of data the name.
        if len(l) == 1:
            l.append(l[0][:30])

        output = l[1].replace(' ','%20') + add_params
        name = "qr_" + l[0].replace(' ','-').replace('/','-') + ".png"
        save_as = os.path.join(destination_dir, name)

        qr = make_qr_code(output)
        qr.save(save_as)

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

if __name__=="__main__":
    make_qr_urls_from_list(list_of_urls)