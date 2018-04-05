import itchat;
import sys;
import _thread;
import random;
itchat.auto_login(hotReload=True);

class myTool:
    to="";
    attr="wechat";
    backlist=[];
    back=False;
    oneAttrTypes=["send","allsend","addret","rmret"];
    allback=False;
    def oneAttr(self,command):
        for each in self.oneAttrTypes:
            if command.startswith(each+" "):
                return True;
        return False;
    def getCommand(self,command):
        if command.startswith("送 "):
            command="send "+command[2:];
        
        if self.oneAttr(command):
            index=command.find(' ');
            return [command[:index],command[index+1:]];
        while command.find("  ")!=-1:
            command=command.replace("  "," ");
        if command.find(' ')==-1:
            return [command];
        res=command.split(' ');
        ret=[];
        for each in res:
            if each.startswith('-'):
                ret.append(each[1:]);
            else:
                ret.append(each);
        return ret;

    def autosend(self,time):
        time=int(time);
        for each in range(time):
            temp=random.randint(0,len(self.backlist)-1);
            ret=self.backlist[temp];
            itchat.send(ret,toUserName=self.to);
        print(self.attr+">>发送完成");

    def init(self):
        userInput=input(self.attr+">>");
        while userInput!="exit":
            res=self.getCommand(userInput);
            if not hasattr(self,res[0]):
                print(self.attr+">>Sorry,你的输入有误");
            else:
                try:
                    fun=getattr(self,res[0]);
                    if len(res)==1:
                        fun();
                    elif len(res)==2:
                        fun(res[1]);
                    elif len(res)==3:
                        fun(res[1],res[2]);
                    else:
                        print(self.attr+">>参数太多!");
                except:
                    print(self.attr+">>输入错误!!!");
            userInput=input(self.attr+">>");
        print("EXIT,Good by");
        itchat.logout();
        
    def send(self,msg):
        itchat.send(msg,toUserName=self.to);
    
    def allsend(self,msg):
        for each in self.friends.keys():
            itchat.send(msg,toUserName=self.friends[each]);
        print("所有朋友已发送完成");


    def aim(self,username):
        if username in self.friends:
            print(self.attr+">>已切换至"+username);
            self.to=self.friends[username];
            self.attr=username;
        else:
            print(self.attr+">>Sorry,你这个朋友不存在!");

    def users(self,show=True):
        friends=itchat.get_friends(update=True);
        res={};
        for each in friends:
            remarkName=each["RemarkName"]
            if remarkName=="":
                remarkName=each["NickName"];
            username=each["UserName"];
            res[remarkName]=username;
        self.friends=res;
        if show==True:
            for each in res.keys():
                print(self.attr+">>我的好友:",each);

    def addret(self,des):
        if not des in self.backlist:
            self.backlist.append(des);
            print(self.attr+">>你已成功添加 '"+des+"' 到回复列表中");
        else:
            print(self.attr+">>Sorry, '"+des+"' 在回复列表中已存在");

    def rmret(self,des):
        if des in self.backlist:
            self.backlist.remove(des);
            print(self.attr+">> '",des,"' 已经从回复列表中移除");
        else:
            print(self.attr+">>Sorry, '"+des+"' 在回复列表中不存在");

    def autoBack(self,chose="True"):
        if chose.upper()=="TRUE":
            self.back=True;
            print(self.attr+">>已成功设置自动回复");
        elif chose.upper()=='ALL':
            self.back=True;
            self.allback=True;
            print(self.attr+">>设置为自动回复所有朋友");
        else:
            self.allback=False;
            self.back=False;
            print(self.attr+">>已成功取消自动回复");

    def backList(self,_type="show"):
        if _type=="rm":
            self.backlist.clear();
            print(self.attr+">>已成功注销所有回复");
        else:
            for each in self.backlist:
                print(self.attr+">>"+each);

    def __init__(self):
        self.users(show=False);

tool=myTool();
_thread.start_new_thread(tool.init,());
#tool.init();

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    if msg["User"]["UserName"]==tool.to or tool.allback:
        print(msg.text+"\n"+tool.attr+">>",end="");
        if tool.back and len(tool.backlist)>0:
            temp=random.randint(0,len(tool.backlist)-1);
            ret=tool.backlist[temp];
            print("send "+ret,"\n",tool.attr+">>",end="");
            return ret;
            


itchat.run();
