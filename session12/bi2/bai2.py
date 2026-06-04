saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn: ")
    match choice:
        case "1":
            if len(saving_accounts) == 0:
                print("Danh sách sổ tiết kiệm hiện đang trống")
            else:
                print("\n--- DANH SÁCH SỔ TIẾT KIỆM ---")

                for index, value in enumerate(saving_accounts, start=1):
                    print(
                        f"{index}. "
                        f"Mã sổ: {value.get('account_id')} | "
                        f"Khách hàng: {value.get('customer_name')} | "
                        f"Số tiền gửi: {value.get('balance')} | "
                        f"Kỳ hạn: {value.get('term_months')} tháng | "
                        f"Lãi suất: {value.get('interest_rate')}%/năm | "
                        f"Trạng thái: {value.get('status')}"
                    )
        case "2":
            account_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()
            customer_name = input("Nhập tên khách hàng: ").strip()

            if customer_name == "":
                print("Tên khách hàng không được để trống")
                continue

            found = False

            for value in saving_accounts:
                if account_id == value.get("account_id"):
                    found = True
                    break

            if found:
                print("Mã sổ tiết kiệm đã tồn tại!")
                continue

            balance = input("Nhập số tiền gửi: ")
            term_months = input("Nhập kỳ hạn gửi theo tháng: ")

            if not balance.isdigit() or not term_months.isdigit():
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue

            balance = int(balance)
            term_months = int(term_months)

            if balance <= 0 or term_months <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue

            interest_rate = input("Nhập lãi suất năm: ")

            if not interest_rate.replace(".", "", 1).isdigit():
                print("Lãi suất không hợp lệ!")
                continue

            interest_rate = float(interest_rate)

            if interest_rate <= 0:
                print("Lãi suất không hợp lệ!")
                continue

            new_account = {
                "account_id": account_id,
                "customer_name": customer_name,
                "balance": balance,
                "term_months": term_months,
                "interest_rate": interest_rate,
                "status": "active"
            }
            saving_accounts.append(new_account)
            print("Mở sổ tiết kiệm thành công!")
        case "3":
            account_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()
            found = False
            for index, value in enumerate(saving_accounts):
                if account_id == value.get("account_id"):
                    found = True

                    if value.get("status") == "closed":
                        print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
                        break

                    customer_name = input("Nhập tên khách hàng mới: ").strip()

                    if customer_name == "":
                        print("Tên khách hàng không được để trống")
                        break

                    balance = input("Nhập số tiền gửi mới: ")
                    term_months = input("Nhập kỳ hạn mới theo tháng: ")

                    if not balance.isdigit() or not term_months.isdigit():
                        print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                        break

                    balance = int(balance)
                    term_months = int(term_months)

                    if balance <= 0 or term_months <= 0:
                        print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                        break

                    interest_rate = input("Nhập lãi suất năm mới: ")

                    if not interest_rate.replace(".", "", 1).isdigit():
                        print("Lãi suất không hợp lệ!")
                        break

                    interest_rate = float(interest_rate)

                    if interest_rate <= 0:
                        print("Lãi suất không hợp lệ!")
                        break

                    saving_accounts[index]["customer_name"] = customer_name
                    saving_accounts[index]["balance"] = balance
                    saving_accounts[index]["term_months"] = term_months
                    saving_accounts[index]["interest_rate"] = interest_rate

                    print("Cập nhật thành công!")
                    break

            if not found:
                print("Không tìm thấy mã sổ tiết kiệm!")
        case "4":
            account_id = input("Nhập mã sổ tiết kiệm cần tất toán: ").strip().upper()
            found = False
            for index, value in enumerate(saving_accounts):
                if account_id == value.get("account_id"):
                    saving_accounts[index]["status"] = "closed"
                    found = True
                    print("Tất toán sổ tiết kiệm thành công!")
                    break
            if not found:
                print("Không tìm thấy mã sổ tiết kiệm!")
        case "5":
            account_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()
            found = False
            for value in saving_accounts:
                if account_id == value.get("account_id"):
                    found = True

                    if value.get("status") == "closed":
                        print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                        break

                    interest = (
                        value.get("balance")
                        * value.get("interest_rate")
                        / 100
                        * value.get("term_months")
                        / 12
                    )
                    total_money = value.get("balance") + interest

                    print(f"Tiền lãi dự kiến: {interest}")
                    print(f"Tổng tiền nhận khi đến hạn: {total_money}")
                    break

            if not found:
                print("Không tìm thấy mã sổ tiết kiệm!")
        case "6":
            account_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()
            found = False
            for value in saving_accounts:
                if account_id == value.get("account_id"):
                    found = True
                    if value.get("status") == "closed":
                        print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                        break
                    actual_months = input("Nhập số tháng thực gửi: ")
                    if not actual_months.isdigit():
                        print("Số tháng thực gửi không hợp lệ!")
                        break
                    actual_months = int(actual_months)
                    if actual_months <= 0:
                        print("Số tháng thực gửi không hợp lệ!")
                        break
                    if actual_months < value.get("term_months"):
                        rate = 0.5
                        print("Khách hàng rút trước hạn")
                    else:
                        rate = value.get("interest_rate")
                        print("Khách hàng đủ điều kiện hưởng lãi đúng hạn")
                    interest = (value.get("balance")* rate/ 100* actual_months/ 12)
                    total_money = value.get("balance") + interest

                    print(f"Tiền lãi thực nhận: {interest}")
                    print(f"Tổng tiền thực nhận: {total_money}")
                    break
            if not found:
                print("Không tìm thấy mã sổ tiết kiệm!")
        case "7":
            print("Thoát chương trình!")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại")