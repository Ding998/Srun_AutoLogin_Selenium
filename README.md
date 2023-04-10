# Srun_AutoLogin_Selenium
深澜软件校园网自动登录（基于Selenium的Python脚本，国科大中关村宿舍区测试）

## 背景
日常需要远程访问宿舍的电脑，但宿舍的深澜校园网时不时自动登出，导致断网影响使用。

## 目标
周期性检测深澜校园网的登录状态，一旦断联，自动登录。

## AutoLogin2UCAS.py功能
1. 判断登录页面的状态
    - 如果页面有“登录”按钮，即有id为login-account的网页元素，判定为**未登录**状态
    - 如果页面有“注销”按钮，即有id为logout的网页元素，判定为**已登录**状态
    - 等待网页加载的时间为3s，超过3s没有结果则判定**超时**
2. 如果登录页面处在**未登录**状态，自动填写用户名（username）和密码（password），点击登录（login-account）按钮

## 使用方法
1. 安装[Python](https://www.python.org/downloads/windows/)，配置环境变量
    - 不详述
2. 安装selenium包（用于模拟浏览器）和pyinstaller包（用于打包exe）
    - <kbd>Win</kbd>+<kbd>R</kbd> &rArr; <kbd>c</kbd><kbd>m</kbd><kbd>d</kbd> &rArr; <kbd>Enter</kbd>
    - ```pip3 install selenium```
    - ```pip3 install pyinstaller```
3. 修改python脚本
    - 下载AutoLogin2UCAS.py到本地
    - 使用记事本打开AutoLogin2UCAS.py
    - 替换第13/14行的```xxxxxxxx```/```xxxxxxxx```为你的登录账号/密码
    - 第9行的URL是登录页面网址，视情况修改
    - 第17行指定浏览器，如果电脑没有Chrome可以替换为
        - Edge浏览器：```driver = webdriver.Edge()```
        - FireFox浏览器：```driver = webdriver.FireFox()```
4. 将修改后的python脚本打包成exe文件
    - 到AutoLogin2UCAS.py的本地目录下，在[地址栏](#jump)直接输入<kbd>c</kbd><kbd>m</kbd><kbd>d</kbd><kbd>Enter</kbd>
    - ```pyinstaller -F -w AutoLogin2UCAS.py```
    - 然后在当前目录下会产生几个文件和文件夹，打开dist文件夹，其中AutoLogin2UCAS.exe就是我们需要的可执行文件
        <div align="center">
            <img src="./FIG/02%20after_pyinstaller.png" alt="Editor" width="460">
        </div>
        <div align="center">
            <img src="./FIG/03%20dist_exe.png" alt="Editor" width="547">
        </div>    
5. 在任务计划程序中创建任务，周期性执行AutoLogin2UCAS.exe
    - 打开任务计划程序：<kbd>Win</kbd>+<kbd>R</kbd> &rArr; <kbd>t</kbd><kbd>a</kbd><kbd>s</kbd><kbd>k</kbd><kbd>s</kbd><kbd>c</kbd><kbd>h</kbd><kbd>d</kbd><kbd>.</kbd><kbd>m</kbd><kbd>s</kbd><kbd>c</kbd> &rArr; <kbd>Enter</kbd>
    - 点击右侧栏的“创建任务…”
        <div align="center">
            <img src="./FIG/04%20taskschd_0.PNG" alt="Editor" width="909">
        </div>
    - 参照下列截图设置任务：
        <div align="center">
            <img src="./FIG/05%20taskschd_1.PNG" alt="Editor" width="474">
        </div>
        <div align="center">
            <img src="./FIG/06%20taskschd_2.PNG" alt="Editor" width="487">
        </div>
        <div align="center">
            <img src="./FIG/07%20taskschd_3.PNG" alt="Editor" width="489">
        </div>
        <div align="center">
            <img src="./FIG/08%20taskschd_4.PNG" alt="Editor" width="474">
        </div>
        <div align="center">
            <img src="./FIG/09%20taskschd_5.PNG" alt="Editor" width="474">
        </div>
        
## 补充说明
- 根据我的经验，每次“登录”或“注销”后会有几秒到几十秒的时间无法加载出登录页面。如果你按照以上的截图设置了任务，那等一两分钟就好了。 
- <span id="jump">不认识“地址栏”的看下图：</span>
    <div align="center">
        <img src="./FIG/01%20cmd_currentDir.png" alt="Editor" width="446">
    </div>
