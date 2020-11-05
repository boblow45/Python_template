#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

# Open readme file and pull in all the data in the file. The information in the readme will be used in the long description
with open("README.md") as readme_file:
    readme = readme_file.read()

# Open the change log, this will appeded to the readme and saved to the long description parameter 
with open("Changelog.md") as history_file:
    history = history_file.read()

# List of dependencies which are requireded for this module.
requirements = ["pyyaml",
                {%- if cookiecutter.command_line_interface|lower == "click" %}'Click>=6.0',{%- endif %}
]

# List of dependencies which are requireded for the developement of this module. 
# Examples are framework for testing, pytest. Documentation module sphinx, deployment package 
dev_requirements = [
{%- if cookiecutter.use_pytest == 'y' %}"pytest-runner", "pytest>=3", "pytest-cov",{% endif %} 
    "sphinx",

    "tox",
    "pip-tools",
    "bump2version",
    "flake8",
    "black",
    "watchdog",
    "pylint",
    'mock',
    "coverage",

    "twine",
]

{%- set license_classifiers = {
    "MIT license": "License :: OSI Approved :: MIT License",
    "BSD license": "License :: OSI Approved :: BSD License",
    "ISC license": "License :: OSI Approved :: ISC License (ISCL)",
    "Apache Software License 2.0": "License :: OSI Approved :: Apache Software License",
    "GNU General Public License v3": "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
}%}


setup(name="{{ cookiecutter.project_slug }}",
      version="{{ cookiecutter.version }}",
      description="{{ cookiecutter.project_short_description }}",
      long_description=readme + '\n\n' + history,
      author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
      author_email="{{ cookiecutter.email }}",
      url="{{ cookiecutter.repo_location}}",
      packages=find_packages(),
      install_requires=requirements,
      dependency_links=[
      ],
      include_package_data=True,
      package_data={"": ["*.yaml", "*.ini", "*.md", "*.txt"]},
      extras_require={"dev": dev_requirements},
      python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*",
      test_suite="tests",
      tests_require=dev_requirements,
      zip_safe=False,

      {%- if 'no' not in cookiecutter.command_line_interface|lower %}
      entry_points={
          "console_scripts": [
              "{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main",
          ],
      },
      {%- endif %}
     {%- if cookiecutter.open_source_license in license_classifiers %}
      license="{{ cookiecutter.open_source_license }}",
     {%- endif %}

      classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Developers",
    {%- if cookiecutter.open_source_license in license_classifiers %}
            "{{ license_classifiers[cookiecutter.open_source_license] }}",
    {%- endif %}
            "Natural Language :: English",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
       ],
       keywords = "{{ cookiecutter.project_slug }}",
)
