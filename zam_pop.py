from flask import Flask, jsonify
import csv

districts = []
with open("zam_district.csv", "r") as file:
    dict_reader = csv.DictReader(file)
    for district in dict_reader:
        districts.append(district)
        #print(districts)

app = Flask(__name__)
# the function is filtering districts by name 
# input: list of a dictionaries and str
#output: a dictionary
@app.route("/name/<Name>")
def filtering_name(Name):
    for district in districts:
        if district["Name"] == Name:
            return jsonify(district)
    return "not found" , 404

# This functionis filtering districts by province 
# Input: a list of dictionaries and a str
# Output: list of dictionaries  
@app.route("/provincial/<Province>")
def filtering_province(Province):
    list_of_districts = []
    for district in districts:
        if district["Province"] == Province:
            list_of_districts.append(district)
    return jsonify(list_of_districts)

# this functionis find the provinces above 800000
# input: list of dictionaries and int
# output: list of dictionaries
@app.route("/<year>/<population>")
def above_population(year, population):
    populated_area = []
    for district in districts:
        if district[year] > population:
            populated_area.append(district)
    return jsonify(populated_area)
