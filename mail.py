import json
import smtplib
import tempfile
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Read data from temp JSON file
temp_json_path = tempfile.gettempdir() + "/services.json"

try:
    with open(temp_json_path, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: JSON data file not found.")
    exit()

username = data.get("username", "Unknown")
location = data.get("location", "Unknown")
services = ", ".join(data.get("services", []))

# Email Configuration
sender_email = "gaitanalysisserver@gmail.com"
receiver_email = "ajitajane@gmail.com"
password = "qzscqxibmzcmxtrq"  # Replace with app-specific password

subject = "New Assistance Request"

body = f"""User Name: {username}
Location: {location}
Requested Services: {services}
"""

# Email setup
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(msg)
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")