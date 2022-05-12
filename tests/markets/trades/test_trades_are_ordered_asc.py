from src.services import ListApiServices, TradesApiServices


def test_trades_are_ordered_asc():
    exchange_pair = ListApiServices().get_random_active_exchange_and_pair()
    exchange = exchange_pair["exchange"]
    pair = exchange_pair["pair"]

    response = TradesApiServices().get_trades(exchange, pair)
    trades = response.result()
    for trade in range(0, len(trades) - 1):
        assert trades[trade][1] <= trades[trade + 1][1]
