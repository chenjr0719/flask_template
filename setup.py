from setuptools import find_packages, setup

install_requires = ["Flask==2.3.2"]

dev_requires = ["black==19.10b0", "pylint==2.4.4", "wheel==0.33.6"]

test_requires = [
    "coverage==5.0",
    "pytest==5.3.2",
    "pytest-cov==2.8.1",
    "pytest-html==2.0.1",
    "pytest-runner==5.2",
    "pytest-sugar==0.9.2",
    "tox==3.14.2",
]

doc_requires = [
    "commonmark==0.9.1",
    "docutils==0.15.2",
    "Pygments==2.5.2",
    "recommonmark==0.6.0",
    "Sphinx==2.3.0",
    "sphinx-autobuild",
    "sphinx-rtd-theme==0.4.3",
]


setup(
    name="flask_template",
    description="Flask template project",
    url="http://github.com/chenjr0719",
    author="Jacob Chen",
    author_email="chenjr0719@gmail.com",
    license="MIT",
    packages=find_packages(exclude=["tests", "test_reports"]),
    install_requires=install_requires,
    extras_require={
        "dev": dev_requires + test_requires + doc_requires,
        "test": test_requires,
        "doc": doc_requires,
    },
    entry_points={"console_scripts": ["flask_template = flask_template.__main__:main",]},
)
