# -*- coding: utf-8 -*-
"""status_example.py: double-click executable that displays the status object.
Author: Garin Wally; Aug 2016

"""

from time import sleep

from aside import status, status_process, wait


print(__doc__)

status.write("Party on magenta 'excellent'...")
sleep(2)
status.custom("Excellent!", "magenta")

status.write("Cha! Standard success...")
status.success()


status.custom("custom Sha-WING status", "cyan")

@status_process
def stairway():
    """This function plays Stairway To Heaven.
    Msg:
        Playing Stairway...
    """
    raise Exception("DENIED")

stairway()
