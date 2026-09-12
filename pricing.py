def calculate_final_price(price, discount_percent=0):
    if price < 0:
        raise ValueError("Price cannot be negative")

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")

    # BUG: discount_percent is incorrectly treated as a fixed amount
    discount_amount = discount_percent

    return price - discount_amount
