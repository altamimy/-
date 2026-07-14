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
def enc (mass,kay) :
    mass_re=mass.replace(" ","_")
    num_col=kay
    anc_maas=[""]*num_col
    for col in range(num_col) :
        pont = col
        while pont<len(mass_re) :
            anc_maas[col]+=mass_re[pont]
            pont+=num_col 
    return "".join(anc_maas)
def dec (mass_enc,kay) :
        mass_rem=mass_enc.replace("_"," ")
        num_col=kay 
        anc_mass=[""]*num_col
        for col in range(num_col) :
            pont = col
            while pont<len(mass_re) :
                anc_maas[col]+=mass_re[pont]
                pont-=num_col 
        return "".join(anc_mass)

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
      

      kay =int(input("enter the kay :"))

      mass_en=enc(mass,kay)
      print (mass_en)
    if x=="2" :
       massd=dec(mass_en,kay)
       print(massd)

    if x=="3" :
      hide_data("mnm.png", "mnmh.png", mass_en)

    if x=="4":
        print(extract_data("mnmh.png"))
    if x=="0" :
        exit    




    

