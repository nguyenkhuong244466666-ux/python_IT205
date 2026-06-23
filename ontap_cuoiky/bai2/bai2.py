class deliveryorder:
    def __init__(self, order_id, receiver_name, base_fee, distance, surcharge):
        self.order_id = order_id
        self.receiver_name = receiver_name
        self.base_fee = base_fee
        self.distance = distance
        self.surcharge = surcharge
        self.total_delivery_cost = 0
        self.delivery_status = "chưa phân loại"

    def calculate_total_cost(self):
        self.total_delivery_cost = (self.base_fee * self.distance) + self.surcharge

    def classify_delivery_status(self):
        if self.total_delivery_cost >= 600000:
            self.delivery_status = "Đơn hàng Đặc biệt (Ưu tiên cao - Rủi ro cao)"
        elif self.total_delivery_cost >= 300000:
            self.delivery_status = "Đơn hàng Đường dài (Cần giám sát)"
        elif self.total_delivery_cost >= 100000:
            self.delivery_status = "Đơn hàng Cận tỉnh"
        else:
            self.delivery_status = "Đơn hàng Tiêu chuẩn (Nội thành)"



class OrderManager:
    def __init__(self):
        self.orders: list[deliveryorder] = []


    def show_all_order(self):

        try:

            if not self.orders:
                raise Exception("Hệ thống chưa có vận đơn nào")

            print(f"{'Mã Đơn':<10} | {'Tên người nhận':<20} | {'Cước nền':<12} | {'Khoảng cách':<15} | {'Phụ phí':<12} | {'Tổng chi phí':<15} | {'Trạng thái'}")

            for o in self.orders:
                print(
                    f"{o.order_id:<10} | "
                    f"{o.receiver_name:<20} | "
                    f"{o.base_fee:<12} | "
                    f"{o.distance:<15} | "
                    f"{o.surcharge:<12} | "
                    f"{o.total_delivery_cost:<15} | "
                    f"{o.delivery_status}"
                )

        except Exception as e:
            print(e)



    def check_id(self, id_input):

        for o in self.orders:
            if id_input.lower() == o.order_id.lower():
                return True

        return False



    def add_order(self):

        while True:

            id_input = input("Nhập mã đơn: ").strip()

            if not id_input:
                print("Không được để trống")
                continue

            if self.check_id(id_input):
                print("Mã đơn đã tồn tại")
                continue

            break


        while True:

            name_input = input("Nhập tên người nhận: ").strip()

            if not name_input:
                print("Không được để trống")
                continue

            break


        while True:

            try:

                base_fee_input = float(input("Nhập cước nền: "))

                if base_fee_input <= 0:
                    print("Cước nền phải lớn hơn 0")
                    continue

                break

            except:

                print("Dữ liệu không hợp lệ")



        while True:

            try:

                distance_input = int(input("Nhập khoảng cách: "))

                if distance_input < 1 or distance_input > 5000:
                    print("Khoảng cách từ 1 đến 5000 km")
                    continue

                break

            except:

                print("Dữ liệu không hợp lệ")



        while True:

            try:

                surcharge_input = float(input("Nhập phụ phí: "))

                if surcharge_input <= 0:
                    print("Phụ phí phải lớn hơn 0")
                    continue

                break

            except:

                print("Dữ liệu không hợp lệ")



        new_order = deliveryorder(
            id_input,
            name_input,
            base_fee_input,
            distance_input,
            surcharge_input
        )


        new_order.calculate_total_cost()
        new_order.classify_delivery_status()


        self.orders.append(new_order)

        print("Đã thêm đơn thành công")




    def update_order(self):

        id_input = input("Nhập mã đơn cần sửa: ")


        for o in self.orders:

            if id_input.lower() == o.order_id.lower():


                while True:

                    try:

                        o.base_fee = float(input("Nhập cước nền mới: "))

                        if o.base_fee <= 0:
                            print("Không hợp lệ")
                            continue

                        break

                    except:

                        print("Dữ liệu không hợp lệ")



                while True:

                    try:

                        o.distance = int(input("Nhập khoảng cách mới: "))

                        if o.distance < 1 or o.distance > 5000:
                            print("Khoảng cách sai")
                            continue

                        break

                    except:

                        print("Dữ liệu không hợp lệ")



                while True:

                    try:

                        o.surcharge = float(input("Nhập phụ phí mới: "))

                        if o.surcharge <= 0:
                            print("Không hợp lệ")
                            continue

                        break

                    except:

                        print("Dữ liệu không hợp lệ")



                o.calculate_total_cost()
                o.classify_delivery_status()


                print("Cập nhật thành công")

                return


        print("Không tìm thấy vận đơn")




    def delete_order(self):

        id_input = input("Nhập mã đơn cần xóa: ")


        for o in self.orders:


            if id_input.lower() == o.order_id.lower():


                confirm = input(
                    "Bạn có chắc muốn xóa vận đơn này khỏi hệ thống không? (Y/N): "
                )


                if confirm.lower() == "y":

                    self.orders.remove(o)

                    print("Đã xóa thành công")

                else:

                    print("Đã hủy xóa")


                return



        print("Không tìm thấy vận đơn")





    def search_by_receiver(self):

        try:


            if not self.orders:

                raise Exception("Hệ thống chưa có vận đơn nào")



            keyword = input("Nhập tên người nhận cần tìm: ").lower()


            check = False



            for o in self.orders:


                if keyword in o.receiver_name.lower():


                    check = True


                    print(
                        o.order_id,
                        "|",
                        o.receiver_name,
                        "|",
                        o.total_delivery_cost,
                        "|",
                        o.delivery_status
                    )



            if check == False:

                print("Không tìm thấy vận đơn phù hợp")



        except Exception as e:

            print(e)






def main():

    current_ordermanager = OrderManager()


    current_ordermanager.orders = [

        deliveryorder("or01","abcxsd",12000,12,20000),

        deliveryorder("or02","123",120000,12,2000)

    ]


    for o in current_ordermanager.orders:

        o.calculate_total_cost()

        o.classify_delivery_status()



    while True:


        choice = input("""
================ MENU ================
1. Hiển thị danh sách vận đơn trong hệ thống
2. Nhập vận đơn mới
3. Cập nhật thông tin vận đơn
4. Xóa vận đơn khỏi hệ thống
5. Tìm kiếm vận đơn theo tên người nhận
6. Thoát
=====================================
Nhập lựa chọn của bạn: """)



        match choice:


            case "1":

                current_ordermanager.show_all_order()



            case "2":

                current_ordermanager.add_order()



            case "3":

                current_ordermanager.update_order()



            case "4":

                current_ordermanager.delete_order()



            case "5":

                current_ordermanager.search_by_receiver()



            case "6":

                print("Cảm ơn bạn đã sử dụng hệ thống quản lý vận đơn!")

                break



            case _:

                print("Lựa chọn không hợp lệ")



main()