alfavit = 'АБВГДЕЁЖЗИЙУЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийулмнопрстуфхцчшщъыьэюя'

def get_mode():
    while True:
        mode = input('Зашифровать или расшифровать?: ').lower()
        if mode in ['зашифровать','расшифровать','р','з']:
            return mode
        else:
            print('Введи то что хочешь сделать')
def get_mes():
    message = input('Введи текст: ')
    return message

max_key = len(alfavit)

def get_key():
    key = 0
    while True:
        key = int(input("Введи ключ: "))
        if key>=1 and key<max_key:
            return key
def get_translated(mode, message, key):
    translate = ''
    if mode == 'расшифровать' or 'р':
        key = -key
    else:
        key = key

    for i in message:
        alfavit_mesto = alfavit.find(i)
        if alfavit_mesto == -1:
            translate += i
        else:
            alfavit_mesto += key
            if alfavit_mesto >= len(alfavit):
                alfavit_mesto += len(alfavit)
            elif alfavit_mesto < 0:
                alfavit_mesto += len(alfavit)

            translate += alfavit[alfavit_mesto]
    print(translate)

mode = get_mode()
message = get_mes()
key = get_key()
print('Преобразованный текст:')
print(get_translated(mode,message,key))