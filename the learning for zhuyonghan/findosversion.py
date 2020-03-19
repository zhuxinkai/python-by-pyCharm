#!/usr/bin/env python3

import sys
import subprocess

CMD = "uname -a"

conn = subprocess.Popen(["ssh", "UNAME@HOST", CMD],
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
res = conn.stdout.readlines()
print(res)