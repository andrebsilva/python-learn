
# Python Learning Codes

## Python virtual Environment for Ubuntu 22.04 LTS

### Prerequisites

Before you get started, let's install or update your python virtual environment:

```bash
# Install python 3.10
sudo apt install python3.10

# Version of the python
python --version

# or 
python3 --version

# Install pip 
sudo apt install pip

# Version of the pip
pip --version

# Update pip:
sudo pip install --upgrade pip

# Instal virtual environment:
sudo pip install virtualenv virtualenvwrapper

# Edit configuration file:
sudo nano ~/.bashrc

# At the end of file:
    # Virtual Environment
    export WORKON_HOME=$HOME/.virtualenvs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    source /usr/local/bin/virtualenvwrapper.sh

# Restart bash terminal.
source ~/.bashrc

# Create a new virtual envirment: tenv (Test Environment)
mkvirtualenv tenv

# Create a new specifying the python path: tenv
mkvirtualenv tenv -p /usr/bin/python3.9

# Deactivate tenv:
deactivate

#Activate tenv
workon tenv

# Remove tenv
rmvirtualenv tenv

# Open python console
python

    # Easter egg
    >>> import this

    ```
