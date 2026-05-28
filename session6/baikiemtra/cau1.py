quantity = int(input("nhập số lượng tồn kho: "))
if (quantity >= 50):
    print("Tình trạng: Hàng đầy kho")
elif (quantity >= 10 and quantity < 50):
    print("Tình trạng: Mức an toàn")
else:
    print("Tình trạng: Sắp hết hàng, cần báo cáo nhập thêm")