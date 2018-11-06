[![license](https://img.shields.io/badge/license-MPL%202.0-blue.svg)](https://github.com/davehunt/fxtbootstrap/blob/master/LICENSE.txt)
[![Build Status](https://travis-ci.org/davehunt/fxbootstrap.svg?branch=master)](https://travis-ci.org/davehunt/fxbootstrap)
[![updates](https://api.dependabot.com/badges/status?host=github&repo=davehunt/fxbootstrap)](https://dependabot.com)
[![style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# fxbootstrap

A simple command line tool for launching Firefox with a temporary profile.

## Installation

```
$ pip install fxbootstrap
```

## Launching Firefox

Running `fxbootstrap` will download and install the latest Firefox Nightly for your
platform to a temporary directory. It will then generate a clean profile and launch
Firefox using the new profile.

```
$ fxbootstrap
✔ Downloaded Firefox to /var/folders/wz/3v_j7g2n2zx_q6qs8g7vmyg00000gn/T/tmpg_WfUI/2018-11-05-22-01-07-mozilla-central-firefox-65.0a1.en-US.mac.dmg
✔ Installed Firefox in /private/var/folders/wz/3v_j7g2n2zx_q6qs8g7vmyg00000gn/T/tmpg_WfUI/Firefox Nightly.app
✔ Generated profile at /var/folders/wz/3v_j7g2n2zx_q6qs8g7vmyg00000gn/T/tmpRZox06.mozrunner
🦊 Running Firefox Nightly 65.0a1 (20181105220107)
```

After closing Firefox, the temporary directory containing the binary, installation,
and the profile will be deleted.

## Installing add-ons

Add-ons can be installed into the Firefox instance by passing one or more
paths to XPI file(s) on the command line:

```
$ pipenv run fxbootstrap --addon fbcontainer.xpi --addon fxlightbeam.xpi
```

# Resources

- [Release Notes](http://github.com/davehunt/fxbootstrap/blob/master/CHANGES.md)
- [Issue Tracker](http://github.com/davehunt/fxbootstrap/issues)
- [Code](http://github.com/davehunt/fxbootstrap)
