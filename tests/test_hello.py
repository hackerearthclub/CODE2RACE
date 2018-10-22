import os
import subprocess
import sys

import pytest


@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires Python >= 3.7")
def test_ascii():
    for direcotry in ("SOLUTIONS", "OPEN CHALLENGE"):
        with os.scandir(direcotry) as it:
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
def test_bottle():
    for direcotry in ("SOLUTIONS", "OPEN CHALLENGE"):
        with os.scandir(direcotry) as it:
            for entry in it:
                name = entry.name.lower()
                if entry.is_file() and "bottle" in name and os.path.splitext(name)[-1] == ".py":
                    if entry.path == "SOLUTIONS/emptybottles.py":
                        continue
                    print(entry.path)
                    result = subprocess.run(["python3", entry.path], input="1\n6\n20 40 50 90 100",
                                            capture_output=True, check=True, text=True)
                    assert "3" in result.stdout, f"{entry.path} 1\n6\n20 40 50 90 100 did not return 3."


@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires Python >= 3.7")
def test_hello():
    for direcotry in ("SOLUTIONS", "OPEN CHALLENGE"):
        with os.scandir(direcotry) as it:
            for entry in it:
                name = entry.name.lower()
                if entry.is_file() and "hello" in name and os.path.splitext(name)[-1] == ".py":
                    if entry.path == "OPEN CHALLENGE/HellodearWorld.py":
                        continue
                    print(entry.path)
                    result = subprocess.run(["python3", entry.path], capture_output=True)
                    assert result.returncode == 0, f"{entry.path} failed to run on Python 3."
                    assert "hello world" in str(result.stdout).lower().replace(",", ""), (
                        f"{entry.path} did not contain 'hello world'.")
