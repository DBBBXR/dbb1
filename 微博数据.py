import requests
from jsonpath import jsonpath
import time
import random      #给随机值


class weibospider(object):
    def __init__(self):
        #一级评论
        self.url = 'https://weibo.com/ajax/statuses/buildComments'
        self.one_data = {
            'is_reload': '1',
            'id': '4992207050510189',
            'is_show_bulletin': '2',
            'is_mix': '0',
            'count': '10',
            'uid': '1790550774',
            'fetch_level': '0',
            'locale': 'zh - CN'
        }
        self.two_data = {
            'is_reload': '1',
            'id': '4992223049679700',
            'is_show_bulletin': '2',
            'is_mix': '1',
            'fetch_level': '1',
            'max_id': '0',
            'count': '20',
            'uid': '1790550774',
            'locale': 'zh-CN'
        }
        self.headers = {
            'User-Agent':'Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,dlike Gecko)Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'Referer':'https://weibo.com/1790550774/NCGJ328IR',
            'Cookie':'SINAGLOBAL=6113273408956.228.1658658198158; ALF=1708324592; SUB=_2A25IrxmgDeThGeFI6loT9C3JyjyIHXVrxRNorDV8PUJbkNANLWbMkW1NfVhh54ubu_T-Tdttf64nbCo_2j7jLs-w; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5MbO_Hro3-v-rfEXmSlRHf5JpX5KzhUgL.FoMceKnEShefeK52dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNSo2ReoB0SK27; _s_tentry=www.weibo.com; Apache=8453981949948.722.1705732848852; ULV=1705732848879:1:1:1:8453981949948.722.1705732848852:; XSRF-TOKEN=uGH_M3vzcwZQvbwzdiZeM-z9; WBPSESS=9RO06aZ9J6eXme_t-ZaCguX5pbNAvFc-iDY_4Fuk0KrO5R1vczlI4AJnzIslH2_F4hbjPSvcW_eWinHnu8IqN7C005KcEuGW4bNVVXsWuH0SXM8IC3ZK1KOPLUyGRum5mxx7ut-0KIBkp5lIbsKi8A=='

        }

    def get_one_data(self):
        #获取一级评论相关数据
        response = requests.get(self.url,headers=self.headers,params=self.one_data)
        json_data = response.json()
        one_text = jsonpath(json_data,'$..data.*.text_raw')
        one_name = jsonpath(json_data,'$..data.*.user.screen_name')
        root_ids =  jsonpath(json_data,'$..data.*.rootid')
        total_numbers = jsonpath(json_data,'$..data.*.total_number')


        print(len(one_text),len(one_name))
        for one_texts,one_names,root_id,total_number in zip(one_text,one_name,root_ids,total_numbers):
            print(one_texts,'-------------->',one_names)
            print('======================================================================================')


            #判断二级评论是否有内容，如果没有就不调用
            if total_number == 0:
                print('此用户二级评论没有内容')

            else:
                # 重新传入id
                self.two_data['id'] = root_id
                # 调用二级评论
                self.get__two_data()



            #翻页
            #翻页逻辑：获取上一页的maxid
        max_id = jsonpath(json_data,'$..max_id')[0]
        print(max_id)
        print('------------------------------------------------------------------------------------------')
            #更改参数实现翻页
        self.one_data['max_id'] = max_id
        self.one_data['flow'] = '0'
        self.one_data['count'] = '20'
        # 生成时间减缓访问频率random随机生成randint随机生成整数2-6秒之间才开始访问模仿人工操作
        time.sleep(random.randint(2,6))
        # 递归调用
        self.get_one_data()
        #多数伪装，因为微博反扒机制一个用户拿取数据有限，可以用不同cookie或多数切换代理ip让微博反扒机制找不到

    def get__two_data(self):
        try:
            response = requests.get(self.url,headers=self.headers,params=self.two_data)
            json_data = response.json()
            one_name = jsonpath(json_data, '$..data.*.user.screen_name')
            id_data = jsonpath(json_data,'$..data.*.user.id')
            dizidata = jsonpath(json_data,'$..data.*.user.location')
            one_text = jsonpath(json_data, '$..data.*.text_raw')
            print(len(one_name), len(id_data), len(dizidata), len(one_text))
            for one_names,id_datas,dizidatas,one_text in zip(one_name,id_data,dizidata,one_text):
                print('名称：%s'%(one_names))
                print('账号id编号：%s'%(id_datas))
                print('用户的地址：%s'%(dizidatas))
                print('发表言论：%s'%(one_text))
                print('-------------------------------------------------------------------------')
        except Exception as e:
            self.one_data['max_id'] = 0

            print('二级评论已经取完')

        else:

            #二级翻页
            max_id = jsonpath(json_data, '$..max_id')[0]
            print(max_id)
            #更改参数
            self.two_data['max_id'] = max_id
            time.sleep(random.randint(4, 8))
            if max_id == 0:
                print('二级翻页结束')
            else:
                self.get__two_data()





    def run(self):
        self.get_one_data()
        # self.get__two_data()



if __name__ == '__main__':
    wbs = weibospider()
    wbs.run()