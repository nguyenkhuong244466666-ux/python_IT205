from abc import ABC, abstractmethod


class BaseEmployee(ABC):

    company_name = "Rikkei Education"
    base_salary_rate = 3000000

    def __init__(self, code, name):
        self.code = code
        self.__name = name.upper()
        self.__working_hours = 0

    @property
    def name(self):
        return self.__name

    @property
    def working_hours(self):
        return self.__working_hours

    def add_hours(self, hours):
        if hours <= 0:
            print("Số liệu cập nhật hiệu suất không hợp lệ")
            return
        self.__working_hours += hours

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def update_kpi(self, progress):
        pass

    def __add__(self, other):
        if isinstance(other, BaseEmployee):
            return self.__working_hours + other.__working_hours
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, BaseEmployee):
            return self.__working_hours < other.__working_hours
        return NotImplemented

    @staticmethod
    def validate_employee_code(code):
        return code.startswith("RKE") and len(code) == 10



class Lecturer(BaseEmployee):

    def __init__(self, code, name):
        super().__init__(code, name)
        self.teaching_slots = 0

    def calculate_salary(self):
        return self.working_hours * BaseEmployee.base_salary_rate + self.teaching_slots * 500000

    def update_kpi(self, progress):
        print(f"KPI giảng viên đạt {progress}%")

    def conduct_class(self):
        self.teaching_slots += 1
        self.add_hours(2)



class AdmissionStaff(BaseEmployee):

    def __init__(self, code, name):
        super().__init__(code, name)
        self.revenue_generated = 0

    def calculate_salary(self):
        return self.working_hours * BaseEmployee.base_salary_rate + self.revenue_generated * 0.05

    def update_kpi(self, progress):
        if progress <= 0:
            print("Doanh số không hợp lệ")
            return
        self.revenue_generated += progress



class HybridManager(Lecturer, AdmissionStaff):

    def __init__(self, code, name):
        super().__init__(code, name)
        self.revenue_generated = 0

    def calculate_salary(self):
        return self.working_hours * BaseEmployee.base_salary_rate + self.teaching_slots * 500000 + self.revenue_generated * 0.05

    def update_kpi(self, progress):
        self.revenue_generated += progress



class VietcombankCorporateService:

    def transfer_salary(self, employee, amount):
        print(f"VCB thanh toán {amount} cho {employee.name}")



class TechcombankCorporateService:

    def transfer_salary(self, employee, amount):
        print(f"TCB thanh toán {amount} cho {employee.name}")



def execute_payroll(service, employee, amount):
    service.transfer_salary(employee, amount)



employees = []

current_employee = None



def menu():

    print("""
===== RIKKEI EDUCATION HR SIMULATOR =====
1. Tuyển dụng nhân sự
2. Xem MRO
3. Cập nhật KPI
4. Tính lương
5. So sánh giờ làm
6. Thanh toán lương
7. Thoát
""")



def main():

    global current_employee

    while True:

        menu()

        choice = input("Chọn: ")

        match choice:


            case "1":

                print("1.Lecturer")
                print("2.Admission")
                print("3.Hybrid")

                type_emp = input("Chọn loại: ")

                code = input("Nhập mã nhân sự: ")

                if not BaseEmployee.validate_employee_code(code):
                    print("Mã nhân sự không hợp lệ")
                    continue

                name = input("Nhập tên: ")


                if type_emp == "1":

                    emp = Lecturer(code,name)


                elif type_emp == "2":

                    emp = AdmissionStaff(code,name)


                else:

                    emp = HybridManager(code,name)


                employees.append(emp)

                current_employee = emp

                print(f"Tạo nhân sự thành công | Tên: {emp.name}")


            case "2":

                if current_employee:

                    print(f"MRO: {HybridManager.__mro__}")

                else:

                    print("Chưa có nhân sự")



            case "3":

                if current_employee:

                    progress = int(input("Nhập KPI: "))

                    current_employee.update_kpi(progress)

                else:

                    print("Chưa có nhân sự")



            case "4":

                if current_employee:

                    print(f"Lương: {current_employee.calculate_salary()}")

                else:

                    print("Chưa có nhân sự")



            case "5":

                if len(employees) >= 2:

                    a = employees[0]

                    b = employees[1]

                    print(f"A ít giờ hơn B: {a < b}")

                    print(f"Tổng giờ làm: {a+b}")

                else:

                    print("Không đủ nhân sự")



            case "6":

                if current_employee:

                    bank = VietcombankCorporateService()

                    execute_payroll(bank,current_employee,current_employee.calculate_salary())

                else:

                    print("Chưa có nhân sự")



            case "7":

                print("Cảm ơn đã sử dụng hệ thống")

                break


            case _:

                print("Sai lựa chọn")



main()