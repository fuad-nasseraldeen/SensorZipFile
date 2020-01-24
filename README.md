# SensorZipFile
it's an python code 
read the sensors from the archive zip file and do some equation and write it in new file 

Class & Home Exercise part A :
Given an archive file named sensors_data.zip containing sensors real data.
The data contains digital readouts of the following sensors:
1- Temperature sensor :
data size 2 bytes  byte0 - holding the int part of the temperature
byte1 – holding the fractional part of the temperature in [1/100 units]
data analog range -10 to +40 degrees C
data digital range 0 to (2**16)-1 (0x0 to 0xFFFF)
A.1 – write a code translating temperature digital value to temperature analog value
( a digital value of 0 should be translated into -10.0 deg C
, a digital value of 32767 (0x7FFF) should be translated into +15.0 degrees C
, a digital value of 65535 (0xFFFF) should be translated into +40.0 degrees C)
2- Pressure sensor :
data size 3 bytes  byte0 to byte1 - holding the int part of the pressure
byte3 – holding the fractional part of the pressure in [1/100 units]
data analog range 0 to 9000 pressure units
data digital range 0 to (2**24)-1 (0x0 to 0xFFFFFF)
A.2 – write a code translating pressure digital value to pressure analog value
( a digital value of 0 should be translated into 0 pressure units
, a digital value of (0x7FFFFF) should be translated into 4500.0 pressure units
, a digital value of (0xFFFFFF) should be translated into 9000.0 pressure units)

Class & Home Exercise part A (Cont.):
The data contains digital readouts of the following sensors (Cont.):
3- Humidity sensor :
data size 1 bytes  byte0 - holding the Humidity % int
data analog range 0 to 100 %
data digital range 0 to (2**8)-1 (0x0 to 0xFF)
A.3 – Write a code translating humidity digital value to humidity analog value
( a digital value of 0 should be translated into 0 % humidity
, a digital value of 127 (0x7F) should be translated into 50 % humidity
, a digital value of 255 (0xFF) should be translated into 100 % humidity)
4- Gas sensors [CO2 & PPG] :
data size 4 bytes  2 LSB bytes - holding the 1E-6 of CO2 Gas particles measurement
2 MSB bytes - holding the 1E-6 of PPG Gas particles measurement
data analog range 0 to 10000 pressure units for each type of gas reading
data digital range 0 to (2**16)-1 (0x0 to 0xFFFF)
A.4 – Write a code separating the digital value into 2 digital values (one for each type of type of
Gas). The code shall translate digital value to Gas particles analog value for both sensors
( a digital value of 0 should be translated into 0 Gas particles
, a digital value of (0x7FFF) should be translated into 5000 Gas particles
, a digital value of (0xFFFF) should be translated into 10000.0 Gas particles)
5- Battery sensor :
data size 1 byte  byte0 - holding the digital reading of the battery
data analog range 3300 to 4200 mv
data digital range 0 to (2**8)-1 (0x0 to 0xFF)
A.5 – write a code translating battery digital value to battery analog value
( a digital value of 0 should be translated into 3300 mv
, a digital value of 127 (0x7F) should be translated into 3750 mv
, a digital value of 255 (0xFF) should be translated into 4200 mv)



Class & Home Exercise part B :
B.1 – Add to your program code to open the zip archive and get the list of the archive file names.
B.2 – Iterate over the archive file list and read each file`s lines. What is the line type ? Can you read the line
data as a usable python type ? If Not , can you convert the line into a usable python type ? What type
did you get?
B.3 – Read the converted line and convert each value to analog value using the code you wrote in part A
add the CO2 value & PPG values (gas readout is no longer relevant !)
B.4 – Create a list to hold each line reading results: you can do it in a separate list for each measurement
(list for each measurement 1D) or combined list holding all results (analog values) (list of lists2D)
Values in this list shall be analog values !


Class & Home Exercise part C :
C.1 :
C.1.1 -Add to your program open a file ‘output.csv’. Open the file for writing.
C.1.2 - Iterate over the results lists created in section B.4 and create a line holding the results with
commas
separated between the values.
C.1.3 – Write all the lines to the csv file and then close it
C.2 – Open the CSV file and save it in XLSX format. Open the excel file and manually create graph out of the
data of each line.
