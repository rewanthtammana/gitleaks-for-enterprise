# Gitleaks for enterprise

Gitleaks customized for enterprise usage. This project allows you to have a centralized rule management.

## Usage

* Save base/matching rule set in `base.toml`
* Save allow list rule set in `allowlist.toml`
* `python run.py > gitleaks.toml`
* Use the above generated `gitleaks.toml` file to perform the operations

```bash
docker run -v ${PWD}:/my-repo zricethezav/gitleaks:latest --path="/my-repo" --repo-config-path="./gitleaks.toml"
```

For further usage refer to, [https://github.com/zricethezav/gitleaks](https://github.com/zricethezav/gitleaks)
