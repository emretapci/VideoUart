This program receives commands from UART 2 interface of banana pro, with
parameters 115200 bps, parity: None, Data bits: 8, Stop bits: 1 and
no hardware flow control.

To configure;

1. Install Ubuntu Mate.

2. Type "su" and login as "root".

3. Type "adduser uart" to add a new user.

4. Type "usermod -aG sudo uart"

5. Copy "uartvideo.py" and "init_dev.sh" files to "/home/uart"

6. Type "visudo -f /etc/sudoers"

7. At the end of "/etc/sudoers" file, add the following lines:
		%sudo ALL= NOPASSWD: /home/uart/init_dev.sh
		%sudo ALL= NOPASSWD: /bin/chmod

8. Open menu: "System > Startup Applications"

9. Click "Add" and type "UART video player" as Name,
   "python /home/uart/uartvideo.py" as Command.

10. Type "chmod 777 /home/uart/uart_dev.sh"

11. Edit "/etc/lightdm/lightdm.conf" file as follows:
		[SeatDefaults]
		autologin-guest=false
		autologin-user=uart
		autologin-user-timeout=0
		autologin-session=lightdm-autologin

12. Restart banana pro.

### Commands expected from UART are: ###

P<file_name><br>
play <file_name> video<br>
<file_name> is a null-terminated string, it ends with a <null> (0) character.<br>
there's no space between "P" and <file_name><br>
e.g. Pintroduction.avi<null> : Starts the movie "introduction.avi" in the current directory.<br>
Pvideos\setup.avi<null> : Starts the movie "setup.avi" in the <current directory>/videos directory.<br><br>

S<br>
stop playback
