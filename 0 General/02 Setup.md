# Setup

This document contains an overview for the software setup for the course. Please try to get as much done as possible before the course starts, but we'll also go over the setup on the first day of class to ensure everyone's up to speed.

## Opening the CLI

CLI stands for 'command-line interface', and it was the only way to use a computer before the development of GUIs 'graphical user interface'. It's still used to perform many computer operations that go 'under the hood'.

In **OSX**, the default CLI is called `Terminal`, which you can find by typing `terminal` in search, or under `Finder -> Applications -> Utilities`.

In **Windows**, the default CLI is `cmd`, which you can find by typing `cmd` in search, or pressing `Windows+R`, typing `cmd`, and hitting `enter`. This will work for executing python, but there's no syntax highlighting and some commands like `ls` and `rm` won't work in `cmd`. A much better CLI is [Cmder](http://cmder.net/). Another option is [Powershell](https://msdn.microsoft.com/en-us/powershell/scripting/setup/installing-windows-powershell).

In **Linux**, you can open a terminal with `Ctrl + Alt + T`.

**Visual Studio Code** also has a terminal built in, which you can access with `ctrl+j` or using the main menu `Terminal -> New Terminal`.

### Common CLI Commands

- `pwd` displays the path of the current directory
- `ls` lists the contents of the current directory
- `cd <directory_name>` change directory
  - `cd ..` will bring you into the parent directory
  - `cd` alone will return you to your 'home' directory
- `mkdir <foldername>` create a new folder
- `rmdir <foldername>` removes a folder
- `rm <filename>` removes a file
- `mv filename1 filename2` moves or renames a file
- `cp filename1 filename2` copies a file
- `up-arrow` will bring up the last command entered
- `tab` will attempt to autocomplete whatever you're typing, which is helpful for long file and directory names. Try typing the first letter of a file name and hit tab to complete the rest.
- `ctrl+c` kill currently running process
- `touch file.txt` creates a file
- `echo "Hello World!" >> hello_world.txt` will create a file with "Hello World!" as the contents

## Install the latest version of Python

Python is a popular programming language we'll be using throughout the course, and we'll be using a python interpreter in order to run our code. You can find a page with insructions to download and install Python [here](https://www.python.org/downloads/). You can find more info in [our docs](../1%20Python/01%20-%20Overview.md) and [official docs](https://docs.python.org/3/using/cmdline.html). If you're on Windows be sure to select "add python to path" when installing. You can check whether the installation was successful by running `python --version` on Windows or `python3 --version` on Mac. If the command isn't recognized you'll have to add the path to the interpreter to your system `PATH`, guide for [Windows](https://superuser.com/questions/143119/how-do-i-add-python-to-the-windows-path) and [Mac](https://stackoverflow.com/questions/3387695/add-to-python-path-mac-os-x).

## Install Git and make a GitHub account

Git is a version control system, it keeps tracks of changes to files to allow developers to undo changes and collaborate on projects. You can download Git [here](https://git-scm.com/downloads). You can check whether the installation was successful by running `git` in a terminal which should show a list of commands.

GitHub is a hosting service for Git repositories. You can create an account [here](https://github.com/join). Our class will have a repository hosted there we'll collaborate on. It also serves as a programmer's portfolio, potential employers can see your activity and code you commit, so make sure you commit changes regularly and only commit clean, working code.

## Install an Editor

### Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) is the recommended editor, in addition to syntax highlighting it's also got a debugger and git integration.

- [editing guide](https://code.visualstudio.com/docs/editor/codebasics)
- [shortcut cheat sheet](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf), and [this list](https://medium.com/better-programming/20-vs-code-shortcuts-for-fast-coding-cheatsheet-10b0e72fd5d)
- [Guide to Python](https://code.visualstudio.com/docs/python/python-tutorial)
- [Guide to Flask](https://code.visualstudio.com/docs/python/tutorial-flask)
- [Guide to Django](https://code.visualstudio.com/docs/python/tutorial-django).

#### Shortcuts

| Command                | Windows            | Mac               |
| ---------------------- | ------------------ | ----------------- |
| Toggle Comment         | `ctrl + /`         | `cmd + /`         |
| Indent Block of Text   | `tab`              | `tab`             |
| Unindent Block of Text | `shift + tab`      | `shift + tab`     |
| Move line up/down      | `alt + up/down`    | `opt + up/down`   |
| Select matching text   | `ctrl + d`         | `cmd + d`         |
| Open/Close sidebar     | `ctrl + b`         | `cmd + b`         |
| File Switcher          | `ctrl + p`         | `cmd + p`         |
| Command Pallet         | `ctrl + shift + p` | `cmd + shift + p` |

#### My setup:

- You can change the color scheme easily `File -> Preferences -> Color Theme` (`Code -> Preferences -> Color Theme` on mac). I am using the Min Light Theme.
- If you don't like the suggestions popping up when you type, you can turn them off `File -> Preferences -> Settings`, search for "parameter hints enabled", and uncheck the checkbox. You can still open suggestions manually with `ctrl + space`.
- Other things I change in settings: disable minimap, disable breadcrumbs, and I prefer my sidebar on the right, this keeps code from jumping around when you open/close the sidebar.

#### Recommended Extensions

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Visual Studio IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)
- [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens)
- [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare)
- [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)


#### Shortcuts

You can find a list of shortcuts [here](https://github.com/nwinkler/atom-keyboard-shortcuts)

- `ctrl + /` toggle comment
- `tab` indent a block of text, `shift + tab` to unindent
- `ctrl + d` select matching text, useful for renaming variables, `ctrl + u` to unselect
- `ctrl + up/down` move a line of text up and down
- `ctrl + shift/cmd + d` duplicate a line of text
- `tab` for autocomplete, e.g. type "html" and hit `tab` to get a stock html page

#### Recommended Extensions

You install and remove packages by going to `File -> Settings -> Packages/Install`.

- [Beautify](https://atom.io/packages/atom-beautify) will make your code pretty.
- [Emmet](https://atom.io/packages/emmet) gives more advanced autocomplete features.
- [Teletype](https://teletype.atom.io/) for collaborating with others.

## Install Slack

Slack is an instant messaging service we'll use to communicate. If you send me an email `sarah@pdxcodeguild.com` I can send you an invite to PDX Code Guild's Slack. You can use Slack in a browser, but it can also be installed as a desktop and mobile app.

- Desktop: [Windows](https://slack.com/downloads/windows), [Mac](https://slack.com/downloads/mac), [Linux](https://slack.com/downloads/linux)
- Mobile: [Android](https://slack.com/downloads/android), [iOS](https://slack.com/downloads/ios)

## Pick a Browser

[Chrome](https://www.google.com/chrome/), [Firefox](https://www.mozilla.org/en-US/firefox/new/) and [Safari](https://www.apple.com/safari/) are all excellent choices. When developing on the front-end (HTML, CSS, & JavaScript) it's best to test on the most popular browsers, you can find statistics on popularity [here](https://en.wikipedia.org/wiki/Usage_share_of_web_browsers#Summary_tables).

## Zoom

[Zoom](https://zoom.us/) is a video chatting service we'll be using to hold class online. I'll post a link to each day's meeting in our Slack channel. Students are required to have their video on the majority of the time to ensure they're engaged, but if you're concerned about privacy you can set a "virtual background" by clicking the arrow next to the video icon and selecting "choose virtual background". You can find some free backgrounds [here](https://www.shutterstock.com/discover/free-virtual-backgrounds). You're also welcome to mute yourself if you're not talking to cut down on background noise. Zoom also allows people to share their screens. If the top panel is getting in your way while sharing your screen, click the ellipses (...) and select "hide floating media controls".

## A Full Test

1. Navigate to our class repository on github in your browser.
2. Locate the green `Code` button. In the dropdown make sure you have HTTPS selected and copy the link.
3. In your terminal navigate to a folder where you would like to keep your work.
4. Enter `git clone` into your terminal then paste the link you copied earlier.
5. Press `enter` or `return` and you should see the repository being downloaded you your machine.
6. `cd` into the newly created folder and open VS Code. You should be able to type `code .` to open VS Code in the current folder.
7. Locate the Code folder and create the following file structure: `Code/YourName/Python`. This is where all of your python labs will go. In the future you will create a folder for HTML-CSS, Django, Javascript.
8. Inside the Python folder create `1-hello_world.py`, write `print('Hello World!')` inside the file and save it.
9. In your terminal, navigate to the newly created python folder and run `python 1-hello_world.py` (`python3` for mac). You should see "Hello World!" in the terminal.
10. `git pull`
11. `git add 1-hello_world.py`
12. `git commit -m "added hello world"`
13. `git push`
14. Go to the repository in your browser and you should see your file.
