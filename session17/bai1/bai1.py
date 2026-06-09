raw_logs = []
processed_logs = []


def clean_logs():
    """
    Nhập và làm sạch dữ liệu log.
    Loại bỏ các ký tự ! @ # $
    Sau đó tách log bằng dấu ';'
    """
    global raw_logs

    print("\n--- NẠP DỮ LIỆU LOG ---")

    log_input = input("Nhập chuỗi log thô (cách nhau bởi dấu ;): ")

    remove_chars = "!@#$"
    translation_table = str.maketrans("", "", remove_chars)

    cleaned_text = log_input.translate(translation_table)

    raw_logs = [log.strip() for log in cleaned_text.split(";") if log.strip()]

    print(f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống.")


def filter_danger_logs():
    """
    Lọc các log chứa ERROR hoặc CRITICAL
    bằng List Comprehension.
    """
    global processed_logs

    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return

    print("\n--- LỌC CẢNH BÁO ---")

    processed_logs = [
        log
        for log in raw_logs
        if "ERROR" in log.upper() or "CRITICAL" in log.upper()
    ]

    if not processed_logs:
        print("Không tìm thấy cảnh báo nguy hiểm nào.")
        return

    print(f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:")

    for log in processed_logs:
        print("-", log)


def mask_ip_logs():
    """
    Mã hóa IP trong các log nguy hiểm.
    Ví dụ:
    192.168.1.1 -> 192.168.*.*
    """
    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return

    if not processed_logs:
        print("Chưa có dữ liệu log nguy hiểm, vui lòng thực hiện chức năng 2")
        return

    print("\n--- MÃ HÓA IP ---")

    masked_logs = []

    for log in processed_logs:

        words = log.split()

        for i in range(len(words)):
            if "." in words[i]:

                ip_parts = words[i].split(".")

                if len(ip_parts) == 4:
                    words[i] = ".".join(
                        [ip_parts[0], ip_parts[1], "*", "*"]
                    )

        masked_logs.append(" ".join(words))

    print("Báo cáo log an toàn:")

    for index, log in enumerate(masked_logs, start=1):
        print(f"{index}. {log}")

    return masked_logs


def show_menu():
    """
    Hiển thị menu.
    """
    print("\n============= SECURITY LOG ANALYZER =============")
    print("1. Nhập và làm sạch dữ liệu Log thô")
    print("2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)")
    print("3. Mã hóa địa chỉ IP (Masking)")
    print("4. Đóng hệ thống")
    print("=================================================")


def main():
    """
    Hàm điều khiển chương trình.
    """
    while True:
        show_menu()

        choice = input("Chọn chức năng (1-4): ")

        match choice:
            case "1":
                clean_logs()

            case "2":
                filter_danger_logs()

            case "3":
                mask_ip_logs()

            case "4":
                print("Đóng hệ thống...")
                print("Cảm ơn bạn đã sử dụng Security Log Analyzer!")
                break

            case _:
                print("Lựa chọn không hợp lệ!")


main()