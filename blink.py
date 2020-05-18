import socket
import time
from blinkstick import blinkstick

"""
This functions checks connection to Google DNS server
If DNS server is reachable on port 53, then it means that
the internet is up and running
"""
myHost = "1.1.1.1"
myPort = 53


def internet_connected(host=myHost, port=myPort):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """

    try:
        socket.setdefaulttimeout(1)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as ex:
        pass
    return False


def main():
    led = blinkstick.find_first()
    connected = False
    if internet_connected() == True:
        print("Internet Up")
        connected = True
        led.set_color(name="green")
    else:
        print("Internet Down")
        led.pulse(name="red", repeats=25, duration=100)
        led.set_color(name="red")
# Can't do anything if BlinkStick is not connected
    if led is None:
        print("BlinkStick Not Available\n")
    else:
        print("Found BlinkStick..")
    print("Exiting...Bye!")


if __name__ == "__main__":
    main()
