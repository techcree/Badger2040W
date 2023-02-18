In principle it is possible with this script to start the code that provides the web server and thus also the web form. It can then be reached under the IP address assigned to the Badger2040W by the router in your WLAN. A short web form will be made available to you on the website. An input field in which you can enter any text that is then displayed directly on the Bagder2040W display after the transfer (Enter/Send).

Start the process from the c_webserver.py file! You must first enter your WLAN access data, such as the WLAN SSID and the WLAN password, in the secret.py file! Alternatively, you can of course also adapt the script so that you can use WIFI_CONFIG.py, which may already be available to you as demo code from pimoroni.

Bugfixes ongoing...
The following error messages have become known in this Version:

s.bind(addr)
After starting the web server, the web server may not start correctly right away. Then you will get an error message whose line of code contains the entry s.bind(addr). You just have to run the script again and it will work. if necessary, briefly disconnect the Badger2040W from the power supply.

little waiting time
if you have made an entry, wait until the browser window is displayed as loaded on the website. as long as it is still loading it will not be possible to make another entry. the script is then interrupted. So pay attention to the update symbol (circle with arrow symbol, next to arrow back and arrow forward symbol)!

Error displaying the space
If you enter text that consists of several words, e.g. For example, "Hello World", the text may appear as "Hello+World" on the Badgers2040w display.

To fix the error, copy the my_utils.py and expand the entry from my_utils import decode_url in c_webserver.py (see update c_webserver.py 02/18/2023)
