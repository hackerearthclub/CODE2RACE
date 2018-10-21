import os
import subprocess
import sys

import pytest


@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires Python >= 3.7")
def test_ascii():
    with os.scandir("SOLUTIONS") as it:
        for entry in it:
            name = entry.name.lower()
            if entry.is_file() and "ascii" in name and os.path.splitext(name)[-1] == ".py":
                if entry.path == "SOLUTIONS/ASCII_CODE_STRING.py":
                    continue
                print(entry.path)
                for in_s, out_s in {"IS": "6059", "GfG": "514182"}.items():
                    result = subprocess.run(["python3", entry.path], input=in_s,
                                            capture_output=True, check=True, text=True)
                    assert out_s in result.stdout, f"{entry.path} {in_s} did not return {out_s}."


@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires Python >= 3.7")
def test_hello():
    with os.scandir("SOLUTIONS") as it:
        for entry in it:
            name = entry.name.lower()
            if entry.is_file() and "hello" in name and os.path.splitext(name)[-1] == ".py":
                print(entry.path)
                result = subprocess.run(["python3", entry.path], capture_output=True)
                assert result.returncode == 0, f"{entry.path} failed to run on Python 3."
                assert "hello world" in str(result.stdout).lower(), f"{entry.path} did not contain 'hello world'."
