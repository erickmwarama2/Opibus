class DriverControl:
    def drive():
        pass

#In order to support the different driving modes e.g. ECO
# SPORT, OFF-ROAD etc, I would add classes that extend the 
# base DriverControl class each with implementations of the drive
# method that support the various driving modes

class EcoDrive(DriverControl):
    def __init__():
        #call the super class constructor
        super()
    
    def drive():
        #implement Eco driving mode
        pass 

class SportsDrive(DriverControl):
    def __init__():
        #call the super class constructor
        super()
    
    def drive():
        #implement the sports driving mode
        pass

class OffRoadDrive(DriverControl):
    def __init__():
        #call the super class constructor
        super()
    
    def drive():
        #implement off-road driving mode
        pass