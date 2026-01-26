## Requirements

### Windows (recommended via Chocolatey)

Install Chocolatey:
https://chocolatey.org/install

Then run:
Install OpenJDK 25 (or newer) — this is the JDK used for building plugins.

choco install -y openjdk maven python git

Install cookiecutter:
pip install cookiecutter

### Linux / WSL2 (Ubuntu)

sudo apt update
sudo apt install -y openjdk-21-jdk maven python3 python3-pip git
pip install cookiecutter