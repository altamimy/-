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

arr_char =['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"1","2","3","4","5","6","7","8","9","0",",",".","/",";"," ","[","]",":","<",">"]
kays    = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','d','c','b','a',"7","8","9","0",",",".","/","[","]",":","<",">","1","2","3","4","5","6",";","&"]
mass=input("enter the massage :\n").lower()
mass_en=encr(arr_char,kays,mass)
print ("the encrp massage :\n", mass_en)
massd=decr(arr_char,kays,mass_en)
print("the massage :\n",massd)