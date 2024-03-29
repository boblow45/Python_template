#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `{{ cookiecutter.project_slug }}` package."""

{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{% else %}
import unittest
{%- endif %}

{%- if cookiecutter.command_line_interface|lower == 'click' %}
from click.testing import CliRunner
from {{ cookiecutter.project_slug }} import cli
{%- endif %}

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}

{%- if cookiecutter.use_pytest == 'y' %}

def test_example():
    assert 1==1

{%- if cookiecutter.command_line_interface|lower == 'click' %}


# def test_command_line_interface():
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert '{{ cookiecutter.project_slug }}.cli.main' in result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert '--help  Show this message and exit.' in help_result.output
# {%- endif %}
{%- else %}


class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
# {%- if cookiecutter.command_line_interface|lower == 'click' %}

#     def test_command_line_interface(self):
#         """Test the CLI."""
#         runner = CliRunner()
#         result = runner.invoke(cli.main)
#         assert result.exit_code == 0
#         assert '{{ cookiecutter.project_slug }}.cli.main' in result.output
#         help_result = runner.invoke(cli.main, ['--help'])
#         assert help_result.exit_code == 0
#         assert '--help  Show this message and exit.' in help_result.output
# {%- endif %}
{%- endif %}


# {%- if cookiecutter.command_line_interface|lower == 'click' %}

# def test_command_line_interface():
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert '{{ cookiecutter.project_slug }}.cli.main' in result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert '--help  Show this message and exit.' in help_result.output

# {%- endif %}

