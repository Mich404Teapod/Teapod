@echo off
title teapod - execute
set copyright = teapod Software 2022

:start
echo What file do you want to run?
set/p "file=>"

ren %file% main.zip
ping localhost -n 2
start main\terminal\main.exe
ren main.zip %file%
