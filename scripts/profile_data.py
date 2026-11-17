"""Profile the supplied raw catalog without reproducing Power BI filters."""
from pathlib import Path
import csv
import json

source = Path(__file__).resolve().parents[1] / 'Dataset/lego_sets.csv'
with source.open(encoding='utf-8-sig', newline='') as stream:
    reader = csv.DictReader(stream)
    rows = list(reader)
    fields = reader.fieldnames
assert len(rows) == 18457, "Source population changed; review documented figures."
assert len({row['set_id'] for row in rows}) == len(rows), "Duplicate set IDs."
assert all(None not in row for row in rows), "Malformed CSV rows."
years = [int(row['year']) for row in rows]
prices = [float(row['US_retailPrice']) for row in rows if row['US_retailPrice']]
print(json.dumps({
    'rows': len(rows), 'columns': fields,
    'year_min': min(years), 'year_max': max(years),
    'themes': len({row['theme'] for row in rows}),
    'missing': {key: sum(not row[key] for row in rows) for key in fields},
    'mean_price_nonmissing': sum(prices) / len(prices),
    'note': 'Raw CSV profile; not the 2669-set screenshot population.'
}, indent=2))
