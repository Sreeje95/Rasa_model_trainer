# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 12:37:40 2018

@author: Sreeje.a
"""

from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
# from rasa_nlu.model import Metadata, Interpreter
import pandas as pd
import os, subprocess, json
import csv_to_rasa


def model_engine(train, model="NA", rasa= False):
    #    model = sys.argv[1]
    config = RASA_CONFIG_SPACY

    if train and model!='NA':
#        tf_model_engine(model)
        # Create separate class/intent based data files
        
        file_path = os.path.join(INPUT_PATH +, (model + '/' + model + '.csv'))
        csv_reader = pd.read_csv(file_path)
        
        if "Intent" in csv_reader.columns:
            print "\n*******************"
            print "Building rasa model for "+ model
            print "********************\n"
            csv_to_rasa.convert_csv_to_rasa_json(model)
            #convert_generic_to_rasa(model)
    
            load_traning_data_path = os.path.join(RASA_JSON_PATH, (model + '.json'))
            model_path = (RASA_MODEL_PATH)
            
            print "starting rasa training..............."
            training_data = load_data(load_traning_data_path)
            print "loaded training data"
            trainer = Trainer(RasaNLUConfig(config))
            trainer.train(training_data)
            print "done training..."
            if not os.path.exists(model_path):
                os.makedirs(model_path)
    
            path_model = trainer.persist(path=model_path)  # , create_unique_subfolder=False)
    
            with open(config, 'rb') as f:
                configfile = json.load(f)
    
            configfile['server_model_dirs'][
                model] = path_model  # Modify the config.spacy.json based on created model with timestamp
    
            with open(config, 'wb') as f:
                json.dump(configfile, f)
            
    if rasa==True and model == 'NA' and train==False:
        print "making subprocess call"
        subprocess.call(["python", "-m", "rasa_nlu.server", "--port", "5000", "-c", RASA_CONFIG_SPACY])
        print "done"
        
    return 'ModelBuilt'
        

if __name__ == "__main__":
   
    model_engine(train=False, model="NA", rasa=True)
