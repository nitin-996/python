import subprocess

ls = subprocess.run(['ls','-lh' ],capture_output=True , universal_newlines=True )
output = ls.stdout

print(__name__)