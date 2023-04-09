# Srun_AutoLogin_Selenium
深澜软件校园网自动登录（基于Selenium的Python脚本，国科大中关村宿舍区测试）

## 背景
宿舍有台电脑，日常远程访问该电脑，但深澜校园网时不时自动登出，断网后得回去重新登录。

## 目标
周期性检测深澜校园网的登录状态，一旦断联，自动登录。

## 具体步骤
1. 安装[Python](https://www.python.org/downloads/windows/)，配置环境变量
    - 不详述
2. 安装selenium包和pyinstaller包
    - <kbd>Win</kbd>+<kbd>R</kbd> &rArr; <kbd>c</kbd><kbd>m</kbd><kbd>d</kbd> &rArr; <kbd>Enter</kbd>
    - ```pip3 install selenium```
    - ```pip3 install pyinstaller```
3. 修改脚本AutoLogin2UCAS.py
    - 下载AutoLogin2UCAS.py到本地
    - 使用记事本打开AutoLogin2UCAS.py
    - 修改第13&14行的登录账号&密码为你的
    - 第9行的URL是登录页面网址，视情况修改
4. 将修改后的python脚本打包成exe文件
    - 到AutoLogin2UCAS.py的本地目录下，在地址栏直接输入<kbd>c</kbd><kbd>m</kbd><kbd>d</kbd><kbd>Enter</kbd>
    - ```pyinstaller -F -w AutoLogin2UCAS.py```
    - 然后在当前目录下会产生几个文件和文件夹，打开dist文件夹，其中AutoLogin2UCAS.exe就是我们需要的可执行文件
5. 在任务计划程序中添加任务，周期性运行AutoLogin2UCAS.exe
    - 打开任务计划程序：<kbd>Win</kbd>+<kbd>R</kbd> &rArr; <kbd>t</kbd><kbd>a</kbd><kbd>s</kbd><kbd>k</kbd><kbd>s</kbd><kbd>c</kbd><kbd>h</kbd><kbd>d</kbd><kbd>.</kbd><kbd>m</kbd><kbd>s</kbd><kbd>c</kbd> &rArr; <kbd>Enter</kbd>
    - 点击右侧栏的“创建任务…”
    - 按照下图设置：
    
    
    
