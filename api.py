import json
import os
from flask import Flask, request

app = Flask(__name__)
data = [{"name":"y9bSIyIHI","marks":2},{"name":"bMwIGI","marks":69},{"name":"ta","marks":95},{"name":"lBfv","marks":2},{"name":"xEH4x","marks":66},{"name":"2POx","marks":31},{"name":"uZs","marks":35},{"name":"Q4rVqV60","marks":12},{"name":"6oFTb","marks":16},{"name":"v","marks":24},{"name":"fcaFb","marks":35},{"name":"nr","marks":30},{"name":"KSLJbnrnD3","marks":71},{"name":"tnG0","marks":78},{"name":"v0JthFI8","marks":64},{"name":"H","marks":61},{"name":"NPM","marks":10},{"name":"gcwI","marks":62},{"name":"U0d","marks":72},{"name":"H","marks":65},{"name":"ZcXcYeRLwL","marks":63},{"name":"teSKJp","marks":18},{"name":"hq","marks":78},{"name":"TVE","marks":53},{"name":"MHpmEm","marks":11},{"name":"XC7","marks":91},{"name":"W9uF","marks":32},{"name":"f1nOuk","marks":16},{"name":"p50Hsoo","marks":52},{"name":"LkoCYCj","marks":85},{"name":"NaOdTEe","marks":40},{"name":"SHn","marks":36},{"name":"T9R","marks":88},{"name":"sKeYfROkZ","marks":42},{"name":"rGl","marks":90},{"name":"gOF3UcyI8c","marks":17},{"name":"yoQrYdGoG","marks":84},{"name":"tIKZr","marks":98},{"name":"CgGRVA4ae","marks":50},{"name":"J","marks":57},{"name":"DKWDZhqh","marks":74},{"name":"HrmG8g6S55","marks":17},{"name":"6idPkrXIU","marks":63},{"name":"j8J5","marks":90},{"name":"ZA","marks":65},{"name":"7nuR","marks":87},{"name":"cY","marks":17},{"name":"y","marks":52},{"name":"rC7vb8MW4O","marks":4},{"name":"l4xI0DUF0h","marks":11},{"name":"ZAtByvczV3","marks":59},{"name":"fiNYSMhD","marks":26},{"name":"bs","marks":91},{"name":"pEk6rQqw","marks":68},{"name":"8UMJCox1X","marks":36},{"name":"L","marks":40},{"name":"jGQnjftU","marks":95},{"name":"aIhTM3dAb","marks":67},{"name":"J","marks":22},{"name":"49nA","marks":67},{"name":"Eujd","marks":30},{"name":"uFXEtD","marks":60},{"name":"xTYHrh","marks":77},{"name":"k3aUqH","marks":41},{"name":"KfTDd","marks":94},{"name":"eM","marks":74},{"name":"zuj3fEmApd","marks":17},{"name":"dt6M","marks":96},{"name":"RwY","marks":2},{"name":"DO7SYkOl","marks":12},{"name":"5zkVHY","marks":30},{"name":"GuaTC","marks":52},{"name":"Zxd2","marks":95},{"name":"Rq","marks":74},{"name":"fVuANFurfY","marks":54},{"name":"4tgp","marks":2},{"name":"E2R","marks":50},{"name":"ygzIfo","marks":6},{"name":"GbyO","marks":97},{"name":"fiF","marks":50},{"name":"XkSz","marks":25},{"name":"nb","marks":65},{"name":"wNhAaZsYm7","marks":85},{"name":"7VvG4iO1r","marks":38},{"name":"Oy05o4tUUX","marks":23},{"name":"l","marks":3},{"name":"ci4","marks":24},{"name":"bT","marks":97},{"name":"OrnaRTuJtj","marks":41},{"name":"y8MhX1dLKA","marks":45},{"name":"RUCkqSk","marks":19},{"name":"kiC","marks":33},{"name":"rz","marks":31},{"name":"n3o2uPz","marks":98},{"name":"5oratLPgQV","marks":88},{"name":"94ENZ","marks":82},{"name":"SXxtu4T6ny","marks":44},{"name":"zUk","marks":94},{"name":"vrPtL1","marks":94},{"name":"L7qhv3I4G","marks":87}]

@app.route('/api', methods=['GET'])
#def handle_request(request):
def handle_request():
    # Extract query parameters from the request
    names = request.args.getlist("name")
    
    # Create a response dictionary
    response = {}
    
    # Look up marks for each requested name
    for name in names:
        matching_entry = next((entry for entry in data if entry["name"] == name), None)
        if matching_entry:
            response[name] = matching_entry["marks"]
        else:
            response[name] = "Name not found"
    
    # Return the response as JSON
    return json.dumps(response)

if __name__ == "__main__":
    os.environ['FLASK_ENV'] = 'production'
    app.run()

# Create a basic handler function to return the response
def handler(request):
    return handle_request(request)

