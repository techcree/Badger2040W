# Badger2040W
Demo Code for the Pimoroni Badger2040 W

What is this repository about? It contains demo code for the Badger2040W, i.e. the wireless version based on a raspberry Pi Pico W. The code is essentially written in Python and works on the Badger2040W in the Micropython version.

As demo code, I covered some applications. These are doorsing and webform. What is each use case about?

***door sign
Use the Badger2040W (also works with the Bader2040 as a door sign for an office. You could also use the Badger as a table sign. You can use the script a_inputtext.py to enter the text via the terminal of e.g. Thonny IDE, which is then stored in the a_setcompany_file.py, a_setroom_file.py and a_settext_file.py is saved. The text is then also saved in these files so that it can later be read in as a usable variable. But you only need to start a_textonbadger.py, which will then start automatically uses the a_input.py script to capture new texts and then transfers them to the Bader to display them on the eInk display.You can also use the led.py if you want the Badger's LED to flash briefly during the process.

***webform
The real big advantage of the Badger2040W is its wireless functionality. For me, it wasn't just about just getting data from the web to display it, such as RRS feeds of weather or news. The PicoW also allows a small web server to run on the PicoW and this also allows us to call up a website at the IP address that the Badger2040W received after logging into the router in your WLAN. This is about sending a message to the Badger2040W. So we can open the website (IP of the Badgers2040W) and find a small web form there. There you can now enter a text and then confirm the entry with enter or send. Now this text is transferred to the badger and shown there in the eInk display!

special feature! I deliberately do not use the WIFI_CONFIG.py used in the pimoroni to record the WLAN access data. Instead I use the secret.py. The point is that it is possible to test the code first. If you don't want to use secret.py, you have to adapt this accordingly and instead of ssid and password, SSID and PSK appear as the corresponding variables for the WLAN access data.

