import operator
from typing import List, Dict, Any

COUNTRIES: List[Dict[str, Any]] = [
{'name': 'Canada', 'size': 9984670, 'population': 38250000},
{'name': 'Italy', 'size': 301340, 'population': 59110000},
{'name': 'United Kingdom', 'size': 242495, 'population': 67220000},
{'name': 'France', 'size': 551695, 'population': 67390000},
{'name': 'Germany', 'size': 357022, 'population': 83200000},
{'name': 'Japan', 'size': 377975, 'population': 125700000},
{'name': 'United States', 'size': 9833517, 'population': 331900000}
]

def alphabetize_names(list_of_dicts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(list_of_dicts, key=operator.itemgetter('name'))
    # return sorted(list_of_dicts, key=lambda x: x['name'])

def main() -> None:
    mylist: List[Dict[str, Any]] = alphabetize_names(COUNTRIES)
    for country in mylist:
        print(f"{country}")
        # print(f"{country['name']}: Size={country['size']}, Population={country['population']}")

if __name__ == "__main__":
    main()
