# json-parser
Create a simple script to parse json from an endpoint, and sort in alphabetical order

## How it works

First up, I saved the endpoint url into a variable. Using the *requests* module I use the variable as an argument for the GET call, 
and return the data as a json object

In order to use the sorted function, I first needed to select the *title* key using a simple function.

Once I was pulling the data by the *title* I could then pass this into *sorted*, using my function as an argument, to sort by the title. 
