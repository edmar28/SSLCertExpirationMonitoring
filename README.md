# SSL Certificate Monitoring Script

## Overview

This Python script monitors SSL certificates located in a specified directory. It checks for certificates that are about to expire within a configured number of days and sends notifications via Telegram.

## Requirements
- Python 3.x
- python-telegram-bot library
- cryptography library

  ## Installation
1. Install Python 3: If you don't have Python 3 installed, you can install it using your package manager. For example, on Ubuntu:


```bash
sudo apt update
sudo apt install python3 python3-pip
```

2. Install Required Libraries: Install the necessary libraries using pip:
```bash
pip3 install python-telegram-bot cryptography
```

## Configuration
Before running the script, configure the following variables in the script:

- CERT_DIR: Path to the directory containing your SSL certificates (e.g., '/etc/nginx/keys').
- DAYS_BEFORE_EXPIRY: The number of days before expiration to trigger a notification (default is set to 5).
- TELEGRAM_TOKEN: Your Telegram bot token. You can create a bot using BotFather.
- CHAT_ID: Your Telegram chat ID where notifications will be sent.

``` bash
# Configuration
CERT_DIR = '/path/to/your/certificates/'
DAYS_BEFORE_EXPIRY = 5
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'
```

## Usage
Run the script using Python 3:
```bash
python3 sslcertomonitoring.py
```

The script will run indefinitely, checking for expiring certificates every 24 hours.


## Setting Up as a Systemd Service
To ensure that the script runs in the background and restarts automatically, you can set it up as a systemd service.

1. Create a Service File: Create a new service file for your script:

```bash
sudo nano /etc/systemd/system/cert_monitor.service
```

2. Add the Following Configuration: Replace /path/to/your_script.py with the actual path to your Python script.
```bash
[Unit]
Description=SSL Certificate Monitor

[Service]
ExecStart=/usr/bin/python3 /path/to/your_script.py
Restart=always

[Install]
WantedBy=multi-user.target
```

3. Enable and Start the Service: Enable the service to start on boot and start it immediately:
```bash
sudo systemctl enable cert_monitor
sudo systemctl start cert_monitor
```

## Error Handling
The script will print any errors encountered while reading certificates to the console. Ensure that your certificates are in the correct format and that the path is correctly specified.

## License
This project is licensed under the MIT License - see the LICENSE file for details.



