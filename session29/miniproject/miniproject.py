from abc import ABC, abstractmethod

class BaseDevice(ABC):
    factory_name = "Rikkei Smart Factory"
    base_maintenance_cost = 1000000

    def __init__(self, code, name, hours):
        self.code = code
        self.name = name
        self.__operating_hours = hours

    @property
    def operating_hours(self):
        return self.__operating_hours

    def add_hours(self, hours):
        self.__operating_hours += hours

    @abstractmethod
    def track_performance(self):
        pass

    @abstractmethod
    def run_diagnostic(self):
        pass

    def __add__(self, other):
        if isinstance(other, BaseDevice):
            return self.__operating_hours + other.__operating_hours
        print("[Lỗi] (ERR-IOT-04): Không thể cộng với kiểu dữ liệu khác!")
        return 0

    def __lt__(self, other):
        if isinstance(other, BaseDevice):
            return self.__operating_hours < other.__operating_hours
        print("[Lỗi] (ERR-IOT-04): Không thể so sánh kiểu dữ liệu khác!")
        return False

    @staticmethod
    def validate_device_code(code):
        return len(code) == 10 and code[0].isalpha()

    @classmethod
    def update_maintenance_cost(cls, cost):
        cls.base_maintenance_cost = cost


class ProductionRobot(BaseDevice):
    def __init__(self, code, name, hours, products):
        super().__init__(code, name, hours)
        self.completed_products = products

    def track_performance(self):
        return self.completed_products / (self.operating_hours * 10) * 100

    def run_diagnostic(self):
        if self.completed_products > 10000:
            return "Cần bảo dưỡng robot"
        return "Robot hoạt động bình thường"


class ThermalSensor(BaseDevice):
    def __init__(self, code, name, hours, temp, threshold):
        super().__init__(code, name, hours)
        self.current_temperature = temp
        self.safety_threshold = threshold

    def track_performance(self):
        return self.safety_threshold - self.current_temperature

    def run_diagnostic(self):
        if self.current_temperature > self.safety_threshold:
            return "Nguy hiểm: Vượt ngưỡng nhiệt!"
        return "Nhiệt độ an toàn"


class HybridSmartActuator(ProductionRobot, ThermalSensor):
    def __init__(self, code, name, hours, products, temp, threshold):
        ProductionRobot.__init__(self, code, name, hours, products)
        self.current_temperature = temp
        self.safety_threshold = threshold

    def track_performance(self):
        return ProductionRobot.track_performance(self)

    def run_diagnostic(self):
        if self.current_temperature > self.safety_threshold:
            return "Nguy hiểm: Vượt ngưỡng nhiệt!"
        return "Thiết bị ổn định"


class MQTTEngineGateway:
    def process_stream(self, device):
        print(f"[MQTT] Xuất dữ liệu thiết bị {device.code} thành công")


class ERPReportGateway:
    def process_stream(self, device):
        print(f"[ERP] Đồng bộ dữ liệu thiết bị {device.code} thành công")


def export_telemetry_data(gateway, device):
    if hasattr(gateway, "process_stream"):
        gateway.process_stream(device)
    else:
        print("[Lỗi] (ERR-IOT-05): Cổng không tương thích")


devices_list = []
current_device = None


def show_menu():
    print(f"===== RIKKEI SMART FACTORY IOT =====")
    print(f"1. Đăng ký thiết bị")
    print(f"2. Xem thông tin thiết bị")
    print(f"3. Cập nhật hiệu suất")
    print(f"4. Chẩn đoán")
    print(f"5. Cộng và so sánh thiết bị")
    print(f"6. Xuất dữ liệu")
    print(f"7. Thoát")


def create_device():
    global current_device

    print(f"1. Robot")
    print(f"2. Sensor")
    print(f"3. Hybrid")

    t = input("Chọn loại: ")

    code = input("Nhập mã thiết bị: ")

    if not BaseDevice.validate_device_code(code):
        print(f"[Lỗi] (ERR-IOT-01): Mã thiết bị không hợp lệ!")
        return

    name = input("Nhập tên thiết bị: ").strip().upper()

    hours = int(input("Nhập giờ chạy: "))

    if t == "1":
        products = int(input("Nhập sản phẩm: "))
        current_device = ProductionRobot(code,name,hours,products)

    elif t == "2":
        temp = float(input("Nhập nhiệt độ: "))
        current_device = ThermalSensor(code,name,hours,temp,80)

    elif t == "3":
        products = int(input("Nhập sản phẩm: "))
        temp = float(input("Nhập nhiệt độ: "))
        current_device = HybridSmartActuator(code,name,hours,products,temp,80)

    else:
        print(f"Lựa chọn sai")
        return

    devices_list.append(current_device)
    print(f"Đăng ký thành công | Tên: {current_device.name}")


def show_device():
    if current_device is None:
        print(f"[Lỗi] (ERR-IOT-02): Chưa có thiết bị")
        return

    print(f"Tên: {current_device.name} | Mã: {current_device.code} | Giờ: {current_device.operating_hours}")
    print(f"MRO: {HybridSmartActuator.__mro__}")


def update_device():
    if current_device is None:
        print(f"[Lỗi] (ERR-IOT-02): Chưa có thiết bị")
        return

    try:
        h = int(input("Nhập giờ mới: "))
        current_device.add_hours(h)
        print(f"Hiệu suất: {current_device.track_performance():.2f}%")
    except:
        print(f"[Lỗi] (ERR-IOT-03): Dữ liệu sai")


def diagnostic():
    if current_device:
        print(f"Kết quả: {current_device.run_diagnostic()}")
        print(f"Chi phí bảo trì: {BaseDevice.base_maintenance_cost}")
    else:
        print(f"[Lỗi] (ERR-IOT-02): Chưa có thiết bị")


def operator_test():
    if len(devices_list) < 2:
        print(f"Cần 2 thiết bị")
        return

    a = devices_list[0]
    b = devices_list[1]

    print(f"Tổng giờ chạy: {a+b}")

    if a < b:
        print(f"{a.code} hao mòn ít hơn {b.code}")
    else:
        print(f"{b.code} hao mòn ít hơn {a.code}")


def export_data():
    if current_device:
        gateway = MQTTEngineGateway()
        export_telemetry_data(gateway,current_device)
    else:
        print(f"[Lỗi] (ERR-IOT-02): Chưa có thiết bị")


def main():
    global current_device

    while True:
        show_menu()

        choice = input("Chọn: ")

        match choice:
            case "1":
                create_device()
            case "2":
                show_device()
            case "3":
                update_device()
            case "4":
                diagnostic()
            case "5":
                operator_test()
            case "6":
                export_data()
            case "7":
                print(f"Cảm ơn đã sử dụng hệ thống")
                break
            case _:
                print(f"[Lỗi] (ERR-IOT-06): Lựa chọn không hợp lệ")

main()