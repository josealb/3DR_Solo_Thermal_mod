scp gimbalsync.h root@10.1.1.10:/etc/init.d/
ssh root@10.1.1.10 'chmod +x /etc/init.d/gimbalsync.h; update-rc.d gimbalsync.h defaults; mkdir /home/root/scripts/'
scp syncGimbalwithThermal.py root@10.1.1.10:/home/root/scripts/
scp GoProManager.py root@10.1.1.10:/usr/bin/