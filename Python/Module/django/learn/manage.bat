@ECHO OFF&PUSHD %~DP0 &TITLE  Django Manage
rem mode con cols=80 lines=30
rem color 2F
:Menu
    Cls
    @ echo. Menu
    @ echo. 
    @ echo. 1.   Check
    @ echo. 2.   Makemigrations
    @ echo. 3.   Migrate
    @ echo. 4.   Dbshell
    @ echo. 0.   Exit

    set /p xj= Please input number and enter:
    if /i "%xj%"=="1" Goto check
    if /i "%xj%"=="2" Goto makemigrations
    if /i "%xj%"=="3" Goto migrate
    if /i "%xj%"=="4" Goto dbshell
    if /i "%xj%"=="0" Goto Exit
    @ echo.
    echo    Input Error...
    ping -n 2 127.1>nul 
goto menu

:check
    python manage.py check
goto done

:makemigrations
    python manage.py makemigrations
goto done

:migrate
    python manage.py migrate
goto done

:dbshell
    python manage.py dbshell
goto menu

:done
    pause
goto menu