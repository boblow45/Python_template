#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = "{{ cookiecutter.email }}"
__version__ = "{{ cookiecutter.version }}"


# -------- Generic Libraries -------
from logging.config import dictConfig
import yaml
import os

# Load the yaml file which contains all the logging config for the 1060
logging_config_path = os.path.join("config_files", "logging.yaml")
config_path = os.path.join(os.path.dirname(__file__), logging_config_path)
with open(config_path, "rt") as f:
    config = yaml.safe_load(f.read())

# Create the path which the log files will be saved in.
logging_dirs = []
for handler in ["info_file_handler", "error_file_handler"]:
    config["handlers"][handler]["filename"] = os.path.join(
        os.path.dirname(__file__), config["handlers"][handler]["filename"]
    )
    logging_dirs.append(os.path.dirname(config["handlers"][handler]["filename"]))

# Ensure that the directory wheres the logs are to saved exists
for dir in logging_dirs:
    if not os.path.exists(dir):
        os.makedirs(dir)

# config the loggers
dictConfig(config)
