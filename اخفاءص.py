from PIL import Image
import cv2
def text_to_bin(text): 
#  ةياهن ةملاع ةفاضإو تاتبلا نم ةلسلس ىلإ صنلا ليوحت (null terminator) 
    return ''.join(format(ord(i),'08b')for i in text) + '00000000'  
def hide_char_in_image(image_path, t, output_path): 
         #  ماظنل اهليوحتو ةروصلا حتف RGB 
    img = Image.open('am.png').convert('RGB') 
    pixels = img.load() 
    #  ىلإ فرحلا ليوحت 8  تاتب ( :لاثم ‘A’ -> 01000001) 
    t_bin = text_to_bin(t) 
    width, height = img.size 
    bit_index = 0 
         #  ـلا نيزختل ةروصلا تلاسكب لوأ ليدعت 8  تاتب 
    for y in range(height): 
        for x in range(width): 
            if bit_index <len(t_bin): 
                r, g, b = pixels[x, y] 
                 # رمحلأا نوللا ةانق يف ريخلأا تبلا ليدعت (R)  
                 #  ب ريخلأا تبلا حسمن(r & ~1)  تب عضن مث فرحلا 
                new_r = (r & ~1) | int(t_bin[bit_index]) 
                pixels[x, y] = (new_r, g, b) 
                bit_index += 1 
            else: 
                break 
        if bit_index >= 8:  
            break 
    img.save(output_path) 
    print( "تم العمليه بنجاح تام ") 
 
x =input("ENTER THE TAXT :")
hide_char_in_image('am.png' , x, 'hidden_image.png') 
