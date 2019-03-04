import subprocess, time, sys
from subprocess import PIPE, STDOUT, DEVNULL

settings_f = open("settings.txt", "r")
settings = settings_f.read()
exec(settings)
# At this point, the variables subprocess_args, subprocess_kargs,
# period, timestamp_output, stdout, stderr, and terminating_condition
# should be defined.

if terminating_condition is None:
	terminating_condition = lambda *args, **kargs: None

while True:
	
