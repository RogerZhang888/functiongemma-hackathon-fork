
import sys
sys.path.insert(0, "cactus/python/src")
functiongemma_path = "cactus/weights/functiongemma-270m-it"

import json, os, time
from cactus import cactus_init, cactus_complete, cactus_destroy
from google import genai
from google.genai import types

import numpy as np
from process_data import process_messages
from train import train_router_gbdt
from import_dataset import extract_from_main_list
from data import main_list

model = cactus_init(functiongemma_path)
n_samples = 1
n_embd = 768
n_features = 10

messages, tools_list, num_tools, labels = extract_from_main_list(main_list)

# tools_list = [{
#         "name": "get_weather",
#         "description": "Get current weather for a location",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "location": {
#                     "type": "string",
#                     "description": "City name",
#                 }
#             },
#             "required": ["location"],
#         },
#     }]

# messages = [
#     {"role": "user", "content": "What is the weather in San Francisco?"}
# ]
num_tools = [1]
y = [0]
p,q = process_messages(model, messages, tools_list, num_tools, n_embd, n_features, n_samples, normalize=False)
bundle = train_router_gbdt(p,q,y)

