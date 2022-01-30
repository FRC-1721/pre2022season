import typing
import commands2
from subsystems.drivetrain import Drivetrain


class FlyByWire(commands2.CommandBase):
    def __init__(
        self,
        drive: Drivetrain,
        forward: typing.Callable[[], float],
        rotation: typing.Callable[[], float],
    ) -> None:
        super().__init__()

        self.drive = drive
        self.forward = forward
        self.rotation = rotation

        self.addRequirements([self.drive])

    def execute(self) -> None:
        self.drive.arcadeDrive(self.forward(), self.rotation())
