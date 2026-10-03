#!/usr/bin/env python3
import subprocess
import shutil

def is_rofi_available():
    return bool(shutil.which("rofi") or shutil.which("rofi-wayland"))

def rofi(prompt, options, rofi_args=None, fuzzy=True):
    if rofi_args is None:
        rofi_args = []
    
    rofi_bin = "rofi"
    optionstr = "\n".join(opt.replace("\n", " ") for opt in options)
    
    args = [rofi_bin, "-dmenu", "-p", prompt, "-i"]
    if fuzzy:
        args += ["-matching", "fuzzy"]
    args += [str(arg) for arg in rofi_args]

    try:
        proc = subprocess.run(
            args,
            input=optionstr,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )
    except Exception as e:
        return -1, -1, ""

    returncode = proc.returncode
    selected = proc.stdout.rstrip("\r\n")

    try:
        index = options.index(selected)
    except ValueError:
        index = -1

    if returncode == 0:
        key = 0
    elif returncode == 1:
        key = -1  # Escaped / cancelled
    elif returncode > 9:
        key = returncode - 9
    else:
        key = returncode

    return key, index, selected

def rofi_input(prompt, prefill=""):
    """Prompt user for a single line of text."""
    rofi_bin = "rofi"
    args = [rofi_bin, "-dmenu", "-p", prompt, "-lines", "0"]
    if prefill:
        args += ["-filter", prefill]
    
    proc = subprocess.run(
        args,
        input="",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False
    )
    if proc.returncode == 0:
        return proc.stdout.strip()
    return None
