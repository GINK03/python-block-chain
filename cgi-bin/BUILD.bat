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
python offline.py
xcopy cache ..\cache /S /I
GOTO :EOF

:B
rd ..\cache /S
del cache\* /Q
GOTO :EOF