# import all dependencies - flask, configparser and json
from flask import Flask
import configparser
import json
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ini_to_json():

    # defining a variable that will be an instance of config parser
    config_object = configparser.ConfigParser()

    # connecting to Mongo DB
    myclient = MongoClient("mongodb+srv://satyaDevops:Nem0Vm5P03jWfxRJ@clusterone.u4fsgyz.mongodb.net")
    mydb = myclient["config_to_json"]
    Collection = mydb["Data"]

    # try-except block for handling exceptions gracefuly
    try:
        # open the file in read mode
        file = open("./example.ini","r")
        config_object.read_file(file)

        # define a variable where the converted data will be stored as dictionary

        output_dict = dict()

        # just like keys and values in dictonary, config file has sections and items
        # store sections as  list in a variable

        sections = config_object.sections()

        # write a for loop to put the sections and items as key-values in the pre-defines dictionary

        for section in sections:
            items = dict(config_object.items(section))

            output_dict[section] = items

        json_string = json(output_dict)

        print(json_string)

        # insert the data into collection
        Collection.insert_many(json_string)

        # retrieve the data from collections
        x = Collection.find()

        # close the file
        file.close()
        
        # print the data that is retrieved from collection
        for data in x:
            return data

    # catch the exceptions that are triggered, printing it on terminal as well as outputting on the API
    except Exception as e:
        print(str(e))
        return str(e)

if __name__ == '__main__':
    app.run(port=3000, debug=True)