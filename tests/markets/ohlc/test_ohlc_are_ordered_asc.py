import datetime

from src.services import ListApiServices, OhlcApiServices


def test_ohlc_are_ordered_asc():
    exchange_pair = ListApiServices().get_random_active_exchange_and_pair()
    exchange = exchange_pair["exchange"]
    pair = exchange_pair["pair"]

    days_1 = int((datetime.datetime.now() - datetime.timedelta(days=1)).timestamp())
    hours_1 = 1 * 60 * 60
    response = OhlcApiServices().get_ohlc_with_date_and_hours(
        exchange,
        pair,
        f"after={days_1}&periods={hours_1}")

    candles = response.candle(hours_1)
    for candle in range(0, len(candles) - 1):
        assert candles[candle][0] < candles[candle + 1][0]
