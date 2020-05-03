import shelve

db = shelve.open('t0txt')

new = shelve.open('new')

for k in db.keys():
    try:
        note = db[k]
    except:
        print('error', k)
        continue

    if not note and not isinstance(note, str):
        print('bad', k)
        continue

    if k == 'HVQH':
        continue
    
    new[k] = note
