#!/usr/bin/python
import MFRC522
import signal
import ConfigParser
import os

# Read config file
Config = ConfigParser.ConfigParser()
Config.read("/home/pi/MFRC522-python/rfidconfig.txt")

# From https://wiki.python.org/moin/ConfigParserExamples
def ConfigSectionMap(section):
  dict1 = {}
  options = Config.options(section)
  for option in options:
        try:
                dict1[option] = Config.get(section, option)
                if dict1[option] == -1:
                        DebugPrint("skip: %s" % option)
        except:
                print("exception on %s!" % option)
                dict1[option] = None
  return dict1

continue_reading = True
MIFAREReader = MFRC522.MFRC522()

# Never stop reading
while continue_reading:
  (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
  if status == MIFAREReader.MI_OK:
    print "Card detected"
  (status,backData) = MIFAREReader.MFRC522_Anticoll()
  if status == MIFAREReader.MI_OK:
    strbackData = str(backData[0])+","+str(backData[1])+","+str(backData[2])+","+str(backData[3])+","+str(backData[4])

    print "Card read UID: " + strbackData

    # Do something (based on card and config file)
   # TagToMplayer(strbackData)
