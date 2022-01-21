import wpilib
import wpilib.drive
import rev
import math

#TEMP FUNCTION MOVE TO ANOTHER FILE
#this function takes in the verticle and horizontal vectors of the joystick 
#and creates angleS and angleL. AngleS is the vector of the joystick when the
#verticle vector is greater than 0, and AngleL is the vector of the joystick when
#the verticle vector is less than 0. 
def vectorMath(vector1, vector2, SorL):
    vector3 = math.sqrt(vector1**2 + vector2**2)
    angleS = math.degrees(math.cos(vector1/vector3))
    angleL = 108 - angleS
    if (SorL == 0):
        return angleS
    elif (SorL == 1):
        return angleL

class UnnamedToaster(wpilib.TimedRobot):
    def robotInit(self):

        self.driveMotor = rev.CANSparkMax(1, rev.MotorType.kBrushless)
        self.spinMotor = rev.CANSparkMax(2, rev.MotorType.kBrushless)

        self.driveEncoder = self.driveMotor.getEncoder()
        self.spinEncoder = self.spinMotor.getEncoder()

        self.spinPID = self.spinMotor.getPIDController()
        self.drivePID = self.driveMotor.getPIDController()

        self.joy = wpilib.Joystick(0)

    def teleopInit(self):
        self.spinEncoder.setPosition(1)
        self.driveEncoder.setPosition(0)

        self.spinPID.setP(0.1)
        self.spinPID.setD(0.5)
        self.spinPID.setFF(0)
        self.spinPID.setI(1e-4)
        self.spinPID.setSmartMotionMaxVelocity(0.3)

        self.drivePID.setP(0.2)
        self.drivePID.setD(0.3)
        self.drivePID.setFF(0)
        self.drivePID.setI(1e-4)
        self.drivePID.setSmartMotionMaxVelocity(0.3)

    def teleopPeriodic(self):
        #methods of spinning
        self.spinMotor.set(self.joy.getRawAxis(2)/10)
        #self.spinPID.setReference(self.joy.getRawAxis(2)*5, rev.ControlType.kPosition, 0)   

        self.driveMotor.set(self.joy.getRawAxis(1)/4)

        #Neo spins to wheel spins ratio: ~11:1
        if (self.joy.getRawAxis(1) < 0):
            joyVectorAngle = vectorMath(-self.joy.getRawAxis(1),self.joy.getRawAxis(0),0)
        elif (self.joy.getRawAxis(1) > 0):
            joyVectorAngle = vectorMath(-self.joy.getRawAxis(1),self.joy.getRawAxis(0),1)
        else:
            joyVectorAngle = 0

        self.neoTurnPercent = 1/11
        self.turnPercent = joyVectorAngle / 360
        self.neoTurns = joyVectorAngle / self.neoTurnPercent
        print(self.neoTurnPercent, " - neoTurn", self.turnPercent, " - turnPercent", self.neoTurns, " - neoTurns")
        #self.spinPID.setReference(self.neoTurns, rev.ControlType.kPosition, 0)

        #print(f"Encoder Drive: {self.driveEncoder.getPosition()}, Encoder Spin: {self.spinEncoder.getPosition()}")

if __name__ == "__main__":
    wpilib.run(UnnamedToaster)
