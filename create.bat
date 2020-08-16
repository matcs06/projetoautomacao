@echo off

set var1=%1
set var2=%2

If "%var1%"=="" (
  
   echo You have to define the folder's name
	
) else (
  
  if "%var2%"=="remote" (
     python remote.py %var1%
  )
 
  python localf.py %var1%    
)

pause
cls
