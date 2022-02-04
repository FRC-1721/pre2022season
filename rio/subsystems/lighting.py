# FRC 1721
# 2022

import logging

from ctre import ErrorCode
from ctre.led import CANdle, CANdleConfiguration, LEDStripType, SingleFadeAnimation

from commands2 import SubsystemBase

from wpilib import DriverStation

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
        self.CANdleConstants = self.constants["misc"]["CANdle"]

        # Configure CANdle module
        self.CANdle = CANdle(self.CANdleConstants["can_id"])

        # Import CANdle configuration
        CANdleConfig = CANdleConfiguration()
        CANdleConfig.stripType = LEDStripType.RGB  # TODO: Move this
        CANdleConfig.brightnessScalar = self.CANdleConstants["brightness"]

        # Write all settings
        self.CANdle.configAllSettings(CANdleConfig)

        # All LEDs off
        self.CANdle.setLEDs(0, 0, 0)

    def periodic(self):
        candleError = self.CANdle.getLastError()  # Gets the last error from the CANdle

        if candleError != ErrorCode.OK:
            logging.error(f"Candle raised an error, code {candleError}")

        # TODO: Change this
        match DriverStation.getAlliance():
            case DriverStation.Alliance.kRed:
                # Sets the LEDs to all red when the alliance is red.
                self.CANdle.setLEDs(255, 0, 0)
            case DriverStation.Alliance.kBlue:
                # Sets the LEDs to all blue when the alliance is blue.
                self.CANdle.setLEDs(0, 0, 255)
            case DriverStation.Alliance.kInvalid:
                # Sets the LEDs to a purple fade when the alliance is invalid/unknown.
                self.CANdle.animate(SingleFadeAnimation(r=255, g=0, b=255, speed=1))
