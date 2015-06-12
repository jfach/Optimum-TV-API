# Optimum-TV-API

This is a python wrapper for the (first!) unofficial Optimum App API documented by your truly.

To get everything up and running, you first need to get your hands on a Device ID.
# Device ID
A Device ID is a UUID4 format identifier that is generated when a machine uses the Optimum App for the first time. Unfortunately I have not yet been able to successfully reverse engineer the generation proccess, although locating your Device ID is a fairly trivial matter. 

# Obtaining a Device ID
1. Open the Optimum App, and sign in.
2. Select the SETTINGS tab on the top of the screen.
3. Select the FAQ tab located on the right side of the screen.
4. On the bottom of the screen, you should see your Device ID next to the words "For System Use Only:"

# Authentication
```python
import optimum
tv = optimum.API(optimum_ID, password, device_ID)
```
# Cable Boxes
```python
# see your cable boxes
for box in tv.boxes:
   print box.name
   print box.serial
   print box.type
   print box.resolution
   if box.recordable:
      print box.space
# turn boxes on/off
result = tv.do_keypress(tv.boxes["Kitchen"], ["KEY_POWER"])
if not result:
   print "Keypress Failed!"
# change the channel
# note that you can chain keys, so for channel 32 you would do:
result = tv.do_keypress(tv.boxes["Living Room"], ["KEY_3","KEY_2"])
```
