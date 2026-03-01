"""Prediction helper for Custom Vision classification."""

from azure.cognitiveservices.vision.customvision.prediction import (
    CustomVisionPredictionClient,
)
from msrest.authentication import ApiKeyCredentials

from . import config


def get_prediction_client() -> CustomVisionPredictionClient:
    """Return an authenticated prediction client."""
    credentials = ApiKeyCredentials(
        in_headers={"Prediction-key": config.PREDICTION_KEY}
    )
    return CustomVisionPredictionClient(config.PREDICTION_ENDPOINT, credentials)


def classify_image(image_path: str) -> list[dict]:
    """Classify an image and return a list of predictions."""
    client = get_prediction_client()
    with open(image_path, "rb") as image_data:
        results = client.classify_image(
            config.PROJECT_ID,
            config.PUBLISH_ITERATION_NAME,
            image_data.read(),
        )
    return [
        {"tag": p.tag_name, "probability": p.probability}
        for p in results.predictions
    ]
