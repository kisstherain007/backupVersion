# -*- coding=utf-8 -*-

import os
import subprocess
import sys
import zipfile
import getCodeInfo

reload(sys)
sys.setdefaultencoding('utf-8')

#8.X
# projectRootDir = 'D:\ydhlBackupCode'
# projectTargetDir = "D:\ydhlBackupCode\yidonghuli"
# zipTargetDir = "D:\ydhlBackupCode\yidonghuli\YiDongHuiLi_Zpdyf_Basic_V8.4.1.0_publish"

#9.X
projectRootDir = 'D:\ydhlBackupCode'
projectTargetDir = "D:\ydhlBackupCode\yidonghuli_new"
zipTargetDir = "D:\ydhlBackupCode\yidonghuli_new\YiDongHuiLi_Zpdyf_Basic"

def clone():
    os.chdir(projectRootDir)
    os.system("clone.sh")

def pull(branchName):
    cmd = "git checkout " + branchName.decode('utf8').encode('GBK')
    os.system(cmd)
    code_info_arr = getCodeInfo.getReleaseBranchName(zipTargetDir.decode('utf8').encode('GBK'))
    print(">>>>>>>>" + code_info_arr[1])
    yiyuan_name = code_info_arr[1]
    result_codepro_name = yiyuan_name + "V"+ code_info_arr[0] + "终端"
    result_codepro_name = result_codepro_name.decode('utf8').encode('GBK')
    zip_dir(zipTargetDir, result_codepro_name + ".zip")
    # zip_dir(zipTargetDir, branchName+".zip")
    print(cmd)

def zip_dir(srcPath, dstname):
    try:
        if(checkBackupFileVersion(projectTargetDir, dstname) == False):
            zipHandle=zipfile.ZipFile(dstname, 'w', zipfile.ZIP_DEFLATED)
            for dirpath,dirs,files in os.walk(srcPath):
                for filename in files:
                    zipHandle.write(os.path.join(dirpath,filename)) #必须拼接完整文件名，这样保持目录层级
                    print filename+" zip succeeded"
            zipHandle.close
        else:
            print(dstname + ">>>已经存在")
    except:
        pass

def checkBackupFileVersion(targetDir, file):
    # targetFile = os.path.join(targetDir, file).decode('utf-8')
    # if os.path.exists(targetFile):
    #     return True
    # else:
    #     return False
    return False

# 获取所有分支信息
def getAllBranchs():
    os.chdir(projectTargetDir)
    cmd = "git branch -a"
    cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (gbranch_out, gbranch_err) = cmd.communicate()
    branches_str = gbranch_out
    branches_str = branches_str.decode('utf-8')
    branches = branches_str.split('\n')
    branch_list = []
    for branch in branches[0:-1]:
        branch_list.append(branch.lstrip('* ').replace('remotes/origin/', ''))
    return branch_list

include_branchs = ["", ""]
exclude_branchs = ["feature", "develop", "new", "master"]

def getNeedUploadBranchs():
    branch_list = getAllBranchs()
    temp_list = []
    for branch_name in branch_list:
        temp = True
        for exclude_keyword in exclude_branchs:
            if exclude_keyword in branch_name:
                temp = False
                break
        if temp == False:
            print("排除：" + branch_name)
        else:
            temp_list.append(branch_name)
            pull(branch_name)
            print("添加：" + branch_name)

getNeedUploadBranchs()
# clone()