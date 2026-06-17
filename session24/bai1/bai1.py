# Hệ thống quản lý hóa đơn Rikkei Coffee

class CoffeeOrder:
    # Class Attribute dùng chung cho toàn bộ hóa đơn
    vat_rate = 0.10

    def __init__(self, table_number):
        self.table_number = table_number

        # SỬA LỖI 1:
        # Đổi từ total_amount thành __total_amount
        # để bảo vệ dữ liệu bằng Name Mangling
        self.__total_amount = 0

    def add_item(self, price):
        if price > 0:
            self.__total_amount += price

    # SỬA LỖI 2:
    # Dùng @property để cho phép đọc
    # nhưng không cho sửa trực tiếp
    @property
    def total_amount(self):
        return self.__total_amount

    def calculate_final_bill(self):
        return self.__total_amount * (1 + CoffeeOrder.vat_rate)

    # SỬA LỖI 3:
    # Đổi từ Instance Method thành Class Method
    # để cập nhật VAT cho toàn bộ hệ thống
    @classmethod
    def update_vat_rate(cls, new_rate):
        cls.vat_rate = new_rate


def main():
    # Tạo hóa đơn cho 2 bàn
    order_table1 = CoffeeOrder("Bàn 1")
    order_table2 = CoffeeOrder("Bàn 2")

    # Thêm món
    order_table1.add_item(50000)
    order_table2.add_item(30000)

    print("===== TRƯỚC KHI CẬP NHẬT VAT =====")
    print(f"VAT Bàn 1: {order_table1.vat_rate}")
    print(f"VAT Bàn 2: {order_table2.vat_rate}")

    # ==================================================
    # KIỂM TRA BẢO MẬT
    # ==================================================

    print("\n===== KIỂM TRA BẢO MẬT =====")

    try:
        # Nhân viên cố tình sửa tổng tiền
        order_table1.total_amount = 0
    except AttributeError:
        print("Không thể chỉnh sửa trực tiếp total_amount!")

    print(f"Tổng tiền thực tế Bàn 1: {order_table1.total_amount} VNĐ")

    # ==================================================
    # CẬP NHẬT VAT TOÀN HỆ THỐNG
    # ==================================================

    CoffeeOrder.update_vat_rate(0.08)

    print("\n===== SAU KHI CẬP NHẬT VAT =====")

    print(f"VAT Bàn 1: {order_table1.vat_rate}")
    print(f"VAT Bàn 2: {order_table2.vat_rate}")

    print(
        f"Tổng tiền Bàn 1 sau VAT: "
        f"{order_table1.calculate_final_bill()} VNĐ"
    )

    print(
        f"Tổng tiền Bàn 2 sau VAT: "
        f"{order_table2.calculate_final_bill()} VNĐ"
    )


if __name__ == "__main__":
    main()
