import math

# التحقق من العدد الأولي
def is_prime(n):
    if n < 2 or (n % 2 == 0 and n != 2): return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0: return False
    return True

# الحصول على عدد أولي من المستخدم
def get_prime(msg):
    while True:
        try:
            n = int(input(msg))
            if is_prime(n): return n
            print("العدد ليس أوليًا، حاول مجددًا.")
        except: print("إدخال غير صالح.")

# إدخال e والتحقق من الشروط
def get_e(phi):
    while True:
        try:
            e = int(input(f"أدخل e (1 < e < {phi}): "))
            if 1 < e < phi and is_prime(e):
                try: return e, pow(e, -1, phi)
                except: print("لا يمكن حساب d، جرّب قيمة أخرى.")
            else: print("قيمة e غير صالحة.")
        except: print("إدخال غير صالح.")

# تحويل النص إلى كتل بناءً على حجم n
def split_into_blocks(msg, block_size):
    blocks = []
    for i in range(0, len(msg), block_size):
        blocks.append(msg[i:i+block_size])
    return blocks

# حساب أقصى حجم للكتلة بناءً على n (للتشفير بـ ASCII)
def calculate_max_block_size(n):
    # في نظام ASCII، كل حرف يمثله رقم من 0-127
    # لكننا نحتاج التأكد أن القيمة بعد التشفير لا تتجاوز n
    # نبحث عن أكبر k حيث 128^k < n
    max_size = 0
    while 128 ** (max_size + 1) < n:
        max_size += 1
    return max(1, max_size)  # على الأقل حرف واحد

# تشفير الرسالة مع تقسيمها إلى كتل
def encrypt_message(msg, e, n):
    # حساب حجم الكتلة المناسب
    block_size = calculate_max_block_size(n)
    print(f"حجم الكتلة المستخدم: {block_size} حرف")
    
    # تقسيم الرسالة إلى كتل
    blocks = split_into_blocks(msg, block_size)
    encrypted_blocks = []
    
    for block in blocks:
        # تحويل الكتلة إلى رقم (ASCII)
        num = 0
        for i, char in enumerate(block):
            num = num * 128 + ord(char)
        
        # تشفير الرقم
        encrypted_num = pow(num, e, n)
        encrypted_blocks.append(encrypted_num)
    
    return encrypted_blocks

# فك تشفير الرسالة
def decrypt_message(encrypted_blocks, d, n):
    # حساب حجم الكتلة المناسب
    block_size = calculate_max_block_size(n)
    decrypted_text = ""
    
    for encrypted_num in encrypted_blocks:
        # فك تشفير الرقم
        decrypted_num = pow(encrypted_num, d, n)
        
        # تحويل الرقم إلى نص
        block_text = ""
        for _ in range(block_size):
            # استخراج الحروف من اليمين إلى اليسار
            char_code = decrypted_num % 128
            if char_code >= 32:  # أحرف قابلة للطباعة فقط
                block_text = chr(char_code) + block_text
            decrypted_num //= 128
        
        # إزالة أي حشوات زائدة (أصفار)
        decrypted_text += block_text.strip('\x00')
    
    return decrypted_text

# البرنامج الرئيسي
def main():
    p = get_prime("أدخل p: ")
    q = get_prime("أدخل q: ")

    n = p * q
    phi = (p - 1) * (q - 1)
    print(f"n = {n}, φ(n) = {phi}")
    print(f"الحجم المتاح لكل كتلة: {calculate_max_block_size(n)} حرف")

    e, d = get_e(phi)
    print(f"\nالمفتاح العام: (e={e}, n={n})")
    print(f"المفتاح الخاص: (d={d}, n={n})")

    msg = input("\nأدخل رسالة (ASCII فقط): ")
    
    # التحقق من أن الرسالة تحتوي فقط على أحرف ASCII
    if any(ord(c) >= 128 for c in msg):
        print("الرجاء استخدام أحرف ASCII فقط (A-Z, a-z, 0-9, الرموز).")
        return
    
    # تشفير الرسالة
    enc = encrypt_message(msg, e, n)
    
    # فك تشفير الرسالة
    dec = decrypt_message(enc, d, n)
    
    print(f"\nالنص المشفر (كمجموعة أرقام): {enc}")
    print(f"النص بعد فك التشفير: {dec}")
    
    # التحقق من صحة النتيجة
    if msg == dec:
        print("✓ فك التشفير ناجح!")
    else:
        print("✗ فشل فك التشفير!")

if __name__ == "__main__":
    main()