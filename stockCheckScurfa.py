import requests
from bs4 import BeautifulSoup
import time
import smtplib

# Product URL
url = 'https://www.scurfawatches.com/product/treasure-seeker-orange-dial/'

# Email configuration
sender_email = 'your_email@example.com'
receiver_email = 'notification_email@example.com'
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'your_email@example.com'
smtp_password = 'your_email_password'

def check_availability():
    # Send a GET request to the product page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element that indicates availability
    availability_element = soup.find('span', {'class': 'stock out-of-stock'})

    # Check if the product is in stock
    if availability_element and 'out-of-stock' in availability_element.text.lower():
        return True
    else:
        return False

    # # Check if the product is in stock
    # if availability_element and 'in stock' in availability_element.text.lower():
    #     return True
    # else:
    #     return False

def send_notification():
    subject = 'Product Back in Stock'
    body = f"The product you were monitoring ({url}) is back in stock!"

    # Compose the email message
    message = f"Subject: {subject}\n\n{body}"

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message)

# Monitoring loop
while True:
    if check_availability():
        send_notification()
        break  # Stop monitoring after the first notification
    else:
        print('Product is currently out of stock. Checking again in 1 hour...')
        time.sleep(3600)  # Sleep for 1 hour before checking again
