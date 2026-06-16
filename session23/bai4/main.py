import utils.random_utils as random_utils

from data.students import student_records

from utils.string_utils import (
    normalize_student_names
)

from reports.report_generator import (
    display_student_scores,
    export_learning_report
)


def main():
    while True:
        print()
        print(
            "===== HỆ THỐNG TIỆN ÍCH "
            "HỌC TẬP RIKKEI ACADEMY ====="
        )

        print(
            "1. Xem danh sách sinh viên "
            "và điểm trung bình"
        )

        print(
            "2. Chuẩn hóa tên sinh viên"
        )

        print(
            "3. Sinh mã bài tập ngẫu nhiên"
        )

        print(
            "4. Xuất báo cáo học tập"
        )

        print("5. Thoát chương trình")

        print(
            "==============================="
            "====================="
        )

        try:
            choice = int(
                input(
                    "Chọn chức năng (1-5): "
                )
            )

            match choice:
                case 1:
                    display_student_scores(
                        student_records
                    )

                case 2:
                    normalize_student_names(
                        student_records
                    )

                case 3:
                    print(
                        "--- SINH MÃ BÀI TẬP ---"
                    )

                    print(
                        "Mã bài tập của bạn là:",
                        random_utils.generate_assignment_code()
                    )

                case 4:
                    export_learning_report(
                        student_records
                    )

                case 5:
                    print(
                        "Cảm ơn bạn đã sử dụng hệ thống!"
                    )
                    break

                case _:
                    print(
                        "Chức năng không hợp lệ. "
                        "Vui lòng chọn từ 1 đến 5."
                    )

        except ValueError:
            print(
                "Chức năng không hợp lệ. "
                "Vui lòng chọn từ 1 đến 5."
            )


if __name__ == "__main__":
    main()