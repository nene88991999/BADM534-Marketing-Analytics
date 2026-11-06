"""Export work-specific OpenAlex university affiliations without using current author profiles."""
from pathlib import Path
import csv
import json

HERE = Path(__file__).resolve().parent
LIBRARY = HERE.parents[1] / '01_Resources/13_Consumer_Agency_and_Recent_Research'


def save(name, rows):
    with (HERE / name).open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def main():
    catalog = json.loads((LIBRARY / 'catalog.json').read_text())['resources']
    works = json.loads((LIBRARY / 'local_sources/openalex_records.json').read_text())
    corrections = json.loads((HERE / 'affiliation_corrections.json').read_text())
    pairs, coverage = [], []
    for paper in catalog:
        if not paper['research_screen_eligible']:
            continue
        work = works.get(paper['doi'], {})
        authors = work.get('authorships', [])
        institutions = {i['id']: i for a in authors for i in a.get('institutions', [])
                        if i.get('type') == 'education'}
        author_sets = [{i['id'] for i in a.get('institutions', [])
                        if i.get('type') == 'education'} for a in authors]
        shared_list = len(authors) > 1 and len(institutions) > 1 and all(s == set(institutions) for s in author_sets)
        amended = {r['institution']['id']: r for r in corrections if r['doi'] == paper['doi']}
        institutions.update({identifier: row['institution'] for identifier, row in amended.items()})
        for identifier, institution in sorted(institutions.items()):
            pairs.append({'paper_id': paper['id'], 'doi': paper['doi'],
                          'institution_id': identifier, 'institution_name': institution['display_name'],
                          'ror': institution.get('ror') or '', 'country_code': institution.get('country_code') or '',
                          'source_work': work.get('id', ''), 'source_updated': work.get('updated_date', ''),
                          'affiliation_basis': amended[identifier]['evidence'] if identifier in amended else 'OpenAlex work-specific authorship metadata'})
        coverage.append({'paper_id': paper['id'], 'doi': paper['doi'], 'journal': paper['journal'],
                         'title': paper['title'], 'review_status': paper['review_status'],
                         'university_count': len(institutions), 'authorship_count': len(authors),
                         'authors_without_university': sum(not s for s in author_sets),
                         'shared_author_affiliation_list': shared_list,
                         'manual_affiliation_correction': bool(amended),
                         'affiliation_status': 'identified' if institutions else 'no_education_affiliation_identified',
                         'source_work': work.get('id', '')})
    save('paper_affiliations.csv', pairs)
    save('affiliation_coverage.csv', coverage)
    print(f'{len(coverage)} eligible papers; {sum(r["university_count"] > 0 for r in coverage)} with university affiliations')
    print(f'{len({r["institution_id"] for r in pairs})} distinct education institutions; {len(pairs)} paper-institution pairs')


if __name__ == '__main__':
    main()
