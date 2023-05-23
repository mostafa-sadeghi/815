# * * * * * 
# for i in range(5):
#     print("*", end=" ")

# exercise 1: 
# با سه حلقه فور
'''
* * * * * * * * * *
* * * * *
* * * * * * * * * * * * * * * * * * * *
'''
# for i in range(10):
#     print("*", end=" ")
# print()
# for i in range(5):
#     print("*", end=" ")
# print()
# for i in range(20):
#     print("*", end=" ")




# exercise 2:
'''
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
'''
for row in range(8):
    for col in range(10):
        print("*", end=" ")
    print()