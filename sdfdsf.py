import random
a = '0123456789ABCDEF1234567890GHIJKLM1234567890N0123456789OPQRSTUVWXYZ1234567890'
b = 0
key = '85AB8FBA4BA3CF3A1BABD5C073ADA172'

file_p = open('Passed.txt', 'w')
file_np = open('Not_passed.txt', 'w')
while True:
    key2 = ''
    b+=1
    for g in range(32):
        key2+=random.choice(a)
    if key == key2:
        file_p.write(f'{b}: {key2} passed')
        break
    elif key != key2:
        file_np.write(f'{b} not passed')
    print(b)