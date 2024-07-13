# Utilities for OpenRGB Control

## dependencies
* python3
* [openrgb-python](https://github.com/jath03/openrgb-python)

## scripts
### set-profile.py
basic python script to control profiles from the command line. 

takes one argument with the profile name, if not passed defaults to 'default'

### openrgb-wake
script to place in `/usr/lib/systemd/system-sleep/` to set a profile on wake-from-sleep. 

edit this to change the on-wake profile name or add support for setting profile pre-sleep

### setup.sh
script to copy `openrgb-sleep` to `/usr/lib/systemd/system-sleep/openrgb`

