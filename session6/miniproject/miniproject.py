qty_laptop = 0
qty_phone = 0
qty_tablet = 0

while True:

    print("\n===== HỆ THỐNG QUẢN LÝ KHO =====")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo hàng tồn kho thấp")
    print("5. Thoát chương trình")

    choice = input("Chọn chức năng: ")

    if choice == "1":

        print("\n===== BÁO CÁO TỒN KHO =====")

        print(f"Laptop ({qty_laptop}): ", end="")
        for i in range(qty_laptop):
            print("*", end="")
        print()

        print(f"Phone ({qty_phone}): ", end="")
        for i in range(qty_phone):
            print("*", end="")
        print()

        print(f"Tablet ({qty_tablet}): ", end="")
        for i in range(qty_tablet):
            print("*", end="")
        print()

    elif choice == "2":

        print("\n1. Laptop")
        print("2. Phone")
        print("3. Tablet")

        product = input("Chọn mặt hàng cần nhập: ")

        while True:

            quantity = int(input("Nhập số lượng cần thêm: "))

            if quantity < 0:
                print("Số lượng không hợp lệ, vui lòng nhập lại!")
                continue

            break

        if product == "1":
            qty_laptop += quantity
            print("Nhập kho Laptop thành công")

        elif product == "2":
            qty_phone += quantity
            print("Nhập kho Phone thành công")

        elif product == "3":
            qty_tablet += quantity
            print("Nhập kho Tablet thành công")

        else:
            print("Mặt hàng không hợp lệ")

    elif choice == "3":

        print("\n1. Laptop")
        print("2. Phone")
        print("3. Tablet")

        product = input("Chọn mặt hàng cần xuất: ")

        while True:

            quantity = int(input("Nhập số lượng cần xuất: "))

            if quantity < 0:
                print("Số lượng không hợp lệ, vui lòng nhập lại!")
                continue

            break

        if product == "1":

            if quantity > qty_laptop:
                print("Không đủ hàng")

            else:
                qty_laptop -= quantity
                print("Xuất kho Laptop thành công")

        elif product == "2":

            if quantity > qty_phone:
                print("Không đủ hàng")

            else:
                qty_phone -= quantity
                print("Xuất kho Phone thành công")

        elif product == "3":

            if quantity > qty_tablet:
                print("Không đủ hàng")

            else:
                qty_tablet -= quantity
                print("Xuất kho Tablet thành công")

        else:
            print("Mặt hàng không hợp lệ")

    elif choice == "4":

        print("\n===== CẢNH BÁO TỒN KHO THẤP =====")

        if qty_laptop < 10:
            print(f"[CẢNH BÁO] Laptop sắp hết (Chỉ còn {qty_laptop} sản phẩm)")

        if qty_phone < 10:
            print(f"[CẢNH BÁO] Phone sắp hết (Chỉ còn {qty_phone} sản phẩm)")

        if qty_tablet < 10:
            print(f"[CẢNH BÁO] Tablet sắp hết (Chỉ còn {qty_tablet} sản phẩm)")

    elif choice == "5":

        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ")