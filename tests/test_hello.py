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
                    assert out_s in result.stdout, (
                        "{} {} did not return {}.".format(entry.path, in_s, out_s))


@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires Python >= 3.7")
def test_bottle():
    with os.scandir("SOLUTIONS") as it:
        for entry in it:
            name = entry.name.lower()
            if entry.is_file() and "bottle" in name and os.path.splitext(name)[-1] == ".py":
                if entry.path in ("SOLUTIONS/emptybottles.py", "SOLUTIONS/empty_bottles.py"):
                    continue
                print(entry.path)
                result = subprocess.run(["python3", entry.path], input="1\n6\n20 40 50 90 100",
                                        capture_output=True, check=True, text=True)
                assert "3" in result.stdout, f"{entry.path} 1\n6\n20 40 50 90 100 did not return 3."


@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires Python >= 3.7")
def test_hello():
    with os.scandir("SOLUTIONS") as it:
        for entry in it:
            name = entry.name.lower()
            if entry.is_file() and "hello" in name and os.path.splitext(name)[-1] == ".py":
                print(entry.path)
                result = subprocess.run(["python3", entry.path], capture_output=True,
                                        check=True, text=True)
                assert "hello world" in str(result.stdout).lower(), (
                    entry.path + " did not contain 'hello world'.")
