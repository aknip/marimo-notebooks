# Start

## Run in Gitpod
https://gitpod.io/#https://github.com/aknip/marimo-notebooks

Read more about how to use Jupyter Notebooks with Gitpod in [the documentation.](https://www.gitpod.io/docs/references/ides-and-editors/jupyter-notebooks)


## Virtual environment using uv
- Install: curl -LsSf https://astral.sh/uv/install.sh | sh
- Create a virtual environment in current dir in folder .venv.
	- `uv venv`
- Activate environment
	- `source .venv/bin/activate`
- Deactivate environment
	- `deactivate`

## Install dependencies

uv pip install -r requirements.txt


# Start marimo

marimo edit 
marimo edit hello-world-marimo.py

# Run as app
marimo run hello-world-marimo.py

# Run as script from CLI
python hello-world-marimo.py

# Run / Deploy as Docker
https://docs.marimo.io/guides/deploying/deploying_docker.html

or via FastAPI App: https://docs.marimo.io/guides/deploying/programmatically.html





# Notes

tasks:
  - name: Setup
    init: > 
        curl -LsSf https://astral.sh/uv/install.sh | sh && 
        uv venv && source .venv/bin/activate && 
        uv pip install -r requirements.txt &&
        gp sync-done initSetup
    command: gp open README.md && gp open CrewAi.ipynb && marimo edit hello-world-marimo.py

  #- name: Marimo
  #  init: gp sync-await initSetup # wait for the above defined 'initSetup' to finish
  #  command: marimo edit hello-world-marimo.py
  #  openMode: split-right

vscode:
  extensions:
    - ms-python.python
    - ms-toolsai.jupyter
    - ms-toolsai.jupyter-keymap
    - ms-toolsai.jupyter-renderers