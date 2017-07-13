# pmt

# In the future I might rewrite this to work much better and not look like a hot mess, but for now, it's dead.

PPA Management Tool - Allows you to search, view, add, and remove Personal Package Archives. Run as root to add and remove ppa's and software packages. You can use this tool to see packages available from the ppa's you have installed and view additional info too.

Requires `lxml` and `bs4` (Beautifulsoup4) to scrape html. Install each with `pip3 install name`. Requires Python3 (probably 3.5+), and an Ubuntu based distribution. Tested on 16.04 - will likely work on 16.10+.

Run: `sudo python3 ppatool.py`, the `sudo` being optional for root privileges.

[PPA's can be dangerous.]( http://askubuntu.com/questions/35629/are-ppas-safe-to-add-to-my-system-and-what-are-some-red-flags-to-watch-out-fo )
