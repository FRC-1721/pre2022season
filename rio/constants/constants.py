# Tidal Force Robotics
# 2022

import yaml
import logging


# A simple series of defs, each used to load
# and prepare a set of yaml constants for use
# elsewhere. Do NOT use this file for anything else!


def getHardwareConstants():
    hardware = {}

    try:
        # Try opening robot_hardware.yaml
        with open("constants/robot_hardware.yaml", "r") as hardware_yaml:
            # Use yaml.safe_load to load the yaml into a dict
            hardware = yaml.safe_load(hardware_yaml)
    except FileNotFoundError as e:
        # If the file is not found, report it!
        logging.error("Hardware config yaml not found!")
        raise e

    # When all is done, return the important bits!
    return hardware


def getControllerConstants():
    controls = {}

    try:
        # Try opening robot_controls.yaml
        with open("constants/robot_controls.yaml", "r") as controls_yaml:
            # Use yaml.safe_load to load the yaml into a dict
            controls = yaml.safe_load(controls_yaml)
    except FileNotFoundError as e:
        # If the file is not found, report it!
        logging.error("Controls config yaml not found!")
        raise e

    # When all is done, return the important bits!
    return controls
