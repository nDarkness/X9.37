# import os
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw

im = Image.open("img2.tiff")
print(im.info)
# exit()
draw = ImageDraw.Draw(im)
font = ImageFont.truetype("micrenc.ttf", 42)
# print(font.getname())
# exit(0)

draw.rectangle([0,450,im.size[0],im.size[1]-20],fill="white")
# im.show()
# exit(0)

message = "C006005C"
# _, _, w, h = draw.textbbox((0,0),message,font=font)
x = 327
y = 460
# y = (250)
draw.text(((x),(y)),message,anchor='mm',font=font)

x = 569
y = 460
message = "A111914742A"

draw.text(((x),(y)),message,anchor='mm',font=font)

x = 839
y = 460
message = "3123456101C"

draw.text(((x),(y)),message,anchor='mm',font=font)
# for i, l in enumerate(message):
#     draw.text(((x + i * 5.5),(y)),l,(0,0,0),font=font)

im.show()
im.save("test_out.tiff", format="tiff")
exit()

__CODEC__ = "cp850"

def reader(n, codec=None):
    read = fp.read(n)
    if codec is not None:
        return read.decode(codec)
    return read


def pad_zero_left(values, length):
    return str(values).rjust(length, "0")


def pad_space_right(data, length):
    data.ljust(length, b" ")


rec_01 = {
    "Record Type": 2,
    "Standard Level": 2,
    "Test File Indicator": 1,
    "Immediate Receiving Point Routing Number": 9,
    "Immediate Origin Routing Number": 9,
    "File Creation Date": 8,
    "File Creation Time": 4,
    "Resend Ind": 1,
    "Immediate Destination Name": 18,
    "Immediate Origin Name": 18,
    "File ID Modifier": 1,
    "Country Code": 2,
    "User Field": 4,
    "Reserved": 1,
}

rec_10 = {
    "Record Type": 2,
    "Collection Type Indicator": 2,
    "Destination Routing Number": 9,
    "Client Institution Routing Number": 9,
    "Cash Letter Business Date": 8,
    "Cash Letter Creation Date": 8,
    "Cash Letter Creation Time": 4,
    "Cash Letter Record Type Indicator": 1,
    "Cash Letter Documentation Type Indicator": 1,
    "Cash Letter ID": 8,
    "Originator Contact Name": 14,
    "Originator Contact Phone Number": 10,
    "Work Type": 1,
    "Returns Indicator": 1,
    "User Field": 1,
    "Reserved": 1,
}

rec_20 = {
    "Record Type": 2,
    "Collection Type Indicator": 2,
    "Destination Routing Number": 9,
    "ECE Institution Routing Number": 9,
    "Bundle Business Date": 8,
    "Bundle Creation Date": 8,
    "Bundle ID": 10,
    "Bundle Sequence Number": 4,
    "Cycle Number": 2,
    "Reserved": 9,
    "User Field": 5,
    "Reserved1": 12,
}

rec_25 = {
    "Record Type": 2,
    "Auxiliary On-Us": 15,
    "External Processing Code": 1,
    "Payor Bank Routing Number": 8,
    "Payor Bank Routing Number Check Digit": 1,
    "On-Us": 20,
    "Item Amount": 10,
    "Client Institution Item Sequence Number": 15,
    "Documentation Type Indicator": 1,
    "Electronic Return Acceptance Indicator": 1,
    "MICR Valid Indicator": 1,
    "BOFD Indicator": 1,
    "Check Detail Record Addendum Count": 2,
    "Correction Indicator": 1,
    "Archive Type Indicator": 1,
}

rec_61 = {
    "Record Type": 2,
    "Record Usage Indicator": 1,
    "Auxiliary On-Us": 15,
    "External Processing Code": 1,
    "Posting Bank Routing Number": 9,
    "On-Us": 20,
    "Item Amount": 10,
    "Item Sequence Number": 15,
    "Documentation Type Indicator": 1,
    "Type of Account Code": 1,
    "Source of Work Code": 2,
    "Reserved": 3,
}

rec_50 = {
    "Record Type": 2,
    "Image Indicator": 1,
    "Image Creator Routing Number": 9,
    "Image Creator Date": 8,
    "Image View Format Indicator": 2,
    "Image View Compression Algorithm Identifier": 2,
    "Image View Data Size": 7,
    "View Side Indicator": 1,
    "View Descriptor": 2,
    "Digital Signature Indicator": 1,
    "Digital Signature Method": 2,
    "Security Key Size": 5,
    "Start of Protected Data": 7,
    "Length of Protected Data": 7,
    "Image Recreate Indicator": 1,
    "User Field": 8,
    "Reserved ": 15,
}

rec_52 = {
    "Record Type": 2,
    "Institution Routing Number": 9,
    "Bundle Business Date": 8,
    "Cycle Number": 2,
    "Client Institution Item Sequence": 15,
    "Security Originator Name": 16,
    "Security Authenticator Name": 16,
    "Security Key Name": 16,
    "Clipping Origin": 1,
    "Clipping Coordinate h1": 4,
    "Clipping Coordinate h2": 4,
    "Clipping Coordinate v1": 4,
    "Clipping Coordinate v2": 4,
    "Length of Image Reference Key": 4,
    "Image reference Key": 0,
    "Length of Digital Signature": 5,
    "Digital Signature": 0,
    "Length of Image Data": 7,
    "Image Data *": 0,
}


def data_52(img, input_data):
    # img = b''.join([b'I' for _ in range(2241)])
    img = img.read()
    rec = {}
    for k, v in rec_52.items():
        if k != "Image Data *":
            data = input_data.read(v).strip()
            rec[k] = data.ljust(v, b' ')
            # print(k, rec[k])
        else:
            rec[k] = img

    data_bytes = b''.join(rec.values())
    return bytes.fromhex(f'{len(data_bytes):08x}') + data_bytes


img = BytesIO(open("frontCheckImage.tif", "rb").read()).read(32)
input_data = BytesIO(("52000909113201302181 102                                                            0                0   0    " + str(len(img))).encode("cp850"))
print(data_52(BytesIO(img), input_data))

# exit(0)

rec_70 = {
    "Record Type": 2,
    "Bundle Item Count": 4,
    "Bundle Total Amount": 12,
    "MICR Valid Total Amount": 12,
    "Images within Bundle Count": 5,
    "User Field": 20,
    "Reserved": 25,
}

rec_90 = {
    "Record Type": 2,
    "Bundle Count": 6,
    "Cash Letter Item Count": 8,
    "Cash Letter Total Amount": 14,
    "Cash Letter Image View Count": 9,
    "ECE Institution Name": 18,
    "Settlement Date": 8,
    "Reserved": 15,
}

rec_99 = {
    "Record Type": 2,
    "Cash Letter Count": 6,
    "Total Record Count": 8,
    "Total Item Count": 8,
    "File Total Amount": 16,
    "Immediate Origin Contact Name": 14,
    "Immediate Origin Contact Phone Number": 10,
    "File Credit Total Amount": 16,
}

records = {
    "01": rec_01,
    "10": rec_10,
    "20": rec_20,
    "25": rec_25,
    "50": rec_50,
    "52": rec_52,
    "61": rec_61,
    "70": rec_70,
    "90": rec_90,
    "99": rec_99,
}

# from PIL import Image
# im = Image.open(r"/home/ap/.config/JetBrains/PyCharmCE2023.2/scratches/frontCheckimage.tiff")
# width, height = im.size
# left = width/4
# top = height/4
# right = 3 * left
# bottom = 334
# print(width, height)
# print(left, top, right, bottom)
# cropped = im.crop((0, 0, width, bottom))
# cropped.save("frontCheckImage.tif", format="tiff")
# from io import BytesIO
#
# img = open("frontCheckImage.tif", "rb").read()
# data_52 = [
#     b'0',
#     ''.join(["52",
#              "000909113",
#              "20130218",
#              "1 ",
#              "102            ",
#              "                ",
#              "                ",
#              "                ",
#              "0",
#              "    ",
#              "    ",
#              "    ",
#              "    ",
#              "0   ",
#              "",
#              "0    ",
#              str(len(img)).ljust(7, " "),
#              ]).encode("cp850"),
#     b'',
# ]
# items = BytesIO(data_52[1])
#
# items.seek(sum(rec_52.values()) - rec_52["Length of Image Data"], 0)
# items.write(str(len(img)).encode("cp850").ljust(7, b" "))
# # items.write(img)
# items.seek(0)
# # print(items.read(sum(rec_52.values()) + 8))
# data_52[1] = items.read()
# row_header_len = bytes.fromhex(f'{len(data_52[1] + data_52[2]):08x}')
# data_52[0] = row_header_len
# print(b''.join(data_52[:2]))
#
# exit(0)
# len_img = 0
# end = sum(rec_52.values())
# start = end - rec_52["Length of Image Data"]
# print()
# items[start:end].replace(items[start:end], str(len(img)).encode("cp850").ljust(7, b" "))
# print(str(len(img)).encode("cp850").ljust(7, b" "))
# print(items[start:end])
# print(bytes.fromhex(f'{len(items):08x}'))
#
#
# doc = open("101Bank Of America20130218.ICL", 'rb').read()
# print(type(doc))
#
# exit(0)
# text = bytes.fromhex("0123456789                                                                      ".encode("cp850").hex())
# line_start = bytes.fromhex(f'{len(text):08x}')
# total_bytes = line_start + text
# print(total_bytes, len(total_bytes))
# exit(0)
line_len = 80
converted = bytes.fromhex(f'{line_len:08x}')
print(converted)
print(converted == b'\x00\x00\x00P')
# exit(0)

with open("101Bank Of America20130218.ICL", 'rb') as fp:
    img_count = 0
    item_count = 0
    total_25_count = 0
    total_25_value = 0
    total_61_count = 0
    total_61_value = 0
    while True:
        line_data = reader(4)

        start = fp.tell()
        rtype = reader(2, __CODEC__)
        if rtype == '':
            break
        print("Rtype", rtype)
        fp.seek(start)
        item_count += 1
        if len(str(line_data)) < 16:
            l_data = f'{line_data} {line_data.hex()}\t\t\t{rtype}'
        else:
            l_data = f'{line_data} {line_data.hex()}\t\t{rtype}'

        if rtype == '52':
            # print(f"Record Type: {rtype}")
            img_size = 0
            total_bytes = 0
            for k, v in rec_52.items():
                if k == "Length of Image Data":
                    img_size = int(reader(v))
                    total_bytes += v
                    print(f"\t{k}: {img_size}")
                elif k == "Image Data *":
                    img_data = reader(img_size)
                    print(img_data[:4])
                    open(f"img{img_count}.tiff", "wb").write(img_data)
                    l_data += f"\t\t{bytes.fromhex(f'{total_bytes + img_size:08x}')}\t\t{img_size}\t\t{total_bytes + img_size}"
                    img_count += 1
                    # exit(0)
                    # if img_count == 4:
                    #     exit(0)
                else:
                    data = reader(v)
                    total_bytes += v
                    print(f"\t{k}: {data.decode(__CODEC__)}")
            # print(f"\t{rec_52.keys()[-1]}")
            # print(f"\t{reader(17)}")
            # img_len = int(reader(7))
            # print(f"\tImage length: {img_len}")
            # reader(img_len)
            # exit(0)
        elif rtype == "25":
            total_25_count += 1
            for k, v in records[(rtype)].items():
                # if k == "Record Type":
                #     print(f"\t{k}: {rtype}")
                # else:
                value = reader(v)
                if k == "Item Amount":
                    total_25_value += int(value.decode(__CODEC__))
                print(f"\t{k}: {value}")
        elif rtype == "61":
            total_61_count += 1
            for k, v in records[(rtype)].items():
                # if k == "Record Type":
                #     print(f"\t{k}: {rtype}")
                # else:
                value = reader(v)
                if k == "Item Amount":
                    total_61_value += int(value.decode(__CODEC__))
                print(f'\t{k}: {value.rjust(v, b"0")}')
        else:
            # print(rtype)
            try:
                for k, v in records[(rtype)].items():
                    # if k == "Record Type":
                    #     print(f"\t{k}: {rtype}")
                    # else:
                    print(f"\t{k}: {reader(v)}")

                    # if k != "Record Type":
                    #     reader(v)
            except (KeyError):
                print(f"Record Type: {rtype}")
                line = reader(80, __CODEC__)
                print(line)
                exit(0)
                # print(f"\t{line}")
        # print(f"{l_data}")

    print(f"\nTotal Image Count: {img_count}\nTotal Record Count: {item_count}\nTotal 61 Count: {total_61_count}\nTotal 61 Amount: {total_61_value}\nTotal 25 Count: {total_25_count}\nTotal 25 Amount: {total_25_value}")
    length = rec_70["Bundle Total Amount"]
    print(f'{pad_zero_left(total_25_value, length)}\n{pad_zero_left(total_61_value, length)}')
    length = rec_99["File Total Amount"]
    print(f'{pad_zero_left(total_25_value, length)}\n{pad_zero_left(total_61_value, length)}')
