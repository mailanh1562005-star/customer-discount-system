from discount import calculate_discount


def test_vip_customer():
    # Khách hàng đã đạt VIP
    assert calculate_discount(60000000) == 0.1


def test_normal_customer():
    # Khách hàng chưa đạt VIP
    assert calculate_discount(30000000) == 0


def test_boundary_customer():
    # Đúng ngưỡng 50 triệu
    assert calculate_discount(50000000) == 0.1
    