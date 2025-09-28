import logging
import os
import sys

from dotenv import load_dotenv
from pyngrok import conf, ngrok

# loggin settings
logging.basicConfig(
    level=logging.DEBUG,
    filename="ngrok_server.log",
    filemode="w",
)

# ngrok setttings
load_dotenv()
auth_token = os.getenv("NGROK_AUTHTOKEN")
domain = os.getenv("NGROK_DOMAIN")

if auth_token:
    ngrok.set_auth_token(auth_token)
    logging.info("NGROK_AUTHTOKEN has been set seccuessfully.")
else:
    logging.info("Error: NGROK_AUTHTOKEN enveironment variable is not set.")
    sys.exit(1)

if domain:
    logging.info("NGROK DOMAIN has benn set successfully.")
else:
    logging.info("Error: NGROK_DOMAIN enveironment variable is not set.")
    sys.exit(1)

conf.get_default().ngrok_path = "./ngrok.exe"
PORT = 8000

# run ngrok
tunnel = ngrok.connect(addr=f"{PORT}", domain=f"{domain}")
process = ngrok.get_ngrok_process()
print(f"public IP: {tunnel}")

try:
    process.proc.wait()  # pyright: ignore [reportUnknownMemberType]
except KeyboardInterrupt:
    logging.info("Shutting down server by user request (Ctrl+ c).")
    ngrok.kill()
