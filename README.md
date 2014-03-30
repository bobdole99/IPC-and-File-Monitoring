IPC-and-File-Monitoring
=======================

Emitter.py will emit a signal to Recipient.py, unfortunetly not a signal indicating a change in the directory. Emitter.py will print to the screen that a change in the directory has occured but not Recipient.py. When I place the directory_changed method into class Emitter and place the monitor set up into the constructor, both Emitter.py and Recipient just hang. I cant seem to resolve the bug, I'm sure its something minor. 
