from PIL import Image 
 
def text_to_binary(text): 
    return ''.join(format(ord(char), '08b') for char in text) 
 
def hide_data(image_path, output_path, secret_text): 
    img = Image.open(image_path) 
    binary_data = text_to_binary(secret_text) + '00000000'  # delimiter 
     
    data_index = 0 
    pixels = img.load() 
 
    for y in range(img.height): 
        for x in range(img.width): 
            pixel = list(pixels[x, y]) 
 
            for i in range(3):  # RGB 
                if data_index < len(binary_data): 
                    pixel[i] = pixel[i] & ~1 | int(binary_data[data_index]) 
                    data_index += 1 
 
            pixels[x, y] = tuple(pixel) 
 
            if data_index >= len(binary_data): 
                img.save(output_path) 
                print("حاجنب ءافخلإا مت") 
                return new_func()

def new_func():
    return
             


from PIL import Image 
def extract_data(image_path): 
    img = Image.open(image_path) 
    binary_data = "" 
    pixels = img.load() 
 
    for y in range(img.height): 
        for x in range(img.width): 
            pixel = pixels[x, y] 
 
            for i in range(3): 
                binary_data += str(pixel[i] & 1) 
 
    #  تاتياب ىلإ ميسقت 
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)] 
 
    extracted_text = "" 
    for byte in all_bytes: 
        if byte == '00000000':  
            break 
        extracted_text += chr(int(byte, 2)) 
 
    return extracted_text 
def encr(arr_char,kays,mass) :
    encr_ms=[]
    for char in mass :
        if char in arr_char :
            kay= arr_char.index(char)
            char_en=kays[kay]
            encr_ms.append(char_en)
        else :
            encr_ms.append(char)
  
    return ''.join(encr_ms)
def decr(arr_char,kays,mass_en) :
    encr_ms=[]
    for char in mass_en :
        if char in kays :
            kay= kays.index(char)
            char_en=arr_char[kay]
            encr_ms.append(char_en)
        else :
            encr_ms.append(char)    
    return ''.join(encr_ms)

arr_char =['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
kays    = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','d','c','b','a']


 
text = extract_data("amh.png")
while True :

    print(" اضغط 1 للتشفير")
    print(" اضغط 2 لفك التشفير")
    print(" اضغط 3 للخفاء")
    print(" اضغط 4 للاظهار")
    print("للخروج اضغط 0")
    
    x =input("ENTER THE TAXT :")
    if x =="1" :
      mass=input("enter the massage ").lower()
      mass_en=encr(arr_char,kays,mass)
      print (mass_en)
    if x=="2" :
       massd=decr(arr_char,kays,mass_en)
       print(massd)

    if x=="3" :
      hide_data("am.png", "amh.png", mass_en)

    if x=="4":
        print(extract_data("amh.png"))
    if x=="0" :
        exit    




    

