===================================
aside -- Glorified Print-statements
===================================

aside is a package for displaying nice shell messages when processes are being and have been executed.
Specifically, this package is designed for scripts which are executed by double-clicking.

When created double-click executable Python source code that just closes whenever it feels like it,
it might be useful to hang the process so the user can see what happened. The wait() and handle_ex()
functions hang the process until the user hits the return key. See the handle_ex_example.py and handle_ex.png
screenshot.


