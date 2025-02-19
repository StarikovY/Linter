@echo off
REM modify only strings below

Rem drive letter for drive with VSO enlistment location
set VSDRV=D:

rem password for test signing certificate
set PASWWD=TMobis01
set SIGNCERT="d:\TMobis\RES2Rel\Certs\TMobisSign2.pfx"

Rem Microsoft tools
set MAGE="c:\Program Files (x86)\Microsoft SDKs\Windows\v10.0A\bin\NETFX 4.7.2 Tools\mage.exe"
set SIGNTOOL="C:\Program Files (x86)\Windows Kits\10\bin\10.0.22621.0\x86\signtool.exe"
set MSBLD="C:\Program Files\Microsoft Visual Studio\2022\Enterprise\MSBuild\Current\Bin\MSBuild.exe"

Rem for Rosetta Hello UWP App
set MAKEAPPX="C:\Program Files (x86)\Windows Kits\10\bin\10.0.22621.0\x86\makeappx.exe"
set PATH="C:\Users\ystms\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts";C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\MSBuild\Current\Bin;C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\CommonExtensions\Microsoft\CMake\CMake\bin;%PATH%

REM DO NOT modify string below, modify only strings avove
set VSO=D:\Linter
set VERFILE="%VSO%\src\version.py"
set TF="C:\Program Files\Microsoft Visual Studio\2022\Enterprise\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\tf.exe"

rem set TSURL="http://timestamp.verisign.com/scripts/timstamp.dll"
set TSURL="http://timestamp.digicert.com"
rem set DTF="%RESNext%\tools\ConfuserEx\Confuser.CLI.exe"


%VSDRV%
cd %VSO%\src

:exit
exit /b 0



PATH="C:\Users\ystms\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts";C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\MSBuild\Current\Bin;C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\CommonExtensions\Microsoft\CMake\CMake\bin;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\dotnet\;C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\;C:\Program Files\Microsoft SQL Server\150\Tools\Binn\;C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\;C:\Users\ystms\.dnx\bin;C:\Program Files\Microsoft DNX\Dnvm\;C:\Program Files\Microsoft SQL Server\120\Tools\Binn\;C:\Program Files\Microsoft SQL Server\130\Tools\Binn\;C:\Program Files (x86)\Incredibuild;C:\Program Files (x86)\HID Global\ActivClient\;C:\Program Files\HID Global\ActivClient\;C:\Program Files\SPYRUS\NcryptNshare;C:\Program Files\Git\cmd;C:\Program Files\SPYRUS\RES\x64;C:\Program Files\SPYRUS\RES\x86;C:\Program Files\NcNs\RES\x64;C:\Program Files\NcNs\RES\x86;C:\Users\ystms\AppData\Local\Programs\Python\Launcher\;C:\Users\ystms\AppData\Local\Microsoft\WindowsApps;C:\Users\ystms\.dotnet\tools;C:\Program Files\CMake\bin;C:\Users\ystms\AppData\Local\Programs\Microsoft VS Code\bin

