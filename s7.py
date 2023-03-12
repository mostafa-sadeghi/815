# numbers = [1, 2, 3, 4, 5]

#  تک تک اعداد لیست بالا را پرینت کنید
# سپس مجموع اعداد لیست بالا را مجاسبه و پرینت نمائید.

# print("number 1:",numbers[0])
# print("number 2:",numbers[1])
# print("number 3:",numbers[2])
# print("number 4:",numbers[3])
# print("number 5:",numbers[4])
# print("sum of all numbers:",numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4])

# print("sum of all numbers:",sum(numbers))


something = ['a', 'b', 'c']

something.append('d')

print("something:", something)

del something[1]
print("something:", something)

something.remove('c')
print("something:", something)

another = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(another[0:3])
print(another[3:6])
print("odd numbers:", another[::2])
print("even numbers:", another[1::2])
