cart_items = [
    {
        "id": "P001",
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
    },
    {
        "id": "P002",
        "name": "Op lung Silicon",
        "number": 2,
        "price": 150000
    }
]

while True:
    print("\n===== SHOPEE CART MANAGEMENT =====")
    print("1. Xem giỏ hàng")
    print("2. Thêm sản phẩm")
    print("3. Cập nhật số lượng")
    print("4. Xóa sản phẩm")
    print("5. Thoát")

    choice = input("Nhập lựa chọn: ")

    match choice:
        case "1":
           
            total_number = 0
            total_money = 0

            print("/n-----------CHI TIẾT GIỎ HÀNG-----------")
            print(f"{'STT':<5} | {'Mã sản phẩm':<20} | {'Tên sản phẩm':<30} | {'SL':<5} | {'Đơn giá':<20} | Thành tiền")
            for index, item in enumerate(cart_items, start=1):
                money = item["number"] * item["price"]

                print(f"{index :<5} | {item['id'] :<20} | {item['name']:<30} | {item['number']:<5} | {item['price']:<20} | {money}")

                total_number += item["number"]
                total_money += money

            print(f"\nTổng số lượng: {total_number}")
            print(f"Tổng tiền: {total_money}")

        case "2":
            product_id = input("Nhập mã sản phẩm: ")
            product_name = input("Nhập tên sản phẩm: ")

            while True:
                number = input("Nhập số lượng: ")
                price = input("Nhập đơn giá: ")

                if (number.isdigit()):
                    number = int(number)
                    break
                else:
                    print("bạn nhập không hợp lệ!!!")
            
            while True:
                price = input("Nhập đơn giá: ")

                if (price.isdigit()):
                    price = int(price)
                    break
                else:
                    print("bạn nhập không hợp lệ!!!")
                

            found = False

            for item in cart_items:
                if item["id"] == product_id:
                    item["number"] += number
                    found = True
                    print("có tồn tại, đã tăng số lượng sản phẩm!")
                    break

            if found==False:
                product = {
                    "id": product_id,
                    "name": product_name,
                    "number": number,
                    "price": price
                }

                cart_items.append(product)
                print("Thêm sản phẩm thành công!")

        case "3":
            product_id = input("Nhập mã sản phẩm cần cập nhật: ")
            while True:
                new_number = input("Nhập số lượng mới: ")
                if new_number.isdigit():
                    new_number = int(new_number)
                    break
                else:
                    print("bạn nhập không hợp lệ")
            found = False
            for item in cart_items:
                if item["id"] == product_id:
                    item["number"] = new_number
                    found = True
                    print("Cập nhật thành công!")
                    break

            if not found:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")

        case "4":
            product_id = input("Nhập mã sản phẩm cần xóa: ")

            found = False

            for item in cart_items:
                if item["id"] == product_id:
                    cart_items.remove(item)
                    found = True
                    print("Xóa sản phẩm thành công!")
                    break

            if not found:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")

        case "5":
            print("Thoát chương trình!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")