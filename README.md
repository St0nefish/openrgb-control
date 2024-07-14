# Utilities for OpenRGB Control

## scripts
### openrgb-wake
script to place in `/usr/lib/systemd/system-sleep/` to set a profile on wake-from-sleep. 

edit this to change the config directory in which your profiles live (default is `/etc/openrgb`), and the profiles to set on sleep and wake. 

### setup.sh
script to copy `openrgb-sleep` to `/usr/lib/systemd/system-sleep/openrgb`

