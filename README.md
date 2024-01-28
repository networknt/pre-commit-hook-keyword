# pre-commit-hook-keyword
A pre-commit hook to scan sensitive keywords passed from the command line argument


## Installation

To install, just add the hook to your `.pre-commit-config.yaml`:

```yaml
repos:
-   repo: https://github.com/networknt/pre-commit-hook-keyword
    rev: master
    hooks:
    - id: keywordscan
      args: ["--keywords=abcdef,opqrst,uvwxyz"]
```
