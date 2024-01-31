# pre-commit-hook-keyword
A pre-commit hook to scan sensitive keywords passed from the command line argument

## Use Cases

For all the GitHub public repoistories, source code can be viewed and modified with pull requests. To ensure that there is no sensitive information in the checked in source code, a keyword based scanner is must to automate this process. 

## Prerequisite

To run the pre-commit hooks locally, we need to install the pre-commit application. I am using Linux and the following command will install it. 

```
pip install pre-commit
```

## Installation

To install, just add the hook to your `.pre-commit-config.yaml` in your repository

```yaml
repos:
-   repo: https://github.com/networknt/pre-commit-hook-keyword
    rev: 356f23a9acfcc8ac12697412e886483d2125cccd
    hooks:
    - id: keywordscan
      args: ["--keywords=abcdef,opqrst,uvwxyz"]
      types: ["text"]
```

If you haven't install the pre-commit, you can install it with the following command in your repository folder.

```
pre-commit install
```

The above command will create a pre-commit executable file in .git/hooks folder in the repository. 

## Local

Once the pre-commit application is install on your computer, and pre-commit hook is installed in your repository folder, each local commit triggers the hook to ensure that there is no sensitive info in the commited files.

Here is an example.

```
steve@lucky:~/networknt/light-runbook$ git commit -m "update test"
Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Failed
- hook id: end-of-file-fixer
- exit code: 1
- files were modified by this hook

Fixing test.md

Check Yaml...........................................(no files to check)Skipped
Check for added large files..............................................Passed
KeywordScan..............................................................Failed
- hook id: keywordscan
- exit code: 1

Keyword 'abcdef' found in test.md at line 2: abcdefg and opqrst are my customers.
Keyword 'opqrst' found in test.md at line 2: abcdefg and opqrst are my customers.
Keyword 'abcdef' found in test.md at line 3: ABCDEF
Keyword 'xyzuvw' found in test.md at line 4: xYzuvw
Keyword 'abcdef' found in test.md at line 6: ABCdef

```

You can also trigger the scanner with the following command. 

```
steve@lucky:~/networknt/light-runbook$ pre-commit run --all-files
Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Passed
Check Yaml...............................................................Passed
Check for added large files..............................................Passed
KeywordScan..............................................................Failed
- hook id: keywordscan
- exit code: 1

Keyword 'abcdef' found in test.md at line 2: abcdefg and opqrst are my customers.
Keyword 'opqrst' found in test.md at line 2: abcdefg and opqrst are my customers.
Keyword 'abcdef' found in test.md at line 3: ABCDEF
Keyword 'xyzuvw' found in test.md at line 4: xYzuvw
Keyword 'abcdef' found in test.md at line 6: ABCdef

```

Sometimes, you want to check in something that contains sensitive keyword to overwrite the keyword scanner rules. If that is the case, you can use the following command to commit locally. 


```
git commit -m "update" --no-verify
```

## GitHub CI

With the above local pre-commit, we can ensure that sensitive info is not commited locally. However, as there are many developers for the project, we cannot guarantee all developers install the pre-commit locally. We need the second level scanner on the GitHub for the pre-commit hook for the pull requests.

The developer behind the pre-commit offer a free CI integration on GitHub to run the pre-commit hooks on the server. We just need to enable the CI access for our repositories. There is no extra setup, the same .pre-commit-config.yaml used locally will be used for the CI to trigger the hooks on the server.



