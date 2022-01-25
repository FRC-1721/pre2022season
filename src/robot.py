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

    #change square axis given by joystick into a circular input
    vector1Circle = vector1 * math.sqrt(1 - 0.5*vector2**2)
    vector2Circle = vector2 * math.sqrt(1 - 0.5*vector1**2)

    #calculate the angel of the joystick from the axes <- thats the plural of axis apparently 
    #I take the angle in degrees rather than radiens because this is just a 
    #prototype and I dont want to deal with radians 
    vector3 = math.sqrt(vector1Circle**2 + vector2Circle**2)
    angleS = math.degrees(math.acos(vector1Circle/vector3))
    angleL = 180 - angleS #redundant at the moment

    #print(angleS, " S ", angleL, " L ", vector1, " Vector1 ", vector2, " Vector2 ", vector3, " Vector3 ", vector1Circle, " V1C ", vector2Circle, " V2C ")

    return angleS


class UnnamedToaster(wpilib.TimedRobot):
    def robotInit(self):
        #Initializing motors, encoders, joysticks, and the PID 
        #(at the moment only the spin motor is enabled)

        #self.driveMotor = rev.CANSparkMax(1, rev.MotorType.kBrushless)
        self.spinMotor = rev.CANSparkMax(1, rev.MotorType.kBrushless)

        #self.driveEncoder = self.driveMotor.getEncoder()
        self.spinEncoder = self.spinMotor.getEncoder()

        self.spinPID = self.spinMotor.getPIDController()
       # self.drivePID = self.driveMotor.getPIDController()

        self.joy = wpilib.Joystick(0)

    def teleopInit(self):
        #Set the current position of the wheel as 0 on 
        #the encoders when the robot is enabled
        self.spinEncoder.setPosition(0)
        #self.driveEncoder.setPosition(0)

        #PID values (Needs heavy tuning)
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
        #METHODS OF SPINNING

        #Spin when joystick is turned
        #self.spinMotor.set(self.joy.getRawAxis(2)/20)

        #Set position to joystick turn value
        #self.spinPID.setReference(self.joy.getRawAxis(2)*5, rev.ControlType.kPosition, 0)   

        #Turn via buttons (Fast and slower speeds) and stop on trigger press
        #Used for debugging when moving the stick does something other than turn the 
        #wheel vie the other two above methods. Trigger stop is especially useful when
        #the motor goes out of control for some reason (saves a lot of robot restarts via e-stop)
        if (self.joy.getRawButton(5) == True):
            self.spinMotor.set(0.001)
        if (self.joy.getRawButton(6) == True):
            self.spinMotor.set(-0.2)

        if (self.joy.getRawButton(3) == True):
            self.spinMotor.set(0.1)
        if (self.joy.getRawButton(4) == True):
            self.spinMotor.set(-0.1)
        
        if (self.joy.getRawButton(1) == True):
            self.spinMotor.set(0)

        #Definitions for the current angle of the joystick. Due to how the joystick values
        #translate into angels, I need to take this slightly differently depending on 
        #whether the joystick is currently on the left or right side. The value returned is
        #in degrees, with straight up as 0 and increasing clockwise to 360. (so straight right
        #is 90, down is 180, left is 270, and technicly up is also 360 although the code
        #deafults to 0)
        if (self.joy.getRawAxis(1) < 0):
            joyVectorAngle = vectorMath(-self.joy.getRawAxis(1),
                                        self.joy.getRawAxis(0), 0)
        elif (self.joy.getRawAxis(1) > 0):
            joyVectorAngle = vectorMath(-self.joy.getRawAxis(1),
                                        self.joy.getRawAxis(0), 1)
        else:
            self.joyVectorAngle = 0

        if (self.joy.getRawAxis(0) < 0):
            self.joyVectorAngle = 360-self.joyVectorAngle
        
        self.neoTurnRatio = 36.5 # Neo spins to wheel spins ratio: ~36.5:1
        self.joyPercent = self.joyVectorAngle / 360 #Converts degrees to a percentage of turning, with 0 being up, 25 is right, 50 is down, 75 is left, etc.
        self.currentPosition = (self.spinEncoder.getPosition() % 11) / 11 #Get the current position of the wheel as a percent, witht the same methodology as above
        self.movePercent = self.joyPercent - self.currentPosition #Difference between the current position and the joysticks position
        self.neoTurns = self.movePercent * self.neoTurnRatio #how many times the neo has to turn to reach the joystick position

        #Set the position of the wheel via PID
        #takes the current position of the wheel and adds the ammount that needs to be turned to get the desired position
        #self.spinPID.setReference(self.spinEncoder.getPosition()+self.neoTurns, rev.ControlType.kPosition, 0)

        print(self.spinEncoder.getPosition())


if __name__ == "__main__":
    wpilib.run(UnnamedToaster)
