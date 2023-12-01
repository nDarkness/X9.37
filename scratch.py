# import os


def reader(n):
    return fp.read(n)


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
    "User Field": 2,
    "Reserved": 1,
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

records = {
    "01": rec_01,
    "10": rec_10,
    "25": rec_25,
    "50": rec_50,
    "52": rec_52,
}

with open("101Bank Of America20130218.ICL", 'rb') as fp:
    # fp.read(4)
    # type = fp.read(2)
    # line = fp.read(78)
    # print(f"Record Type: {type}")
    # print(line)
    img_count = 0
    while True:
        fp.read(4)
        type = fp.read(2)

        if type == b'52':
            print(f"Record Type: {type}")
            img_size = 0
            for k, v in rec_52.items():
                if k == "Length of Image Data":
                    img_size = int(fp.read(v))
                    print(f"\t{k}: {img_size}")
                elif k == "Image Data *":
                    img_data = fp.read(img_size)
                    open("img.tiff", "wb").write(img_data)
                    # print(f"\t{k}: {img_data}")
                    img_count += 1
                    if img_count == 4:
                        exit(0)
                else:
                    print(f"\t{k}: {fp.read(v)}")
            # print(f"\t{rec_52.keys()[-1]}")
            # print(f"\t{fp.read(17)}")
            # img_len = int(fp.read(7))
            # print(f"\tImage length: {img_len}")
            # fp.read(img_len)
            # exit(0)
        elif type == b'99':
            print(f"Record Type: {type}")
            line = fp.read(78)
            print(f"\t{line}")
            break
        else:
            print(type)
            try:
                for k, v in records[(type.decode('utf-8'))].items():
                    if k == "Record Type":
                        print(f"\t{k}: {type}")
                    else:
                        print(f"\t{k}: {fp.read(v)}")
            except (KeyError):
                print(f"Record Type: {type}")
                line = fp.read(78)
                print(f"\t{line}")



