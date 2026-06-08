def calculate_discount(total_purchase):
    """
    Trả về tỷ lệ giảm giá:
    - 10% nếu tổng mua hàng >= 50 triệu
    - 0% nếu chưa đạt
    """
    if total_purchase >= 50000000:
        return 0.1
    return 0