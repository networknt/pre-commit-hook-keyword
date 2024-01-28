from setuptools import setup

setup(
    name="pre_commit_hook_keyword",
    version="1.0.0",
    packages=["keyword"],
    entry_points={"console_scripts": ["keyword=keyword.cli:main"]},
)
