# import random
# ACTIONS = ('rock', 'paper', 'scissors')
# computer_score = 0
# user_score = 0

# while True:
#     computer_choice = random.choice(ACTIONS)
#     user_choice = input('enter "rock" "paper" "scissors" ')

#     print(f"player's choice is: {user_choice}")
#     print(f"computer's choice is: {computer_choice}")

#     if user_choice == "rock":
#         if computer_choice == "paper":
#             computer_score += 1
#             print("computer is the winner!")
#         elif computer_choice == "scissors":
#             user_score += 1
#             print("player is the winner!")
#         else:
#             print("player and computer are both equal!")

#     elif user_choice == "paper":
#         if computer_choice == "scissors":
#             computer_score += 1
#             print("computer is the winner!")
#         elif computer_choice == "rock":
#             user_score += 1
#             print("player is the winner!")
#         else:
#             print("player and computer are both equal!")

#     elif user_choice == "scissors":
#         if computer_choice == "rock":
#             computer_score += 1
#             print("computer is the winner!")
#         elif computer_choice == "paper":
#             user_score += 1
#             print("player is the winner!")
#         else:
#             print("player and computer are both equal!")
#     print(f"player's score is: {user_score}")
#     print(f"computer's score is: {computer_score}")
#     print("Do you want to quit?(yes or no) ")
#     if input('> ') == "no":
#         break



# exercise1 : برنامه ای بنویسید که صد عدد تصادفی بین ده تا پانصد در لیستی اضافه نماید
# از لیست بالا مجموع اعداد را نمایش دهید
# از لیست بالا مجموع اعداد زوج را نمایش دهید
# از لیست بالا مجموع اعداد فرد را نمایش دهید


# import random

# all_numbers = []
# sum_of_even_numbers = 0
# sum_of_odd_numbers = 0
# for i in range(100):
#     new_number = random.randrange(10,501)
#     all_numbers.append(new_number)
#     if new_number % 2 == 0:
#         # sum_of_even_numbers = sum_of_even_numbers + new_number
#         sum_of_even_numbers += new_number
#     else:
#         sum_of_odd_numbers += new_number


# print("sum of all numbers:",sum(all_numbers))
# print("sum of even numbers:",sum_of_even_numbers)
# print("sum of odd numbers:",sum_of_odd_numbers)

# total = 0
# for i in range(len(all_numbers)):
#     total = total + all_numbers[i]

# print(total)








# برای نصب پای گیم
# در ترمینال دستور زیر را اجرا کنید
# pip install pygame


