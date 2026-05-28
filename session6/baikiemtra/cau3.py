ton_kho = 100
while True:
    quantity=int(input("nhập vào Số lượng muốn xuất: "))
    if quantity < 0:
        print( "Không được nhập số âm, vui lòng nhập lại!")
    elif quantity > ton_kho:
        print("Kho không đủ hàng, vui lòng nhập lại!")
    else:
        ton_kho = ton_kho - quantity
        print("Xuất kho thành công!")
        print("Tồn kho còn lại:",ton_kho)
        break