# [PGS] 치킨 쿠폰/21/오슬기

def solution(chicken):
    coupon = 0
    service = 0

    while True:
        if chicken + coupon < 10:
            break
        a, b = divmod(chicken, 10)
        service += a
        coupon += b

        if coupon >= 10:
            chicken = a + 1
            coupon -= 10
            service += 1
        else:
            chicken = a

    return service