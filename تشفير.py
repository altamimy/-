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

mass =input("enter the massage :")
kay =int(input("enter the kay :"))
mass_enc=enc(mass,kay)
print(mass_enc)
        