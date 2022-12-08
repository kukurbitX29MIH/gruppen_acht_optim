echo xxxxxx
cd "C:\projects_ansys\optimis_mag_sem_1_lab_2"
set PATH=%PATH%;"C:\Program Files\ANSYS Inc_2\ANSYS Student\v222\ansys\bin\winx64\"
echo PATH

"C:\Program Files\ANSYS Inc_2\ANSYS Student\v222\ansys\bin\winx64\ANSYS222.exe"     -p ansys  -np 2   -dir "C:\projects_ansys\optimis_mag_sem_1_lab_2\calc_8_the_last_success"   -s read   -b -i "C:\projects_ansys\optimis_mag_sem_1_lab_2\calc_8_the_last_success\macro3.mac"  -o "out.txt" 
pause
