import os

# To use a consistent encoding
from codecs import open
from os import path

from setuptools import setup

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


def get_external_reqs():
    """
    The get_external_reqs function reads the requirements.txt file and returns a list of strings,
    where each string is an external requirement for this project.

    :return: A list of strings
    The get_internal_reqs function is used to get the internal requirements for the project.
    This function will read from a file called &quot;internal-requirements.txt&quot; and parse it into a list of strings that can be passed to pip install as dependencies.

    :return: A list of dependencies
    """
    with open("requirements.txt", "r") as f:
        return [x for x in f.read().split("\n") if x]


def get_internal_reqs():
    """
    The get_internal_reqs function is used to get the internal requirements for the project.
    This function will read from a file called &quot;internal-requirements.txt&quot; and parse it into a list of strings that can be passed to pip install as dependencies.

    :return: A list of dependencies
    """
    token = os.getenv("GIT_TOKEN")
    if not token:
        raise ImportError(
            "Please make sure you set an env called GIT_TOKEN. \n $export GIT_TOKEN=<your token>"
        )
    deps = []
    with open("internal-requirements.txt", "r") as f:
        for req in f.read().split("\n"):
            if not req:
                continue
            pkg, ver = req.split("==")
            deps.append(
                f"{pkg} @ git+https://{os.getenv('GIT_TOKEN')}@github.com/BankBuddy/bud-core-{pkg}-lib@{ver}"
            )
        return deps


# This call to setup() does all the work
setup(
    name="boilerplate",
    version="5.2.4.0",
    description="boilerplate library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://affinsys.com/",
    author="Ashutosh Pednekar",
    author_email="ashutosh.pednekar@affinsys.com",
    license="Proprietary",
    classifiers=[
        "Intended Audience :: Affinsys Developers",
        "License :: Proprietary",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    packages=["boilerplate"],
    scripts=[
        "scripts/runserver",
        "scripts/runworker",
        "scripts/create_project",
        "scripts/rebase_project",
        "scripts/create_app",
        "scripts/install_deps",
        "scripts/setenv",
        "scripts/run",
        "scripts/cluster-setup",
        "scripts/cluster-install",
        "scripts/cluster-uninstall",
    ],
    include_package_data=True,
    install_requires=[],
    # install_requires=get_external_reqs() + get_internal_reqs(),
)
