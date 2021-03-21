# ANRO Zadanie1
### `custom control` -pakiet ROS, przechowuje logikę napisanego programu
### `install` - folder, pozwalający zidentyfikować źródło
#### Aby uruchomić system należy:
##### Wsyztkie polecenia należy wpisywać w terminalu(`CTR+ALT+T`)
1. Pobrać repozytorium za pomocą polecenia `git clone 'https://github.com/pw-eiti-anro-21l/klimuk_stankevich.git'`
2. Przejść do foldera klimuk_stankevich za pomocą polecenia `cd klimuk_stankevich/` i wpisać polecenie `git checkout pklimuk_zad1`
3. Wpisać polecenie `colcon build --packages-select custom_control`
4. Otworzyć nowe okno terminala przejść do foldera klimuk_stankecich i wpisać `. install/local_setup.bash `
5. Wpisać polecenie `ros2 launch custom_control custom_control_launch.py `
6. Dla zakończenia pracy sytemu należy wcisnąć `CTRL+C` i zamknąć otwrte terminale

## Opis systemu:
Węzeł *custom control* komunikuje się z węzłem *turtlesim* za pomocą topic'a _turtle1/cmd_vel_\
https://wutwaw-my.sharepoint.com/:i:/g/personal/01155513_pw_edu_pl/EXLaKRa5-MBEqqMS99O64a8BYQNM8U-90o1d0JNnxhqApg?e=mWXTh6
