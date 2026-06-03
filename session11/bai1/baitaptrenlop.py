# number = (1,2,3,4,5)
# products = ("P001","P002","P003","P004")
# info = ("khuong",19,"cny",True)

# for index, value in enumerate(info, start=1):
#     print(f"gia tri thu {index}: {value}")
# for i in range(len(info)):
#     print(f"gia tri thu {i+1}: {info[i]}")
# for item in info:
#     print(item)

# users = {
#     "name": "khương",
#     "age": 19,
#     "status": "đã đầu thai"
# }
# print(users["status"])

# print(users.get("name", "không tìm thấy "))# nếu không thấy key thì in ra none nếu có cho giá trị mặc định thì in ra giá trị mặc định(là giá trị sau dấu phẩy)
 
# del users["phone"]
# users.pop("status")

# for key in users.keys():
#     print(key)

# for value in users.values():
#     print(value)

# for key, value in users.items():
#     print(f"{}")

# list_user = ("user001", "user002", "user003")
# users = {
#     "list_user[0]": { "name": "Bao", "age": 18},
#     "list_user[1]": { "name": "Phúc", "age": 20},
#     "list_user [2]": { "name": "Tin", "age": 19},
# }
# print(users["list_user[0]"]["name"])

# ===> yêu cầu: Tạo 1 danh sách users.
# Thêm 5 phần tử vào danh sách.
# Mỗi phần tử là 1 dict
# Hiến thị toàn bộ thông tin user ra màn hình

users = [
    {"name": "Khuong", "age": 18},
    {"name": "my", "age": 88},
    {"name": "sang", "age": 102},
    {"name": "nhat", "age": 99},
    {"name": "duy", "age": 21},
    {"name": "phu", "age": 81}
]


print("Danh sách người dùng:")
for index, user in enumerate(users, start=1):
    print(f"{index}. Name: {user["name"]:<10}| Age: {user["age"]}")