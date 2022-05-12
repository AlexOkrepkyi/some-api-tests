from src.services import ListApiServices, SummaryApiServices


def test_high_price_is_larger_than_low_price():
    exchange_pair = ListApiServices().get_random_active_exchange_and_pair()
    exchange = exchange_pair["exchange"]
    pair = exchange_pair["pair"]

    response = SummaryApiServices().get_pair_summary(exchange, pair)
    assert response.price_high() >= response.price_low()
