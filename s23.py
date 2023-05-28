# x = 1
# print(type(x))
# x = 1.5
# print(type(x))
# x = '1.5'
# print(type(x))
# x = True
# print(x)

x = [1,2]
print(type(x))

z = x[0] + x[1]
print(z)

print(sum(x))

total = 0
for i in range(len(x)):
    total += x[i]
print(total)

total = 0
for number in x:
    total = total + number
print(total)

# تمرین:
# برنامه ای بنویسید که سه عدد از ورودی بگیرد و در یک لیست ذخیره نماید
# سپس با چهار روش بالا، مجموع اعداد موجود در لیست را محاسبه نمائید.