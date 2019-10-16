# t0txt

## Website

[txt.t0.vc](https://txt.t0.vc)

## Description

Command line pastebin.

This allows you to upload text notes from your command line or browser. A URL to the note is returned.

## Usage

`<command> | curl -F 'txt=<-' https://txt.t0.vc`

You can also upload from the web at [txt.t0.vc](https://txt.t0.vc).

## Example

```text
$ cat yourfile | curl -F 'txt=<-' https://txt.t0.vc
  https://txt.t0.vc/MOJV
$ firefox https://txt.t0.vc/MOJV
```

### Bash Alias

Add this to your .bashrc, then `source ~/.bashrc`:

```text
alias txt=" \
    sed -r 's/\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g' \
    | curl -F 'txt=<-' https://txt.t0.vc"
```

Now you can pipe directly into txt! Sed removes colours.

```text
$ cat yourfile | txt
  https://txt.t0.vc/MOJV
$ firefox https://txt.t0.vc/MOJV
```

## Self-hosting

Install dependencies:
```text
$ sudo apt install python3 python3-pip python-virtualenv python3-virtualenv
```

Clone repo, create a venv, activate it, and install:
```text
$ git clone https://github.com/tannercollin/t0txt.git
$ cd t0txt
$ virtualenv -p python3 env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
```

You can now run it directly:
```text
(env) $ python t0txt.py
```

It's recommended to run t0txt as its own Linux user, kept alive with [supervisor](https://pypi.org/project/supervisor/):
```text
[program:t0txt]
user=t0txt
directory=/home/t0txt/t0txt
command=/home/t0txt/t0txt/env/bin/python -u t0txt.py
autostart=true
autorestart=true
stderr_logfile=/var/log/t0txt.log
stderr_logfile_maxbytes=1MB
stdout_logfile=/var/log/t0txt.log
stdout_logfile_maxbytes=1MB
```

To expose t0txt to http / https, you should configure nginx to reverse proxy:
```text
server {
    listen 80;

    root /var/www/html;
    index index.html index.htm;

    server_name txt.t0.vc;

    location / {
        proxy_pass http://127.0.0.1:5002/;
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Then run `sudo certbot --nginx` and follow the prompts.

## See Also

Image host: [pic.t0.vc](https://pic.t0.vc) - [Source Code](https://github.com/tannercollin/t0pic)

Short URL: [url.t0.vc](https://url.t0.vc) - [Source Code](https://github.com/tannercollin/t0url)

## License
This program is free and open-source software licensed under the MIT License. Please see the `LICENSE` file for details.

That means you have the right to study, change, and distribute the software and source code to anyone and for any purpose. You deserve these rights. Please take advantage of them because I like pull requests and would love to see this code put to use.

## Acknowledgements

This project was inspired by [sprunge.us](http://sprunge.us/), which kept going down.

Thanks to all the devs behind Flask and Python.
