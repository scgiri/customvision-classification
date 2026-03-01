"""CLI entry-point for Custom Vision classification."""

import argparse
import json
import sys

from .predict import classify_image


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Classify an image using Azure Custom Vision."
    )
    parser.add_argument("image", help="Path to the image file to classify.")
    parser.add_argument(
        "--json", action="store_true", dest="as_json", help="Output results as JSON."
    )
    args = parser.parse_args(argv)

    predictions = classify_image(args.image)

    if args.as_json:
        print(json.dumps(predictions, indent=2))
    else:
        for p in predictions:
            print(f"{p['tag']:30s} {p['probability']:.4f}")


if __name__ == "__main__":
    main()
