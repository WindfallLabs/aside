# -*- coding: utf-8 -*-
"""nix_example.py: double-click executable that displays the Nix object.
Author: Garin Wally; Aug 2016

"""

from time import sleep

from aside import nix, nix_decorator, wait


print(__doc__)

nix.write("Party on Garth")
sleep(2)
nix.ok()

nix.write("It's like a new pair of underware")
nix.ok()

nix.info("I don't have much to say right now")

nix.warn("It's sucking my will to live!")

@nix_decorator
def get_date():
    """Function that will get me a hot date.
    Msg:
        Why don't you just go talk to her?
    """
    sleep(3)
    raise ZeroDivisionError("I must have slipped")

get_date()
