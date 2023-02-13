import os
#import badger2040
import badger2040w as badger2040

setroom = input("Room Number? ")
with open("a_setroom_file.py", "w") as f:
    f.write("setroom = '" + setroom + "'")

settext = input("Employee Name? ")
with open("a_settext_file.py", "w") as f:
    f.write("settext = '" + settext + "'")

setcompany = input("Job Title? ")
with open("a_setcompany_file.py", "w") as f:
    f.write("setcompany = '" + setcompany + "'")

print ("Eingabe wurde gespeichert!")
