# Washing Days

Predicting the ideal times to dry clothes outside using meteorological data.

Currently using **temperature, relative humidity, precipitation, wind speed and direct solar radiation** to calculate the best time frames. Further refinment will be based on real-world testing. See washing-days.py for more information.

Weather data very kindly provided by: <a href="https://open-meteo.com/">CleanOpen-Meteo.com</a>

## Live Demo

<a href="https://wshelley.github.io/washing-days.txt">Live Data Hourly Export from Washing Days</a>


Updating every hour.

## Example Usage:
```
pip3 install -r requirements.txt
python3 washing-days.py --lon -3.35 --lat 55.75
```
## Example Output:

![Output](docs/example-output.png)

## Intial Project Setup:
```
mkdir washing-days
cd washing-days
python3 -m venv venv
git init
```

```
source venv/bin/activate
Select Command Palete > Python > Select Interpreter ./venv/bin/python3.9
pip3 install -r requirements.txt
```
