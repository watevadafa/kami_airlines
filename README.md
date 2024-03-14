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
- Clone the repository
- Run `pip install -r requirements.txt`
- Run `bash run_tests.sh` to exucte the test cases
- Run `bash run_app.sh` to execute the application
