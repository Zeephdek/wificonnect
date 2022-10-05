This is a simple script to automatically connect to a specified wifi network, activated using a macro.

The macro uses Autohotkey, with the actual connection script run in Python.

https://www.hanselman.com/blog/how-to-connect-to-a-wireless-wifi-network-from-the-command-line-in-windows-7

# How To Use
Setup.py is set up to modify the "Currently Running.ahk" default startup ahk script that I use, with the location changeable only in code. (The one that is currently modified is `C:\Code\Startup`)
The edited code is between `;wificonn_start` and `;wificonn_end`

The default key combination is `Win+Shift+F3`

# Requirements
[winotify](https://pypi.org/project/winotify/)

    pip install winotify
