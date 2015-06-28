<div id="table-of-contents">
<h2>&#30446;&#24405;</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#sec-1">1. mac快捷键</a></li>
<li><a href="#sec-2">2. Cmd Tab技巧</a>
<ul>
<li><a href="#sec-2-1">2.1. Cmd Tab切换程序不显示窗口</a></li>
<li><a href="#sec-2-2">2.2. Cmd Tab反方向选择应用程序</a></li>
<li><a href="#sec-2-3">2.3. Cmd Q退出</a></li>
<li><a href="#sec-2-4">2.4. Cmd H隐藏</a></li>
<li><a href="#sec-2-5">2.5. Cmd Tab时鼠标滚轮左右选择</a></li>
<li><a href="#sec-2-6">2.6. Cmd Tab时左右键左右选择</a></li>
<li><a href="#sec-2-7">2.7. Cmd `</a></li>
</ul>
</li>
<li><a href="#sec-3">3. Terminal里Options作为meta键</a></li>
<li><a href="#sec-4">4. ShiftIt管理窗口</a></li>
<li><a href="#sec-5">5. 行首行尾</a></li>
<li><a href="#sec-6">6. 命令行加载.bashrc</a></li>
<li><a href="#sec-7">7. 显示隐藏文件</a></li>
<li><a href="#sec-8">8. 终端大小写不敏感</a></li>
<li><a href="#sec-9">9. 安装Goldendict</a></li>
<li><a href="#sec-10">10. 打开多个应用程序实例</a></li>
<li><a href="#sec-11">11. office</a></li>
<li><a href="#sec-12">12. MATLAB2014A模糊</a></li>
<li><a href="#sec-13">13. Cmd+d 创建当前文件复本</a></li>
<li><a href="#sec-14">14. 剪切</a></li>
<li><a href="#sec-15">15. delete键</a></li>
<li><a href="#sec-16">16. OS X更改默认打开文件应用程序</a>
<ul>
<li><a href="#sec-16-1">16.1. 为单个文件设置默认打开时使用的程序</a></li>
<li><a href="#sec-16-2">16.2. 为打开同一种文件类型设置默认应用。</a></li>
</ul>
</li>
<li><a href="#sec-17">17. 快速创建便笺</a></li>
<li><a href="#sec-18">18. 拖动窗口时保持窗口层叠位置</a></li>
<li><a href="#sec-19">19. 禁止系统进入休眠状态</a></li>
<li><a href="#sec-20">20. 隐藏桌面上其它程序</a></li>
<li><a href="#sec-21">21. 关闭通知</a></li>
<li><a href="#sec-22">22. 截屏</a></li>
<li><a href="#sec-23">23. 配置Eclipse CDT</a></li>
<li><a href="#sec-24">24. X Lossless Decoder</a></li>
<li><a href="#sec-25">25. alfred</a></li>
<li><a href="#sec-26">26. Paragon NTFS</a></li>
<li><a href="#sec-27">27. go2shell</a></li>
<li><a href="#sec-28">28. zsh</a>
<ul>
<li><a href="#sec-28-1">28.1. 安装</a></li>
<li><a href="#sec-28-2">28.2. 导入bash history</a></li>
<li><a href="#sec-28-3">28.3. autojump</a></li>
</ul>
</li>
<li><a href="#sec-29">29. matlab yosemite</a></li>
<li><a href="#sec-30">30. 为连接VPN添加快捷键</a></li>
</ul>
</div>
</div>
<link rel="stylesheet" type="text/css" href="../../layout/css/bootstrap_old.css" />
<link rel="stylesheet" type="text/css" href="../../layout/css/too_many_toc.css" />
<script src="../../layout/js/jquery_1.7.1.js"></script>
<script src="../../layout/js/bootstrap_old.js"></script>

# mac快捷键

<http://support.apple.com/kb/HT1343?viewlocale=zh_CN&locale=zh_CN>  

# Cmd Tab技巧

## Cmd Tab切换程序不显示窗口

Command+Tab到需要切换的程序，按住Command不松，按住Option，然后松开Command  

## Cmd Tab反方向选择应用程序

Cmd+~  

## Cmd Q退出

## Cmd H隐藏

## Cmd Tab时鼠标滚轮左右选择

## Cmd Tab时左右键左右选择

## Cmd \`

切换同个app不同窗口。  

# Terminal里Options作为meta键

Terminal／Preferences／Keyboard，勾选“Use Option As Meta Key”  
这样就可以options-b/a前后移动单词了  

# ShiftIt管理窗口

可轻松用快捷键实现窗口管理：窗口占据上/下/左/右半屏，窗口最大化，当前窗口居中等操作均绑定快捷键  

# 行首行尾

Cmd-左右方向键  

# 命令行加载.bashrc

    if [ -f ~/.bashrc ]; then
    . ~/.bashrc
    fi   

加入到/etc/profile中。  

# 显示隐藏文件

<http://jingyan.baidu.com/article/86fae346947c453c48121a66.html>  

    defaults write com.apple.finder AppleShowAllFiles -bool true
    defaults write com.apple.finder AppleShowAllFiles -bool false   

# 终端大小写不敏感

在HOME目录下的.inputrc中加入以下说一句并重启终端  

    set completion-ignore-case on
    set show-all-if-ambiguous on
    TAB: menu-complete   

# 安装Goldendict

Goldendict已经支持Retina屏幕。  

1.  下载源码<https://github.com/goldendict/goldendict>

2.  安装QT $brew install qt &#x2013;build-from-source

3.  编译Goldendict $qmake && make

4.  将生成的Goldendict.app拷贝到/Applications中

# 打开多个应用程序实例

Cmd+Space打开应用程序时只能打开一个，即当前如果有应用程序正在运行则会打开正在运行的而不会新打开另外一个应用程序。  
可以使用open命令加-n选项来新打开另一个应用程序：  

    ~$open -n /Applications/Emacs.app

# office

mac下破解office <http://soft.macx.cn/soft4350.html>  

# MATLAB2014A模糊

<http://www.mathworks.com/matlabcentral/answers/103056-how-do-i-change-the-java-virtual-machine-jvm-that-matlab-is-using-for-mac-os>  

    export MATLAB_JAVA="/Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home"
    open /Applications/MATLAB_R2014a.app   

# Cmd+d 创建当前文件复本

# 剪切

MAC没有直接的剪切操作，可以用COMMAND+C拷贝，然后按住option按键，再COMMAND+V粘贴操作，就可以剪切文件了。  

# delete键

1.  fn+delete 键，删除光标之后的一个字符

2.  option+delete 键，删除光标之前的一个单词

3.  command+delete 键，删除光标之前整行内容

4.  选中文件后按 command+delete，删除掉该文件

# OS X更改默认打开文件应用程序

## 为单个文件设置默认打开时使用的程序

　　在Finder里的文件上使用右键（或Control＋左键）点击后，按住Alt，这时修你会看到原来的打开方式会变成总是以此方式打开。  
　　不要松Alt，然后在右边选择你想要选择的默认程序就好了。  

## 为打开同一种文件类型设置默认应用。

从Mac系统中选择一个想要更改文件类型。  
点击Conmmand+i来查看文件信息。  
点击打开方式并选择相应的程序然后按下全部更改（如果发现全部更新是灰的，说明你修改后的和之前的一样）并确认。  

# 快速创建便笺

复制文字后shift+cmd+y即可快速创建便笺  

# 拖动窗口时保持窗口层叠位置

拖动同时按住Cmd键  

# 禁止系统进入休眠状态

使用命令pmset noidle  

# 隐藏桌面上其它程序

opt+cmd+h  

# 关闭通知

opt+单击右上角通知图标  

# 截屏

Cmd+Shift+3/4  

# 配置Eclipse CDT

Eclipse help->install marketplace中搜索cdt安装。  
配置gdb <http://ntraft.com/installing-gdb-on-os-x-mavericks/>  
安装最新gcc4.9 使用  

    brew tap homebrew/versions
    brew install gcc49

将/usr/bin中的gcc和g++链接到/usr/local/Cellar/gcc49/4.9.1/bin中gcc-4.9和g++-4.9  

# X Lossless Decoder

转换音频格式  

# alfred

macx上下载破解版<http://soft.macx.cn/5412.htm>  
使用教程<http://www.cnbeta.com/articles/203640.htm>  

# Paragon NTFS

可以使用disk utility将移动硬盘分出ntfs格式的分区。  
<http://tieba.baidu.com/p/2560041739>  
<http://www.macx.cn/thread-2041108-1-1.html>  

# go2shell

可以实现在当前目录中打开终端，安装完毕之后进入应用程序文件夹中按住 option + command 拖动 Go2Shell 图标到 Finder 工具栏中即可。（如果不嫌难看，可以用这种方法把其它程序也放到 Finder 的工具栏中）  
删除时也需要opt+cmd  

# zsh

<http://macshuo.com/?p=676>  

## 安装

    brew install zsh
    brew install zsh-completions
    curl -L https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh | sh

## 导入bash history

以下脚本将bash history导入zsh  

<div class="accordion-group"> <div class="accordion-heading"> <a href="#CollapseIDbash-history-to-zsh-history" data-toggle="collapse" class="accordion-toggle">bash-history-to-zsh-history</a> </div> <div class="accordion-body collapse" style="height: 0px" id="CollapseIDbash-history-to-zsh-history"> <div class="accordion-inner">

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # 
    # This is how I used it:
    # $ cat ~/.bash_history | bash-history-to-zsh-history >> ~/.zsh_history
    
    import sys
    
    
    def main():
        timestamp = None
        for line in sys.stdin.readlines():
            line = line.rstrip('\n')
            if line.startswith('#') and timestamp is None:
                t = line[1:]
                if t.isdigit():
                    timestamp = t
                    continue
            elif timestamp:
                sys.stdout.write(': %s:0;%s\n' % (timestamp, line))
                timestamp = None
    
    
    if __name__ == '__main__':
        main()

</div> </div> </div>

## autojump

    brew install autojump
    source /usr/local/Cellar/autojump/22.2.4/etc/autojump.sh   

之后 `j 目录名` 即可跳转  

# matlab yosemite

<http://www.mathworks.com/matlabcentral/answers/143601-i-cannot-install-matlab-2014a-on-os-x-yosemite-10-10-public-beta>  

# 为连接VPN添加快捷键

<http://www.cnet.com/how-to/how-to-create-a-vpn-shortcut-in-os-x/>  
Automator中添加Utilities -> Run AppleScript  

    tell application "System Events"
       tell current location of network preferences
            set VPN to "这里修改为想要连接的VPN的名称"
            set VPNactive to connected of current configuration of service VPN
            if VPNactive then
                 disconnect service VPN
            else
                 connect service VPN
            end if
       end tell
    end tell

保存后在keyboard中添加快捷键。  
