import shelve
import random

WHITELIST = ['t0.vc', 'tanner', 'protospace', 'seed combinations', 'tcoins in circulation', 'pokemon trade', 'pokemon battle', 'unique in collection', '%) left.', 'telethon', 'datetime', ' +0000', 'print(', 'console.log', 'systemd', '-Iinclude', 'BOOT_IMAGE', '#endif', '/bin/bash', 'python3.', 'stdio.h']

db = shelve.open('data/t0txt')

keys = list(db.keys())

while True:
    while True:
        note_id = random.choice(keys)
        note = db[note_id]

        for good_word in WHITELIST:
            if good_word in note.lower():
                break
        else: #for
            break

    print(note)

    num_http = note.count('http')
    num_line = note.count('\n')

    print('num http:', num_http, 'lines:', num_line, 'ratio:', num_http / num_line if num_line else 'inf')

    input()
