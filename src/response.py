import logging


class AssertableResponse(object):

    def __init__(self, response):
        logging.info(f"request: {response.request.method} {response.request.url}")
        logging.info(f"response: status code [{response.status_code}]")
        self._response = response

    def result(self):
        return self._response.json()["result"]

    def status_code(self, code):
        return self._response.status_code == code


class AssertableDetailsResponse(AssertableResponse):

    def __init__(self, response):
        super().__init__(response)
        self._response = response

    def routes(self):
        return self.result()["routes"]


class AssertableOhlcResponse(AssertableResponse):

    def __init__(self, response):
        super().__init__(response)
        self._response = response

    def candle(self, timeframe):
        return self.result()[f"{timeframe}"]


class AssertableOrderbookResponse(AssertableResponse):

    def __init__(self, response):
        super().__init__(response)
        self._response = response

    def asks(self):
        return self.result()["asks"]


class AssertablePriceResponse(AssertableResponse):

    def __init__(self, response):
        super().__init__(response)
        self._response = response

    def price(self):
        return self.result()["price"]


class AssertableSummaryResponse(AssertableResponse):

    def __init__(self, response):
        super().__init__(response)
        self._response = response

    def result_price(self):
        return self.result()["price"]

    def price_high(self):
        return self.result_price()["high"]

    def price_low(self):
        return self.result_price()["low"]


class AssertableTradesResponse(AssertableResponse):

    def __init__(self, response):
        super().__init__(response)
        self._response = response
