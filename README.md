
# Cookiecutter Python Package

-------------------------------

[Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) template for a Python package. This repo contains a 
template which is used for each python project. The idea is to create a common structure for python projects and 
make it easy for team members to create a new project by using cookiecutter to fill in the boiler plate parameters.

* GitHub repo: https://github.com/boblow45/Python_template
* Free software: MIT license

## Features

-------------------------------

* Testing setup with pytest
* Tox_ testing: Setup to easily test for Python 2.7, 3.5, 3.6, 3.7
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
* bump2version_: Pre-configured version bumping with a single command

## Quickstart

-------------------------------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/boblow45/Python_template.git

Then:

* Create a repo and put it there.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Add package to Jenkins by pointing Jenkins CI to Jenkinsfile. Jenkins will then test, build and deploy the package 
* Release your package by pushing a new tag to master.
* Add a `requirements.txt` file that specifies the packages you will need for
  your project and their versions. For more info see the [pip docs for requirements files](https://pip.pypa.io/en/stable/user_guide/#requirements-files)

### Support this Project

-------------------------------

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.


### Fork This / Create Your Own

-------------------------------

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

### Or Submit a Pull Request

-------------------------------

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.
