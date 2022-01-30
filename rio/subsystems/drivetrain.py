# FRC 1721
# 2022

from commands2 import SubsystemBase

from rev import CANSparkMax, CANSparkMaxLowLevel
import wpimath


class Drivetrain(SubsystemBase):
    """
    This class represents the whole drivetrain
    subsystem on the robot.
    """

    def __init__(self):
        super().__init__()

        # Create swerve drive modules
        # TODO: pass neatly formatted dict defs for each module
        self.fs_module = SwerveModule(1, 2, 0.5, -0.5)  # Fore starboard module
        self.as_module = SwerveModule(3, 4, -0.5, -0.5)  # Aft starboard module
        self.fp_module = SwerveModule(5, 6, 0.5, 0.5)  # Fore port module
        self.ap_module = SwerveModule(7, 8, -0.5, 0.5)  # Aft port module

        # Create kinematics model
        # TODO: Flesh this out later...
        self.swerveKinematics = wpimath.kinematics.SwerveDrive4Kinematics(
            self.fs_module.getPose(),
            self.as_module.getPose(),
            self.fp_module.getPose(),
            self.ap_module.getPose(),
        )

    def periodic(self):
        """
        Called periodically when possible,
        ie: when other commands are not running.
        Odom/constant updates go here
        """
        pass

    def arcadeDrive(self, fwd, rot):
        """
        Fill this out later...
        """
        pass


class SwerveModule:
    """
    Normally we inherit 'components'
    from vendors. Ex: CANSparkMax, Pneumatics,
    etc. But i think this may make it easier
    to organize.
    """

    def __init__(self, drive_id, steer_id, x_pose, y_pose):
        # Setup one drive and one steer motor each.
        self.drive_motor = CANSparkMax(
            drive_id, CANSparkMaxLowLevel.MotorType.kBrushless
        )
        self.steer_motor = CANSparkMax(
            steer_id, CANSparkMaxLowLevel.MotorType.kBrushless
        )

        # TODO: This formatting needs to be cleaned, and ideally done in yaml
        self.module_pose = wpimath.geometry.Translation2d(x_pose, y_pose)

    def getPose(self):
        return self.module_pose
