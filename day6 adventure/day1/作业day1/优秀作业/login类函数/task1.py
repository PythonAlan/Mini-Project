#/usr/bin/env python3
#antuor:cj
# -*- coding:utf-8 -*-
import json
import logging
#from prettytable import PrettyTable

class task1(object):
    def __init__(self):
        self.read_from_txt()
        self.make_userlist()


    def read_from_txt(self):
        user_txt=open("users","r")
        txt_lines=user_txt.readlines()
        self.users = []  #user_list
        for i in range(len(txt_lines)):
            self.users.append(json.loads(txt_lines[i].strip().strip("\n")))
        user_txt.close()

#make an user index
    def make_userlist(self):
        #read from self.users and make  dict,link by username
        self.user_list = {}
        for i in range(len(self.users)):
            #id:2,passwd:123,tag:unlocked,superuser:no
            user = self.users[i]
            temp = {}
            #print(user.keys())
            temp["id"]=user["id"]
            temp["passwd"]=user["information"]["authentication"]["passwd"]
            temp["tag"]=user["status"]["tag"]
            temp["superuser"]=user["status"]["superuser"]
            self.user_list[user["information"]["authentication"]["username"]]= temp
        print(self.user_list)
        self.user_id_num = len(self.users)

#login model
    def login_model(self):
        username_count = 0
        while True:
            self.username = input("please input username:")
            if self.username not in self.user_list.keys():
                print("bad username")
                username_count = username_count + 1
                if username_count == 2:
                    print("foolish")
                    break
                else:
                    continue
            else:
                if self.user_list[self.username]["tag"] == "locked":
                    print("this user is locked")
                    continue
                for i in range(3):
                        passwd = input("please input password:")
                        if passwd == self.user_list[self.username]["passwd"]:
                            if self.user_list[self.username]["superuser"] == "yes":
                                print("Hello " + self.username +" login successfully")
                                self.superuser_menu()
                            else:
                                print("Hello " + self.username +" login successfully")
                                self.commonuser_menu()
                        else:
                            print("key error")
                            chance_number = str(2 - i)
                            print("you have " + chance_number + " chance")
                            if i == 2:
                                print("sorry,this user would be locked immediately")
                                self.user_list[self.username]["tag"] = "locked"
                                id = self.user_list[self.username]["id"]
                                for i in range(self.user_id_num):
                                    if self.users[i]["id"] == id:
                                        self.users[i]["status"]["tag"] = "locked"
                                        self.write_to_txt()
                                        #print(self.users[i])
                                        break


#modify txt
    def write_to_txt(self):
        f = open("users","w")
        for i in range(self.user_id_num):
            line = json.dumps(self.users[i]) + "\n"
            #print(line)
            f.write(line)
        f.close()
        self.make_userlist()

#complete
    def superuser_menu(self):
        print("***********************")
        print("1.add user")
        print("2.unlocked user")
        print("3.list all of users' information")
        print("4.logout")
        print("***********************")
        action_id = input("please input action id:")
        if action_id == "1":
            self.superuser_add_user()
        elif action_id == "2":
            self.superuser_unlocked_user()
        elif action_id == "3":
            self.superuser_list_info()
        elif action_id == "4":
            self.username = " "
            self.login_model()
        else:
            print("input error")
            self.superuser_menu()

#complete  superuser_add_user
    def superuser_add_user(self):
        print("superuser_add_user")
        #do action
        while True:
            username = input("input username")
            if username:
                break
            else:
                print("username can not be null")
        while True:
            passwd = input("input passwd")
            if passwd:
                break
            else:
                print("passwd can not be null")
        name = input("please input name")
        age = int(input("please input age"))
        make_sure = input("do you want to set passwd question y/n")
        pwd_ques = []
        while make_sure == "y" or make_sure == "yes":
            qanda = {}
            question = input("input question")
            answer = input("input answer")
            qanda[question]=answer
            pwd_ques.append(qanda)
            conti = input("continue input q&a? y/n")
            if conti != "y" or conti != "yes":
                break
        superuser = input("is this user is a superuser? y/n")
        if superuser == "y" or superuser == "yes":
            superuser = "yes"
        else:
            superuser = "no"
        authentication = {}
        authentication["username"]=username
        authentication["passwd"]=passwd
        authentication["unpass_question"]=pwd_ques

        new_user_info = {}
        new_user_info["name"]=name
        new_user_info["age"]=age
        new_user_info["authentication"]=authentication

        new_user_status = {}
        new_user_status["tag"]="unlocked"
        new_user_status["superuser"]= superuser

        new_user = {}
        new_user["id"]=self.user_id_num + 1
        new_user["status"]= new_user_status
        new_user["information"] = new_user_info
        print(new_user)
        self.user_id_num = self.user_id_num + 1
        self.users.append(new_user)
        print(self.users)
        self.write_to_txt()
        self.read_from_txt()
        action = input("press b,back to menu")
        if action == "b":
            self.superuser_menu()
        pass

#complete superuser_unlocked_user
    def superuser_unlocked_user(self):
        print("superuser_unlocked_user")
        x = PrettyTable(["id","username","tag"])
        x.align["id"] = "1"
        x.padding_width = 1
        for i in self.user_list.keys():
            tem_id = self.user_list[i]["id"]
            tem_uname = i
            tem_tag = self.user_list[i]["tag"]
            x.add_row([tem_id,tem_uname,tem_tag])
        print(x)
        x.clear_rows()
        unlock_id = int(input("which user id you want to unlocked:"))
        if unlock_id <= self.user_id_num:
            for i in range(self.user_id_num):
                if self.users[i]["id"] == unlock_id and self.users[i]["status"]["tag"] == "locked":
                    make_sure = input("make sure y/n:")
                    if make_sure == "y" or make_sure == "yes":
                        self.users[i]["status"]["tag"] = "unlocked"
                        self.write_to_txt()
                        self.read_from_txt()
                        self.make_userlist()
                        for i in self.user_list.keys():
                            tem_id = self.user_list[i]["id"]
                            tem_uname = i
                            tem_tag = self.user_list[i]["tag"]
                            x.add_row([tem_id,tem_uname,tem_tag])
                        print(x)
                        break
                    else:
                        print("bad value")
                        break
                else:
                    if self.users[i]["id"] == unlock_id:
                        print("this user is not locked")
        else:
            print("bad value")
        action = input("press b,back to menu")
        if action == "b":
            self.superuser_menu()

#complete superuser_list_info
    def superuser_list_info(self):
        print("superuser_list_info")
        print_table = PrettyTable(["id","username","name","age","tag","superuser"])
        print_table.align["id"] = "1"
        print_table.padding_width = 1
        for i in range(self.user_id_num):
            id = self.users[i]["id"]
            username = self.users[i]["information"]["authentication"]["username"]
            name = self.users[i]["information"]["name"]
            age = self.users[i]["information"]["age"]
            tag = self.users[i]["status"]["tag"]
            superuser = self.users[i]["status"]["superuser"]
            print_table.add_row([id,username,name,age,tag,superuser])
        print(print_table)
        action = input("press b,back to menu")
        if action == "b":
            self.superuser_menu()
        pass


    def commonuser_menu(self):
        print("***********************")
        print("1.modify passwd")
        print("2.lock me")
        print("3.my information")
        print("4.logout")
        print("***********************")
        action_id = input("please input action id:")
        pass




if __name__ == "__main__":
    tt = task1()
    tt.login_model()

#logging
#backup
#logout