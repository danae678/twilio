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
    
    # get the message sent to the Twilio number
    body = request.values.get('Body', None)

    # create a response
    resp = MessagingResponse()
    resp.message("Message recieved!")
    
    # display message on lcd 
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(body)) 

    print("Message body: " + str(body))
    print("Displayed on LCD screen!")

    return str(resp) # return the response
 
if __name__ == "__main__":
    app.run(debug=True)
