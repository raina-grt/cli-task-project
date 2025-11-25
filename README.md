# cli-task-project
https://roadmap.sh/projects/task-tracker
A command line interface task tracking app, conditional argument with cool features



\# CLI Task Manager



A lightweight, feature-rich command-line task tracker built with Python.



\## Features

\- Add tasks with title, priority, status, time, and description  

\- Update any task field  

\- Mark tasks as `todo` • `in-progress` • `done`  

\- Delete tasks  

\- List all tasks or filter by status (`list done`, `list in-progress`, etc.)  

\- Auto-save to `tasks.json`  

\- Automatic created/updated timestamps  

\- Clean table output with emojis and colors



\## Installation

```bash

git clone https://github.com/raina-grt/cli-task-project.git

cd cli-task-project

python -m venv .venv

.\\.venv\\Scripts\\activate    # Windows

\# source .venv/bin/activate # macOS / Linux

USAGE

# Show help

python taskproj.py --help



\# Examples

python taskproj.py add "Finish CLI project"

python taskproj.py list

python taskproj.py list done

python taskproj.py update 1

python taskproj.py in-progress 3

python taskproj.py done 5

python taskproj.py delete 2

Project Structure

cli-task-project/

├── taskproj.py      # main script

├── tasks.json       # auto-generated storage

├── .gitignore

└── README.md

''Built by raina-grt

Simple today. AI-powered tomorrow.''

https://roadmap.sh/projects/task-tracker