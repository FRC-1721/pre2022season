import wpilib
import wpilib.drive
import rev

#id 1 = drive, id 2 = turn
class UnnamedToaster(wpilib.TimedRobot):
    def robotInit(self):

        
        self.drive = rev.CANSparkMax(1, rev.MotorType.kBrushless)
        self.turn = rev.CANSparkMax(2, rev.MotorType.kBrushless)

    
        

        self.joy = wpilib.Joystick(0)

    def teleopPeriodic(self):
        self.drive.set(self.joy.getRawAxis(1))
        self.turn.set(self.joy.getRawAxis(0))


if __name__ == "__main__":
    wpilib.run(UnnamedToaster)
    
