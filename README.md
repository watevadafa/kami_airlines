# KAMI Airlines

API written in Python for a airline company called KAMI Airlines, to create the solution for the aircraft passenger capacity issue.

## Requirements

- The company is assessing 10 different airplanes.
- Each airplane has a fuel tank of (200 liters * id of the airplane) capacity. For example, if the airplane id = 2, the fuel tank capacity is 2*200 = 400 liters.
- The airplane fuel consumption per minute is the logarithm of the airplane id multiplied by 0.80 liters.
- Each passenger will increase fuel consumption for additional 0.002 liters per minute.

### Features

- Takes input of 10 airplanes with user defined `id` and `number_of_passengers` (passenger assumptions).
- Prints total airplane`fuel_consumption_per_minute` and maximum minutes able to fly%

### Installation

1. Clone the repository
2. Run `pip install -r requirements.txt`
3. Run `bash run_tests.sh` to exucte the test cases
4. Run `bash run_server.sh` to execute the application
5. Using Postman or any other API testing tool, hit the following endpoints
   - GET `http://localhost:8000/airplanes` to list all the airplanes
   - GET `http://localhost:8000/airplanes/<airplane_id>` to view details a specific airplane
   - POST `http://localhost:8000/airplanes/evaluate` to assess in bulk the airplanes for their fuel consumption and maximum minutes able to fly

### Example

- POST `http://localhost:8000/airplanes/evaluate`

- Request Body

```
[
    { "id": 10, "number_of_passengers": 100 },
    { "id": 20, "number_of_passengers": 200 },
    { "id": 30, "number_of_passengers": 300 },
    { "id": 40, "number_of_passengers": 400 },
    { "id": 50, "number_of_passengers": 500 },
    { "id": 60, "number_of_passengers": 600 },
    { "id": 70, "number_of_passengers": 700 },
    { "id": 80, "number_of_passengers": 800 },
    { "id": 90, "number_of_passengers": 900 },
    { "id": 99, "number_of_passengers": 999 }
]
```

- Response Body

```
[
    {
        "id": 10,
        "number_of_passengers": 100,
        "fuel_consumption_rate_per_minute": 2.042068074395237,
        "maximum_flight_duration_in_minutes": 979.3992791314288
    },
    {
        "id": 20,
        "number_of_passengers": 200,
        "fuel_consumption_rate_per_minute": 2.7965858188431927,
        "maximum_flight_duration_in_minutes": 1430.3154843481968
    },
    {
        "id": 30,
        "number_of_passengers": 300,
        "fuel_consumption_rate_per_minute": 3.3209579053297245,
        "maximum_flight_duration_in_minutes": 1806.7076340747187
    },
    {
        "id": 40,
        "number_of_passengers": 400,
        "fuel_consumption_rate_per_minute": 3.7511035632911494,
        "maximum_flight_duration_in_minutes": 2132.7057131371084
    },
    {
        "id": 50,
        "number_of_passengers": 500,
        "fuel_consumption_rate_per_minute": 4.1296184043425175,
        "maximum_flight_duration_in_minutes": 2421.5312459583333
    },
    {
        "id": 60,
        "number_of_passengers": 600,
        "fuel_consumption_rate_per_minute": 4.475475649777681,
        "maximum_flight_duration_in_minutes": 2681.2792514234993
    },
    {
        "id": 70,
        "number_of_passengers": 700,
        "fuel_consumption_rate_per_minute": 4.798796193639488,
        "maximum_flight_duration_in_minutes": 2917.3983297219725
    },
    {
        "id": 80,
        "number_of_passengers": 800,
        "fuel_consumption_rate_per_minute": 5.105621307739105,
        "maximum_flight_duration_in_minutes": 3133.800772835852
    },
    {
        "id": 90,
        "number_of_passengers": 900,
        "fuel_consumption_rate_per_minute": 5.3998477362642125,
        "maximum_flight_duration_in_minutes": 3333.4273259440047
    },
    {
        "id": 99,
        "number_of_passengers": 999,
        "fuel_consumption_rate_per_minute": 5.674095880107672,
        "maximum_flight_duration_in_minutes": 3489.542725108881
    }
]
```

### Coverage
```
> bash run_tests.sh
Found 17 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.................
----------------------------------------------------------------------
Ran 17 tests in 0.020s

OK
Destroying test database for alias 'default'...
Name                           Stmts   Miss  Cover   Missing
------------------------------------------------------------
airplanes/__init__.py              0      0   100%
airplanes/admin.py                 8      0   100%
airplanes/apps.py                  4      0   100%
airplanes/constants.py             6      0   100%
airplanes/models.py               18      0   100%
airplanes/serializers.py          10      0   100%
airplanes/tests/__init__.py        0      0   100%
airplanes/tests/factories.py      21      0   100%
airplanes/utils.py                10      0   100%
airplanes/views.py                18      0   100%
kami_airlines/__init__.py          0      0   100%
kami_airlines/settings.py         19      0   100%
kami_airlines/urls.py              7      0   100%
------------------------------------------------------------
TOTAL                            121      0   100%

```