# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 12:50:54 2018

@author: Sreeje.a
"""

import  requests
import subprocess

def get_rasa_intent(query, modelname):
        
    subprocess.call(["python", "-m", "rasa_nlu.server", "--port", "5000", "-c", RASA_CONFIG_SPACY])
    nlu_data = requests.get(RASA_PARSER_URL + query + '&model=' + modelname).json()

    entity_list = []
    values_list = []

    for i in xrange(len(nlu_data['entities'])):
        entity_list.append(nlu_data['entities'][i]['entity'])
        values_list.append(nlu_data['entities'][i]['value'])

    intent_data = nlu_data['intent']['name']
    
    confidence_data = nlu_data['intent']['confidence']

    return intent_data, confidence_data

