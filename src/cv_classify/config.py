"""Configuration for Custom Vision classification."""

import os


PREDICTION_KEY = os.getenv("CV_PREDICTION_KEY", "")
PREDICTION_ENDPOINT = os.getenv("CV_PREDICTION_ENDPOINT", "")
PROJECT_ID = os.getenv("CV_PROJECT_ID", "")
PUBLISH_ITERATION_NAME = os.getenv("CV_PUBLISH_ITERATION_NAME", "")
