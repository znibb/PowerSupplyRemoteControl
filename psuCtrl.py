import serial

serialPort = serial.Serial()
serialPort.port='/dev/ttyUSB0'
serialPort.baudrate=9600
serialPort.bytesize=8
serialPort.timeout=2
serialPort.stopbits=serial.STOPBITS_ONE

def getID():
    cmd = '*IDN?\\n'
    print(getCommand(cmd))

def getCurrent():
    cmd = "ISET1?\\n"
    print(getCommand(cmd))

def getVoltage():
    cmd = "VSET1?\\n"
    print(getCommand(cmd))

def setCurrent(current):
    cmd = "ISET1:" + "{:01.3f}".format(current) + "\\n"
    setCommand(cmd)

def setVoltage(voltage):
    cmd = "VSET1:" + "{:05.2f}".format(voltage) + "\\n"
    setCommand(cmd)

def getRealCurrent():
    cmd = "IOUT1?\\n"
    print(getCommand(cmd))

def getRealVoltage():
    cmd = "VOUT1?\\n"
    print(getCommand(cmd))

def getStatus():
    cmd = "STATUS?\\n"
    print(getCommand(cmd))

def outputControl(state):
    cmd = ""
    if state:
        cmd = "OUTPUT1\\n"
    else:
        cmd = "OUTPUT0\\n"
    setCommand(cmd)

def getCommand(command):
    serialPort.open()
    serialPort.write(command.encode())
    out = serialPort.readline()
    serialPort.close()
    return out[:-1].decode()

def setCommand(command):
    serialPort.open()
    serialPort.write(command.encode())
    serialPort.close()