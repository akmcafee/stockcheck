import requests
from bs4 import BeautifulSoup
import time
import smtplib
import html5lib

# Product URL
product_list = {
    '20mm black strap': 'https://www.scurfawatches.com/product/20mm-black-strap-with-stainless-steel-buckle/',
    'Treasure Seeker - Orange': 'https://www.scurfawatches.com/product/treasure-seeker-orange-dial/'
}

# Email configuration
sender_email = 'your_email@example.com'
receiver_email = 'notification_email@example.com'
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'your_email@example.com'
smtp_password = 'your_email_password'


# def pretty_page():
#     # pull a pretty copy of the page
#     response = requests.get(product_list)
#     soup = BeautifulSoup(response.content, 'html5lib')
#     print(soup.prettify())

def stock_status():
    for product, url in product_list.items():
        # Send a GET request to the product page
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the stock indicator on the page and prove it is being read properly.
        current_status = soup.find('p', {'class': 'stock out-of-stock'}) or soup.find('p', {'class': 'stock in-stock'})

        if current_status:
            print(product, 'is', current_status.text)
        else:
            print('No stock status available at this time for the', product, 'product.')

        # if 'out of stock' in current_status.text.lower():
        #     print(url, 'is ', current_status.text)
        # elif 'in stock' in current_status.text.lower():
        #     print(url, 'is ', current_status.text)
        # else:
        #     print('No stock status available at this time for the ', url, 'product.')

    # print(current_status)

    # if current_status and 'Out of stock' in current_status.text.lower():
    #     print('There is currently no stock of this item.')
    # else:
    #     print('Stock Status unavailable.')


# def check_availability():
#     # Send a GET request to the product page
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     # Find the element that indicates availability
#     availability_element = soup.find('p', {'class': 'stock out-of-stock'})
#
#     # Check if the product is out of stock
#     if availability_element and 'Out of stock' in availability_element.text.lower():
#         print('It is out of stock')
#     else:
#         print('Not sure what happened.')


# pretty_page()
stock_status()
# check_availability()
# stock_status.notify_me()


# # Check if the product is in stock
# if availability_element and 'in stock' in availability_element.text.lower():
#     return True
# else:
#     return False

# def send_notification():
#     subject = 'Product Back in Stock'
#     body = f"The product you were monitoring ({url}) is back in stock!"

#     # Compose the email message
#     message = f"Subject: {subject}\n\n{body}"

#     # Connect to the SMTP server and send the email
#     with smtplib.SMTP(smtp_server, smtp_port) as server:
#         server.starttls()
#         server.login(smtp_username, smtp_password)
#         server.sendmail(sender_email, receiver_email, message)

# Monitoring loop
# while True:
#     if check_availability():
#         send_notification()
#         break  # Stop monitoring after the first notification
#     else:
#         print('Product is currently out of stock. Checking again in 1 hour...')
#         time.sleep(3600)  # Sleep for 1 hour before checking again
