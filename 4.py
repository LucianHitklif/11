number = int(input("Введите натуральное число: "))
last = number%10
count3 = 0
count_last = 0
even = 0
summ_5 = 0
produc7 = 1
less7 = False
count05 = 0

while True:
    num = number % 10
    if num == 3:
        count3 += 1
    if num == last:
        count_last += 1
    if num%2 == 0:
        even += 1
    if num > 5:
        summ_5 += num
    if num > 7:
        produc7 *= num
        less7 = True
    if num == 0 or num == 5:
        count05 += 1
    number //= 10
    if number == 0:
        break

print(f"цифр 3: {count3}")
print(f"последняя цифра встречается: {count_last} раз")
print(f"кол-во четных цифр: {even}")
print(f"сумма цифр больше 5: {summ_5}")
print(f"произведение цифр больше 7: {produc7}")
print(f"сколько встречаются цифры 0 и 5: {count05}")
