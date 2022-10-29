@ECHO OFF
chcp 65001
title 0nvg/nitrogen - by aeg#0001
echo Hoşgeldin %username%.
echo Herhangi bir tuşa basarak gereken paketleri indirebilirsin.
echo İndirme bittiğinde bu dosyayı tekrar açmana gerek olmayacak.
pause >nul
call py -3 -m pip install requests
call py -3 -m pip install discord_webhook
call py -3 -m pip install numpy
call nitrogen.bat
echo .
echo .
echo .
echo Bu pencereyi kapatabilirsiniz.
pause >nul