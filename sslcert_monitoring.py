import os
import time
from datetime import datetime, timedelta, timezone
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from telegram import Bot

# Configuration
CERT_DIR = '/path/to/certificates/'
DAYS_BEFORE_EXPIRY = 5
TELEGRAM_TOKEN = 'TOKEN'
CHAT_ID = 'Chat-ID'

def check_certificates():
    for filename in os.listdir(CERT_DIR):
        if filename.endswith('.crt'):
            cert_path = os.path.join(CERT_DIR, filename)
            try:
                with open(cert_path, 'rb') as cert_file:
                    cert_data = cert_file.read()
                    cert = x509.load_pem_x509_certificate(cert_data, default_backend())
                    expire_time = cert.not_valid_after_utc  # This is aware datetime
                    now_utc = datetime.now(timezone.utc)  # Make 'now' aware
                    if expire_time < now_utc + timedelta(days=DAYS_BEFORE_EXPIRY):
                        notify_expiry(filename, expire_time)
            except Exception as e:
                print(f"Error reading certificate {filename}: {e}")

def notify_expiry(cert_name, expire_time):
    bot = Bot(token=TELEGRAM_TOKEN)
    message = f"⚠️ Certificate '{cert_name}' is expiring on {expire_time.strftime('%Y-%m-%d %H:%M:%S')} UTC. Please renew it."
    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    while True:
        check_certificates()
        time.sleep(86400)  # Check every 24 hours
