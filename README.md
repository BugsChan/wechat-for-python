# python wechat
微信，风格类似于shell，可自动回复，可批量操作,基于python3和itchat库

使用方法：
1.安装python3
2.安装itchat
      方法：
      打开cmd，然后输入：
      pip install itchat
      或 pip3 install itchat
      
3.你可能需要安装_thread
      方法：
      打开cmd，输入：
      pip install _thread
      或 pip3 install _thread
      
4.把wechat.py文件放到任意文件夹里，打开cmd，输入：python3 wechat.py。
  这时会弹出一个窗口，其中有一个二维码，请用微信手机版扫描二维码然后在手机上确认，此时你已经登录完成。
  
5.等屏幕现出“wechat>>”字样的时候你就可以使用了。
    各种命令：
    0.users :获取你的所有朋友;
    1.aim -朋友名：切换到相应朋友；
    2.send 信息：向当前朋友（使用aim命令切换）发送信息，也可使用中文“送”代替 send；
    3.allsend 信息：将信息发送给所有朋友
    4.backList -show：显示自动回复消息的列表
    5.backList -rm：删除所有自动回复消息
    6.addret 消息：向自动回复消息列表中增加消息
    7.rmret 消息：从自动回复消息列表中删除消息
    8.autoBack -true:设置对当前朋友（使用aim命令切换）的消息自动回复，回复的消息将从自动回复消息列表中随机抽取，如未使用addret增加列表，则程序不会回复消息。
    9.autoBack -all:自动回复所有朋友的消息，回复内容同上
    10.autoBack -no:取消消息的自动回复
    11.autosend -time:给当前朋友多次发送消息，内容同自动回复的一样，即从自动回复消息的列表中随机抽取；
