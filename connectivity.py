import os
import subprocess
answer = "0"
answer=0
def home():
    print("[1]ping联通性测试\n[2]ping联通性测试（持续）")
    answer = input("请选择需要运行的项目，并输入其的编号：")
    if answer==1:
        answer2=input("请输入你想要测试的域名/IP地址：")
        subprocess.Popen(["cmd.exe",f"ping {answer2}"])
    elif answer==2:
        answer2=input("请输入你想要持续测试的域名/IP地址：")
        print("注意！您正在尝试持续测试。持续测试将会永远不停地测试，直到您按下Ctrl+C才停止。")
        input("您真的要继续吗？按下回车键继续。")
        subprocess.Popen(["cmd.exe",f"ping {answer} -t"])

