
import robo
import time


FORWARD = robo.CODE_RSWalkForward
STOP = robo.CODE_RSStop
NO_OP = robo.CODE_RSNoOp

rs=robo.Robo(21)    #create Robo object for GPIO 21

#print("Forward...")
#rs.send_code(FORWARD)
#time.sleep(5.0)
#rs.send_code(NO_OP)
#time.sleep(2.0)
#print("Should be stopped")
#rs.send_code(STOP)
#print("Stopped")

#from bottom - goes a bit up
#print("right arm up")
#rs.send_code(robo.CODE_RSRightArmUp)
#time.sleep(5.0)
##half way up
#print("right arm up")
#rs.send_code(robo.CODE_RSRightArmUp)
#time.sleep(5.0)
##over shoulder
#print("right arm up")
#rs.send_code(robo.CODE_RSRightArmUp)
#time.sleep(5.0)
#
#print("right arm down")
#rs.send_code(robo.CODE_RSRightArmDown)
#time.sleep(5.0)
#print("right arm down")
#rs.send_code(robo.CODE_RSRightArmDown)
#time.sleep(5.0)
#print("right arm down")
#rs.send_code(robo.CODE_RSRightArmDown)
#time.sleep(5.0)
#
#print("right arm out")
#rs.send_code(robo.CODE_RSRightArmOut)
#time.sleep(5.0)
#print("right arm out")
#rs.send_code(robo.CODE_RSRightArmOut)
#time.sleep(5.0)
#print("right arm out")
#rs.send_code(robo.CODE_RSRightArmOut)
#time.sleep(5.0)
#
#print("right arm in")
#rs.send_code(robo.CODE_RSRightArmIn)
#time.sleep(5.0)
#print("right arm in")
#rs.send_code(robo.CODE_RSRightArmIn)
#time.sleep(5.0)
#print("right arm in"):q

#rs.send_code(robo.CODE_RSRightArmIn)
#time.sleep(5.0)

rs.send_code(robo.CODE_RSRightArmOut)
time.sleep(5.0)

rs.send_code(robo.CODE_RSRightArmOut)
time.sleep(5.0)

rs.send_code(robo.CODE_RSRightArmIn)
time.sleep(5.0)

rs.send_code(robo.CODE_RSRightArmIn)
time.sleep(5.0)


rs.clean_up()
