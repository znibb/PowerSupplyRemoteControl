import serial

class LABPS3005DN:
    ## Constructor
    def __init__(self, serialPort):
        self.ser = serial.Serial(port=serialPort,
                                baudrate=9600,
                                bytesize=8,
                                timeout=2,
                                stopbits=serial.STOPBITS_ONE)

    ## Destructor
    def __del__(self):
        try:
            self.ser.close()
        except AttributeError:
            pass

    ## Private methods
    # Write instruction to the PSU
    def __setCommand(self, command):
        self.ser.write(command.encode())

    # Write instruction to the PSU and read reply
    def __getCommand(self, command):
        self.__setCommand(command)
        return self.ser.readline()[:-1].decode()
        
    ## Public methods
    # Get PSU ID
    def getID(self):
        cmd = '*IDN?\\n'
        return self.__getCommand(cmd)

    # Get current limit
    def getCurrent(self):
        cmd = "ISET1?\\n"
        return self.__getCommand(cmd)

    # Get voltage setpoint
    def getVoltage(self):
        cmd = "VSET1?\\n"
        return self.__getCommand(cmd)

    # Get actual current output
    def getRealCurrent(self):
        cmd = "IOUT1?\\n"
        return self.__getCommand(cmd)

    # Get actual voltage output
    def getRealVoltage(self):
        cmd = "VOUT1?\\n"
        return self.__getCommand(cmd)

    # Get status flags
    def getStatus(self):
        cmd = "STATUS?\\n"
        return self.__getCommand(cmd)

    # Check Constant Voltage flag
    def getFlagCV(self):
        if (self.getStatus()[0] == "1"):
            return True
        else:
            return False

    # Check output active flag
    def getFlagOutput(self):
        if (self.getStatus()[1] == "1"):
            return True
        else:
            return False

    # Check Over Current Protection flag
    def getFlagOCP(self):
        if (self.getStatus()[2] == "1"):
            return True
        else:
            return False

    # Set new current limit
    def setCurrent(self, current):
        cmd = "ISET1:" + "{:01.3f}".format(current) + "\\n"
        self.__setCommand(cmd)

    # Set new voltage setpoint
    def setVoltage(self, voltage):
        cmd = "VSET1:" + "{:05.2f}".format(voltage) + "\\n"
        self.__setCommand(cmd)

    # Set output state
    def setOutput(self, state):
        cmd = ""
        if state:
            cmd = "OUTPUT1\\n"
        else:
            cmd = "OUTPUT0\\n"
        self.__setCommand(cmd)