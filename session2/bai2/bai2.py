print("--- HỆ THỐNG KIỂM TRA HIẾN MÁU ---")

donor_age = int(input("Nhập tuổi người hiến: "))
donor_weight = float(input("Nhập cân nặng người hiến (kg): "))

# Kiểm tra điều kiện hiến máu
if donor_age >= 18 and donor_weight >= 50:
    print("Kết quả: ĐỦ ĐIỀU KIỆN hiến máu.")

else:
    print("Kết quả: KHÔNG ĐỦ ĐIỀU KIỆN hiến máu.")

    if donor_age < 18:
        print("- Lý do: Chưa đủ 18 tuổi.")

    if donor_weight < 50:
        print("- Lý do: Cân nặng dưới 50kg.")