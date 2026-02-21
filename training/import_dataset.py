import json
import numpy as np
def extract_from_main_list(main_list):
    """
    Reads dataset from JSON file and separates:
      - prompts (list of strings)
      - num_available_tools (list of ints)
      - labels (numpy array)
    """


    # Extract fields
    prompts = [item["prompt"] for item in main_list]
    tools_list = [item["available_tools"] for item in main_list]
    num_tools = [item["num_available_tools"] for item in main_list]
    labels = np.array([item["route_label"] for item in main_list])

    return prompts, tools_list, num_tools, labels


