heart_rate = int(input("Nhập nhịp tim bệnh nhân (bpm): "))

# Hệ thống phân loại ưu tiên
if heart_rate > 120:
    print("Mức ưu tiên: ĐỎ - Nguy kịch! Cần cấp cứu ngay.")

elif heart_rate > 100:
    print("Mức ưu tiên: VÀNG - Bất thường, cần theo dõi sát.")

elif heart_rate < 60:
    print("Mức ưu tiên: XANH DƯƠNG - Nhịp tim chậm, cần kiểm tra thêm.")

else:
    print("Mức ưu tiên: XANH LÁ - Ổn định, chờ theo thứ tự.")

print("Hoàn tất quá trình phân loại.")