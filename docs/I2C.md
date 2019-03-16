# I<sup>2</sup>C Development Crash Course

## Orbitty Carrier Pin Layout

|      |    |
|------|----|
|  1   | 2  |
|  3   | 4  |
|  5   | 6  |
|  7   | 8  |
|  9   | 10 |
| **11** | **12** |
|  13  | 14 |
|  15  | 16 |
|  17  | 18 |
|  19  | **20** |

Pin 11: `SCL`

Pin 12: `SDA`

Pin 20: `GND`

## Development Tips

To determine the I<sup>2</sup>C address of a device connected to the TX2:

* `sudo apt-get install libi2c-dev i2c-tools`
* `sudo i2cdetect -y -r 0`

The device address will be shown in the table output as a two digit hex character (ignore u characters).

In python, we use the `python-smbus` package, which you can find some docs for [here](http://wiki.erazor-zone.de/wiki:linux:python:smbus:doc).