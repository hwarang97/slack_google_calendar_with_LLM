import os

from dotenv import load_dotenv
from pyngrok import conf, ngrok

# setttings
load_dotenv()
conf.get_default().ngrok_path = "./ngrok.exe"
ngrok.set_auth_token(os.getenv("NGROK_AUTHTOKEN"))
PORT = 8000

# run ngrok
tunnel = ngrok.connect(PORT)

process = ngrok.get_ngrok_process()
print(f"public IP: {tunnel}")

try:
    process.proc.wait()
except KeyboardInterrupt:
    print(" Shutting down server.")
    ngrok.kill()
