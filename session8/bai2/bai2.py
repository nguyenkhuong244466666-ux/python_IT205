# ==========================================
# PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
# ==========================================

# Input:
# - Lựa chọn menu (1-5)
# - Tên shop
# - Tên sản phẩm
# - Mô tả sản phẩm
# - Danh mục sản phẩm
# - Danh sách từ khóa
# - Mã giảm giá
# - Từ khóa cần tìm và thay thế

# Output:
# - Thông tin sản phẩm đã được chuẩn hóa
# - Tên shop chuẩn hóa
# - Kết quả kiểm tra mã giảm giá
# - Kết quả tìm kiếm và thay thế từ khóa
# - Thông báo lỗi khi dữ liệu không hợp lệ

# Giải pháp:
# - Sử dụng vòng lặp while True để tạo menu.
# - Sử dụng match-case để xử lý các chức năng.
# - Dùng strip() để xóa khoảng trắng thừa.
# - Dùng title() để chuẩn hóa tên sản phẩm.
# - Dùng lower() và upper() để chuyển đổi chữ hoa/thường.
# - Dùng split() để tách danh sách từ khóa.
# - Dùng replace() để thay thế từ khóa.
# - Dùng len() để tính độ dài chuỗi và số lượng từ khóa.
# - Kiểm tra dữ liệu hợp lệ trước khi xử lý.

# Thuật toán:
# B1. Hiển thị menu.
# B2. Người dùng chọn chức năng.
# B3. Kiểm tra lựa chọn hợp lệ.
# B4. Thực hiện chức năng tương ứng:
#     - Nhập và thống kê sản phẩm.
#     - Chuẩn hóa tên shop.
#     - Kiểm tra mã giảm giá.
#     - Tìm kiếm và thay thế từ khóa.
# B5. Quay lại menu.
# B6. Nếu chọn 5 thì kết thúc chương trình.

shop_name = ""
product_name = ""
description = ""
category = ""
keywords = []

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM =====")
    print("1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê")
    print("2. Chuẩn hóa tên Shop")
    print("3. Kiểm tra mã giảm giá hợp lệ")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả sản phẩm")
    print("5. Thoát chương trình")

    choice = input("Chọn chức năng: ")


    match choice:

        case "1":
            shop_name = input("Nhập tên shop: ")

            if shop_name.strip() == "":
                print("Tên shop không được bỏ trống")
                continue

            product_name = input("Nhập tên sản phẩm: ")
            description = input("Nhập mô tả sản phẩm: ")

            if description.strip() == "":
                print("Mô tả sản phẩm không được rỗng")
                continue

            category = input("Nhập danh mục sản phẩm: ")
            keyword_input = input("Nhập danh sách từ khóa (cách nhau bởi dấu phẩy): ")

            clean_shop = shop_name.strip()
            clean_product = product_name.strip().title()
            clean_description = description.strip()
            clean_category = category.strip().lower()

            keywords = []
            for keyword in keyword_input.split(","):
                keywords.append(keyword.strip())

            print("\n===== BÁO CÁO THỐNG KÊ =====")
            print("Tên shop:", clean_shop)
            print("Tên sản phẩm:", clean_product)
            print("Mô tả sản phẩm:", clean_description)
            print("Độ dài mô tả:", len(clean_description))
            print("Danh mục:", clean_category)
            print("Danh sách từ khóa:", keywords)
            print("Số lượng từ khóa:", len(keywords))
            print("Mô tả chữ thường:", clean_description.lower())
            print("Mô tả chữ hoa:", clean_description.upper())

        case "2":
            original_shop = input("Nhập tên shop: ")

            if original_shop.strip() == "":
                print("Tên shop không được bỏ trống")
                continue

            normalized_shop = original_shop.strip().lower()
            normalized_shop = "-".join(normalized_shop.split())

            if not normalized_shop.startswith("shop-"):
                normalized_shop = "shop-" + normalized_shop

            print("Tên shop ban đầu:", original_shop)
            print("Tên shop chuẩn hóa:", normalized_shop)

        case "3":
            discount_code = input("Nhập mã giảm giá: ")

            if discount_code == "":
                print("Mã giảm giá không được rỗng")

            elif " " in discount_code:
                print("Mã giảm giá không được chứa khoảng trắng")

            elif len(discount_code) < 6 or len(discount_code) > 12:
                print("Mã giảm giá phải có độ dài từ 6 đến 12 ký tự")

            elif discount_code != discount_code.upper():
                print("Mã giảm giá phải được viết hoa toàn bộ")

            elif not discount_code.isalnum():
                print("Mã giảm giá chỉ được chứa chữ cái và chữ số")

            elif not discount_code.startswith("SALE"):
                print("Mã giảm giá phải bắt đầu bằng SALE")

            else:
                print("Mã giảm giá hợp lệ")

        case "4":
            if description.strip() == "":
                print("Chưa có mô tả sản phẩm")
                continue

            find_keyword = input("Nhập từ khóa cần tìm: ")
            replace_keyword = input("Nhập từ khóa thay thế: ")

            keyword_count = description.count(find_keyword)

            if keyword_count > 0:
                new_description = description.replace(
                    find_keyword,
                    replace_keyword
                )

                print("Số lần xuất hiện của từ khóa:", keyword_count)
                print("Mô tả sau khi thay thế:")
                print(new_description)

            else:
                print("Không tìm thấy từ khóa")

        case "5":
            print("Thoát chương trình")
            break

        case _:
            print("Lựa chọn không hợp lệ")