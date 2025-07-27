#String

ism = 'Sayyora'
familiya = 'Sobirjonova'

viloyat = "Андижан"
shahar = 'Bo"ston'

# STRING USTIDA AMALLAR

print("Mening ismim " + ism)

print(ism+familiya)

print(ism + ' ' + familiya)

# F string

ism = "Zaynura"
familiya = 'Saidova'
ism_sharif = f"{ism} {familiya}"

print(ism_sharif)

ism = 'Sherzod'
familiya = "Akbaraliyev"
shahar = 'Krosnodar'

print(f"Salom mening ismim {ism} {familiya}. Men hozir {shahar}da yashayapman.")

print('Hello World!')
print('Hello \tWorld!')
print('Hello \nWorld!')

# String Methodlar

ism = 'Diyor'
familiya = 'Teshaboyev'
print(f'{ism} {familiya}')

ism_sharif = f'{ism} {familiya}'
print(ism_sharif.upper())
print(ism_sharif.lower())
print(ism_sharif.title())
print(ism_sharif.capitalize())

meva = '        uzum        '
print('Men ' + meva.lstrip() + " yeyishni yaxshi ko'raman.")
print('Men ' + meva.rstrip() + " yeyishni yaxshi ko'raman.")
print('Men ' + meva.strip() + " yeyishni yaxshi ko'raman.")
print('Men ' + meva + " yeyishni yaxshi ko'raman.")

ism = input('Ismingiz nima?')
print("Assalomu alaykum," + ism)

ism = input('Ismingiz nima?\n>>>')
print('Assalomu alaykum, ' + ism.title())

# Amaliyot


kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = 'Bodomzor'
viloyat = 'Samarqand'

print(f'{kocha} ko\'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati')

kocha = input('Ko\'changizni Kiritin:\n>>>')
mahalla = input('Mahallangizni Kiriting:\n>>>')
tuman = input('Tumaningizni Kiriting:\n>>>')
viloyat = input("Viloyatingizni Kiriting:>>>")
print(f"Sizning manzilingiz: {kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyatidansiz")

#ChatGpt berga muraKKab mashqlar


