total_def_goods = 0
i = 1
while True:
    quantity = int(input(f"nhập số lượng hàng lỗi của quầy {i}: "))
    i+=1
    if quantity == -1:
        print("Tổng số hàng lỗi thu hồi trong ngày là:",total_def_goods)
        break
    else:
        total_def_goods += quantity