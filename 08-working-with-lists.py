# 8-Dars Ro'yhat bilan ishlash
# Sana: 24.07.2025

# sort() metodi ro'yhatdagi malumotlarni alifbo tartibida joylashtiradi
# agar biror malumot katta harf bilan yozilgan bo'lsa alifboga qaramay
# birinchi o'ringa o'tib oladi

cars = ['audi', 'Bmw', 'general motors', 'mercades benz','tesla', 'volvo']
cars.sort()
print(cars)

# agar ro'yhatimizni alifbodan teskari tartibda chiqarmoqchi bo'lsak
# sort() methodi ichigan reverse argumentini qo'shamiz
# sort(reverse=True)

cars.sort(reverse=True)
print(cars)

# sorted metodi orqali esa ro'yhat ichidagi elementlarni o'zgartirmagan holatda
# consolega chiqarishimiz mumkin

print(sorted(cars))

print(sorted(cars, reverse=True))

sonlar = [2, 14, -3, 98, -145.3, 88, 71, 536]
print(sorted(sonlar, reverse=True))
print(sorted(sonlar))

# reverse() metodi ro'yhatdagi malumotlari teskari tartibga o'zgartiradi
cars.reverse()
print(cars)

# len() metodi esa ro'yhat uzunligini o'lchaydi

print(len(cars))
print(len(sonlar))

uzunlik = len(cars)

# range() metodi ma'lum bir oraliqdagi sonlarni qaytaradi

print(list(range(0, 10)))
sonlar = list(range(21, 31))
print(sonlar)

# range() metodi foydalanayotganimizda etibor beramizki ohirgi kiritayotgan
# elementimiz chiqmaydi misol yuqorida 31 yozdim lekin 30 gacha bitta kam chiqaradi

print(list(range(0, 11))) # 0 dan 10 gacha chiqaradi 11 kirmaydi!
print(list(range(99, 150))) # 99 dan 150 gacha 150 kirmaydi 

# range() metodidan foydalanganda biz qadamlarni ham berishimiz mumkin
toq_sonlar = list(range(1, 20, 2)) # qadamni 2 tadan oldi
print(toq_sonlar)

# juft_sonlar = list(range(2, 20, 2)) #2 qadamdan oldi va juft sonlar chiqdi
print(juft_sonlar)

sanash = list(range(0, 101, 10))
print(sanash)

# max() min() sum() 

narxlar = [4000, 7500, 60_000, 12_000, 25_000]
arzon = min(narxlar)
qimmat = max(narxlar)
jami = sum(narxlar)
print(f"Eng arzon {arzon}, eng qimmat {qimmat}, jami summa {jami}")

#Ro;yhatni Kesish

print(cars[0:3]) #belgilangan index bo'yicha chiqaradi
print(cars[3:-1])
print(cars[:-2]) # agar birinchi qiymatni bermasak automatic 0 qiymatdan hisoblaydi
print(cars[:]) #boshidan ohirigacha Kesadi
print(cars[1:]) # 2- qiymatni bermasaK automatic ohirgi qiymatgacha Kesib oladi 

# Ro'yhatdan nusxa olish 

my_cars = cars[:] #listdan nusxa olish
my_cars = cars # bitta listga 2 ta nom berish

print(cars)
print(my_cars)

my_cars.remove('volvo')
print(my_cars)

my_cars[0] = 'lacetti'
print(my_cars)

# TUPLE - bu o'zgarmas ro'yhat. listning boshqacha turi

toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
print(toys)

print(toys[0])
print(toys[-1])
print(toys[3])
print(toys[1:3])
print(toys[:4])
print(toys[2:])
print(toys[:])

# TUPLE list bu o'zgarmas ro'yhat bo'lganligi uchun uni ichidagi elementlarini
# o'zgartirb , qo'shib yoki o'chirib bo'lnmaydi.
# Agarda shunday qilmoqchi bo'lsaK ham uning turini oddiy listga
# o'zgartirib olish KeraK.

print(type(toys))
toys = list(toys) #tupleni listga o'zgartirish
print(type(toys))

toys.append("teddy")
print(toys)

toys = tuple(toys)

print(type(toys))

#AMALIYOT

davlatlar = ['Angliya', 'Hindiston', "Afg'oniston", 'Fransiya', 'Germaniya', 'Korea', "Qozog'iston"]
print(davlatlar)

print(len(davlatlar))

print(sorted(davlatlar))

davlatlar.reverse()
print(davlatlar)

davlatlar.sort(reverse=True)
print(davlatlar)

davlatlar.sort()
print(davlatlar)

davlatlar.sort(reverse=True)
print(davlatlar)

juftlar = list(range(120, 1201, 2))
print(juftlar)

juftlar_yigindisi = sum(juftlar)
print(juftlar_yigindisi)
print(sum(juftlar))

juftlar_max = max(juftlar)
juftlar_min = min(juftlar)
print(f"{juftlar_max}-{juftlar_min}={juftlar_max-juftlar_min}")
print(len(juftlar))

print('Boshidan 20 ta:', juftlar[:20])
print("O'rtasidan 20 ta:", juftlar[250:270])
print('Oxiridan 20 ta:', juftlar[-20:])

taomlar = ['palov', 'mastava', 'norin', "lag'mon", "Kabob"]
print(taomlar)

nonushta = taomlar[:]

print(nonushta)
nonushta.remove('mastava')
nonushta.remove("lag'mon")
nonushta.append("shiringuruch")
nonushta.append('quymoq')

print(taomlar)
print(nonushta)

nonushta = tuple(nonushta)
nonushta[0] = 'non va qaymoq'

nonushta = list(nonushta)

sonlar = []
sonlar.append(int(input(f"{len(sonlar)+1} -sonni Kiriting:\n>>>")))
sonlar.append(int(input(f"{len(sonlar)+1} -sonni Kiriting:\n>>>")))
sonlar.append(int(input(f"{len(sonlar)+1} -sonni Kiriting:\n>>>")))
sonlar.append(int(input(f"{len(sonlar)+1} -sonni Kiriting:\n>>>")))
sonlar.append(int(input(f"{len(sonlar)+1} -sonni Kiriting:\n>>>")))
sonlar.append(int(input(f"{len(sonlar)+1} -sonni Kiriting:\n>>>")))
sonlar.append(int(input(f"{len(sonlar)+1} -sonni Kiriting:\n>>>")))
sonlar.append(int(input(f"{len(sonlar)+1} -sonni Kiriting:\n>>>")))
sonlar.append(int(input(f"{len(sonlar)+1} -sonni Kiriting:\n>>>")))
sonlar.append(int(input(f"{len(sonlar)+1} -sonni Kiriting:\n>>>")))

print('Siz Kiritgan sonlar: ', sonlar, 'TesKari tartibda ', sorted(sonlar, reverse=True))




