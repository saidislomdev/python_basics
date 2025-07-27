# 6 - Dars SOnlar
# Sana: 23.07.2025

a = 20
b = 5.5
temp = 36.6
print(type(a))

aholi_soni = 7_567_893_392
print("Aholi sonI: ", aholi_soni)

x, y, z = 34, 23, -89

print(x,y,z)

c = a*b

print(c)

g =  20/5

print(g)

print(type(g))

''' Butun sonlar ( 2, 45, 80, 53) hech qanday nuqtasi bo'lmagan sonlar
 int - yani Integer deyiladi.
 Float sonlar bu o'nlik sonlar(4.6 / 23.8 / 43.1) dir.
 Float degani Floating point numbers yani suzuvchi nuqtali sonlar degani.
 Constanta degani bu o'zgarmas qiymatlar degani,
 boshqa dasturlash tillaridan farqli pythonda constantadagi qiymatlarni
 o'zgartirsa bo'ladi yani boshqa dasturlash tillarideK butunlay o'zgartirib
 bo'lmaydigan o'zgaruvchi emas.
 LeKin, barcha dasturchilar Kelishgan holda agar o'zgaruvchilar nomini
 katta harf bilan yozilsa constanta deyiladi va dasturlash favomida 
 ko'rib qolsak bunday qiymatlarga tegmaymiz.
'''

radius = 20
PI = 3.14159
diametr = 2*radius

print('Aylana uzunligi = ', PI*diametr)

print(type(PI))

ism = 'Jobir'
yosh = 36
xabar = ism + ' ' + str(yosh) + ' da'
print(xabar)
# str() funksiya orqali biz int larni matnga aylantira olamiz

yosh = str(yosh)

print(type(yosh))

t_yil = int(input("Tug'ilgan Kuningiz KUningizni Kiriting:\n>>> "))
yosh = 2025 - t_yil
print("Siz", yosh,"yoshda eKansiz.")

# input() funkisiyasi har doim foydalanuvchidan str ma'lumot oladi
# biz uni agar intga aylantirmoqchi bo'lsak int() funksiyasidan foydalanamiz

# AMALIYOT

# son = int(input('Istalgan sonni Kiriting:\n>>>'))
# print(f"{son} ning kvadrati {son**2} ga teng\n{son} ning kubi {son**3} ga teng.")

# yosh = int(input("Yoshingiz nechada?\n>>>"))
# print(f"Siz {2025-yosh} - yilda tug'ilgansiz.")

a = float(input('Birinchi sonni Kiriting:\n>>>'))
b = float(input("Ikkinchi sonni Kiriting:\n>>>"))

print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")

#Chatgpt bergan muraKKab mashqlar


