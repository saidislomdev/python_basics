# ELIF operatori 
# Sana: 25/07/2025

"""
    if va else orqali biz faqatgina bitta shartni bajarilishini tekshirardik.
    Elif - operatorini biz bir nechta shartlarni tekshirishda ishlatamiz/
    
"""
son = -45 
if son < 0:
    print("Manfiy son!")
else:
    print("Musbat son!")
    
yosh = int(input("Yoshingizni Kiriting:\n>>>"))
if yosh <= 4:
    narh = 'bepul'
elif yosh<=12:
    narh=5000
else:
    narh=10000
print(f"Sizga kirish {narh}")

kun = input("Bugun qaysi kun?>>>")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print("Bugun dam olish Kuni!😉")
else:
    print("Bugun ish Kuni")
    
kun = input("Bugun qaysi Kun?>>>")
harorat = float(input("Havo harorati qanday?>>>"))

if kun.lower()=="yakshanba" and harorat>=30:
    print("Cho'milgani KetdiK 🤩")
elif kun.lower()=='yakshanba' and harorat < 30:
    print("Uyda dam olamiz!!!")
    
kun = input("Bugun kun qaysi?>>>")
harorat = float(input("Harorat necha gradus?"))
 
if kun.lower()=='yakshanba' or kun.lower()=='shanba' and harorat >= 30:
    print("Cho'milgani KetdiK!")
elif kun.lower()=="yakshanba" or kun.lower()=='shanba' and harorat < 30:
    print("Uyda qolamiz:(")

# BOOLEAN mantiqiy ma'lumot 

narh = 15000
choy = True
salat = False

if choy and salat:
    narh = narh + 10000
elif choy or salat:
    narh = narh + 5000
print(f"Jami {narh} so'm")

narh = 15000
choy = 1
salat = 0
non = 1
kompot = 1
assorti = 0

#Quyida har bir shart alohida tekshiriladi va bir biriga bog'liq emas

if choy:
    print("Mijoz choy oldi")
    narh = narh + 5000
if salat:
    print("Mijoz salat oldi")
    narh = narh + 5000
if non:
    print("Mijoz non oldi")
    narh = narh + 5000
if kompot:
    print("Mijoz kompot oldi")
    narh = narh + 5000
if assorti:
    print("Mijoz assorti oldi")
    narh = narh + 5000
print(f"Jami {narh} so'm")

# in operatori yordamida list ichidagi ma'lumotni bor yoki yo'qligini tekshirishimiz mumkin
menu = ["osh", "qozonkabob", 'shashlik', "norin", 'somsa']
'manti' in menu # menuda manti bormi?
ovqat = input("Nima ovqat yeysiz?")
if ovqat.lower() in menu:
    print("Buyurtma qabul qilindi")
else:
    print("Afsuski, bizda bunday ovqat yo'q")
    
# not in opertori yordamida list ichidagi ma'lumotni ro'yhatda bor yoki yo'qligini tekshirsak bo'ladi

menu = ["osh", "qozonkabob", 'shashlik', "norin", 'somsa']
buyurtmalar = []

if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Afsuski, menuda {taom} yo'q")
else:
    print("Kechirasiz, savatchangiz bo'sh")

#AMALIYOT

son = int(input("Juft son Kiriting:>>>"))
if son % 2 == 0:
    print("Rahmat!")
else:
    print("Bu son juft emas.")


yosh = int(input("Iltimos, yoshingizni Kiriting:>>>"))

if yosh <= 4 or yosh >= 60:
    print("Sizga chipta bepul, Kiravering😎")
elif yosh <= 18:
    print("Sizga bilet 10.000 so'm")
else:
    print("Sizga bilet 20.000 so'm")
    
son1 = int(input("Iltimos, birinchi sonni Kiriting:>>>"))
son2 = int(input("Iltimos, ikkinchi sonni Kiriting:>>>"))

if son1 > son2:
    print(f"{son1} > {son2}")
elif son1 < son2:
    print(f"{son1} < {son2}")
else:
    print(f"{son1} = {son2}")


mahsulotlar = ["sabzi", "piyoz", 'guruch', 'un', "yog'", 'kartoshka', 'loviya', 'mosh', 'grechka' ]

print('5 ta mahsulot yozing.')
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1} - mahsulotni qo'shing: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Do'konimizda {mahsulot} yo'q")
        
mahsulotlar = ["sabzi", "piyoz", 'guruch', 'un', "yog'", 'kartoshka', 'loviya', 'mosh', 'grechka' ]

print('5 ta mahsulot yozing.')
bor_mahsulotlar = []
mavjud_emas = []

for n in range(5):
    mahsulot = input(f"Savatga {n+1} - mahsulotni qo'shing: ")
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print(f"Quyidagi mahsulotlar do'konimizda yo'q:\n {mavjud_emas} ")

else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

foydalanuvchilar = ['admin', 'guli', 'alisher', 'suhrob', 'jahon']
login = input("Yangi login Kiriting:>>>")
if login not in foydalanuvchilar:
    print(f"Xush Kelibsiz, {login}!")
else:
    print("Login band, iltimos yangi login tanglang!")

son = int(input("Biror butun son Kiriting:>>>"))
for n in range(2,11):
    if son % n == 0:
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")



