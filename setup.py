from setuptools import setup

setup(
    name="pre_commit_hook_keyword",
    version="1.0.0",
    packages=["keywordscan"],
    entry_points={"console_scripts": ["keywordscan=keywordscan.cli:main"]},
)
