import os
answer=0
def cm():
        input("\n按下任意键返回首页")
        home()
def home():
    global answer
    os.system("cls")
    print("欢迎使用InternetToolBox！\n[1]连通性测试\n[2]...\n[3]关于")
    answer=int(input("请选择需要运行的项目，并输入其的编号："))
    os.system("cls")
    if answer==1:
        print("连通性测试")
        cm()
    elif answer==3:
        about()
        cm()
    else :
        os.system("cls")
        print("当前编号不存在，请检查后再试")
        cm()
def about():
    print("关于InternetToolBox")
    print("Copyright © 2025 RMDCXY&CodeGlitch95 All Rights Reserved.")
    print("Github项目地址：https://github.com/Weizirui-hi/InternetToolBox/")
    print("作者空间：\nCodeGlitch95：\nRMDCXY：https://space.bilibili.com/3493142110144946")
    cm()
home()
