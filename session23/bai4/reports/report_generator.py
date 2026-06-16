from datetime import datetime

from colorama import Fore
from colorama import init

from utils.score_utils import (
    calculate_average,
    classify_student
)

init(autoreset=True)


def display_student_scores(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("--- DANH SÁCH ĐIỂM SINH VIÊN ---")

    for index, student in enumerate(records, start=1):
        average = calculate_average(
            student["scores"]
        )

        rank = classify_student(average)

        print(
            f"{index}. [{student['student_id']}] "
            f"{student['name']} | "
            f"Điểm: {student['scores']} | "
            f"ĐTB: {average:.2f} - {rank}"
        )

    print("---------------------------------")


def export_learning_report(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total_students = len(records)
    passed = 0
    failed = 0

    for student in records:
        average = calculate_average(
            student["scores"]
        )

        if average >= 5:
            passed += 1
        else:
            failed += 1

    with open(
        "learning_report.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(
            "BÁO CÁO HỌC TẬP\n"
        )

        file.write(
            f"Thời gian tạo: "
            f"{datetime.now()}\n"
        )

        file.write(
            f"Tổng sinh viên: "
            f"{total_students}\n"
        )

        file.write(
            f"Đạt yêu cầu: "
            f"{passed}\n"
        )

        file.write(
            f"Cần cải thiện: "
            f"{failed}\n"
        )

    print(
        f"Tổng số sinh viên: "
        f"{total_students}"
    )

    print(
        f"Số sinh viên đạt yêu cầu: "
        f"{passed}"
    )

    print(
        f"Số sinh viên cần cải thiện: "
        f"{failed}"
    )

    print(
        Fore.GREEN +
        ">> Đã xuất báo cáo ra file "
        "learning_report.txt"
    )