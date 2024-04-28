import os

os.system("pip install dload")

import subprocess
import webbrowser
import dload
dload.git_clone("https://github.com/Illumi14/Llama-3-simple.git")
webbrowser.open('https://ollama.com/download/OllamaSetup.exe')

input("click enter when you have sucessfully downloaded and installed ollama")

os.system("pip install ollama")
subprocess.call("powershell.exe ollama pull llama3", shell=True) 