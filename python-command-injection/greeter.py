import os
import sys

class Greeter:
    def greet(self, filename):
        os.system(f"ls {filename}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        greeter = Greeter()
        greeter.greet(sys.argv[1])
    else:
        print("Usage: python3 greeter.py <filename>")
