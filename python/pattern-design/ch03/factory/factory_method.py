"""
Factory Method Pattern implementation for data extraction.
Supports JSON and XML file formats from the current directory.
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Dict, List

class JSONDataExtractor:
    def __init__(self, filepath: Path):
        self.data: List[Dict[str, Any]] = []
        with open(filepath, encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self) -> List[Dict[str, Any]]:
        return self.data

class XMLDataExtractor:
    def __init__(self, filepath: Path):
        self.tree = ET.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree

def extract_factory(filepath: Path):
    ext = filepath.name.split(".")[-1]
    if ext == "json":
        return JSONDataExtractor(filepath)
    if ext == "xml":
        return XMLDataExtractor(filepath)
    raise ValueError("Cannot extract data")

def extract(case: str):
    dir_path = Path(__file__).parent

    if case == "json":
        path = dir_path / Path("movies.json")
        factory = extract_factory(path)
        if isinstance(factory, JSONDataExtractor):
            data = factory.parsed_data

            for movie in data:
                print(f"\tDirector: {movie['director']}")
                genre = movie["genre"]
                if genre:
                    print(f"\tGenre: {genre}")
        else:
            raise ValueError("Expected JSONDataExtractor for JSON case")
    elif case == "xml":
        path = dir_path / Path("person.xml")
        factory = extract_factory(path)
        data = factory.parsed_data

        search_xpath = ".//person[lastName='Garcia']"
        items = data.findall(search_xpath)
        for item in items:
            first = item.find("firstName").text
            last = item.find("lastName").text
            print(f"-\t{first} {last}")
            for pn in item.find("phoneNumbers"):
                pn_type = pn.attrib["type"]
                pn_val = pn.text
                phone = f"{pn_type}: {pn_val}"
                print(f"\t{phone}")

if __name__ == "__main__":
    print("* JSON case *")
    extract(case="json")
    print("* XML case *")
    extract(case="xml")
