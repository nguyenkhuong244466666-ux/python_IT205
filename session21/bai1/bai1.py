import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(current_dir, "momo_transactions.log")

logging.basicConfig(
    filename=log_path,
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def deposit(amount):
    """Xử lý nạp tiền, ném lỗi ValueError nếu tiền âm."""
    if amount <= 0:
        logging.error(f"InvalidAmountError: Attempted to process {amount} VND.")
        raise ValueError("InvalidAmountError: Số tiền giao dịch phải lớn hơn 0.")
        
    logging.info(f"Deposit successful: +{amount} VND.")
    return amount

def transfer(balance, phone, amount):
    """Xử lý chuyển tiền, ném lỗi ValueError nếu sai điều kiện."""
    if len(phone) != 10 or not phone.isdigit():
        raise ValueError("Số điện thoại không hợp lệ.")
        
    if amount <= 0:
        logging.error(f"InvalidAmountError: Attempted to process {amount} VND.")
        raise ValueError("InvalidAmountError: Số tiền giao dịch phải lớn hơn 0.")
        
    if amount > balance:
        logging.error(f"InsufficientBalanceError: Attempted to transfer {amount} VND with balance {balance} VND.")
        raise ValueError("InsufficientBalanceError: Giao dịch thất bại: Số dư của bạn không đủ.")
        
    if amount >= 10000000:
        logging.warning(f"High value transaction detected: {amount} VND to {phone}")
        
    logging.info(f"Transfer successful: -{amount} VND to {phone}.")
    return amount

def menu():
    print("\n========== VÍ MOMO GIẢ LẬP ==========")
    print("1. Nạp tiền vào ví")
    print("2. Chuyển tiền")
    print("3. Xem số dư hiện tại")
    print("4. Thoát chương trình")
    print("=======================================")

def main():
    user_mmoney = 0
    while True:
        menu()
        choice = input("Chọn chức năng (1-4): ")
        
        match choice:
            case "1":
                print("\n--- NẠP TIỀN VÀO VÍ ---")
                try:
                    input_money = int(input("Nhập vào số tiền cần nạp: "))
                    added_money = deposit(input_money)
                    user_mmoney += added_money
                    print(f"Nạp tiền thành công: +{added_money:,} VND")
                    print(f"Số dư hiện tại: {user_mmoney:,} VND")
                except ValueError as e:
                    print(f"Lỗi: {e}")
                    
            case "2":
                print("\n--- CHUYỂN TIỀN ---")
                try:
                    phone = input("Nhập số điện thoại người nhận: ")
                    input_money = int(input("Nhập số tiền cần chuyển: "))
                    deducted_money = transfer(user_mmoney, phone, input_money)
                    user_mmoney -= deducted_money
                    print(f"Chuyển tiền thành công tới số điện thoại {phone}.")
                    print(f"Số tiền đã chuyển: {deducted_money:,} VND")
                    print(f"Số dư còn lại: {user_mmoney:,} VND")
                except ValueError as e:
                    print(f"Lỗi: {e}")
                    
            case "3":
                print("\n--- SỐ DƯ VÍ MOMO ---")
                print(f"Số dư hiện tại: {user_mmoney:,} VND")
                logging.info(f"Balance checked. Current Balance: {user_mmoney}")
                
            case "4":
                print("Thoát chương trình")
                logging.info("System shutdown")
                break
                
            case _:
                print("Lựa chọn không hợp lệ")

main()