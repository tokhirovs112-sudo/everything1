
class Service:
    def __init__(self, model, brand, balance=2200):
        self.model = model
        self.brand = brand
        self.balance = balance

    def buy_phone(self):
        g = input("""
        Bizda mavjud bo'lgan Iphone 16 narxlari:

        1. 1600$ (blue)
        2. 1500$ (black)

        0. Orqaga qaytish
        """)

        if g == "1" and self.balance >= 1600:
            print("Sotib olindi")
            self.balance -= 1600

        elif g == "2" and self.balance >= 1500:
            print("Sotib olindi")
            self.balance -= 1500
        elif g == "0":
            return
        elif g == "1" or g == "2":
            print("Balansingiz yetarli emas!")
        else:
            print("Xatolik yuz berdi!")

        print("Balansingizda", self.balance, "qoldi")

        w = input("""Boshqa xizmatlardan foydalanishni istaysizmi? 
                    1. Ha
                    2. Yo'q""")
        if w == "1":
            self.service_types()
        elif w == "2":
            print("Xizmatimizdan foydalanganingiz uchun rahmat!")

    def sell_phone(self):
        r = input("""
        Biz sotib oladigan telefon turlari:

        1. Iphone
        2. Redmi
        3. Samsung

        0. Ortga qaytish
        """)

        if r == "1":
            self.balance += 1400
            print("Sotib oldik")
        elif r == "2":
            self.balance += 400
            print("Sotib oldik")
        elif r == "3":
            self.balance += 600
            print("Sotib oldik")
        elif r == "0":
            return
        else:
            print("Xatolik yuz berdi!")
            return
        print("Balansingiz", self.balance, "ga o'zgardi")
        q = input("""Boshqa xizmatlardan foydalanishni istaysizmi? 
                    1. Ha
                    2. Yo'q""")
        if q == "1":
            self.service_types()
        elif q == "2":
            print("Xizmatimizdan foydalanganingiz uchun rahmat!")

    def repair_phone(self):
        t = input("""
        Bizda tuzatadigan telefon turlari:

        1. Iphone (Ekran almashtirish): 100
        2. Redmi (Aksessuarlar): 20
        3. Samsung (Registratsiyadan o'tlazish): 50

        0. Ortga qaytish
        """)
        if t == "1":
            print("Ekran almashtirildi!")
            self.balance-=100
        elif t == "2":
            print("Aksessuarlar qo'yildi!")
            self.balance-=20
        elif t == "3":
            print("Registratsiyadan o'tkazildi!")
            self.balance-=50
        elif t == "0":
            return
        else:
            print("Xatolik yuz berdi")
        print("Balansingiz", self.balance, "ga o'zgardi")
        p = input("""Boshqa xizmatlardan foydalanishni istaysizmi? 
                    1. Ha
                    2. Yo'q""")
        if p == "1":
            self.service_types()
        elif p == "2":
            print("Xizmatimizdan foydalanganingiz uchun rahmat!")

    def service_types(self):
        a = input("""
        ============ PHONE SERVICE ============

        1. Telefon sotib olish
        2. Telefon sotib yuborish
        3. Telefon tuzatish
        0. Chiqish
        """)

        if a == "1":
            self.buy_phone()
        elif a == "2":
            self.sell_phone()
        elif a == "3":
            self.repair_phone()
        elif a == "0":
            print("Xizmatdan foydalanganingiz uchun rahmat!")
        else:
            print("Xatolik yuz berdi!")

b = Service(16, "Iphone")
b.service_types()