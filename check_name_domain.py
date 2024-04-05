#!/usr/bin/env python3
import subprocess


expectedName = "vaishnavimatre"
name = subprocess.run(["git", "config", "user.name"], capture_output=True, text=True).stdout.strip()


if name == expectedName:
    print("You are using email as per configuration, proceeding to commit")
    exit(0)
else:
    print(f"Configured email is not as per config. It should be {expectedName}")
    exit(1)
