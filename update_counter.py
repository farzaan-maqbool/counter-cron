import os
import subprocess

COUNTER_FILE = "counter.txt"

if os.path.exists(COUNTER_FILE):
    with open(COUNTER_FILE, "r") as f:
        count = int(f.read().strip())
else:
    count = 0

count += 1

with open(COUNTER_FILE, "w") as f:
    f.write(str(count))

subprocess.run(["git", "add", "counter.txt"])
subprocess.run(["git", "commit", "-m", f"Counter {count}"])
subprocess.run(["git", "push"])

print(f"Counter updated to {count}")