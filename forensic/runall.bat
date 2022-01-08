@ECHO OFF & setlocal EnableDelayedExpansion
title Running all batch files

:: 运行当前目录下的所有bat脚本
cd /d "%~dp0"
set OUTPUTPATH=%~dp0\OUTPUT
echo ========================================
for %%i in (.\*.bat) do @(
	@if not "%%i" == ".\%0" (
	    echo Running %%i
	    %%i
		echo ========================================
	)
)
echo [*] Finished.
echo Thank you~ Bye....

pause >nul