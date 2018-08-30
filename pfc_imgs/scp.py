import subprocess
import sys
import os
import time
print(sys.version)

# cmd = "farmer@210.92.91.225:/var/www/html/pfc_rest_api/pfc_log_data.log"
# p = subprocess.Popen(["scp",cmd,"."])
# sts = os.waitpid(p.pid,0)

# sys.exit()

for i in range(0,24):
	hour_s = str(i).zfill(2)
	for j in [2,5] :
		min_s = str(j) + str(0);
		f_path = "2018-08-22_" + hour_s + ":" + min_s + ":01.jpg"
		# print(f_path)

# print(f_path)
		cmd = "farmer@210.92.91.225:/var/www/html/pfc_rest_api/imgs/" + f_path

		p = subprocess.Popen(["scp",cmd, "./sum/"])
		time.sleep(0.6)
		# sts = os.waitpid(p.pid,0)
		# print(p.pid)
# subprocess.popen(cmd)