"""
Docstring for sorting-algorithms.routes
houses the app routes for flask to reference
"""
from typing import Literal
from flask import Blueprint, Response, jsonify, render_template, request
from .SortingAlgorithms import ALGORITHMS

main = Blueprint("main", __name__) # Flask object blueprint marker

# Flask URL function to display contents of "index.html"
@main.route("/")
def index() -> str:
    return render_template("index.html")

# Flask URL function to retrieve HTML user inputs for back-end python calculations
@main.route("/get_data")
def get_data() -> tuple[Response, Literal[400]] | Response:

    user_entry_num = int(request.args.get('userEntry', 10)) # HTML user input: number of elements
    algo_key = request.args.get('algoType') # HTML user input: Algorithm option selected

    AlgoClass = ALGORITHMS.get(algo_key) # Retrieves Algorithm class from associated key in ALGORITHMS registry
    if AlgoClass is None:
        return jsonify({"Error": "Invalid Value Type"}), 400 # return HTTP status code 400
    
    sorter = AlgoClass(user_entry_num) # Instantiate the class instance with user input data
    sorter.generate_data() # Generates random values corresponding to length of list (user_entry_num) 
    result = sorter.sort() # Sorting logic
    return jsonify({"result": result}) # Return array sorting states as JSON response

