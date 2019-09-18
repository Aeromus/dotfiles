#!/usr/bin/env python3
#
# current_workspace.py
#
# Print out just the current "focused" i3 workspace when it changes
#

import i3ipc
import sys

i3 = i3ipc.Connection()

def on_workspace_change(self, useless):
    workspaces = self.get_workspaces()
    for workspace in workspaces:
        if workspace.get('focused', False):
            print(workspace.get('name', 'unknown'))
    sys.stdout.flush()

i3.on('workspace::focus', on_workspace_change)

on_workspace_change(i3, None)

i3.main()
