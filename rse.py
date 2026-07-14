import math

#التحقق من العدد الأولي
def is_prime(n):
    if n < 2 or (n % 2 == 0 and n != 2): return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0: return False
    return True

#الحصول على عدد أولي من المستخدم
def get_prime(msg):
    while True:
        try:
            n = int(input(msg))
            if is_prime(n): return n
            print("العدد ليس أوليًا، حاول مجددًا.")
        except: print("إدخال غير صالح.")

#إدخال e والتحقق من الشروط
def get_e(phi):
    while True:
        try:
            e = int(input(f"أدخل e (1 < e < {phi}): "))
            if 1 < e < phi and is_prime(e):
                try: return e
                except: print("لا يمكن حساب d، جرّب قيمة أخرى.")
            else: print("قيمة e غير صالحة.")
        except: print("إدخال غير صالح.")
        
            

#تشفير / فك التشفير (ASCII فقط)
def encrypt(msg, e, n):
    ms_en=" "
    encrypt_ms=[]
    for c in msg:
        encrypt_ms.append(pow(ord(c), e, n))
        en_ms=chr(encrypt_ms)
        ms_en+=en_ms
    return encrypt_ms

def decrypt(data, d, n):
    try:
        return ''.join(chr(pow(x, d, n)) for x in data)
    except ValueError:
        return "[خطأ: يحتوي النص على رموز غير مدعومة بالـ ASCII]"

#البرنامج الرئيسي
p = get_prime("أدخل p: ")
q = get_prime("أدخل q: ")

n = p * q
phi = (p - 1) * (q - 1)
print(f"n = {n}, φ(n) = {phi}")


e = get_e(phi)
d=pow(e,-1,phi)
print(f"\nالمفتاح العام: (e={e}, n={n})")
print(f"المفتاح الخاص: (d={d}, n={n})")

msg = input("\nأدخل رسالة (ASCII فقط): ")
for c in msg:
    if ord(c) < 128 :
        enc = encrypt(msg, e, n)
        dec = decrypt(enc, d, n)
    else:
        print(" الرجاء استخدام أحرف ASCII فقط (A-Z, 0-9, ...).")

print(f"\n encrypt: {enc}")
print(f"decrypt: {dec}")
