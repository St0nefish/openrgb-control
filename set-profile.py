import sys
from openrgb import OpenRGBClient

# get profile from commmand line or default 
profile = "default"
if (len(sys.argv) > 1):
    # arg passed, use it
    profile = sys.argv[1]

print("\nusing profile:" + profile)

client = OpenRGBClient()
client.load_profile(profile)
