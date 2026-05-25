print("=== HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ===")

# Nhập thông tin bệnh nhân
name_patient = input("Nhập tên bệnh nhân: ")

# Ép kiểu dữ liệu sang float
weight = float(input("Nhập cân nặng bệnh nhân: "))

# Hiển thị dữ liệu lưu trữ
print("\n=== KIỂM TRA DỮ LIỆU LƯU TRỮ ===")
print("Bệnh nhân:", name_patient)
print("Cân nặng đã nhập:", weight)

# Kiểm tra kiểu dữ liệu
print("Kiểu dữ liệu của cân nặng:", type(weight))

# Thông báo thành công
print("\nDữ liệu đã được lưu chính xác!")