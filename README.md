# Mixcloud Downloader
+ Author: [@ModalSeoul](https://twitter.com/ModalSeoul)
+ Date: June 22nd, 2016

# Requires the following Python modules:
+ requests
+ lxml
+ random

# Description(also in main.py)
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
