product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn: ")

    match choice:

        case "1":
            if len(product_list) == 0:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                print("Danh sách sản phẩm hiện tại:")
                for i in range(len(product_list)):
                    print(
                        f"{i + 1}. Mã SP: {product_list[i]['product_id']} | "
                        f"Tên: {product_list[i]['product_name']} | "
                        f"Giá: {product_list[i]['price']} | "
                        f"Số lượng: {product_list[i]['quantity']}"
                    )

        case "2":
            product_id = input("Nhập mã sản phẩm: ").strip().upper()

            duplicate = False
            for product in product_list:
                if product["product_id"] == product_id:
                    duplicate = True
                    break

            if duplicate:
                print("Mã sản phẩm bị trùng")
            else:
                product_name = input("Nhập tên sản phẩm: ")

                price = input("Nhập giá sản phẩm: ")
                quantity = input("Nhập số lượng sản phẩm: ")

                if (not price.isdigit()) or int(price) <= 0:
                    print("Giá/Số lượng không hợp lệ")
                elif (not quantity.isdigit()) or int(quantity) <= 0:
                    print("Giá/Số lượng không hợp lệ")
                else:
                    product_list.append({
                        "product_id": product_id,
                        "product_name": product_name,
                        "price": int(price),
                        "quantity": int(quantity)
                    })

                    print("Thêm sản phẩm thành công")

        case "3":
            product_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()

            found = False

            for product in product_list:
                if product["product_id"] == product_id:
                    found = True

                    product_name = input("Nhập tên sản phẩm mới: ")

                    price = input("Nhập giá sản phẩm mới: ")
                    quantity = input("Nhập số lượng mới: ")

                    if (not price.isdigit()) or int(price) <= 0:
                        print("Giá/Số lượng không hợp lệ")
                    elif (not quantity.isdigit()) or int(quantity) <= 0:
                        print("Giá/Số lượng không hợp lệ")
                    else:
                        product["product_name"] = product_name
                        product["price"] = int(price)
                        product["quantity"] = int(quantity)

                        print("Cập nhật sản phẩm thành công")

                    break

            if found == False:
                print("Không tìm thấy mã sản phẩm cần cập nhật!")

        case "4":
            product_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()

            found = False

            for i in range(len(product_list)):
                if product_list[i]["product_id"] == product_id:
                    product_list.pop(i)
                    found = True
                    print("Xóa sản phẩm thành công")
                    break

            if found == False:
                print("Không tìm thấy mã sản phẩm cần xoá!")

        case "5":
            print("Thoát chương trình.")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")