import commands2


class ReZero(commands2.CommandBase):
    def __init__(self) -> None:
        super().__init__()

    def initialize(self) -> None:
        print("Zeroed")

    def isFinished(self) -> bool:
        return True
