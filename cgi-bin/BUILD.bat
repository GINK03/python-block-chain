@echo off
IF "%1"=="/b" GOTO :A
IF "%1"=="/d" GOTO :B
IF "%1"=="" GOTO :HELP
GOTO :EOF

:HELP
echo BUILD [/b] is BuildMode
echo BUILD [/d] is DestroyMode
GOTO :EOF

:A
IF NOT EXIST cache mkdir cache
python offline.py
xcopy cache ..\cache /S /I /Q
GOTO :EOF

:B
rd ..\cache /S
del cache\* /Q
GOTO :EOF