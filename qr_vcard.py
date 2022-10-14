import pyqrcode
import pandas as pd

csv_in = "in.csv"
csv_out = csv_in.split(".csv")[0] + "_out.csv"

def createQRCode():
    df = pd.read_csv(csv_in)
    df["@QR_Code"] = "C:\\Users\\<user>\\Downloads\\QRcodes\\" + df["Name"].str.replace(" ","_") + ".png"
    for index, values in df.iterrows():
        lastname = values["Name"].split(" ")[1].strip()
        firstname = values["Name"].split(" ")[0].strip()
        title = values["Title"]
        phone = values["Phone"]
        email = values["Email"]
        website = "https://www.lucidprivateoffices.com"
        org = "Lucid Private Offices"
        cell = values["Cell"]
        # street = values["street"]
        # city = values["city"]
        # p_code = values["p_code"]
        # country = values["country"]

        data = f'''BEGIN:VCARD\nVERSION:3.0\nN:{lastname};{firstname}\nFN:{firstname} {lastname}\nORG:{org}\nTITLE:{title}\nTEL;WORK;VOICE:{phone}\nTEL;CELL:{cell}\nEMAIL;WORK;INTERNET:{email}\nURL:{website}\nEND:VCARD'''

        image = pyqrcode.create(data)
        # image.svg(f"vcard_qrs/{lastname}_{firstname}.svg", scale="5")
        image.png(f"vcard_png_qrs/{firstname}_{lastname}.png")
    
    df.to_csv(csv_out, index=False)

createQRCode()

'''
BEGIN:VCARD
VERSION:3.0
N:Lastname;Surname
FN: Displayname
ORG:Example Inc
URL:http://www.example.com/
EMAIL:info@example.com
TEL;TYPE=voice,work,pref:+18008008000
ADR;TYPE=intl,work,postal,parcel:;;1234 Main St;Anytown;;75024;USA
END:VCARD
'''
