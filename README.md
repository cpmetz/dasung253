# Dasung 253 Python control

(c) 2022, Philip Metzler

The Dasung Paperlike 253 uses a different protocol than it's previous monitors to control settings, and most importantly, clearing the ghosting effects.

The Paperlike 253 control is done using a USB-to-serial converter (CH340) that seems to be attached to an internal USB hub. So for all this to work, you need to connect the monitor with the USB cable.

Make sure to install the driver for the CH340; I only tested under Windows so far, didn't check if Linux brings a device driver for it (but probably).

Based on using wireshark, it seems that the Dasung tool send ASCII strings to the USB-serial converter. I guess they have some fancy ASCII-to-I2C bridge (nigh) happening there...

This is all far from perfect (e.g. the wait periods before clearing ghosting to get rid of the info boxes).
