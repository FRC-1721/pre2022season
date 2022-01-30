# Tidal Force Robotics
# 2022
# MIT License

import yaml


class RobotConfiguration:
    def __init__(self):
        """
        Constructs a RobotConfiguration
        we can use to query for yaml database values.
        """

        # Setup dictionaries
        self.dimms = {}
        self.network = {}

        with open("config/robot_diensions.yaml", "r") as robot_dimms:
            self.dimms = yaml.safe_load(robot_dimms)
