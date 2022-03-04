from src.calc import *

def test_mul():
    assert 6 == mul(3, 2)

def test_div():
    assert 6 == div(12,2)

def test_plus():
    assert 2 == plus(1,1) # 間違えたテスト