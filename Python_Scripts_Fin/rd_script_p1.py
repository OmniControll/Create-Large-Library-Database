#open browser in default browser
import webbrowser

webbrowser.open('https://www.google.com')


#open file from RD
import subprocess

subprocess.run(['open', '/path/to/file.pdf'])