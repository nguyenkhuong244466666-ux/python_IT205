print("=== HỆ THỐNG QUẢN LÝ BỆNH NHÂN ===")

# Nhập thông tin bệnh nhân
patient_name = input("Nhập họ tên bệnh nhân: ")
medical_code = input("Nhập mã bệnh án: ")
department = input("Nhập khoa/phòng khám: ")

# Hiển thị phiếu khám điện tử
print("\n=== PHIẾU KHÁM BỆNH ĐIỆN TỬ ===")

print(
    f"Bệnh nhân: {patient_name} - "
    f"Mã BA: {medical_code} - "
    f"Chuyển tới: {department}"
)

# Thông báo hoàn tất
print("\nTiếp nhận bệnh nhân thành công!")