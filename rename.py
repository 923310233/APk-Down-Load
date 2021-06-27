import shutil
from os import walk
import subprocess
import re
import configparser
import random
import os


def get_apk(work_path):
    apk_files = []
    for (dirpath, dirnames, filenames) in walk(work_path):
        for file_name in filenames:
            if file_name.__contains__('.apk') is True:
                apk_files.append(dirpath + '/' + file_name)
    return apk_files

def get_FileSize(filePath):
    # filePath = unicode(filePath,'utf8')
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024)
    return round(fsize,2)

def get_package_name(apk_path):
    cmd = aapt_path + r'aapt dump badging "' + apk_path + '"'  # need to modify
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    # active_proc_list.append(proc)
    cmd_output, error = proc.communicate()
    cmd_output = cmd_output.decode()
    reg = re.compile('package: name=\'(\S+)\'')
    strs = re.findall(reg, cmd_output)
    proc.terminate()
    if len(strs) != 1:
        return ''
    else:
        return strs[0]

if __name__ == '__main__':
    apk_folder = r'/home/tomwu/app/top1000/vpn/'
    output_folder = r'/home/tomwu/app/top1000/temp/'
    config = configparser.ConfigParser()
    try:
        config.read('config.ini')
        cmd_path = config['DEFAULT']['adb_cmd_path']
        aapt_path = config['DEFAULT']['aapt_cmd_path']
    except Exception as exc:
        print(exc)
        exit(1)
    apk_list = get_apk(apk_folder)
    random.shuffle(apk_list)
    for i in range(len(apk_list)):
        apk = apk_list[i]
        if get_FileSize(apk) < 10:
            print(apk)
            continue
        try:
            aaa = get_package_name(apk)
            dst_name = output_folder + aaa + '.apk'
            app_name = shutil.copy2(apk, dst_name)
            print(aaa)
        except Exception as exc:
            print(exc)
    print('Done!')