#!/usr/bin/env python3
import os
import subprocess
import sys

if sys.version_info <= (3, 5):
    sys.exit()

with os.scandir("solutions") as it:
    for entry in it:
        name = entry.name.lower()
        if entry.is_file() and "hello" in name and os.path.splitext(name)[-1] == ".py":
            print(entry.path)
            result = subprocess.run(["python3", entry.path], capture_output=True)
            assert result.returncode == 0, "Failed to run on Python 3."
            assert "hello world" in str(result.stdout).lower(), "Did not contain 'hello world'."
