vncserver -localhost -geometry 1280x720; export DISPLAY=":1";xrandr -s 1280x720;pulseaudio --start --disable-shm=1 --exit-idle-time=-1
