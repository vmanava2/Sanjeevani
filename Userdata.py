import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'symbol':'GE',
'datatype':'equity',
'entitlement':'DL',
'delaymin':15,
'datetime':'2010-06-08T15:03:40-04:00',
'exchange':'NYE',
'longname':'GENERAL ELECTRIC',
'shortname':'GE',
'pricedata':{

   'last':15.3499,
   'change':-0.0601,
   'changepercent':-0.390006,
   'tick':1,
   'open':15.46,
   'high':15.55,
   'low':15.05,
   'prevclose':15.41,
   'bid':15.34,
   'ask':15.35,
   'bidsize':20100,
   'asksize':19100,
   'tradevolume':149741,
   'sharevolume':68300391,            
   'lasttradedatetime':'2010-06-08T15:03:40-04:00'

}},
    {'id': 1,
     'symbol':'MSFT',
'datatype':'equity',
'entitlement':'DL',
'delaymin':15,
'datetime':'2010-06-08T15:03:40-04:00',
'exchange':'NGS',
'longname':'Microsoft Corp.',
'shortname':'MSFT',
'pricedata':{

   'last':24.95,
   'change':-0.34,
   'changepercent':-1.3444,
   'tick':0,
   'open':25.25,
   'high':25.26,
   'low':24.65,
   'prevclose':25.29,
   'bid':24.94,
   'ask':24.95,
   'bidsize':28900,
   'asksize':10400,
   'tradevolume':198456,
   'sharevolume':68356390,            
   'lasttradedatetime':'2010-06-08T15:03:38-04:00'

     
}
},
    {'id': 2,
     'symbol':'AWS',
'datatype':'equity',
'entitlement':'DL',
'delaymin':15,
'datetime':'2010-06-08T15:03:40-04:00',
'exchange':'NGS',
'longname':'AMANZON Corp.',
'shortname':'AWS',
'pricedata':{

   'last':24.95,
   'change':-0.34,
   'changepercent':-1.3444,
   'tick':0,
   'open':25.25,
   'high':25.26,
   'low':24.65,
   'prevclose':25.29,
   'bid':24.94,
   'ask':24.95,
   'bidsize':28900,
   'asksize':10400,
   'tradevolume':198456,
   'sharevolume':68356390,            
   'lasttradedatetime':'2010-06-08T15:03:38-04:00'

     
}
}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()
