# if

print('learn if')

a = int(input())
if a < -5:
    print('Low')
elif -5 <= a <= 5:
    print('Mid')
else:
    print('High')

print("================================================")

# Проверка истинности в Python
# Любое число, не равное 0, или непустой объект - истина.
# Числа, равные 0, пустые объекты и значение None - ложь
# Операции сравнения применяются к структурам данных рекурсивно
# Операции сравнения возвращают True или False
# Логические операторы and и or возвращают истинный или ложный объект-операнд

if ( 2 and 2 or 3 or (1 and 1) ):
    print('223')

print("================================================")

if( 0 and 2 or 0 or (True and False)):
    print('32201')
else:
    print('kurwa ruska ja pierdole')

print("================================================")
print("input not 0")

value = int(input())

# is not

if (value is not 0):
    print("you data not 0")
else:
    print("you data == 0")

print("=======================================")
print ("URDL")

x = input()

if x in ("abc"):
    print("X in abc")
else:
    print("X not in abc")

if x in ("a","b","c"):
    print("X in abc")
else:
    print("X not in abc")
    
print("=======================================")
