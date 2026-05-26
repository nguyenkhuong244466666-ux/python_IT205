print("===== HỆ THỐNG PHÂN LUỒNG BỆNH NHÂN =====")

# Nhập dữ liệu
patient_name = input("Nhập họ tên bệnh nhân: ")
patient_age = int(input("Nhập tuổi bệnh nhân: "))

# Kiểm tra dữ liệu không hợp lệ
if patient_name.strip() == "" or patient_age < 0 or patient_age > 150:
    print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")

else:
    # Phân luồng bệnh nhân
    if patient_age < 6:
        priority = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."

    elif patient_age >= 80:
        priority = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."

    else:
        priority = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

    # In phiếu khám bệnh
    print("\n===== PHIẾU KHÁM BỆNH ĐIỆN TỬ =====")
    print("Họ tên:", patient_name)
    print("Tuổi:", patient_age)
    print("Kết quả phân luồng:", priority)