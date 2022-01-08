@ECHO OFF & setlocal EnableDelayedExpansion

set TIME_START='2021-12-15 00:00:00'
set TIME_END='2022-11-10 23:34:00'

cd /d "%~dp0"
set OUTPUTPATH=%~dp0\OUTPUT
set WINEVTPATH="C:\windows\system32\winevt\Logs"
IF NOT EXIST "%OUTPUTPATH%" ( 
       mkdir "%OUTPUTPATH%"
    )


dir /a/s/b/on %WINEVTPATH%\*.evtx > "%OUTPUTPATH%\Winevtx.lst"
IF NOT EXIST "%OUTPUTPATH%\Winevtx" ( 
       mkdir "%OUTPUTPATH%\Winevtx"
    )
IF NOT EXIST "%OUTPUTPATH%\Winevtx\csv" ( 
       mkdir "%OUTPUTPATH%\Winevtx\csv"
    )

for /f "delims=" %%i in (!%OUTPUTPATH%\Winevtx.lst!) do (
	set "NAMEX=%%~ni"
	set "NAMEX=!NAMEX: =_!"
	echo copy "%%i" 
	@copy "%%i" "%OUTPUTPATH%\Winevtx\!NAMEX!.evtx"
rem goto IGN_LOGPARSE
	@logparser.exe "select * INTO '%OUTPUTPATH%\Winevtx\csv\!NAMEX!.csv' from '%OUTPUTPATH%\Winevtx\!NAMEX!.evtx' where TimeGenerated>%TIME_START% and TimeGenerated<%TIME_END%" -i:EVT -headers:ON -q:ON
rem :IGN_LOGPARSE
)

for %%i in (%OUTPUTPATH%\Winevtx\csv\*.csv) do (
    type "%%i" >> %OUTPUTPATH%\result.csv
)
