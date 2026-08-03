#!/usr/bin/env python3

from flask import Flask, make_response

# Sample contract records and customer names for the lab exercise.
contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"},
]
customers = ["bob", "bill", "john", "sarah"]
app = Flask(__name__)


@app.route('/contract/<int:id>')
def get_contract(id):
    """Return contract details for a matching contract ID, or 404 if missing."""
    contract = next((item for item in contracts if item["id"] == id), None)

    if contract is None:
        return make_response("Contract not found", 404)

    return make_response(contract["contract_information"], 200)


@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    """Return a 204 response when a customer exists without exposing sensitive data."""
    if customer_name.lower() in [name.lower() for name in customers]:
        return make_response("", 204)

    return make_response("Customer not found", 404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
