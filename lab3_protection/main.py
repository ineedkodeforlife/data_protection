import struct

def hide_byte_into_pixel(pixel, hide_byte):
    pixel[0] &= 0xFC
    pixel[0] |= (hide_byte >> 6) & 0x3
    pixel[1] &= 0xFC
    pixel[1] |= (hide_byte >> 4) & 0x3
    pixel[2] &= 0xFC
    pixel[2] |= (hide_byte >> 2) & 0x3
    pixel[3] &= 0xFC
    pixel[3] |= hide_byte & 0x3

def extract_byte_from_pixel(pixel):
    hide_byte = 0
    hide_byte |= (pixel[0] & 0x3) << 6
    hide_byte |= (pixel[1] & 0x3) << 4
    hide_byte |= (pixel[2] & 0x3) << 2
    hide_byte |= (pixel[3] & 0x3)
    return hide_byte

def hide_data_in_image(bmp_filename, data_filename):
    with open(bmp_filename, 'rb+') as bmp_file:
        bmp_file_header = bmp_file.read(14)
        bmp_info_header = bmp_file.read(40)

        bmp_file.seek(54)  # Skip to the pixel data

        with open(data_filename, 'rb') as data_file:
            while True:
                data_byte = data_file.read(1)
                if not data_byte:
                    break
                pixel = bmp_file.read(4)
                if not pixel:
                    break
                hide_byte_into_pixel(bytearray(pixel), ord(data_byte))

                bmp_file.seek(-4, 1)  # Move back 4 bytes to overwrite the pixel
                bmp_file.write(pixel)

def extract_data_from_image(bmp_filename, extracted_filename):
    with open(bmp_filename, 'rb') as bmp_file:
        bmp_file_header = bmp_file.read(14)
        bmp_info_header = bmp_file.read(40)

        bmp_file.seek(54)  # Skip to the pixel data

        with open(extracted_filename, 'wb') as extracted_file:
            while True:
                pixel = bmp_file.read(4)
                if not pixel:
                    break
                data_byte = extract_byte_from_pixel(bytearray(pixel))
                if data_byte == 0xFF:
                    break
                extracted_file.write(bytes([data_byte]))


if __name__ == '__main__':

    action = 'extract'
    bmp_filename = 'C:\\Users\\vitrl\\Downloads\\8.bmp'
    data_filename = 'data.txt'

    if action == 'hide':
        hide_data_in_image(bmp_filename, data_filename)
    elif action == 'extract':
        extract_data_from_image(bmp_filename, data_filename)
    else:
        print("Invalid action. Please use 'hide' or 'extract'.")
