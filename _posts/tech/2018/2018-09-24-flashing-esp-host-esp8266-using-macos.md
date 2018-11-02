---
layout: post
title: 'Flashing esp-host onto an ESP8266 WiFI Board using macOS'
date: 2018-09-24 18:00:00 +0200
category: tech
tags:
- PS4Homebrew
---

Here is a quick tutorial on how to flash esp-host onto an ESP8266 WiFI board using macOS. I used the [NodeMCU V2](https://www.amazon.de/AZDelivery-NodeMCU-ESP8266-ESP-12E-Development/dp/B06Y1LZLLY/) board, however any ESP8266 board with 4M flash or larger should work.

1. Install SiLabs serial drivers ([direct link](https://www.silabs.com/documents/public/software/Mac_OSX_VCP_Driver.zip))
2. Install esptool
3. Download the desired esp-host
4. Flash the esp-host to the ESP8266

```
esptool.py --port=/dev/cu.SLAB_USBtoUART  write_flash  -fm=dio -fs=32m 0x00000 ./PATH_TO_BIN
```

It should take about a minute to flash the bin. Once successfully completed, you can quickly verify that everything is okay by connecting a device to PS4-WIFI and going to 10.10.10.1. You should see the following screen:

![]({{site.baseurl}}/assets/images/posts/2018/18-09-24/01.jpg)

At this point you can plug the ESP8266 into the PS4, switch on the console and connect to the PS4-WIFI network (easy settings), before going to Settings -> User Guide and running the exploit.

### Remarks

1. Apparently the build quality of ESP8266 boards can vary. Before starting the flashing process on a new board, ensure that the board is actually functioning. Simply connected the board to a power source (i.e. USB port on the computer) and then check that there is some new unsecured WiFi network available (i.e. one that doesn't require a password).
2. Codworth's instructions leave out the commands ```-fm=dio -fs=32m```. The standard command ```sudo esptool.py --port PATH_TO_DEVICE write_flash 0x00000 PATH_TO_BIN``` always failed with the error ```A fatal error occurred: Timed out waiting for packet header```. By added the aforementioned commands as noted in the *Getting Started on OSX* guide by NodeMCU, the flashing worked perfectly first time.
3. If you prefer using a GUI, check out [NodeMCU-PyFlasher](https://github.com/marcelstoer/nodemcu-pyflasher/releases) or [esptool-gui](https://github.com/Rodmg/esptool-gui/releases).

### Resources

[Codworth: esp-host](https://github.com/Codworth/esp-host)

[esptool.py](https://github.com/espressif/esptool)

[NodeMCU: Getting Started on OSX](Getting Started on OSX)

[Silicon Labs: CP210x USB to UART Bridge VCP Drivers](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers)
