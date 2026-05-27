quantity = int(input("nhập số lượng hóa đơn trong ca: "))
min = 0
max = 0
for i in range(quantity):
    bill = int(input(f"nhập giá trị hóa đơn thứ {i}: "))
    if i == 0:
        min = bill
        max = bill
    if bill > max:
        max = bill
    if bill < min:
        min = bill
print("---KẾT QUẢ KIỂM TOÁN CA RIKKEI STORE---")
print(f"hóa đơn có giá trị cao nhất: {max}VND") 
print(f"hóa đơn có giá trị thấp nhất: {min}VND") 
