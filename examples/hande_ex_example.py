# -*- coding: utf-8 -*-
"""handle_ex_example.py: double-click executable that displays the handle_ex
function.
Author: Garin Wally; Aug 2016

"""

from time import sleep

from aside import status, wait, handle_ex


print(__doc__)

status.write("Run important task...")
sleep(2)
status.success()

try:
    status.write("Divide 1 by 'str'...")
    1 / 'str'
    status.success()
except:
    status.failure()
    handle_ex()
