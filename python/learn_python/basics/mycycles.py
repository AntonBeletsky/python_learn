print("Введите 2 числа")
n = int(input())
m = int(input())

i = 0; j = 0;

print(" ======================================================")

while i < n:
    i += 1
    print('   ', end='')
    print('*' * m, end='\n')

print(" ======================================================")


str = "ne9hi4hg943hig34ilgbh4839*oghi43hgio34yh9gy439tyy349tyu934uy93"
a = 0
ch = chr(0)

for ch in str:
    if ch == '*':
        print(a, end="")
        print(" before *")
        break
    else:
        print(a, end=' ')

    a += 1
    pass

print(" ======================================================")

#  https://pythonworld.ru/osnovy/vstroennye-funkcii.html
# https://pythonworld.ru/osnovy/klyuchevye-slova-modul-keyword.html
