import pyusbio
usbio = pyusbio.USBIO()
if usbio.find_and_init():
  usbio.send2read([0x00, 0x11])
  #port0, port1 = usbio.send2read([0x00, 0x11])
  print("{0:x}, {1:x}".format(port0, port1))

