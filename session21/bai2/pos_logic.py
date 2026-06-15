import logging

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Dữ liệu mặc định
DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}

def view_menu():
    """Hiển thị thực đơn đồ uống."""
    print("--- THỰC ĐƠN HIGHLANDS COFFEE ---")
    for code, info in DRINK_MENU.items():
        price_formatted = f"{info['price']:,}".replace(',', ',') 
        print(f"[{code}] - {info['name']} - {price_formatted} VNĐ")

def add_to_order(order: list, drink_code: str, quantity_str: str):
    """
    Xử lý thêm đồ uống vào giỏ hàng và kiểm tra các bẫy dữ liệu (bắn lỗi bằng Exception cơ bản).
    """
    code_upper = drink_code.strip().upper()
    
    if code_upper not in DRINK_MENU:
        raise Exception(f"ItemNotFoundError|{code_upper}")
    
    try:
        quantity = int(quantity_str)
    except ValueError:
        raise ValueError("Invalid quantity input")
        
    if quantity <= 0:
        raise Exception(f"InvalidQuantityError|{quantity_str}")

    item_found = False
    for item in order:
        if item["code"] == code_upper:
            item["quantity"] += quantity
            item_found = True
            break
            
    if not item_found:
        order.append({
            "code": code_upper,
            "name": DRINK_MENU[code_upper]["name"],
            "price": DRINK_MENU[code_upper]["price"],
            "quantity": quantity
        })
        
    logging.info(f"Added {quantity} of {code_upper} to order")
    return code_upper, quantity, DRINK_MENU[code_upper]["name"]

def calculate_total(order: list) -> int:
    """Tính tổng tiền của giỏ hàng hiện tại."""
    return sum(item["price"] * item["quantity"] for item in order)

def print_order_details(order: list):
    """In chi tiết giỏ hàng."""
    print("--- GIỎ HÀNG HIỆN TẠI ---")
    print(f"{'Mã SP':<5} | {'Tên đồ uống':<20} | {'Đơn giá':<8} | {'Số lượng':<8} | {'Thành tiền'}")
    print("-" * 64)
    
    for item in order:
        thanh_tien = item["price"] * item["quantity"]
        price_str = f"{item['price']:,}"
        thanh_tien_str = f"{thanh_tien:,} VNĐ"
        print(f"{item['code']:<5} | {item['name']:<20} | {price_str:<8} | {item['quantity']:<8} | {thanh_tien_str}")
    
    print("-" * 64)
    total = calculate_total(order)
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")
    return total