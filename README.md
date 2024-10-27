When using screen make sure you use the CTRL key not the CMD key :/

esptool.py --chip esp32 --port /dev/cu.usbserial-02528237 --baud 921600 write_flash -x 0x1000 ~/Downloads/UM_TINYPICO-20241025-v1.24.0.bin

esptool.py --chip esp32 --port /dev/cu.usbserial-02528237 erase_flash

screen -ls

screen -X -S 83405 quit

