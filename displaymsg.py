import time
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from pyfirmata import Arduino, util, STRING_DATA

"""
This program will display a message sent to the Twilio number on a 16x02 LCD 
using an Ardunio UNO

"""
app = Flask(__name__)

board = Arduino('/dev/cu.usbmodem14101')


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()
    resp.message("Message recieved!") #respond to incoming message
    
    #display message on lcd 
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(body)) 

    print("Message body: " + str(body))
    print("Displayed on LCD screen!")

    return str(resp)
 


if __name__ == "__main__":
    app.run(debug=True)
