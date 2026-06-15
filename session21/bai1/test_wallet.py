import pytest
from bai1 import deposit, transfer

def test_deposit_success():
    assert deposit(50000) == 50000

def test_transfer_insufficient_balance():
    with pytest.raises(ValueError, match="InsufficientBalanceError"):
        transfer(10000, "0987654321", 50000)

def test_invalid_amount():
    with pytest.raises(ValueError, match="InvalidAmountError"):
        deposit(-10000)

def test_transfer_success():
    assert transfer(100000, "0912345678", 20000) == 20000