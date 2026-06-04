parking_lot = []
next_id = 1

while True:
    print("\nQUẢN LÝ BÃI XE - SMART PARKING")
    print("1. Check-in (Đăng ký xe vào)")
    print("2. Báo cáo tồn kho (Hiển thị danh sách)")
    print("3. Tìm kiếm xe (Theo biển số)")
    print("4. Check-out (Xử lý xe ra & Tính phí)")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn (1-5): ")

    match choice:
        case "1":
            plate = input("Nhập biển số: ").strip().upper()

            if plate == "":
                print("[Lỗi]: Biển số không được để trống!")
                continue

            exist = False

            for vehicle in parking_lot:
                if vehicle["plate"] == plate:
                    exist = True
                    break

            if exist:
                print("[Lỗi]: Xe với biển số này đã tồn tại trong bãi!")
                continue

            while True:
                vehicle_type = input("Nhập loại xe (1: Xe máy, 2: Ô tô): ")

                if vehicle_type.isdigit():
                    vehicle_type = int(vehicle_type)

                    if vehicle_type == 1 or vehicle_type == 2:
                        break

                print("[Lỗi]: Loại xe không hợp lệ (1: Xe máy, 2: Ô tô)!")

            while True:
                entry_time = input("Nhập giờ vào: ")

                if entry_time.isdigit():
                    entry_time = int(entry_time)

                    if 0 <= entry_time <= 24:
                        break

                print("[Lỗi]: Giờ vào không hợp lệ!")

            parking_lot.append({
                "id": next_id,
                "plate": plate,
                "type": vehicle_type,
                "entry_time": entry_time
            })

            print(f"[Thành công]: Xe {plate} đã được đăng ký vào bãi")

            next_id += 1

        case "2":
            if len(parking_lot) == 0:
                print("[Thông báo]: Bãi xe hiện đang trống!")
            else:
                print(f"\n{'ID':<5}{'Biển số':<15}{'Loại xe':<15}{'Giờ vào':<10}")

                for vehicle in parking_lot:
                    if vehicle["type"] == 1:
                        vehicle_name = "Xe máy"
                    else:
                        vehicle_name = "Ô tô"

                    print(
                        f"{vehicle['id']:<5}"
                        f"{vehicle['plate']:<15}"
                        f"{vehicle_name:<15}"
                        f"{vehicle['entry_time']:<10}"
                    )

        case "3":
            if len(parking_lot) == 0:
                print("[Thông báo]: Bãi xe hiện đang trống!")
                continue

            plate = input("Nhập biển số xe cần tìm: ").strip().upper()

            found = False

            for vehicle in parking_lot:
                if vehicle["plate"] == plate:
                    print("Thông tin chi tiết:", vehicle)
                    found = True
                    break

            if found == False:
                print(f"[Lỗi]: Không tìm thấy biển số {plate} trong hệ thống!")

        case "4":
            if len(parking_lot) == 0:
                print("[Thông báo]: Bãi xe hiện đang trống!")
                continue

            plate = input("Nhập biển số xe cần ra: ").strip().upper()

            found = False

            for i in range(len(parking_lot)):
                if parking_lot[i]["plate"] == plate:
                    found = True

                    while True:
                        exit_time = input("Nhập giờ ra: ")

                        if exit_time.isdigit():
                            exit_time = int(exit_time)

                            if exit_time >= parking_lot[i]["entry_time"]:
                                break

                        print("[Lỗi]: Giờ ra phải sau hoặc bằng giờ vào!")

                    hours = exit_time - parking_lot[i]["entry_time"]

                    if parking_lot[i]["type"] == 1:
                        fee = hours * 5000
                    else:
                        fee = hours * 10000

                    print(f"Tổng phí phải trả: {fee} VNĐ")

                    vehicle_id = parking_lot[i]["id"]

                    parking_lot.pop(i)

                    print(f"[Thành công]: Đã xóa xe ID {vehicle_id} thành công!")

                    break

            if found == False:
                print(f"[Lỗi]: Không tìm thấy biển số {plate} trong hệ thống!")

        case "5":
            print("Thoát chương trình")
            break

        case _:
            print("[Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5!")