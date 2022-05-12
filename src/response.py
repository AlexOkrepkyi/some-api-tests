import logging


class AssertableResponse(object):

    def __init__(self, response):
        logging.info(f"Request URL={response.request.url}")
        self._response = response

    def result(self):
        return self._response.json()["result"]


class AssertableDetailsResponse:

    def __init__(self, response):
        logging.info(f"Request URL={response.request.url}")
        self._response = response

    def result(self):
        return self._response.json()["result"]

    def routes(self):
        return self.result()["routes"]


class AssertableOhlcResponse:

    def __init__(self, response):
        logging.info(f"Request URL={response.request.url}")
        self._response = response

    def result(self):
        return self._response.json()["result"]

    def candle(self, timeframe):
        return self.result()[f"{timeframe}"]


class AssertableOrderbookResponse:

    def __init__(self, response):
        logging.info(f"Request URL={response.request.url}")
        self._response = response

    def result(self):
        return self._response.json()["result"]

    def asks(self):
        return self.result()["asks"]


class AssertablePriceResponse:

    def __init__(self, response):
        logging.info(f"Request URL={response.request.url}")
        self._response = response

    def result(self):
        return self._response.json()["result"]

    def price(self):
        return self.result()["price"]


class AssertableSummaryResponse:

    def __init__(self, response):
        logging.info(f"Request URL={response.request.url}")
        self._response = response

    def result_price(self):
        return self._response.json()["result"]["price"]

    def price_high(self):
        return self.result_price()["high"]

    def price_low(self):
        return self.result_price()["low"]
