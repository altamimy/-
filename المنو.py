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
mass=input("enter the massage ").lower()
mass_en=encr(arr_char,kays,mass)
print (mass_en)
massd=decr(arr_char,kays,mass_en)
print(massd)