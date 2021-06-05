
import robo
import time


FORWARD = robo.CODE_RSWalkForward
STOP = robo.CODE_RSStop
NO_OP = robo.CODE_RSNoOp

rs=robo.Robo(21)    #create Robo object for GPIO 21

print("Forward...")
rs.send_code(FORWARD)
time.sleep(5.0)
rs.send_code(NO_OP)
time.sleep(2.0)
print("Should be stopped")
rs.send_code(STOP)
print("Stopped")
