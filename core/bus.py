import sys
from config.board import I2CConfig

from machine import I2C


def i2c_factory() -> I2C:
    return I2C(
        I2CConfig.ID,
        scl=I2CConfig.SCL,
        sda=I2CConfig.SDA,
        freq=I2CConfig.FREQUENCY,
    )
