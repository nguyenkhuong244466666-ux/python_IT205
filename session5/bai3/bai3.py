print("===== HỆ THỐNG IN SƠ ĐỒ CHỖ HỌC =====")

room_count = int(input("Nhập số lượng phòng học cần kiểm tra: "))

if room_count <= 0:
    print("Số lượng phòng học không hợp lệ")
    print("Chương trình kết thúc")

else:

    for room in range(1, room_count + 1):

        print(f"\n===== PHÒNG HỌC {room} =====")

        row_count = int(input("Nhập số hàng ghế: "))
        seat_count = int(input("Nhập số ghế mỗi hàng: "))

        if row_count > 10 or seat_count > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break

        if row_count <= 0 or seat_count <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue

        print("\nSơ đồ chỗ ngồi:")

        for row in range(row_count):

            for seat in range(seat_count):
                print("*", end="")

            print()