import os
import random

import requests

from src.response import AssertableResponse, AssertableSummaryResponse, AssertableOrderbookResponse, \
    AssertablePriceResponse, AssertableDetailsResponse, AssertableOhlcResponse


class MarketsApiServices(object):

    def __init__(self):
        self.base_markets_url = os.environ["BASE_MARKETS_URL"]
        self.api_key = os.environ["API_KEY"]

    def _get_base_url(self):
        return requests.get(f"{self.base_markets_url}?apikey={self.api_key}")

    def _get_base_url_including_exchange_pair(self, exchange, pair):
        return requests.get(f"{self.base_markets_url}/{exchange}/{pair}?apikey={self.api_key}")

    def _get_base_url_including_exchange_pair_endpoint(self, exchange, pair, endpoint):
        return requests.get(f"{self.base_markets_url}/{exchange}/{pair}/{endpoint}?apikey={self.api_key}")

    def _get_base_url_including_exchange_pair_endpoint_params(self, exchange, pair, endpoint, params):
        return requests.get(f"{self.base_markets_url}/{exchange}/{pair}/{endpoint}?apikey={self.api_key}&{params}")


class DetailsApiServices(MarketsApiServices):

    def __init__(self):
        super().__init__()

    def get_exchange_and_pair_details(self, exchange, pair):
        return AssertableDetailsResponse(self._get_base_url_including_exchange_pair(exchange, pair))


class ListApiServices(MarketsApiServices):

    def __init__(self):
        super().__init__()

    def get_random_active_exchange_and_pair(self):
        random_exchange_pair = self.get_random_exchange_and_pair()
        if random_exchange_pair["active"]:
            return random_exchange_pair
        else:
            return self.get_random_active_exchange_and_pair()

    def get_random_exchange_and_pair(self):
        response = self._get_base_url()
        result = response.json()["result"]
        return result[random.randint(0, len(result))]


class OhlcApiServices(MarketsApiServices):

    def __init__(self):
        super().__init__()

    def get_ohlc_with_date_and_hours(self, exchange, pair, params):
        return AssertableOhlcResponse(self._get_base_url_including_exchange_pair_endpoint_params(exchange, pair, "ohlc", params))


class OrderbookApiServices(MarketsApiServices):

    def __init__(self):
        super().__init__()

    def get_orderbook(self, exchange, pair):
        return AssertableOrderbookResponse(self._get_base_url_including_exchange_pair_endpoint(exchange, pair, "orderbook"))


class PriceApiServices(MarketsApiServices):

    def __init__(self):
        super().__init__()

    def get_price_for_pair_at_exchange(self, exchange, pair):
        return AssertablePriceResponse(self._get_base_url_including_exchange_pair_endpoint(exchange, pair, "price"))


class SummaryApiServices(MarketsApiServices):

    def __init__(self):
        super().__init__()

    def get_pair_summary(self, exchange, pair):
        return AssertableSummaryResponse(self._get_base_url_including_exchange_pair_endpoint(exchange, pair, "summary"))


class TradesApiServices(MarketsApiServices):

    def __init__(self):
        super().__init__()

    def get_trades(self, exchange, pair):
        return AssertableResponse(self._get_base_url_including_exchange_pair_endpoint(exchange, pair, "trades"))
