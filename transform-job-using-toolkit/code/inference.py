import json
import os
import pandas

from sagemaker_inference import logging

logging.configure_logger()
logger = logging.get_logger()

def model_fn(model_dir):
    return json.load(open(os.path.join(model_dir, "model.json"), "r"))

def input_fn(input_data, content_type=None):
    if content_type == "application/json":
        return json.loads(input_data)
    else:
        raise ValueError("Supports only JSON")

def predict_fn(data, model):
    logger.info(data)
    logger.info(model)
    return data

def output_fn(prediction, accept=None):
    return json.dumps(prediction)
