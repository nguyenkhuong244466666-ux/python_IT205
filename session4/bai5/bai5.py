i = 1
count = 0
hoa_don = 0
total=0
quantity_big=0
quantity=0
while True:
    revenue= int(input(f"khách hàng {i} - nhập giá trị hóa đơn: "))
    quantity += 1
    total += revenue
    hoa_don+=1
    if revenue >= 1000000:
        quantity_big += 1
    while True:
        choice = input("có muốn nhập tiếp không? (C/K): ").lower()
        if choice == "c" or choice == "k":
            break
        else:
            print("vui lòng nhập (C/K)")
    match choice:
        case "c":
            i+=1
            continue
        case "k":
            break
print("---BÁO CÁO DOANH THU CUỐI NGÀY RIKKEI STORE---")
print(f"tổng số đơn đã xử lý: {hoa_don} hóa đơn.")
print(f"tổng doanh thu ngày hôm nay: {total} VND.")
print(f"số hóa đơn (>= 1,000,000 VND): {quantity_big} hóa đơn.")
print(f"tỷ lệ hóa đơn lớn đạt: {(quantity_big/quantity)*100}% trên tổng số đơn hàng.")
    
    
