while True:
    print(f"+{"="*50}+")
    print("|          HỆ THÔNG QUẢN LÝ NỘI DUNG TIKTOK        |")
    print(f"+{"="*50}+")
    print("|  1. Nhập và phân tích  thông tin video           |")
    print("|  2. Chuân hóa tên tài khoản                      |")
    print("|  3. Kiem tra tính hợp lệ của hashtag             |")
    print("|  4. Tìm kiem và thay the từ khoa trong mô tả     |")
    print("|  5. Thoát chương trình                           |")
    print(f"+{"="*50}+")
    choice=input("==> Mời bạn chọn (1-5): ")

    match choice:
        case "1":
            account_name = input("Nhập vào tên tài khoản: ")
            title = input("Nhập vào tiêu đề: ")
            description = input("Nhập vào mô tả: ")
            list_hashtag = input("Nhâp vào ds hashtag: ")

            print(f"Tên tài khoản: {account_name.strip()}")
            print(f"Tiêu đề: {title.title().strip()}")
            print(f"Mô tả: {description.strip()}")
            print(f"Độ mô tả video: {len(description)}")

            count_space = description.count(" ")
            print(f"Số lượng từ trong mô tả: {count_space + 1}")

            temp_list_hashtag = list_hashtag.split(",")
            new_list_hashtag ="".join(temp_list_hashtag)
            print(f"Danh sách hashtag sau khi chuẩn hóa khoảng trắng: {new_list_hashtag}")

            count_hashtag = list_hashtag.split(",")
            print(f"Số lượng hashtag: {len(count_hashtag)}")

            print(f"Mo tả video chuyến thành chữ thường {description. lower()}")
            print(f"Mô tả video chuyến thành chữ hoa {description. upper()}")
        case "2":
            print (f"Tên tài khoản ban đầu: {account_name}")
            print (f"Tên tài khoản được chuẩn hoa: @{account_name. lower()}")
        case "3":
            new_hashtag = input("Nhập vào hashtag mới: ")
            if (len(new_hashtag) == 0):
                print ("Không được rỗng!")
            elif (not new_hashtag. startswith("#") ):
                print ("Phải bắt đầu bằng dấu #")
            elif (" " in new_hashtag):
                print ( 'Khong được chua khoảng trắng')
            elif (len(new_hashtag < 2)):
                print("Hashtag khong đuoc be hơn 2 ki tu")
            else:
                print("Hashtag hợp lệ!")
                list_hashtag = list_hashtag + new_hashtag
                print(f"Danh sach hashtag moi {list_hashtag}")
        case "4":
            find_word = input ("Nhap vao từ khóa cần tìm: ")
            replace_word = input ("Nhap vao từ khoa cần thay thế: ")
            count_word = description.count(find_word. lower())
            if (count_word > 0):
                description = description.replace(find_word, replace_word)
                print(f"Mô tả sau khi thay thế: {description}")
            print (f"Số lượng từ tìm đưoc la: {count_word}")
        case "5":
            print("đã thoát chương trình")
            break
        case _ :
            print("lựa chọn không hợp lệ!!!")



    