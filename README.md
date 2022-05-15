# Gitleaks for enterprise

Gitleaks customized for enterprise usage. This project allows you to have a centralized rule management.

## Disclaimer !

1. The `description` field in `base.toml` is mandatory & it should start with **Rule: <id>**
1. The `id` field in `[[rules]]` in `allowlist.toml` is mandatory & it should be an integer

## Usage

* Save base/matching rule set in `base.toml`
* Save allow list rule set in `allowlist.toml`
* `python run.py` - This generates `gitleaks.toml` file
* Use the above generated `gitleaks.toml` as gitleaks repo scanning configuration file

```bash
python3 run.py
gitleaks detect -c ./gitleaks.toml --source /path/to/repo
```

For further usage refer to, [https://github.com/zricethezav/gitleaks](https://github.com/zricethezav/gitleaks)

## Installation

### Linux machine

```bash
pip install -r requirements.txt
pyinstaller run.py --onefile
./dist/run
```
