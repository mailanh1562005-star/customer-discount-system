from discount import calculate_discount


def test_vip_customer():
    # Khách hàng đã đạt VIP
    assert calculate_discount(62000000) == 0.1


def test_normal_customer():
    # Khách hàng chưa đạt VIP
    assert calculate_discount(32000000) == 0


def test_middle_customer():
    # Khách hàng chưa đạt VIP
    assert calculate_discount(51000000) == 0.1
    