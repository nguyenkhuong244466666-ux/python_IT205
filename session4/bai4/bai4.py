number = 51
temp = 0
print("===BẠN CÓ 5 LƯỢT ĐOÁN===")
for i in range(1,6):
    du_doan=int(input(f"lượt đoán {i} - Nhập số của bạn: "))
    if du_doan == number:
        temp = 1
        print("chúc mừng! bạn đã đoán chính xác mã số may mắn!@_@")
        break
    if du_doan < number:
        print("số của bạn nhỏ hơn mã số may mắn!!!!")
    if du_doan > number:
        print("số của bạn lớn hơn mã số may mắn!!!!")
if temp == 0:
    print("======HAHAHAHAHAHAHA đồ ngu đồ ăn hại=========")
    print(f"=====>số may mắn là {number}<=====")