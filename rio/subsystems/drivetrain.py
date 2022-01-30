# FRC 1721
# 2022

import logging

from wpimath import kinematics, geometry
from commands2 import SubsystemBase
from rev import CANSparkMax, CANSparkMaxLowLevel

from constants.constants import getHardwareConstants


class Drivetrain(SubsystemBase):
    """
    This class represents the whole drivetrain
    subsystem on the robot.
    """

    def __init__(self):
        super().__init__()

        # Get hardware constants
        self.constants = getHardwareConstants()

        # Create swerve drive modules
        # Fore starboard module
        self.fs_module = SwerveModule(self.constants["drivetrain"]["fs_module"])
        # Aft starboard module
        self.as_module = SwerveModule(self.constants["drivetrain"]["as_module"])
        # Fore port module
        self.fp_module = SwerveModule(self.constants["drivetrain"]["fp_module"])
        # Aft port module
        self.ap_module = SwerveModule(self.constants["drivetrain"]["ap_module"])

        # Create kinematics model
        # TODO: Flesh this out later...
        self.swerveKinematics = kinematics.SwerveDrive4Kinematics(
            self.fs_module.getTranslation(),
            self.as_module.getTranslation(),
            self.fp_module.getTranslation(),
            self.ap_module.getTranslation(),
        )

        # Swerve drive odometry (needs gyro.. at some point)
        # starting_pose = geometry.Pose2d(5.0, 13, geometry.Rotation2d())
        kinematics.SwerveDrive4Odometry(self.swerveKinematics, geometry.Rotation2d(0))

    def periodic(self):
        """
        Called periodically when possible,
        ie: when other commands are not running.
        Odom/constant updates go here
        """
        pass

    def arcadeDrive(self, fwd, rot):
        """
        Generates a chassis speeds using the joystick commands
        im not sure if this is the best way to do it, but
        it can always be replaced!
        """

        arcade_chassis_speeds = kinematics.ChassisSpeeds(fwd, 0, rot)
        _fs, _as, _fp, _ap = self.swerveKinematics.toSwerveModuleStates(
            arcade_chassis_speeds
        )

        self.fs_module.setModuleState(_fp)
        self.as_module.setModuleState(_as)
        self.fp_module.setModuleState(_fp)
        self.ap_module.setModuleState(_ap)


class SwerveModule:
    """
    Normally we inherit 'components'
    from vendors. Ex: CANSparkMax, Pneumatics,
    etc. But i think this may make it easier
    to organize.
    """

    def __init__(self, constants):
        # Setup one drive and one steer motor each.
        self.drive_motor = CANSparkMax(
            constants["drive_id"], CANSparkMaxLowLevel.MotorType.kBrushless
        )
        self.steer_motor = CANSparkMax(
            constants["steer_id"], CANSparkMaxLowLevel.MotorType.kBrushless
        )

        # TODO: This formatting needs to be cleaned, and ideally done in yaml
        self.module_pose = geometry.Translation2d(
            constants["pose_x"], constants["pose_y"]
        )

    def getTranslation(self):
        return self.module_pose

    def setModuleState(self, newState):
        """
        Important method that updates
        the "state" (steering and speed)
        of a module.
        """

        # TODO: Use optimization at some point.
        print(newState)
