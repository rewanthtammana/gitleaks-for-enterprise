# Gitleaks for enterprise

Gitleaks is customized for use across multiple projects/enterprises. This project allows you to have a centralized detection rule management.

## Architecture

When we use Gitleaks with `"n"` number of projects, the architecture will be similar to below.

### With default gitleaks design

![Gitleaks-Default-Design.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1652714624519/7Tl6T_k-D.png)

### With customized gitleaks for enterprise design

![Gitleaks-For-Enterprises-Design.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1652714633471/wZ4day3ry.png)

## Disclaimer !

### base.toml

1. The `description` field in `base.toml` is mandatory & it should start with **"Rule: <id>"**
1. The `id` field in `[[rules]]` in `allowlist.toml` is mandatory & it should be an integer
1. **DO NOT** edit `id` field in `base.toml`. All the whitelisting/allowlist id are dependent on it

```toml
# Sample rule structure

[[rules]]
    description = "Rule 99: New rule description here"
    regex = '''newrule-regex-here'''
    tags = ["rule-tag-1", "rule-tag-2"]
```

### allowlist.toml

1. Except `commits`, all the below fields are `regex` matches.
1. The `id` field in `[[rules]]` is mandatory & it should be an integer
1. Folder structure
    1. rewanthtammana > gitleaks-demo-repo > allowlist.toml
    1. rewanthtammana > another-repo > allowlist.toml

```toml
# Rule specific allow lists
# Sample allowlist structure

[[rules]]
    id = "99"
    [rules.allowlist]
        commits = ["commit-id-here"]
        files = ['''keys/eGuardKey.id_dsa$''']
```

## Usage

* By default all detection rules are in in `base.toml`
* Save your allowlist rules in `allowlist/$USERNAME/$REPONAME/allowlist.toml`
* `python run.py <allowlist-path> > gitleaks.toml` - Combines your repo specific `allowlist.toml` & `base.toml` to generatee `gitleaks.toml` file
* Use the above generated `gitleaks.toml` as gitleaks repo scanning configuration file

```bash
python3 run.py allowlist/$USERNAME/$REPONAME/allowlist.toml > gitleaks.toml
gitleaks detect -c ./gitleaks.toml --source /path/to/repo -v
```

For further usage refer to, [https://github.com/zricethezav/gitleaks](https://github.com/zricethezav/gitleaks)

## Contribution

You can add new rules to `base.toml` file. It's parent file.

```toml
[[rules]]
    description = "Rule <id here>: AWS Secret Key"
    regex = '''(?i)aws(.{0,20})?(?-i)['\"][0-9a-zA-Z\/+]{40}['\"]'''
    tags = ["key", "AWS"]
```
  
## Installation

### Linux machine

```bash
pip install -r requirements.txt
pyinstaller run.py --onefile
./dist/run #This binary can also be used
```
