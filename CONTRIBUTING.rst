============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs to https://github.com/boblow45/Python_template/issues

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
and "help wanted" is open to whoever wants to implement a fix for it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.


Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to log an issue @ https://github.com/boblow45/Python_template/issues
If you are proposing a new feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `cookiecutter-pypackage` for local
development. Please note this documentation assumes you already have
`virtualenv` and `Git` installed and ready to go.

1. Fork the `cookiecutter-pypackage` repo on GitHub.

::

2. Clone your fork locally:

   .. code-block:: bash

    $ cd path_for_the_repo
    $ git clone https://github.com/boblow45/Python_template.git

::

3. Assuming you have virtualenv installed (If you have Python3.5 this should
   already be there), you can create a new environment for your local
   development by typing:

   .. code-block:: bash

        $ virtualenv venv
        $ source venv/bin/activate

   This should change the shell to look something like:

   .. code-block:: bash

        (venv) $

::

4. Create a branch for local development:

   .. code-block:: bash

        $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

::

5. When you're done making changes, check that your changes pass flake8.

   .. code-block:: bash

        $ flake8 ./tests

::

6. Commit your changes and push your branch to Bit-Bucket:

   .. code-block:: bash

        $ git add .
        $ git commit -m "Your detailed description of your changes."
        $ git push origin name-of-your-bugfix-or-feature

::

7. Submit a pull request through the Bit-Bucket website.

::

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should build when used with cookiecutter.

2. If the pull request adds functionality, the docs should be updated. Put your
   new functionality into a function with a docstring, and add the feature to
   the list in README.rst.

3. The pull request should work for Python 2.7, 3.5, 3.6 and 3.7, and for PyPy.
