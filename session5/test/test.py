# for i in range(5):
#     for j in range(i+1):
#         print("*", end=" ")
#     print() 
# canh=5
# for i in range(canh):
#     for j in range(canh-i):
#         if i == 1:
#             if j == 1 or j == 2:
#                 print(" ", end=" ")
#                 continue
#         print("*",end=" ")
#     for k in range(i+1):
#         print(" ", end=" ")
#     print() 


# for i in range(5):
#     for j in range(5-i-1):
#         print(" ",end=" ")
#     for k in range(i*2+1):
#         print("*",end=" ")
#     print()

number = int(input("nhập một số nguyên: "))
if number < 2:
    print("không phải số nguyên tố!!")
else: 
    for i in range(2,number):
        if number % i == 0: 
        print("không phải số nguyên tố!!")
        break



