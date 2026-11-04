"""Build an importable iCalendar file from the confirmed course meeting dates.

Uses Python's standard library. Each meeting has its own stable UID and topic.
America/Chicago local times are converted to UTC separately for each date so
class remains at 15:30 through the daylight-saving transition.
"""
from datetime import datetime, timezone
from pathlib import Path
from uuid import NAMESPACE_URL, uuid5
from zoneinfo import ZoneInfo
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
REPO = 'https://github.com/nene88991999/BADM534-Marketing-Analytics'


def text(value):
    return str(value).replace('\\', '\\\\').replace('\n', r'\n').replace(';', r'\;').replace(',', r'\,')


def fold(line):
    """Fold at 75 UTF-8 octets, counting the continuation's leading space."""
    chunks = []; current = ''
    for char in line:
        if len((current + char).encode('utf-8')) > 75:
            chunks.append(current); current = ' '
        current += char
    chunks.append(current)
    return '\r\n'.join(chunks)


def main():
    course = json.loads((ROOT / 'course.json').read_text())
    plan = json.loads((ROOT / '05_Slides/session_plan.json').read_text())
    meeting = course['meeting']
    assert meeting['dates'] == [s['date'] for s in plan['sessions']]
    assert not set(meeting['dates']) & {d['date'] for d in meeting['no_class_dates']}
    zone = ZoneInfo(meeting['timezone'])
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    lines = ['BEGIN:VCALENDAR', 'VERSION:2.0',
             'PRODID:-//Nathan Yang//Marketing Analytics//EN',
             'CALSCALE:GREGORIAN',
             'X-WR-CALNAME:' + text(course['title'] + ' - ' + course['term']),
             'X-WR-TIMEZONE:' + meeting['timezone']]
    for session in plan['sessions']:
        day = session['date']
        start = datetime.fromisoformat(day + 'T' + meeting['start_time']).replace(tzinfo=zone)
        end = datetime.fromisoformat(day + 'T' + meeting['end_time']).replace(tzinfo=zone)
        assert start.weekday() == 2 and (end-start).total_seconds() == 170*60
        uid = str(uuid5(NAMESPACE_URL, REPO + '/' + meeting['crn'] + '/' + day))
        description = (f"Session {session['session']:02d}: {session['title']}\n"
                       f"Module: {session['modules']}\n"
                       f"Instructor: {course['instructor']}\n"
                       f"Email: {course['instructor_email']}\n"
                       f"Office hours: {course['office_hours']}\n"
                       f"Class time: 15:30-18:20 America/Chicago\n"
                       f"Session materials: {REPO}/blob/main/05_Slides/{session['companion']}")
        if session['session'] in course['planning_assumptions']['presentation_meetings']:
            description += '\nPresentation requirements will be specified separately.'
        lines += ['BEGIN:VEVENT', 'UID:' + uid, 'DTSTAMP:' + stamp,
                  'DTSTART:' + start.astimezone(timezone.utc).strftime('%Y%m%dT%H%M%SZ'),
                  'DTEND:' + end.astimezone(timezone.utc).strftime('%Y%m%dT%H%M%SZ'),
                  'SUMMARY:' + text(f"{course['title']} - Session {session['session']:02d}: {session['title']}"),
                  'LOCATION:' + text(meeting['building'] + ', Room ' + meeting['room']),
                  'DESCRIPTION:' + text(description),
                  'URL:' + REPO + '/blob/main/' + course['current_syllabus'],
                  'STATUS:CONFIRMED', 'TRANSP:OPAQUE', 'END:VEVENT']
    lines.append('END:VCALENDAR')
    output = HERE / 'Marketing_Analytics_Spring_2027.ics'
    output.write_bytes(('\r\n'.join(fold(line) for line in lines) + '\r\n').encode('utf-8'))
    print(f'Wrote {len(plan["sessions"])} events: {output}')


if __name__ == '__main__':
    main()
