import logging
from pos_logic import (
    view_menu, add_to_order, calculate_total, print_order_details
)

def main():
    current_order = []
    
    while True:
        print("\n========== HIGHLANDS MINI POS ==========")
        print("1. Xem thực đơn")
        print("2. Thêm món vào giỏ")
        print("3. Xem giỏ hàng & Tính tổng tiền")
        print("4. Thanh toán & Xóa giỏ hàng")
        print("5. Thoát ca làm việc")
        print("========================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        match choice:
            case '1':
                view_menu()
                
            case '2':
                print("--- THÊM MÓN VÀO GIỎ ---")
                drink_code = input("Nhập mã đồ uống: ")
                quantity_str = input("Nhập số lượng: ")
                
                try:
                    code, qty, name = add_to_order(current_order, drink_code, quantity_str)
                    print(f"Đã thêm {qty} x {name} vào giỏ hàng.")
                    
                except ValueError:
                    print("Vui lòng nhập số lượng là một số nguyên!")
                    logging.error("ValueError - Invalid quantity input")
                    
                except Exception as e:
                    error_msg = str(e)
                    
                    if "ItemNotFoundError" in error_msg:
                        code_loi = error_msg.split("|")[1]
                        print("Mã đồ uống không hợp lệ, vui lòng kiểm tra lại thực đơn!")
                        logging.warning(f"ItemNotFoundError - Code: {code_loi}")
                        
                    elif "InvalidQuantityError" in error_msg:
                        qty_loi = error_msg.split("|")[1]
                        print("Số lượng phải lớn hơn 0!")
                        logging.warning(f"InvalidQuantityError - Quantity: {qty_loi}")
                    
            case '3':
                if not current_order:
                    print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
                else:
                    print_order_details(current_order)
                    
            case '4':
                if not current_order:
                    print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
                    continue
                    
                print("--- THANH TOÁN ---")
                total = calculate_total(current_order)
                print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")
                
                confirm = input(f"Xác nhận thanh toán {total:,} VNĐ? (y/n): ").strip().lower()
                if confirm == 'y':
                    print("Thanh toán thành công.")
                    logging.info("Checkout successful")
                    current_order.clear()
                    print("Giỏ hàng đã được làm trống.")
                elif confirm == 'n':
                    print("Đã hủy thao tác thanh toán. Quay lại menu chính.")
                else:
                    print("Lựa chọn không hợp lệ. Thanh toán đã bị hủy.")
                    
            case '5':
                logging.info("Cashier logged out. System shutdown.")
                print("Đã thoát ca làm việc. Hẹn gặp lại!")
                break
                
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5.")

main()