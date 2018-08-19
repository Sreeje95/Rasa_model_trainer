# Rasa_model_trainer

Rasa_trainer.py

1) Traines the intent with its respective queries.
2) Given the required json and the model name , the module builds the model in the paah specified with its own name and time stamp.

Intent_identfier.py

1) Firstly makes the subprocess call and makes the server up.
2) Uses the model and identifies the intent respective to the query thats specified.
3) Provides the sorted intent names with confidence score. 
