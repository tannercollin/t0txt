# t0txt - txt.t0.vc
# MIT License

import random
import shelve
import string

from flask import abort, Flask, request, redirect

DB = 'data/t0txt'
PORT = 5002
URL = 'https://txt.t0.vc'
POST = 'txt'

def help():
    form = (
        '<form action="{0}" method="POST" accept-charset="UTF-8">'
	'<input name="web" type="hidden" value="true">'
        '<input name="name" style="border: none;">'
        '<br><textarea name="{1}" cols="60" rows="18"></textarea>'
        '<br>CAPTCHA: Who owns this site? <input name="captcha">'
        '<br><button type="submit">Submit</button></form>'.format(URL, POST)
    )
    return """
<meta name="color-scheme" content="light dark" />
<meta name="viewport" content="width=1%" />
<pre>
                        txt.t0.vc
NAME
    t0txt: command line pastebin.

USAGE
    &lt;command&gt; | curl -F '{0}=&lt;-' {1}
    or upload from the web:
{2}

DESCRIPTION
    I got sick of sprunge.us always going down, so I built this

EXAMPLES
    ~$ cat yourfile | curl -F '{0}=&lt;-' {1}
       {1}/MOJV
    ~$ firefox {1}/MOJV

    Add this to your .bashrc:

    alias {0}=" \\
    sed -r 's/\x1B\[([0-9]{{1,2}}(;[0-9]{{1,2}})?)?[m|K]//g' \\
    | curl -F '{0}=<-' {1}"

    Now you can pipe directly into {0}! Sed removes colours.

SOURCE CODE
    https://txt.t0.vc/GPBV
    https://github.com/tannercollin/t0txt

SEE ALSO
    https://pic.t0.vc
    https://url.t0.vc
    http://github.com/rupa/sprunge
</pre>""".format(POST, URL, form)

def new_id():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(4))

flask_app = Flask(__name__)

@flask_app.route('/', methods=['GET'])
def index():
    return '<html><body>{}</body></html>'.format(help())

@flask_app.route('/', methods=['POST'])
def new():
    print()
    try:
        is_web = 'web' in request.form

        name = request.form.get('name', None)
        if name:
            # TODO: fail if name field is filled out
            print('Name filled out:', name)

        captcha = request.form.get('captcha', None)
        if is_web and 'tanner' not in captcha.lower() and 'collin' not in captcha.lower():
            print('Captcha failed:', captcha)
            return redirect('https://txt.t0.vc/LPPZ')
        else:
            print('Captcha passed:', captcha)

        with shelve.open(DB) as db:
            nid = new_id()
            while nid in db:
                nid = new_id()

            txt = request.form['txt']

            if not txt:
                print('Note is empty.')
                raise
            if len(txt) > 250000:
                print('Note too large.')
                raise

            db[nid] = txt

        print('Adding note {} via {}:\n{}'.format(nid, 'web' if is_web else 'api', txt))

        url = '{}/{}'.format(URL, nid)

        if is_web:
            return redirect(url)
        else:
            return url + '\n'
    except:
        abort(400)

@flask_app.route('/<nid>', methods=['GET'])
@flask_app.route('/<nid>/<filename>', methods=['GET'])
def get(nid, filename=None):
    try:
        with shelve.open(DB) as db:
            return db[nid] + '\n', 200, {'Content-Type': 'text/plain; charset=utf-8'}
    except:
        abort(404)

flask_app.run(port=PORT)
