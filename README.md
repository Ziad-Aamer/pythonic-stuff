## Linux
### Install Python and pip
```
sudo apt-get update
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get install python3.12 python3.12-venv python3.12-dev

# install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.12 get-pip.py

```

### Virtual Environment
```
# Create a virtual environment
python -m venv .venv

# Enter the environment
source .venv/bin/activate

# exit the environment
deactivate
```
