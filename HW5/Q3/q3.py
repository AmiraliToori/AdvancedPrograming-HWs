
from PIL import Image

def encode_image(img, msg):
    length = len(msg)
    
    if length > 255:
        print("text too long! (don't exceed 255 characters)")
        return False
    if img.mode != 'RGB':
        print("image mode needs to be RGB")
        return False
    
    encoded = img.copy()
    width, height = img.size
    index = 0
    
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            
            if row == 0 and col == 0 and index < length:
                asc = length
            elif index <= length:
                c = msg[index -1]
                asc = ord(c)
            else:
                asc = r
            encoded.putpixel((col, row), (asc, g , b))
            index += 1
    return encoded

def decode_image(img):
    width, height = img.size
    msg = ""
    index = 0
    for row in range(height):
        for col in range(width):
            try:
                r, g, b = img.getpixel((col, row))
            except ValueError:
                
                r, g, b, a = img.getpixel((col, row))		
            
            if row == 0 and col == 0:
                length = r
            elif index <= length:
                msg += chr(r)
            index += 1
    return msg




original_image_file = "/home/glados/Documents/AmirAli Toori/Lessons/Python/HWs/AdvancedPrograming-HWs/HW5/Q3/picture.bmp"


img = Image.open(original_image_file)

print(img, img.mode) 


encoded_image_file = "answer" + "picture.bmp"


secret_msg = "Hello this"
print(len(secret_msg))  

img_encoded = encode_image(img, secret_msg)

if img_encoded:
    
    img_encoded.save(encoded_image_file)
    print("{} saved!".format(encoded_image_file))

    
    import os
    os.system(encoded_image_file)
   
    img2 = Image.open(encoded_image_file)
    hidden_text = decode_image(img2)
    print("Hidden text:\n{}".format(hidden_text))
