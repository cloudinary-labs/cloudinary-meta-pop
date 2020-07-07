from flask import Flask, request, render_template
import os
import json
from retry import retry

import cloudinary
import cloudinary.uploader

app = Flask(__name__)

@app.route('/', methods=['POST'])
# @retry(tries=5, delay=2)
def inbound_parse():
    print(json.dumps(request.json))
    payload = request.json

    #add security layer to match password

    #take split logic from var

    #update resource via update api
    # asset = cloudinary.api.resource(payload['public_id'])
    result = cloudinary.api.update(payload['public_id'], metadata='cat_name=garfield')
    return "OK"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    upload_preset = str(os.environ.get('UP_PRESET', 'email_uploader'))
    cld_url = str(os.environ.get('CLOUDINARY_URL', '')) 
    print ("app will run on port:", port)
    app.run(host='0.0.0.0', port=port)