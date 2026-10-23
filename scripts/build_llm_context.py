"""Build a portable text context from explicit course files and resource metadata.

Uses Python's standard library. Does not execute notebooks, fetch URLs, or copy
third-party full texts. Paths in course.json are relative to the repository root.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def safe_path(relative):
    path = (ROOT / relative).resolve()
    path.relative_to(ROOT)
    if not path.is_file():
        raise ValueError(f'Missing context source: {relative}')
    return path


def build():
    manifest = json.loads((ROOT / 'course.json').read_text())
    parts = [
        '# BADM 534: Portable Course Context\n\n'
        'Generated from course.json and the source files identified below. '
        'This file contains course navigation and original catalog annotations, '
        'not the complete contents of the linked readings. '
        'Source documents take precedence over this generated copy.\n',
        '## Source: course.json\n\n```json\n' + json.dumps(manifest, indent=2) + '\n```\n'
    ]
    for relative in manifest['llm_context_paths']:
        parts.append(f'## Source: {relative}\n\n' + safe_path(relative).read_text().strip() + '\n')
    for catalog in manifest['catalogs']:
        data = json.loads(safe_path(catalog['path']).read_text())
        resources = data['resources']
        parts.append(f"## Resource Metadata: {catalog['namespace']}\n\n"
                     f"Source: {catalog['path']}\n\n"
                     f"{len(resources)} entries. Overlap with other catalogs is possible. "
                     'Recommendations are not assigned readings. Consult each source for full details.\n')
        for r in resources:
            modules = r.get('modules') or []
            fields = [
                f"### {catalog['namespace']}:{r['id']} | {r['title']}",
                f"Source URL: {r['url']}",
                'Modules: ' + ', '.join(modules),
                f"Priority: {r.get('priority', 'unspecified')}",
            ]
            for label, keys in [
                ('Focus', ['focus', 'summary']),
                ('Teaching Suggestion', ['teaching_use', 'wiki_use']),
                ('Cautions', ['cautions', 'notes']),
                ('Rights or Access', ['rights', 'access'])
            ]:
                values = [r[k] for k in keys if r.get(k)]
                if values:
                    rendered = '; '.join(v if isinstance(v, str) else json.dumps(v, ensure_ascii=False) for v in values)
                    fields.append(label + ': ' + rendered)
            parts.append('\n\n'.join(fields) + '\n')
    output = '\n---\n\n'.join(parts)
    (ROOT / 'llms-full.txt').write_text(output)
    print(f'Built llms-full.txt: {len(output.encode()):,} bytes, {len(parts)} source sections')


if __name__ == '__main__':
    build()
