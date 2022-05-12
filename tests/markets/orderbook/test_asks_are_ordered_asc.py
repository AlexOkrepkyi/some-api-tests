from src.services import ListApiServices, OrderbookApiServices


def test_asks_are_ordered_asc():
    exchange_pair = ListApiServices().get_random_active_exchange_and_pair()
    exchange = exchange_pair["exchange"]
    pair = exchange_pair["pair"]

    response = OrderbookApiServices().get_orderbook(exchange, pair)

    asks = response.asks()
    for ask in range(0, len(asks) - 1):
        assert float(asks[ask][0]) <= float(asks[ask + 1][0])
