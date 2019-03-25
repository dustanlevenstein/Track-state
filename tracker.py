import subprocess, time, sys
from subprocess import PIPE # , STDOUT, DEVNULL

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
	 heading = None, *subproc_args, **subproc_kargs)

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

	The heading parameter is prepended to the file output. It must be
	passed by keyword.
	"""
	keys = kargs.keys()
	if "post_process_output_file" in keys:
		pass # ... TODO incorporate all the ways that kargs could be involved here.
	if isinstance(args[0], int):
		post_process_output_file = None
		period = args[0]
		args = args[1:]
	elif "period" in keys:
		period = kargs["period"]
		del kargs["period"]
	if isinstance(args[0], str):
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
			subprocess.run(["rm", post_process_output_file])
			args = args[1:]
		if "period" not in dir():
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
		pass # TODO... define timestamp and terminal output.
	time_stamp = time.asctime
	terminal_output = sys.stdout
	continue_tracking = True
	if "stdout" not in keys:
		kargs["stdout"] = PIPE
	if "stderr" not in keys:
		kargs["stderr"] = PIPE
	heading = None
	if "heading" in keys:
		heading = kargs["heading"]
		del kargs["heading"]
	f = open(output_file, "w")
	if heading is not None:
		print(heading, file = terminal_output, flush = True)
		print(heading, file = f, flush = True)
	while continue_tracking:
		if time_stamp is not False:
			print(time_stamp(), file = terminal_output, flush = True)
			print(time_stamp(), file = f, flush = True)
		cp = subprocess.run(*args, **kargs)
		out = cp.stdout.decode("utf-8")
		err = cp.stderr.decode("utf-8")
		print(out, file = terminal_output, flush = True)
		print(err, file = terminal_output, flush = True)
		print(out, file = f, flush = True)
		print(err, file = f, flush = True)
		continue_tracking = out.find(terminating_substring) == -1
		if continue_tracking: time.sleep(period)
	f.flush()
	f.close()
	if post_process_output_file is not None:
		subprocess.run(["mv", output_file, post_process_output_file])

class NullStream(object):
	def write(*args, **kargs): return None

if __name__ == "__main__":
	pass # TODO come up with a snazzy default...

