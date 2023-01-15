@ECHO off   
if /I %1 == default goto :default
if /I %1 == clean goto :clean
if /I %1 == help goto :help
if /I %1 == test goto :test

@REM SET SERVER_LOC=

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
if exist pytest_output rmdir /q/s pytest_output
if exist .pytest_cache rmdir /q/s .pytest_cache
if exist __pycache__ rmdir /q/s __pycache__
goto :eof

:test
python -m pytest --verbose
coverage html
coverage xml
goto :eof


REM -----------------------------------------------------------------------------