@ECHO off   
if /I %1 == default goto :default
if /I %1 == clean goto :clean
if /I %1 == help goto :help
if /I %1 == test goto :test
if /I %1 == lint goto :lint
if /I %1 == docs goto :docs
if /I %1 == dist goto :dist
if /I %1 == release goto :release
if /I %1 == install goto :install
if /I %1 == install-dev goto :install-dev

@ REM SET SERVER_LOC=

goto :eof ::can be ommited to run the `default` function similarly to makefiles

:default
echo DEFAULT
goto :eof

REM ---------- Sections which can only be ran on packager Jenkins node -----------

:help
ECHO clean: remove all build and Python artifacts
ECHO docs: builds all the documentents for the module
ECHO test: test the module and generate coverage report
ECHO lint: Lint all the python scripts using flake8
ECHO release: push python package and wheel to artifactory
ECHO dist: create python package and wheel
ECHO install: install module with packages are required for it to run, development packages are not installed
ECHO install-dev: install module with packages all requiredments and development packages 
goto :eof

:clean
del /f/s/q *.egg-info
for /d /r ./{{cookiecutter.project_slug}} %%d in (__pycache__) do @if exist "%%d" rd /s/q "%%d"
for /d /r ./tests %%d in (__pycache__) do @if exist "%%d" rd /s/q "%%d"
for /d /r . %d in (__pycache__) do @if exist "%%d" rd /s/q "%%d"
rmdir /q/s build/
rmdir /q/s dist/
rmdir /q/s .eggs/
cd tests
call make.bat clean
cd ..
goto :eof

:docs
cd docs
call make.bat html
cd ..
goto :eof

:test
cd tests
call make.bat test
cd ..
goto :eof

:lint
flake8 {{cookiecutter.project_slug}} tests
goto :eof

:dist
@ REM pip-compile --extra-index-url %SERVER_LOC% 
pip-compile
pip install wheel 
python setup.py sdist
python setup.py bdist_wheel
goto :eof

:release 
twine upload dist/*
goto :eof

:install
@ REM pip install --extra-index-url %SERVER_LOC% -e .
pip install -e .
goto :eof

:install-dev
@ REM pip install --extra-index-url %SERVER_LOC% -e .[dev]
pip install -e .[dev]
goto :eof

REM -----------------------------------------------------------------------------