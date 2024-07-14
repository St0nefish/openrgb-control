# Utilities for OpenRGB Control

## scripts
### openrgb-wake
script to place in `/usr/lib/systemd/system-sleep/` to set a profile on wake-from-sleep. 

edit this file prior to running `setup.sh` to change the config directory in which your profiles live (default is `/etc/openrgb`), and the profiles to set on sleep and wake. (defaulted to `sleep` and `default` respectively)

### setup.sh
script to copy `openrgb-sleep` to `/usr/lib/systemd/system-sleep/openrgb`

see [the Arch wiki](https://wiki.archlinux.org/title/Power_management#Using_a_script_and_an_udev_rule) for further details

