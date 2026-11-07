#!/usr/bin/env python3
"""A temporary fix. Python 3, no dependencies. Ctrl+C to leave it running elsewhere."""
import argparse
import sys
import time

EVENTS = [
    ('2022', 'Added temporary fix', 'remove next sprint', 1.6),
    ('2023', 'Replaced frontend', 'temporary fix retained', 1.3),
    ('2024', 'Migrated database', 'temporary fix retained', 1.3),
    ('2025', 'Rebuilt backend', 'temporary fix retained', 1.3),
    ('2026', 'Tried removing temporary fix', 'everything stopped', 2.0),
    ('2026', 'Restored temporary fix', 'architecture decision', 3.8),
]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fast', action='store_true', help='skip the dramatic pauses')
    args = parser.parse_args()
    print('system.log\n', flush=True)
    for year, action, note, pause in EVENTS:
        print(f'{year}  {action}', flush=True)
        if sys.stdout.isatty() and not args.fast:
            time.sleep(pause)
    print('\n# architecture decision')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nTemporary fix unaffected.')
