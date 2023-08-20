#

#pip install pywhatkit

import pywhatkit

# Set the target phone number (with country code) and the message
phone_number = "+1234567890"
message = "Hello, this is an automated WhatsApp message!"

# Schedule the message to be sent at a specific time (24-hour format)
hour = 13
minute = 30

# Send the scheduled message
pywhatkit.sendwhatmsg(phone_number, message, hour, minute)

