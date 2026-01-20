from typing import List, Dict


def extract_isbn_identifiers(industry_identifiers: List[Dict[str, str]] | None) -> Dict[str, str | None]:
    isbn_10 = None
    isbn_13 = None

    if industry_identifiers:
        for identifier in industry_identifiers:
            id_type = identifier.get('type', '')
            id_value = identifier.get('identifier', '')

            if id_type == 'ISBN_10':
                isbn_10 = id_value
            elif id_type == 'ISBN_13':
                isbn_13 = id_value

    return {'isbn_10': isbn_10, 'isbn_13': isbn_13}