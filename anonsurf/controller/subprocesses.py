import os
import subprocess


def subprocess_args(include_stdout=True):
    if hasattr(subprocess, "STARTUPINFO"):
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        env = os.environ
    else:
        si = None
        env = None
    return ({"stdout": subprocess.PIPE} if include_stdout else {}) | {
        "stdin": subprocess.PIPE,
        "stderr": subprocess.PIPE,
        "startupinfo": si,
        "env": env,
    }
