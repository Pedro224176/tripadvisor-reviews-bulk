thonpython
import json
import logging
from pathlib import Path
from extractors.review_parser import ReviewParser
from extractors.location_parser import LocationParser
from extractors.filters import FilterEngine
from outputs.exporters import JSONExporter

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def load_input_urls(path: str):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with p.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    input_file = Path(__file__).resolve().parent.parent / "data" / "inputs.sample.txt"
    output_file = Path(__file__).resolve().parent.parent / "data" / "sample_output.json"

    urls = load_input_urls(str(input_file))
    logging.info(f"Loaded {len(urls)} URLs")

    parser = ReviewParser()
    location_parser = LocationParser()
    filter_engine = FilterEngine()

    all_reviews = []

    for url in urls:
        logging.info(f"Processing URL: {url}")
        location_data = location_parser.get_location_metadata(url)
        reviews = parser.extract_reviews(url)

        filtered = filter_engine.apply_filters(reviews, rating_min=3)

        for r in filtered:
            r["location"] = location_data
            all_reviews.append(r)

    exporter = JSONExporter()
    exporter.export(all_reviews, str(output_file))

    logging.info(f"Export complete: {output_file}")

if __name__ == "__main__":
    main()