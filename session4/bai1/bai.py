total = int(input("tổng số tiền ban đầu của hóa đơn (số nguyên): "))
total_giam = 0
total_tra = total
if total > 500000 :
    total_giam = total * 0.1
    total_tra = total * 0.9
print("---HÓA ĐƠN THANH TOÁN RIKKEI STORE---")
print("số tiền được giảm giá là:",total_giam)
print("tổng số tiền khách phải trả:",total_tra)