thonpython
import json
import logging

class JSONExporter:
    """Exports data to JSON."""

    def export(self, data, path: str):
        logging.info(f"Exporting JSON to {path}")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        logging.info("JSON export completed")