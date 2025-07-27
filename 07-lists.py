# LIST
# SANA: 23.07.2025

# Bo'sh list yaratish: listnomi = []

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
narhlar = [1200, 5893, 1245, -93412, 4.2]
sonlar = ['yetti', 'besh', 13, 83, -90]
ismlar = []

print(ismlar)

'''
List(ro'yhat) o'zgaruvchiga bir nechta qiymatlarni ro'yhat ma'lumotlarni
     yuklash mumkin bo'lgan ma'lumot turidir. list[]
     List ichidagi har bir alohida qiymat element index deb ataladi va 
     ularning tartibi 0 dan boshlandi 0. 1. 2. 3... umuman olganda,
     dasturlash tillarida sanaganda doimo sanoq 0 dan boshlanadi.
     
'''

print(mevalar[2])
print(mevalar[-1])

print(mevalar[0].upper())
print(mevalar[1].title())
print(mevalar[0].capitalize())
print(mevalar[0].lower())

# append() metodi har doim ro'yhatning ohiridan element qo'shadi

mevalar.append("anor")

# insert() metodi esa ro'yhatning ma'lum belgilangan qismiga qiymat qo'shadi
# b.uchun insert(0, 'malumot') qavs ichida index tartib raqamini va malumot/

mevalar.insert(0, 'bodom')

 # List nomini yozishda ohiriga -lar qo'shimchasi qo'shish muhim
# sababi, uning ro'yhatligini bilib turamiz. misol: cars = []
 

cars = ['Tico', 'Damas', 'Nexia3', 'BMW', "Malibu", "BYD", "HONDA"]
del cars[0] # del metodi list ichidagi indexdagi qiymatni o'chiradi
print(cars)

cars.remove("BMW") # remove() metodi list ichidagi elementni toppib o'chiradi
print(cars)

# remove() methodi agar listda ikkita bir xil element bor bo'lsa birinchisini o'chiradi

hayvonlar = ["Arslon", "Fil", "Maymun", "Zebra", "Bo'ri", "Fil", "Begemot"]
hayvonlar.remove('Fil')

print(hayvonlar)

# remove() metodi bn agar o'chirib tashlamoqchi bo'lsaK va listda bir xil 
# qiymatlar Ko'p bo'lsa u holda bu metodni qayta va qayta taKrorlashimiz KeraK

# pop() methodi listdagi qiymatlarni sug'urib olish imKonini beradi
bozorlik = ['un', "yog'", 'sabzi', 'piyoz', 'pomidor']
mahsulot = bozorlik.pop(1)

print(f'Men {mahsulot} sotib oldim.\nSotib olinmagan mahsulotlar {bozorlik}')

# agar pop() methodiga hech qanday index berilmasa ro'yhat ohiridan sug'uradi

# AMALIYOT


# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting

# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 


ismlar = []

ismlar.append(input("Do'stingizni ismini yozing:\n>>>"))
ismlar.append(input("Do'stingizni ismini yozing:\n>>>"))
ismlar.append(input("Do'stingizni ismini yozing:\n>>>"))

print(f"Salom {ismlar[0]}, bugun choyxonaga boramizmi?\n{ismlar[1]} choyxonaga bo'ladimi?")

sonlar = [21, 13, 54, -90, -0.5, -21.7]
print(sonlar[0] - sonlar[1])
print(sonlar[2] + sonlar[-1])

sonlar[2] = 'yigirma'

print(sonlar)
