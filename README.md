# IBSS_RpiBased_Gecko
南京航空航天大学放生所庇护机器人_基于树莓派的小玩意_暂由白泥与泥鳅维护

The gecko robot drived by Raspiberry Pi 3B+. The robot is constructed by the 12 servos which echo to PWM.

机器人有四条腿，每条腿3自由度，所以12个舵机，都是用PWM控制的垃圾玩意

When using RPi.GPIO, the servos shake rapidly, so I use ServoBlaster. Here is the detail about it: github.com/richardghirst/PiBits.git. Thanks to Richard!

我一直开始用RPi.GPIO库调试，结果舵机患上了小儿麻痹，查病发现了大佬的库专治这病，详细内容查看大佬的库，感谢大佬
Aft install ServoBlaster and run it, we do some adjustment to the setting cause we gotta 12 servos to drive. Input codes below in your terminal:

------------------------------------------------------

sudo ./servod --p1pins=7,11,12,13,15,16,18,22,29,31,32,33

------------------------------------------------------

we add 29, 31, 32, 33 to p1pins( default setting is --p1pins=7,11,12,13,15,16,18,22)

And here is the connection relationship:

7--servo_rf_0

11--servo_rf_1

12--servo_rf_2

13--servo_lf_0

15--servo_lf_1

16--servo_lf_2

18--servo_rh_0

22--servo_rh_1

29--servo_rh_2

31--servo_lh_0

32--servo_lh_1

33--servo_lh_2


I will update the pic of gecko after I finish the main part of job.


I can't code a shell script to make the gecko move, which is the more efficient way to access my target. So I code some python scripts to make that.

I use subprocess to do that like:

------------------------------------------------------

import subprocess

subprocess.call("echo 2=100 > /dev/servoblaster", shell=True)

------------------------------------------------------

If you have checked github.com/richardghirst/PiBits.git, you will understand it soon.

My code and English level are both very very very poooooor! So if you gotta ANY suggestion, PLZ PULL REQUESTS! Or you can contact with me by mail, here is my mail address: happywbc@qq.com

Here is the file structure:

geckorobot_gait_data.py-- used to generate gait data

geckorobot_drive.py-- haven't coded it yet!

