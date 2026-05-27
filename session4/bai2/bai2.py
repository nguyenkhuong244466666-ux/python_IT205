total_revenue = 0
day = 0
for i in range(1,8):
    revenue = int(input(f"nhap doanh thu ngày thứ {i}: "))
    total_revenue += revenue
    if revenue >=5000:
        day +=1
print("--BÁO CÁO DOANH THU TUẦN RIKKEI STORE---")
print("tổng doanh thu cả tuần là: ",total_revenue)
print ("doanh thu trung binh: ",total_revenue/7)
print(f"số ngày đạt doanh thu mục tiêu (>=5000): {day} ngày")