print("===== HỆ THỐNG SÀNG LỌC PHẪU THUẬT =====")

# Nhập dữ liệu
age = int(input("Nhập tuổi bệnh nhân: "))
blood_pressure = int(input("Nhập huyết áp tâm thu (mmHg): "))
blood_sugar = int(input("Nhập đường huyết (mg/dL): "))

# Kiểm tra dữ liệu âm
if age < 0 or blood_pressure < 0 or blood_sugar < 0:
    print("Dữ liệu nhập vào không hợp lệ")

else:
    # Kiểm tra điều kiện phẫu thuật
    if age < 75:

        if 90 <= blood_pressure <= 140:

            if blood_sugar < 150:
                print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")

            else:
                print("TỪ CHỐI PHẪU THUẬT")
                print("- Lý do: Đường huyết quá cao.")

        else:
            print("TỪ CHỐI PHẪU THUẬT")
            print("- Lý do: Huyết áp ngoài ngưỡng an toàn.")

    else:
        print("TỪ CHỐI PHẪU THUẬT")
        print("- Lý do: Tuổi vượt giới hạn cho phép.")