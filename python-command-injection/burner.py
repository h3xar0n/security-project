import os
import sys

class Burner:
    def burn(self, filename):
        print("Burning now")
        os.system("cat {filename} > /dev/sda")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        burner = Burner()
        burner.burn(sys.argv[1])
    else:
        print("Usage: python3 burner.py <filename>")
