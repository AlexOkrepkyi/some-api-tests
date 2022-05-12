
- 2 assertions - not good
- I did not use cryptowatch SDK but pure requests
- created a function that returns random exchange-pair object 
to increase the coverage
- added simple logging to see the request URL

e2e tests:
- orderbook is a dummy test, since I used a random generation of market 
and pair, and some may have no active orderbook
- same for the ohlc

todo:
* add env to store secret keys
* add logging
* add pytest.ini creation example file 

Tests:

* test_routes_are_accessible --> tests the status code of each route 
in the /details endpoint
* test_price_is_positive_digit --> test that a price >= 0
