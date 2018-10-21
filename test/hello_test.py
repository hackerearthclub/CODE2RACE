#!/usr/bin/env python3
import os
import subprocess
import sys

import pytest


@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires Python >= 3.7")
def test_hello():
    with os.scandir("solutions") as it:
        for entry in it:
            name = entry.name.lower()
            if entry.is_file() and "hello" in name and os.path.splitext(name)[-1] == ".py":
                print(entry.path)
                result = subprocess.run(["python3", entry.path], capture_output=True)
                assert result.returncode == 0, f"{entry.path} failed to run on Python 3."
                assert "hello world" in str(result.stdout).lower(), f"{entry.path} did not contain 'hello world'."
