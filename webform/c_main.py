#TechCree - ssk start mainscript with webserver and webform
import network
import socket
import time
from secret import ssid, password

import badger2040w
import badger2040w as badger2040
from badger2040w import WIDTH
#import led
from c_settext_file import settext

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

html = """<!DOCTYPE html>
<html>
    <head>
        <title>Raspberry Pi Pico W</title>
    </head>
    <body>
        <h1>Input the Text you like to display!</h1>
    </body>
    
    
    <div class="container my-3 rounded">
    <div class="container bg-light">
        <form method="POST">
                      
            <div class="mb-3">
                <label for="exampleInputsettext" class="form-label">Text</label>
                <input type="text" name="settext" class="form-control" id="settext"/>             
            </div>
            </br>
            <button type="submit" value="save">Submit</button>
        </form>
    </div>
</div>
</html>
"""

def save_text(text):
    with open("c_settext_file.py", "w") as f:
        f.write(text)

print('waiting for connection...')
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('.', end='')
    time.sleep(1)

print('')

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0])

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024).decode("utf-8")
        if request.startswith("POST"):
            cl.send("HTTP/1.1 200 OK\r\n\r\n")
            request_body = request.split("\r\n\r\n")[1]
            settext = request_body.split("=")[1]
            save_text("settext = '" + settext + "'")
            cl.send(html)
            
            ### print on Badger
            while True:
                #TEXT_SIZE
                LINE_HEIGHT = 20

                display = badger2040w.Badger2040W()
                #display.led(128)

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

                display.text(settext, 10, 70, WIDTH, TEXT_SIZE_B)

                display.update()
                
                f = open("c_main.py")
                exec(f.read())
                f.close()
                        
        else:
            cl.send("HTTP/1.1 200 OK\r\n\r\n")
            cl.send(html)
            cl.close()

    except OSError as e:
        cl.close()
        pass
