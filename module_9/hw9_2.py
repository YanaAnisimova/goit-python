DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):

    return price * (1 - customer.get('discount', DEFAULT_DISCOUNT))
