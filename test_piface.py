import pifacedigitalio
import datetime
pifacedigital = pifacedigitalio.PiFaceDigital()


def switch_pressed(event):
    print "[{}] Switch {} pressed".format(datetime.datetime.now(), event.pin_num)


def switch_unpressed(event):
    print "[{}] Switch {} released".format(datetime.datetime.now(), event.pin_num)


listener = pifacedigitalio.InputEventListener(chip=pifacedigital)
for i in range(4):
    listener.register(i, pifacedigitalio.IODIR_ON, switch_pressed)
    listener.register(i, pifacedigitalio.IODIR_OFF, switch_unpressed)

listener.activate()
