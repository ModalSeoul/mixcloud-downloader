import requests
import os
from lxml import html
from random import randint


"""
Mixcloud is basically a place for people to post
their music. It's essentially just Soundcloud. If you
play a song and look at your network requests, you'll
see you eventually hit a .m4a file on their stream3
sub-domain. The file has a seemingly random path,
and the file name is a randomly-generated ID.
The .m4a files are all in the same initial path -
/c/m4a/64/. The filename is {}.m4a. {} being the same
filename as the preview mp3 that is pulled from
Mixcloud's HTML.

This has been forwarded to Mixcloud. If you want,
you can go as far as to find the endpoints they have
that contain song splices for each mix. These endpoints
contain what song plays(title, artist) at X seconds in a mix.
Endpoints also contain kb/s of each mix, so you can modify this
script to download individual songs from mixes and name them
accordingly. Of course, that'd be immoral.
"""


# Constants
_STREAM = 'https://stream3.mixcloud.com/c/m4a/64/'
URL = 'http://mixcloud.com'

# Initial request
r = requests.get(URL)
tree = html.fromstring(r.content)
buyers = tree.xpath('.//span[contains(@class, m-preview)]')


def download_m4a(m4a):
    file_name = '{}{}'.format(str(randint(1000, 9000)), '.m4a')
    with open(file_name, 'wb') as mix:
        resp = requests.get(m4a, stream=True)

        if not resp.ok:
            print('Request to the .m4a file failed. Attempted url was %' % m4a)

        for data in resp.iter_content(1024):
            mix.write(data)


def parse_preview(preview_url):
    parse = preview_url.split('previews')[1].split('.mp3')[0]
    m4a = '{}{}.m4a'.format(_STREAM, parse)
    download_m4a(m4a)


def preview_loop():
    for buyer in buyers:
        for item in buyer.items():
            if '.mp3' in str(item):
                parse_preview(item[1])

preview_loop()
