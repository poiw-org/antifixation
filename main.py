from accelerometer import Accelerometer
from colorama import Fore
import socketio

accelerometers = [0,1,2,3,4,5,6]
workingAccelerometers = 0

print(Fore.YELLOW+"\n- Antifixation Node -\n")
for i in accelerometers:
    try:
        acceletometers[i] = Accelerometer(i+1,0,0)
        workingAccelerometers += 1
        print(Fore.GREEN+"[  OK  ] Accelerometer " + str(i+1) + " has been detected.")
    except:

        print(Fore.RED+ "[ FAIL ] Accelerometer " + str(i+1) + " is not responsive.")


if workingAccelerometers == 0:
    print(Fore.RED+"\nNo accelerometers where found, exiting.")
    exit(1)