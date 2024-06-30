import sys
import shelve

if len(sys.argv) < 2:
    print('Please give the note ID to delete.')
    print('Example: python misc/delete.py IEGA')
    exit()
else:
    del_id = sys.argv[1]

print('Deleting note:', del_id)

with shelve.open('data/t0txt') as db:
    if del_id not in db:
        print('Not found.')
        exit()

    print('Contents:')
    print(db[del_id])

    print()
    print('Enter to confirm, ctrl-c to cancel')
    input()

    del db[del_id]

    print('done.')
