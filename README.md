SublimeLinter-contrib-brew
==========================

[![The MIT License](https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square)](http://opensource.org/licenses/MIT)
[![Package Control](https://packagecontrol.herokuapp.com/downloads/SublimeLinter-contrib-brew.svg?style=flat-square)](https://packagecontrol.io/packages/SublimeLinter-contrib-brew)
[![GitHub](https://img.shields.io/github/release/idleberg/SublimeLinter-contrib-brew.svg?style=flat-square)](https://github.com/idleberg/SublimeLinter-contrib-brew/releases)
[![Travis CI](https://img.shields.io/travis/idleberg/SublimeLinter-contrib-brew/master.svg?style=flat-square)](https://travis-ci.org/idleberg/SublimeLinter-contrib-brew)

This linter plugin for [SublimeLinter][docs] provides an interface to [brew](https://brew.sh/). It will be used with Homebrew formulas.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that Homebrew is installed on your system. Visit the developer's [website](https://brew.sh/) and follow the installation steps.

### Linter configuration
In order for `brew` to be executed by SublimeLinter, you must [ensure that its path is available][path] to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `brew`, you can proceed to install the SublimeLinter-contrib-brew plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `brew`. Among the entries you should see `SublimeLinter-contrib-brew`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[path]: http://superuser.com/a/284351/195953
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
