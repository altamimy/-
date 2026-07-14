from PIL import Image 
def extract_char_from_image(image_path): 
    img =Image.open("hidden_image.png") 
    pixels = img.load() 
    char_bin = "" 
    width, height = img.size 
    #   لوأ ةءارق 8  تلاسكبلا نم تاتب 
    for y in range(height): 
        for x in range(width): 
            if len(char_bin) < 8: 
                r, g, b = pixels[x, y] 
                #  مادختساب ريخلأا تبلا ىلع لوصحلا (r & 1) 
                char_bin += str(r & 1) 
            else: 
                break 
        if len(char_bin) >= 8: 
            break 
    # فرح ىلإ يئانثلا ليوحت 
    return chr(int(char_bin, 2)) 
#  جارختسلإا ةبرجت 
print(extract_char_from_image("hidden_image.png")) 