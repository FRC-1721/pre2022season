import wpilib
import wpilib.drive
import rev
import math

# TEMP FUNCTION MOVE TO ANOTHER FILE
# this function takes in the verticle and horizontal vectors of the joystick
# and creates angleS and angleL. AngleS is the vector of the joystick when the
# verticle vector is greater than 0, and AngleL is the vector of the joystick when
# the verticle vector is less than 0.


def vectorMath(vector1, vector2, SorL):
    vector1Circle = vector1 * math.sqrt(1 - 0.5*vector2**2)
    vector2Circle = vector2 * math.sqrt(1 - 0.5*vector1**2)
    vector3 = math.sqrt(vector1Circle**2 + vector2Circle**2)
    angleS = math.degrees(math.acos(vector1Circle/vector3))
    angleL = 180 - angleS
    #print(angleS, " S ", angleL, " L ", vector1, " Vector1 ", vector2, " Vector2 ", vector3, " Vector3 ", vector1Circle, " V1C ", vector2Circle, " V2C ")
    #if (SorL == 0):
    #    return angleS
    #elif (SorL == 1):
    #    return angleL
    return angleS


class UnnamedToaster(wpilib.TimedRobot):
    def robotInit(self):

        #self.driveMotor = rev.CANSparkMax(1, rev.MotorType.kBrushless)
        self.spinMotor = rev.CANSparkMax(1, rev.MotorType.kBrushless)

        #self.driveEncoder = self.driveMotor.getEncoder()
        self.spinEncoder = self.spinMotor.getEncoder()

        self.spinPID = self.spinMotor.getPIDController()
       # self.drivePID = self.driveMotor.getPIDController()

        self.joy = wpilib.Joystick(0)

    def teleopInit(self):
        self.spinEncoder.setPosition(0)
        #self.driveEncoder.setPosition(0)

        self.spinPID.setP(0.02)
        self.spinPID.setD(0.5)
        self.spinPID.setFF(0)
        self.spinPID.setI(1e-4)
        self.spinPID.setSmartMotionMaxVelocity(0.3)

        #self.drivePID.setP(0.2)
        #self.drivePID.setD(0.3)
        #self.drivePID.setFF(0)
        #self.drivePID.setI(1e-4)
        #self.drivePID.setSmartMotionMaxVelocity(0.3)

    def teleopPeriodic(self):
<<<<<<< HEAD
        #methods of spinning
        #self.spinMotor.set(self.joy.getRawAxis(2)/20)
        #self.spinPID.setReference(self.joy.getRawAxis(2)*5, rev.ControlType.kPosition, 0)   
        if (self.joy.getRawButton(5) == True):
            self.spinMotor.set(0.001)
        if (self.joy.getRawButton(6) == True):
            self.spinMotor.set(-0.2)
=======
        # methods of spinning
        self.spinMotor.set(self.joy.getRawAxis(2)/10)
        #self.spinPID.setReference(self.joy.getRawAxis(2)*5, rev.ControlType.kPosition, 0)
>>>>>>> d8e3774d899d3be1b5b25d22b2843305542d705b

        if (self.joy.getRawButton(3) == True):
            self.spinMotor.set(0.1)
        if (self.joy.getRawButton(4) == True):
            self.spinMotor.set(-0.1)
        
        if (self.joy.getRawButton(1) == True):
            self.spinMotor.set(0)

<<<<<<< HEAD
        #self.driveMotor.set(self.joy.getRawAxis(1)/4)

        #Neo spins to wheel spins ratio: ~36.5:1
        if (self.joy.getRawAxis(1) < 0):
            self.joyVectorAngle = vectorMath(-self.joy.getRawAxis(1),self.joy.getRawAxis(0),0)
        elif (self.joy.getRawAxis(1) > 0):
            self.joyVectorAngle = vectorMath(-self.joy.getRawAxis(1),self.joy.getRawAxis(0),1)
=======
        # Neo spins to wheel spins ratio: ~11:1
        if (self.joy.getRawAxis(1) < 0):
            joyVectorAngle = vectorMath(-self.joy.getRawAxis(1),
                                        self.joy.getRawAxis(0), 0)
        elif (self.joy.getRawAxis(1) > 0):
            joyVectorAngle = vectorMath(-self.joy.getRawAxis(1),
                                        self.joy.getRawAxis(0), 1)
>>>>>>> d8e3774d899d3be1b5b25d22b2843305542d705b
        else:
            self.joyVectorAngle = 0

<<<<<<< HEAD
        if (self.joy.getRawAxis(0) < 0):
            self.joyVectorAngle = 360-self.joyVectorAngle
        
        self.neoTurnRatio = 36.5
        self.joyPercent = self.joyVectorAngle / 360
        self.currentPosition = (self.spinEncoder.getPosition() % 11) / 11
        self.movePercent = self.joyPercent - self.currentPosition
        self.neoTurns = self.movePercent * self.neoTurnRatio
=======
        self.neoTurnPercent = 1/11
        self.turnPercent = joyVectorAngle / 360
        self.neoTurns = joyVectorAngle / self.neoTurnPercent
        print(self.neoTurnPercent, " - neoTurn", self.turnPercent,
              " - turnPercent", self.neoTurns, " - neoTurns")
        #self.spinPID.setReference(self.neoTurns, rev.ControlType.kPosition, 0)
>>>>>>> d8e3774d899d3be1b5b25d22b2843305542d705b

        #self.spinPID.setReference(self.spinEncoder.getPosition()+self.neoTurns, rev.ControlType.kPosition, 0)

        print(self.spinEncoder.getPosition())


if __name__ == "__main__":
    wpilib.run(UnnamedToaster)
