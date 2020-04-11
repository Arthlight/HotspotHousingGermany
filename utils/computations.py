

def get_difference(mean_price: float, current_price: int) -> float:
    if mean_price > current_price:
        return mean_price - current_price

    return current_price - mean_price
