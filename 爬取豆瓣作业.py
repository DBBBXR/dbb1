import requests
import re
import os
import jsonpath

                                                         #请求数据


                                                        # 豆瓣url
url = 'https://book.douban.com/'
                                                        # 伪装服务器
dats = {
'Cookie':'douban-fav-remind=1; bid=Am7hDIssUBw; ap_v=0,6.0; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1697369583%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_id.100001.3ac3=cba25530d713058d.1697369583.; _pk_ses.100001.3ac3=1; __utma=30149280.852061172.1663489434.1688362692.1697369584.8; __utmc=30149280; __utmz=30149280.1697369584.8.4.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt_douban=1; __utma=81379588.457203457.1697369584.1697369584.1697369584.1; __utmc=81379588; __utmz=81379588.1697369584.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; _vwo_uuid_v2=D686FFF2E9C521FFCBF9D9517EE2E0151|b0fdb6c03b8e4d40489591126b179b39; __yadk_uid=GGTho7YITuXJZAHAa5BI7xUdN6z1nyq0; _ga=GA1.1.852061172.1663489434; _ga_RXNMP372GL=GS1.1.1697369596.1.1.1697369612.44.0.0; __utmb=30149280.3.10.1697369584; __utmb=81379588.3.10.1697369584',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
}
res = requests.get(url,headers=dats)

print(res.status_code)                         #打印状态码

                                                       # 获取数据
html_data = res.text
# print(html_data)
#
# # data = res.content
# with open('豆瓣.html','w',encoding='utf-8') as szk:               #写入html格式
#      szk.write(html_data)



#      正则表达示
# with open('豆瓣.html','r',encoding='utf-8') as f:                          #读取写入
#     data = f.read()

                                                               #解析数据


recon = re.findall('<li>.*?<img\ssrc="(.*?.jpg)"\salt="(.*?)">.*?<a\shref=(.*?)\stitle="(.*?)">(.*?).*?<p>.*?<span\sclass=.*?>(.*?)</span>.*?<span\sclass=.*?>(.*?)</span>.*?<span\sclass=.*?>(.*?)</span>.*?',html_data,re.S)
# print(recon)
for i in recon:
    # print(len(i))
    # print(i)
    title_link = i[0]                                    #上面括号对应索引去掉空格
    shuming = i[1]
    tite = i[2]
    szk = i[3]
    neirong = i[5].strip()
    time = i[6].strip()
    cbs = i[7].strip()
    # print(photo)
    print(shuming)
    print(title_link)
    print(tite)
    print(szk)
    print(neirong)
    print(time)
    print(cbs)
    print('----------------------------------------------------')


                                                        #保存数据
    with open('豆瓣爬取数据.txt','a',encoding='utf-8') as d:
        d.write(shuming+'\n')
        d.write(title_link+'\n')
        d.write(tite+'\n')
        d.write(szk+'\n')
        d.write(neirong+'\n')
        d.write(time+'\n')
        d.write(cbs+ '\n')


    img_data = requests.get(title_link).content                           #请求图片链接
    if not os.path.exists('img豆瓣图'):    #not 只有不存在才会返回tu    判断文件是不是创建过
        os.mkdir('img豆瓣图')                                              #用os创建文件
    with open('img豆瓣图/{}.jpg'.format(shuming),'wb') as e:       #format  引入文件名
        e.write(img_data)




