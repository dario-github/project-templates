sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y

sudo apt install python3.10 -y
sudo apt install python3-pip -y
sudo apt-get install python3.10-distutils -y
sudo curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10

python3.10 -m pip install --upgrade pip
python3.10 -m pip install --upgrade wheel
python3.10 -m pip install --upgrade setuptools

python3.10 -m pip install --upgrade requests
python3.10 -m pip install --ignore-installed poetry
python3.10 -m poetry env use /usr/bin/python3.10
python3.10 -m poetry install
