#!/usr/bin/env python3
#
# networks.py <iface> [--hide]
#
# Print basic connection information for the given interface in statusbar format.
#
# If the --hide flag is passed, will not display when offline.

import sys
from sys import argv
import netifaces as ifaces

if len(argv) != 2 and len(argv) != 3:
    print("err: bad arguments")
    sys.exit(1)

iface_name = argv[1]

iface_list = ifaces.interfaces()

if not iface_name in iface_list and len(argv) == 2:
    sys.stdout.write("%s: unavailable\n"%iface_name)
    sys.stdout.flush()
    sys.exit()
elif not iface_name in iface_list:
    print()
    sys.exit()

iface_data = ifaces.ifaddresses(iface_name).get(ifaces.AF_INET)
if iface_data == None:
    sys.stdout.write("%s: offline\n"%iface_name)
    sys.stdout.flush()
    sys.exit()

sys.stdout.write("%s: online "%iface_name)

addr = iface_data[0].get('addr')
subnet = str(iface_data[0].get('netmask').count('255')*8)

sys.stdout.write("%s/%s"%(addr,subnet))

sys.stdout.write("\n")
sys.stdout.flush()
