# 1. INPUT
# - Lựa chọn menu (1 - 5)
# - Tên người gửi
# - Số điện thoại người gửi
# - Địa chỉ lấy hàng
# - Tên người nhận
# - Số điện thoại người nhận
# - Địa chỉ giao hàng
# - Mã đơn hàng
# - Ghi chú giao hàng
# - Từ khóa cần tìm
# - Từ khóa thay thế

# 2. OUTPUT
# - Báo cáo thông tin đơn hàng đã chuẩn hóa
# - Mã đơn hàng sau khi chuẩn hóa
# - Số điện thoại đã được ẩn thông tin
# - Kết quả tìm kiếm và thay thế từ khóa
# - Các thông báo lỗi khi dữ liệu không hợp lệ

# 3. GIẢI PHÁP
# - Sử dụng vòng lặp while True để hiển thị menu liên tục.
# - Sử dụng match-case để xử lý từng chức năng.
# - Dùng strip() để loại bỏ khoảng trắng đầu cuối.
# - Dùng title() để chuẩn hóa tên người gửi và người nhận.
# - Dùng split() và join() để chuẩn hóa địa chỉ.
# - Dùng upper() để chuẩn hóa mã đơn hàng.
# - Dùng replace() để thay khoảng trắng bằng dấu "-".
# - Dùng isdigit() để kiểm tra số điện thoại hợp lệ.
# - Dùng len() để kiểm tra độ dài số điện thoại và ghi chú.
# - Dùng count() để đếm số lần xuất hiện từ khóa.
# - Dùng replace() để thay thế từ khóa trong ghi chú.
# - Kiểm tra dữ liệu hợp lệ trước khi xử lý.

# 4. THUẬT TOÁN
# Bước 1: Hiển thị menu chức năng.
#
# Bước 2: Người dùng chọn chức năng.
#
# Bước 3:
# - Nếu chọn 1:
#   + Nhập thông tin đơn hàng.
#   + Kiểm tra dữ liệu rỗng.
#   + Chuẩn hóa dữ liệu.
#   + Hiển thị báo cáo thống kê.
#
# - Nếu chọn 2:
#   + Nhập mã đơn hàng.
#   + Chuẩn hóa mã theo yêu cầu.
#   + Hiển thị kết quả.
#
# - Nếu chọn 3:
#   + Kiểm tra số điện thoại người gửi và người nhận.
#   + Nếu hợp lệ thì ẩn thông tin.
#   + Nếu không hợp lệ thì thông báo lỗi.
#
# - Nếu chọn 4:
#   + Kiểm tra đã có ghi chú giao hàng hay chưa.
#   + Nhập từ khóa cần tìm và thay thế.
#   + Tìm kiếm trong ghi chú.
#   + Nếu tồn tại thì thay thế và hiển thị kết quả.
#   + Nếu không tồn tại thì thông báo.
#
# - Nếu chọn 5:
#   + Hiển thị "Thoát chương trình".
#   + Kết thúc chương trình bằng break.
#
# Bước 4: Quay lại menu cho đến khi người dùng chọn thoát.

sender_name = ""
sender_phone = ""
pickup_address = ""
receiver_name = ""
receiver_phone = ""
delivery_address = ""
order_code = ""
delivery_note = ""


def normalize_spaces(text):
    return " ".join(text.strip().split())


def mask_phone(phone):
    if phone == "":
        print("Số điện thoại không được bỏ trống")
        return None

    if not phone.isdigit():
        print("Số điện thoại không hợp lệ")
        return None

    if len(phone) != 10:
        print("Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
        return None

    return phone[:3] + "*****" + phone[-2:]


while True:
    print("\n+==============================================================+")
    print("|            HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS            |")
    print("+==============================================================+")
    print("| 1. Nhập dữ liệu đơn hàng và xem báo cáo thống kê             |")
    print("| 2. Chuẩn hóa mã đơn hàng                                     |")
    print("| 3. Ẩn số điện thoại khách hàng                               |")
    print("| 4. Tìm kiếm và thay thế từ khóa trong ghi chú giao hàng      |")
    print("| 5. Thoát chương trình                                        |")
    print("+==============================================================+")

    choice = input("\n> Mời bạn chọn chức năng (1-5): ")

    match choice:

        case "1":
            sender_name = input("Tên người gửi: ")
            sender_phone = input("Số điện thoại người gửi: ")
            pickup_address = input("Địa chỉ lấy hàng: ")
            receiver_name = input("Tên người nhận: ")
            receiver_phone = input("Số điện thoại người nhận: ")
            delivery_address = input("Địa chỉ giao hàng: ")
            delivery_note = input("Ghi chú giao hàng: ")

            if sender_name.strip() == "":
                print("Tên người gửi không được bỏ trống")
                continue

            if sender_phone.strip() == "":
                print("Số điện thoại người gửi không được bỏ trống")
                continue

            if pickup_address.strip() == "":
                print("Địa chỉ lấy hàng không được bỏ trống")
                continue

            if receiver_name.strip() == "":
                print("Tên người nhận không được bỏ trống")
                continue

            if receiver_phone.strip() == "":
                print("Số điện thoại người nhận không được bỏ trống")
                continue

            if delivery_address.strip() == "":
                print("Địa chỉ giao hàng không được bỏ trống")
                continue

            if delivery_note.strip() == "":
                print("Ghi chú giao hàng không được bỏ trống")
                continue

            sender_name = normalize_spaces(sender_name).title()
            receiver_name = normalize_spaces(receiver_name).title()

            pickup_address = normalize_spaces(pickup_address)
            delivery_address = normalize_spaces(delivery_address)

            delivery_note = delivery_note.strip()

            print("\n===== BÁO CÁO ĐƠN HÀNG =====")
            print("Tên người gửi:", sender_name)
            print("Tên người nhận:", receiver_name)
            print("Địa chỉ lấy hàng:", pickup_address)
            print("Địa chỉ giao hàng:", delivery_address)
            print("Ghi chú:", delivery_note)

            print("Độ dài ghi chú:", len(delivery_note))
            print("Số lượng từ:", len(delivery_note.split()))

            print("Ghi chú chữ thường:")
            print(delivery_note.lower())

            print("Ghi chú chữ hoa:")
            print(delivery_note.upper())

        case "2":
            order_code = input("Nhập mã đơn hàng: ")

            if order_code.strip() == "":
                print("Mã đơn hàng không được bỏ trống")
                continue

            original_code = order_code

            order_code = order_code.strip()
            order_code = order_code.upper()
            order_code = order_code.replace(" ", "-")

            if not order_code.startswith("GRAB-"):
                order_code = "GRAB-" + order_code

            print("\n===== CHUẨN HÓA MÃ ĐƠN HÀNG =====")
            print("Mã ban đầu:", original_code)
            print("Mã chuẩn hóa:", order_code)

        case "3":
            print("\n===== ẨN THÔNG TIN KHÁCH HÀNG =====")

            sender_result = mask_phone(sender_phone)
            receiver_result = mask_phone(receiver_phone)

            if sender_result and receiver_result:
                print("SĐT người gửi:", sender_result)
                print("SĐT người nhận:", receiver_result)

        case "4":
            if delivery_note.strip() == "":
                print("Chưa có ghi chú giao hàng để tìm kiếm")
                continue

            keyword = input("Nhập từ khóa cần tìm: ").strip()
            replace_keyword = input("Nhập từ khóa thay thế: ").strip()

            count = delivery_note.lower().count(keyword.lower())

            if count == 0:
                print("Không tìm thấy từ khóa trong ghi chú giao hàng")
            else:
                new_note = delivery_note.replace(keyword, replace_keyword)

                print("\nSố lần xuất hiện của từ khóa:", count)
                print("Ghi chú giao hàng sau khi thay thế:")
                print(new_note)

        case "5":
            print("Thoát chương trình")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")