import subprocess

f = open("app_list.csv","r")
lines = f.readlines()
for line in lines:
    print(line.strip())
    command = "node app.js " + line.strip();
    display = subprocess.run(command, stdout=subprocess.PIPE, shell=True)



# display = subprocess.run(["sudo","-u",username,"tshark", "-r", pcapname, "-Y", display_filter[sp]],  stdout=subprocess.PIPE)
# display_in_list = display.stdout.split()