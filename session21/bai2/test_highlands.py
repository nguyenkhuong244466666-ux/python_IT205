import unittest
from pos_logic import calculate_total, add_to_order

class TestHighlandsPOS(unittest.TestCase):

    def test_calculate_total(self):
        """Test tính tổng tiền với giỏ hàng giả (Mock list)."""
        mock_order = [
            {"code": "P1", "name": "Phin Sữa Đá", "price": 35000, "quantity": 2},
            {"code": "F1", "name": "Freeze Trà Xanh", "price": 55000, "quantity": 1}
        ]
        result = calculate_total(mock_order)
        self.assertEqual(result, 125000)

    def test_invalid_quantity(self):
        """Test truyền số lượng âm vào hàm add_to_order để kiểm tra ngoại lệ số lượng."""
        mock_order = []
        with self.assertRaisesRegex(Exception, "InvalidQuantityError"):
            add_to_order(mock_order, "T1", "-1")

unittest.main()