import requests

from src.services import DetailsApiServices, ListApiServices


def test_routes_are_accessible():
    exchange_pair = ListApiServices().get_random_active_exchange_and_pair()
    exchange = exchange_pair["exchange"]
    pair = exchange_pair["pair"]

    response = DetailsApiServices().get_exchange_and_pair_details(exchange, pair)
    routes = response.routes()
    for r in routes:
        route = requests.get(routes[r])
        assert route.status_code == 200
