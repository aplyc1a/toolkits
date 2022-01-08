@ECHO OFF
echo "ssCollet any files listed in qingdan.txt"
cd /d "%~dp0"
mkdir sample
@for /f %%i in (qingdan.txt) do (
echo begin copy... "%%i"
copy /y "%%i" "sample\"
echo copy complate ... "%%i"
)
pause
