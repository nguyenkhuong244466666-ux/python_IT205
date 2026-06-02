cart_items = [
         ["P001", "Dien thoai iPhone 15", 1, 25000000],
         ["P002", "Op lung Silicon", 2, 150000]
]
while True:
    print("="*50)
    print("           SHOPEE CART MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("2. Thêm sản phẩm mới / Cộng dồn số lượng")
    print("3. Cập nhật số lượng của một sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")
    print("="*50)
    choice = input("Mời bạn chọn chức năng (1-5): ")
    match choice:
        case "1":
            print("--- CHI TIẾT SẢN PHẨM ---")
            print("STT| Mã SP | Tên Sản Phẩm           | SL | Đơn Giá         | Thành Tiền")
            print("-----------------------------------------------------------------------")
            for index, value in enumerate(cart_items, start=0):
                print(f"{index +1} | {cart_items[index] [0]} | {cart_items[index] [1]} | {cart_items [index] [2]} | {cart_items [index] [3]}        | {cart_items [index] [3]*cart_items [index] [2]}")


        case "2":
            product_id = input("Mã sản phẩm mới:I")
            product_name = input("Tên sản phẩm mới: ")
            product_quantity = int(input("Nhập số lượng: "))
            product_price = float (input ("Nhập đơn giá: "))
            flag = False
            for i in range(len(cart_items)):
                if (cart_items [i] [0] == product_id):
                    print("Mã sản phẩm nay đa ton tại, tiến hành cập nhật!")
                    cart_items [i] [2] += product_quantity
                    flag = True
                    break
            if (flag == False):
                cart_items.append( [product_id, product_name, product_quantity, product_price])
        case "3":
            new_product_id = input("Mã sản phẩm mới: ")
            new_product_quantity = int(input("Nhập số lượng: "))
            flag = False
            for i in range(len(cart_items)):
                if (cart_items[i] [0] == new_product_id):
                    cart_items [i] [2] = new_product_quantity
                    print("Đã cập nhật!")
                    flag = True
                    break
            if (flag == False):
                print ("Không tìm thấy !")
        case "4":
            new_product_id = input("nhập mã sản phẩm cần xóa: ")
            flag = False
            for i in range(len(cart_items)):
                if (cart_items[i] [0] == new_product_id):
                    cart_items.pop(i)
                    print("Đã xóa")
                    flag = True
                    break
            if (flag == False):
                print ("Không tìm thấy !")
        case "5":
            print("đã thoát !!!!")
            break
        case _:
            print()