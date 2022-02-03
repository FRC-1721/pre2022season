# FRC 1721
# 2022

import logging

from ctre import ErrorCode
from ctre.led import CANdle, CANdleConfiguration, LEDStripType
from commands2 import SubsystemBase
from constants.constants import getConstants


class Lighting(SubsystemBase):
    """
    This class represents the whole lighting
    and effects subsystem on the robot.
    """

    def __init__(self):
        super().__init__()

        # Get hardware constants
        self.constants = getConstants("robot_hardware")

        # Configure CANdle module
        self.CANdle = CANdle(self.constants["misc"]["CANdle"]["can_id"])

        # Import CANdle configuration
        CANdleConfig = CANdleConfiguration()
        CANdleConfig.stripType = LEDStripType.RGB
        CANdleConfig.brightnessScalar = self.constants["misc"]["CANdle"]["brightness"]

        # Write all settings
        logging.info(type(CANdleConfig))
        self.CANdle.configAllSettings(CANdleConfig)

        self.CANdle.setLEDs(255, 255, 255)

    def periodic(self):
        candleError = self.CANdle.getLastError()  # Gets the last error from the CANdle

        if candleError != ErrorCode.OK:
            logging.error(f"Candle raised an error, code {candleError}")
