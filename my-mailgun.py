# A module to make HTTP requests
import requests

# A function
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox6a3b87db852f48d38cf716df17b1c39d.mailgun.org/messages",
        auth=("api", "83d539302bee6d94995b42c663f66946-acb0b40c-18f17c51"),
        data={"from": "Excited User <mailgun@sandbox6a3b87db852f48d38cf716df17b1c39d.mailgun.org>",
              "to": "g.sofi@lse.ac.uk",
              "subject": "Hello",
              "text": "Testing some Mailgun awesomeness!"})

response = send_simple_message()
print response.json()
