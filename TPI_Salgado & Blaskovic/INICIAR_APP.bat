@echo off
title Sistema de Gestion de Paises - UTN Programacion 1
cls
echo ==============================================================================
echo       INICIANDO SISTEMA DE GESTION DE PAISES - TPI PROGRAMACION 1 (UTN)
echo ==============================================================================
echo.
echo  Iniciando servidor web en Python nativo...
echo  Se abrira automaticamente la aplicacion en su navegador web.
echo.
echo  Para detener el servidor en cualquier momento, presione CTRL + C.
echo ==============================================================================
echo.

python app_web.py

if errorlevel 1 (
    echo.
    echo [ERROR] No se pudo iniciar con 'python'. Intentando con 'py'...
    py app_web.py
)

pause
