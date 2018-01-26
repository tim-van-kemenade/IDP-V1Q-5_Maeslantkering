# Maeslantkering
This project contains a proof of concept for the Maeslantkering.

## How to run
To run the application make sure you have the dependencies installed.
```sh
$ pip install -r requirements.txt
```

To run the server locally you need to mock the pin factory since a
normal computer doesn't have any GPIO pins.
```sh
$ export GPIOZERO_PIN_FACTORY=mock
```