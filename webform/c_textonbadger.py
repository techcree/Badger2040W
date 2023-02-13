import badger2040w
import badger2040w as badger2040
from badger2040w import WIDTH
#import c_webserver
#import led
#import a_inputtext
#from a_setroom_file import setroom
#from a_settext_file import settext
#from a_setcompany_file import setcompany
from c_settext_file import settext

#TEXT_SIZE = 2.00
LINE_HEIGHT = 20

display = badger2040w.Badger2040W()
display.led(128)

# Clear to white
display.set_pen(15)
display.clear()

#next
display.set_pen(0)

TEXT_SIZE_A = 1.50
TEXT_SIZE_B = 1.00
TEXT_SIZE = 0.96
y = 25 + int(LINE_HEIGHT / 3)

display.set_font("serif")

#display.text(setroom, 10, 20, WIDTH, TEXT_SIZE_A)
display.text(settext, 10, 70, WIDTH, TEXT_SIZE_B)
#display.text(setcompany, 10, 100, WIDTH, TEXT_SIZE)

display.update()

f = open("c_webserver.py")
exec(f.read())
f.close()

def stop_script():
    sys.exit()

# Call halt in a loop, on battery this switches off power.
# On USB, the app will exit when A+C is pressed because the launcher picks that up.
while True:
    display.halt()
