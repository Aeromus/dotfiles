#!/usr/bin/env python3
#
# alert_workspaces.py
#
# Print a space-separated list of urgent workspaces
#

import i3ipc
import sys

i3 = i3ipc.Connection()

workspaces = i3.get_workspaces()

alerts = False

for workspace in workspaces:
    if workspace.get('urgent', False):
        alerts = True
        sys.stdout.write(' %s'%workspace.get('name','?'))

if not alerts:
    sys.stdout.write('none')

sys.stdout.write('\n')

sys.stdout.flush()
