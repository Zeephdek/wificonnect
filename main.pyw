from winotify import Notification
import os
import re
import time


def winNotification(title='', msg=''):
    print(title)

    toast = Notification(app_id="WifiConn",
                     title=title,
                     msg=msg)

    toast.show()


def main():
    # loads SSID and password
    try:
        with open("network.txt") as f:
            text = f.read()
            ssid = re.search(r'(?<=ssid=).*', text).group()
            profile = re.search(r'(?<=profile=).*', text).group()

    except Exception as e:
        print(e)
        input("some issue with reading network.txt and grabbing the network ssid and profile")
        winNotification("Network.txt/ network config reading error.")
        return

    # check if already connected
    res = os.popen('netsh wlan show interfaces').read() # checks for connected interfaces
    # lazy
    if ": connected" in re.search(r'(?<=State).*', res).group():
        conn_state = True
        if ssid in re.search(r'(?<=SSID).*', res).group():
            winNotification(f"Already Connected to {ssid}.")
            return

    else:
        conn_state = False
    
    # check if Monke is available:
    res = os.popen('netsh wlan show networks').read()
    if ssid not in res: # lazy
        winNotification("Network Not Found.", 
            "This may be a Windows issue, try the Macro again.")
        return

    # and so it runs the connection attempts.
    os.system("netsh wlan disconnect")

    os.system(f"netsh wlan connect ssid={ssid} name={profile}")
    
    time.sleep(0.1) # Windows things; otherwise this doesn't show properly
    res = os.popen('netsh wlan show interfaces').read()
    if ": connected" in re.search(r'(?<=State).*', res).group():
        if ssid in re.search(r'(?<=SSID).*', res).group():
            winNotification(f"Connection to {ssid} Successful.")
            return
    
    winNotification("Connection Unsuccessful.")
    return


if __name__ == "__main__":
    main()


