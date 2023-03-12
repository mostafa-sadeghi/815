# x = 2 * 3

# string = 'abc' * 3

# print(string)

# string1 = 'asd'
# string2 = 'efg'

# print(string1 + string2)

# shopping_list = ['apple', 'banana', 'bread']
# shopping_list.append('tomato')

# print("shopping list:", shopping_list)

# print("first item in shopping list is:", shopping_list[0])
# print("second item in shopping list is:", shopping_list[1])
# print("third item in shopping list is:", shopping_list[2])
# item = input('enter product name:> ')
# shopping_list.append(item)
# print("shopping list:", shopping_list)

# exercise 1:
# برنامه ای بنویسید که اسامی چهار دانش آموز را از ورودی بگیرد و
# داخل یک لیست اضافه نماید
# لیست را پرینت کنید
# اولین اسم را از داخل لیست پرینت کنید
# آخرین اسم را از داخل لیست پرینت کنید.

s1 = input('enter student name> ')
s2 = input('enter student name> ')
s3 = input('enter student name> ')
s4 = input('enter student name> ')

students = []
students.append(s1)
students.append(s2)
students.append(s3)
students.append(s4)

print("students are:", students)
print("first student:", students[0])
print("last student:", students[3])