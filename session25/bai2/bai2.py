class NetflixAccount:
    """
    Netflix Account Manager
    """

    platform_name = "Netflix"
    max_profiles = 5

    def __init__(self, email):
        self.email = email
        self.__password = ""
        self.__plan = "Basic"
        self.profiles = []

    # Property dùng để đọc mật khẩu
    @property
    def password(self):
        return "********"

    # Setter kiểm tra độ dài mật khẩu
    @password.setter
    def password(self, new_password):
        if len(new_password) < 6:
            raise ValueError("Password is too short")

        self.__password = new_password

    # Property chỉ đọc gói cước
    @property
    def plan(self):
        return self.__plan

    # Static Method kiểm tra email
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email

    # Class Method cập nhật số profile tối đa
    @classmethod
    def update_max_profiles(cls, new_limit):
        cls.max_profiles = new_limit

    # Thêm profile
    def add_profile(self, profile_name):
        if len(self.profiles) >= NetflixAccount.max_profiles:
            print(
                "Đã đạt giới hạn số lượng Profile trên tài khoản này"
            )
            return

        self.profiles.append(profile_name)
        print("Thêm Profile thành công!")

    # Nâng cấp gói cước
    def upgrade_plan(self, new_plan):
        valid_plans = ["Basic", "Standard", "Premium"]

        if new_plan not in valid_plans:
            print("Gói cước không hợp lệ!")
            return

        self.__plan = new_plan
        print(f"Đã nâng cấp lên gói {new_plan}")

    # Hiển thị thông tin tài khoản
    def display_info(self):
        print("\n--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Nền tảng: {NetflixAccount.platform_name}")
        print(f"Email: {self.email}")
        print(f"Mật khẩu: {self.password}")
        print(f"Gói cước: {self.__plan}")

        if self.profiles:
            print("Danh sách Profile:")
            for index, profile in enumerate(
                self.profiles, start=1
            ):
                print(f"{index}. {profile}")
        else:
            print("Chưa có Profile nào")


current_account = None

while True:
    print("\n===== NETFLIX ACCOUNT MANAGER =====")
    print("1. Đăng ký tài khoản mới")
    print("2. Xem thông tin tài khoản")
    print("3. Thêm người xem")
    print("4. Nâng cấp gói cước")
    print("5. Cập nhật chính sách Netflix")
    print("6. Thoát chương trình")
    print("===================================")

    choice = input("Chọn chức năng (1-6): ")

    match choice:
        case "1":
            print("\n--- ĐĂNG KÝ TÀI KHOẢN ---")

            while True:
                email = input("Nhập email: ")

                if NetflixAccount.validate_email(email):
                    break

                print(
                    "Email không hợp lệ, vui lòng chứa ký tự '@' và '.'"
                )

            while True:
                password = input("Nhập mật khẩu: ")

                try:
                    account = NetflixAccount(email)
                    account.password = password
                    current_account = account
                    break

                except ValueError as e:
                    print(e)

            print("Đăng ký tài khoản thành công!")

        case "2":
            if current_account is None:
                print(
                    "Vui lòng đăng ký tài khoản trước (Chức năng 1)"
                )
            else:
                current_account.display_info()

        case "3":
            if current_account is None:
                print(
                    "Vui lòng đăng ký tài khoản trước (Chức năng 1)"
                )
                continue

            profile_name = input(
                "Nhập tên Profile mới: "
            )

            current_account.add_profile(profile_name)

        case "4":
            if current_account is None:
                print(
                    "Vui lòng đăng ký tài khoản trước (Chức năng 1)"
                )
                continue

            print("\nCác gói cước:")
            print("1. Basic")
            print("2. Standard")
            print("3. Premium")

            plan = input(
                "Nhập tên gói muốn nâng cấp: "
            )

            current_account.upgrade_plan(plan)

        case "5":
            try:
                new_limit = int(
                    input(
                        "Nhập số lượng Profile tối đa mới: "
                    )
                )

                if new_limit <= 0:
                    print("Giới hạn phải lớn hơn 0")
                    continue

                NetflixAccount.update_max_profiles(
                    new_limit
                )

                print(
                    f"Đã cập nhật giới hạn Profile "
                    f"toàn hệ thống thành {new_limit}"
                )

            except ValueError:
                print("Dữ liệu không hợp lệ!")

        case "6":
            print(
                "Cảm ơn bạn đã sử dụng Netflix Account Manager!"
            )
            break

        case _:
            print("Lựa chọn không hợp lệ!")