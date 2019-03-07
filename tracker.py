import subprocess, time, sys
from subprocess import PIPE, STDOUT, DEVNULL

# settings_f = open("settings.txt", "r")
# settings = settings_f.read()
# exec(settings)
# At this point, the variables subprocess_args, subprocess_kargs,
# period, timestamp_output, stdout, stderr, and terminating_condition
# should be defined.
def track(output_file, terminating_substring, *args, **kargs):
	"""
	track(output_file, terminating_substring, post_process_output_file =
	 None, period = 15, time_stamp = True, terminal_output = True,
	 *subproc_args, **subproc_kargs)

	Outputs the result of subproc_args and subproc_kargs being passed to
	subprocess.run() periodically. Output file must be specified.
	post_process_output_file specifies where output_file should be moved
	after the terminating substring shows up in the subprocess PIPE. If an
	exception occurs before the terminating substring is seen, the file is
	not moved.

	If the parameter after output_file is an integer, then it is assumed to
	be the period.
	If the parameter after output_file is a string which can't be opened
	as a file, it is assumed to be a subproc_arg.

	If the parameter after period is a bool or a function, it is assumed to
	be time_stamp - if it is a function, then it will be called to obtain
	the time stamp. Otherwise time.asctime is used.
	If the parameter after time_stamp is a bool or contains a .write()
	method, then it is assumed to be terminal_output; in the case that it
	contains a .write() method, it is used as the output to print(file = ).
	"""
	# output_file, terminating_substring, post_process_output_file = None,
	# period = 15, time_stamp = True, terminal_output = True,
	# *subproc_args, **subproc_kargs)
	keys = kargs.keys()
	if "post_process_output_file" in keys:
		pass # ... TODO incorporate all the ways that kargs could be involved here.
	if isinstance(args[0], int):
		post_process_output_file = None
		period = args[0]
		args = args[1:]
	elif isinstance(args[0], str):
		try:
			post_process_output_file = args[0]
			f = open(post_process_output_file, "a")
		except:
			subproc_args = args
			subproc_kargs = kargs
			post_process_output_file = None
			period = 15
			time_stamp = time.asctime
			terminal_output = sys.stdout
		else:
			f.close()
			args = args[1:]
		if isinstance(args[0], int):
			period = args[0]
			args = args[1:]
		else:
			period = 15
	else:
		post_process_output_file = None
		period = 15
	# Now post_process_output_file and period have been defined.
	if isinstance(args[0], int):
		pass # TODO...
		

class NullStream(object):
	def write(*args, **kargs): return None
