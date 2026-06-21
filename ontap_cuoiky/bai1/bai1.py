class Student:
    def __init__(self, student_id, name, theory_score, practice_score, project_score):
        self.__id = student_id
        self.__name = name
        self.__theory_score = theory_score
        self.__practice_score = practice_score
        self.__project_score = project_score
        self.__final_score = 0
        self.__academic_rank = ""

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def theory_score(self):
        return self.__theory_score

    @property
    def practice_score(self):
        return self.__practice_score

    @property
    def project_score(self):
        return self.__project_score

    @property
    def final_score(self):
        return self.__final_score

    @property
    def academic_rank(self):
        return self.__academic_rank

    def update_theory_score(self, theory_score):
        self.__theory_score = theory_score

    def update_practice_score(self, practice_score):
        self.__practice_score = practice_score

    def update_project_score(self, project_score):
        self.__project_score = project_score

    def calculate_final_score(self):
        self.__final_score = (
            self.__theory_score * 0.2
            + self.__practice_score * 0.3
            + self.__project_score * 0.5
        )

    def classify_academic_rank(self):
        if self.__final_score < 5:
            self.__academic_rank = "Yếu"
        elif self.__final_score < 7:
            self.__academic_rank = "Trung bình"
        elif self.__final_score < 8.5:
            self.__academic_rank = "Khá"
        else:
            self.__academic_rank = "Giỏi"


class StudentManager:
    def __init__(self):
        self.students = []

    def input_score(self, message):
        while True:
            try:
                score = float(input(message))

                if 0 <= score <= 10:
                    return score

                print("Điểm phải từ 0 đến 10!")

            except ValueError:
                print("Vui lòng nhập số hợp lệ!")

    def add_student(self):
        student_id = input("Nhập mã sinh viên: ").strip()

        if not student_id:
            print("Mã sinh viên không được để trống")
            return

        for student in self.students:
            if student.id == student_id:
                print("Mã sinh viên đã tồn tại")
                return

        name = input("Nhập họ tên: ").strip()

        if not name:
            print("Họ tên không được để trống")
            return

        theory_score = self.input_score("Nhập điểm lý thuyết: ")
        practice_score = self.input_score("Nhập điểm thực hành: ")
        project_score = self.input_score("Nhập điểm đồ án: ")

        student = Student(
            student_id,
            name,
            theory_score,
            practice_score,
            project_score
        )

        student.calculate_final_score()
        student.classify_academic_rank()

        self.students.append(student)

        print("Thêm sinh viên thành công!")

    def show_all(self):
        if not self.students:
            print("Không có sinh viên nào")
            return

        print("-" * 120)

        print(
            f"{'Mã SV':<10}"
            f"{'Họ tên':<25}"
            f"{'Lý thuyết':<15}"
            f"{'Thực hành':<15}"
            f"{'Đồ án':<15}"
            f"{'Tổng kết':<15}"
            f"{'Học lực'}"
        )

        print("-" * 120)

        for student in self.students:
            print(
                f"{student.id:<10}"
                f"{student.name:<25}"
                f"{student.theory_score:<15.1f}"
                f"{student.practice_score:<15.1f}"
                f"{student.project_score:<15.1f}"
                f"{student.final_score:<15.2f}"
                f"{student.academic_rank}"
            )

    def update_student(self):
        student_id = input("Nhập mã sinh viên cần cập nhật: ")

        for student in self.students:
            if student.id == student_id:

                theory_score = self.input_score(
                    "Nhập điểm lý thuyết mới: "
                )

                practice_score = self.input_score(
                    "Nhập điểm thực hành mới: "
                )

                project_score = self.input_score(
                    "Nhập điểm đồ án mới: "
                )

                student.update_theory_score(theory_score)
                student.update_practice_score(practice_score)
                student.update_project_score(project_score)

                student.calculate_final_score()
                student.classify_academic_rank()

                print("Cập nhật thành công!")
                return

        print("Không tìm thấy sinh viên")

    def delete_student(self):
        student_id = input("Nhập mã sinh viên cần xóa: ")

        for student in self.students:
            if student.id == student_id:

                choice = input(
                    "Bạn có chắc muốn xóa sinh viên này không? (Y/N): "
                ).lower()

                if choice == "y":
                    self.students.remove(student)
                    print("Đã xóa thành công!")
                else:
                    print("Hủy thao tác")

                return

        print("Không tìm thấy sinh viên")

    def search_student(self):
        keyword = input("Nhập tên cần tìm: ").lower()

        found = False

        for student in self.students:
            if keyword in student.name.lower():
                found = True

                print(
                    f"{student.id} | "
                    f"{student.name} | "
                    f"{student.final_score:.2f} | "
                    f"{student.academic_rank}"
                )

        if not found:
            print("Không tìm thấy sinh viên phù hợp")


def menu():
    print("""
================ MENU ================
1. Hiển thị danh sách sinh viên
2. Thêm sinh viên mới
3. Cập nhật thông tin sinh viên
4. Xóa sinh viên
5. Tìm kiếm sinh viên theo tên
6. Thoát
=====================================
""")


def main():
    manager = StudentManager()

    while True:
        menu()

        choice = input("Nhập lựa chọn của bạn: ")

        match choice:

            case "1":
                manager.show_all()

            case "2":
                manager.add_student()

            case "3":
                manager.update_student()

            case "4":
                manager.delete_student()

            case "5":
                manager.search_student()

            case "6":
                print(
                    "Cảm ơn bạn đã sử dụng hệ thống quản lý học tập!"
                )
                break

            case _:
                print("Lựa chọn không hợp lệ!")


main()