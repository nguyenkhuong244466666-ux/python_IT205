print("===== HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI =====")

while True:

    employee_count = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))

    if employee_count <= 0:
        print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.\n")

    else:
        print("[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho", employee_count, "nhân sự mới!")
        break

print("===== CHƯƠNG TRÌNH KẾT THÚC =====")