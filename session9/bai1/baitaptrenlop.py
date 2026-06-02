# students = ["Sang","Khương","Nhat nhi nhanh"]
# # for i in range(0,len(students)):
# #     print(f"sinh vieen thu {i+1}: {students[i]}")
# # i=1
# # for item in students:
# #     print(f"sinh vieen thu {i}: {item}")
# #     i+=1
# for index, value in enumerate(students, start=0):
#     print(f"sinh vieen thu {index+1}: {value}")
students = []
while True :
    print("1 thêm sinh viên")
    print("2 danh sách sv")
    print("3 thoát")
    choice = input("==> vui lòng chọn (1-3): ")
    match choice:
        case "1":
            stu_quantity = int(input("Nhập số lượng sinh viên: "))
            for i in range(1,stu_quantity+1):
                temp_students = input(f"Nhập sv thứ {i}: ")
                students.append(temp_students)
        case "2":
            print("===========================danh sách sv===========================")
            for index, value in enumerate(students, start=0):
                print(f"sinh viên thứ {index+1}: {value}")
            print("==================================================================")
        case "3":
            print("đã thoát!!!!!")
            break
        case _:
            print("vui long chọn (1-3)!!!!!")
