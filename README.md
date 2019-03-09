# Track-state
Repeats a command periodically and records the results

Example usage:

```import tracker, platform, time, os
from tracker import *
heading = platform.node()
outfilename = "%s__dropbox_status_%s.txt" %(heading, time.strftime("%Y_%m_%d__%H_%M_%S"))
output_file = os.path.expanduser("~/%s" % outfilename)
post_output_file = os.path.expanduser("~/Dropbox/Dropbox_statuses/%s" % outfilename)
terminating_substring = "Up to date"

track(output_file, terminating_substring, post_output_file, ["dropbox", "status"], heading = heading)
```
