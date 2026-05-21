@echo off
echo =======================================
echo     AUTO DEPLOY GITHUB PAGES
echo =======================================

echo 1. Mengumpulkan file statis (CSS/JS/IMG) terbaru...
python manage.py collectstatic --noinput

echo.
echo 2. Menyatukan proyek menjadi web statis murni...
python manage.py distill-local docs --force

echo.
echo 3. Membersihkan dan memperbarui folder docs\static...
if exist docs\static rmdir /s /q docs\static
mkdir docs\static
xcopy staticfiles\* docs\static\ /s /e /y /q >nul

echo.
echo 4. Memperbaiki link rusak agar cocok dengan GitHub Pages...
powershell -Command "(Get-Content docs\index.html) -replace '\"/static/', '\"/web-portofolio-withDjango/static/' | Set-Content docs\index.html"

echo.
echo =======================================
echo PROSES BUILD SELESAI!
echo =======================================
echo Untuk menaikkan (deploy) ke GitHub Pages, jalankan perintah ini di Terminal:
echo git add .
echo git commit -m "Update website terbaru"
echo git push origin main
echo.
pause
