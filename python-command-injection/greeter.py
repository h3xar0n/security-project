import os
import sys
import subprocess

class Greeter:
    def greet(self, filename):
        try:
            # Use subprocess.run with a list of arguments to prevent command injection
            subprocess.run(["ls", filename], check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing ls: {e.stderr}")
        except FileNotFoundError:
            print(f"Error: 'ls' command not found. Is it in your PATH?")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        greeter = Greeter()
        greeter.greet(sys.argv[1])
    else:
        print("Usage: python3 greeter.py <filename>")
