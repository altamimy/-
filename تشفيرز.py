def encr(mass,kay):
    mass_en= ""
    for char in mass :
        mass_ch =ord(char)
        mass_isc = mass_ch + kay 
        isc_char= chr(mass_isc)
        mass_en +=isc_char
    return mass_en
def ma (mass_enc ,kay) :
    mass_en= ""
    for char in mass_enc :
        mass_ch =ord(char)
        mass_isc = mass_ch - kay 
        isc_char= chr(mass_isc)
        mass_en +=isc_char
    return mass_en


mass= input("enter your massige :")
kay = int(input("enter your kay :"))
if kay > 26 :
            kay = kay%26
mass_enc = encr(mass, kay)
print("the encryption massage : " , mass_enc )
print("the decryption massage : " , ma(mass_enc , kay) )

    