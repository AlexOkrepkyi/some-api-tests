from src.services import ListApiServices, PriceApiServices


def test_price_is_positive_digit():
    exchange_pair = ListApiServices().get_random_active_exchange_and_pair()
    exchange = exchange_pair["exchange"]
    pair = exchange_pair["pair"]

    response = PriceApiServices().get_price_for_pair_at_exchange(exchange, pair)
    assert response.price() >= 0
