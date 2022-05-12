## Project description

A total of 6 tests have been created, 1 per endpoint (/details, /price, etc.). 
As a diversification of test data, each test utilizes a random object of active 
exchange-pair set, randomly obtained from the /list endpoint. 

Simple logging has been added.

The following external libraries have been user:
* `pytest`
* `request` 
* `pytest-env`

### Run tests

* Install Python v3.9 or higher.
* Clone the project.
* Navigate to the root directory of the cloned project. 
* `pipenv install`
* `pipenv shell`
* Create the `pytest.ini` file in the same root directory.
Populate it according to the following blueprint, and substitute the 
<YOUR_API_KEY> with your valid API key.

```
[pytest]

log_cli = 1
log_cli_level = info
log_cli_format = %(asctime)s [%(levelname)s] %(message)s

env =
    BASE_MARKETS_URL=https://api.cryptowat.ch/markets
    API_KEY=<YOUR_API_KEY>
```


* `pytest tests/markets/` <-- run tests


### Comments

* Files response.py and services.py might be conceived as redundant for a few tests, 
however, they help to keep everything a bit cleaner and organized.