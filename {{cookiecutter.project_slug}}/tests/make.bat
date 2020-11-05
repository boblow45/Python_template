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

SET SERVER_LOC=

goto :eof ::can be ommited to run the `default` function similarly to makefiles

:default
echo DEFAULT
goto :eof

REM ---------- Sections which can only be ran on packager Jenkins node -----------

:help
ECHO clean: remove all build and Python artifacts
ECHO test: test the module and generate coverage report
goto :eof

:clean
del /f/s/q .coverage
rmdir /q/s htmlcov/
rmdir /q/s pytest_output/
rmdir /q/s .pytest_cache/
goto :eof

:test
python -m pytest --verbose
python -m coverage html
goto :eof


REM -----------------------------------------------------------------------------