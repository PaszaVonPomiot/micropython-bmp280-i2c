from bmp280 import BMP280I2C
from config.board import I2CConfig
from config.sensors import get_bmp280_config

from core.rtc import clock
from core.bus import i2c_factory
from machine import Pin


class BMP280GPIO:
    """I2C to GPIO mapping and configuration."""

    SDA = Pin(I2CConfig.SDA)
    SCL = Pin(I2CConfig.SCL)


class BMP280Sensor:
    def __init__(self, address: int) -> None:
        self.bmp280_config = get_bmp280_config()
        self.bmp280_i2c = BMP280I2C(
            address=address,
            i2c=i2c_factory(),
            configuration=self.bmp280_config,
        )

    def get_readout(self) -> tuple[float, float]:
        """Get temperature and pressure readout from BMP280 sensor"""
        readout = self.bmp280_i2c.measurements
        return (readout["t"], readout["p"])

    def get_csv_record(self) -> str:
        """Get a formatted CSV record with the current timestamp, temperature and pressure"""
        readout = self.bmp280_i2c.measurements
        return f"{clock.now()};{readout['t']:.2f};{readout['p']:.2f}"
