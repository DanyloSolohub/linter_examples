git clone https://github.com/DanyloSolohub/linter_examples.git

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

pre-commit install

pre-commit install --hook-type prepare-commit-msg
