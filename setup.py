# !/usr/bin/env python

from setuptools import setup, find_packages

__name__ = "python-cookiecutter-pypackage"

install_requires = [
    "cookiecutter==1.4.0",
]

dev_requirements = [
    "pytest==5.3.1",
    "pytest-cookies==0.4.0",
    "alabaster==0.7.12",
    "watchdog==0.9.0",
]

setup(
    name=__name__,
    install_requires=install_requires,
    packages=[],
    version="0.5.11",
    description="Cookiecutter template for a Python package",
    author="Cillian O'Brien",
    license="MIT",
    author_email="cillianobrien01@gmail.com",
    url="https://github.com/boblow45/Python_template",
    keywords=["cookiecutter", "template", "package"],
    extras_require={"dev": dev_requirements},
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development",
    ],
)
