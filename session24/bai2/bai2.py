# Hệ thống Thẻ thành viên Rikkei Coffee

class MemberCard:
    def __init__(self, customer_name, points=0):
        self.customer_name = customer_name

        # SỬA LỖI 1:
        # Đóng gói dữ liệu bằng Name Mangling
        self.__points = 0

        # Đi qua setter để kiểm tra dữ liệu
        self.points = points

    def add_points(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.__points += amount

    # SỬA LỖI 2:
    # Property chỉ cho đọc
    @property
    def points(self):
        return self.__points

    # SỬA LỖI 3:
    # Setter kiểm tra dữ liệu trước khi gán
    @points.setter
    def points(self, value):
        if isinstance(value, int) and value >= 0:
            self.__points = value
        else:
            print("Dữ liệu điểm không hợp lệ!")

    # SỬA LỖI 4:
    # Hàm tiện ích -> Static Method
    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        return bill_amount >= 200000


def main():
    card1 = MemberCard("Le Van C", 100)

    print("===== THÔNG TIN BAN ĐẦU =====")
    print(f"Khách hàng: {card1.customer_name}")
    print(f"Điểm hiện tại: {card1.points}")

    print("\n===== KIỂM TRA VALIDATION =====")

    # Thử gán điểm âm
    card1.points = -50

    print(f"Điểm sau khi gán -50: {card1.points}")

    # Thử gán chuỗi
    card1.points = "mot tram"

    print(f"Điểm sau khi gán chuỗi: {card1.points}")

    print("\n===== KIỂM TRA STATIC METHOD =====")

    result = MemberCard.is_eligible_for_voucher(250000)

    print(
        f"Hóa đơn 250000 VNĐ "
        f"có được tặng Voucher không? {result}"
    )


if __name__ == "__main__":
    main()

