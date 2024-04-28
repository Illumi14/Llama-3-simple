import os
import subprocess
import webbrowser

os.system("pip install ollama")
subprocess.call("powershell.exe ollama pull llama3", shell=True) 

webbrowser.open('https://ollama.com/download/OllamaSetup.exe')



