import scrapy
from bs4 import BeautifulSoup as BS
import os
from baidu.items import BaiduItem
import re
province=
class BDSpider(scrapy.Spider):
    name = "baidu"
    #allowed_domains = ["dmoz.org"]
    #province='guizhou'
    if not os.path.exists('E:/Py/com/2008a/'+province):
        os.mkdir('E:/Py/com/2008a/'+province)
    url="http://zhaopin.baidu.com/company?query="
    start_urls = []
    with open('E:/Py/com/minglu/a/'+province+'.txt','r',encoding='utf-8') as f:
    	keys=f.read().split()
    for k in keys[:]:
    	start_urls.append(url+k)
    count=0  
    allnum=len(start_urls)  
    print(allnum)

    def parse(self, response):
        #print(response.body)
        item=BaiduItem()
        soup=BS(response.body,'lxml')
        print(soup.title.text,self.count,self.allnum)
        self.count+=1
        if soup.title.text.strip()!='__全网最全的公司信息聚合':
            
            com=soup.find('span',class_="title line-clamp1").text.strip()
            filename='E:/Py/com/2008a/'+province+'/'+com+'.txt'
            s1=soup.find('div',class_='top mb16')
            s2=soup.find('div',class_='left width-left')
            with open(filename,'w',encoding='utf-8') as f:
               f.write(str(s1)+'\n'+str(s2))
            
            item["url"]=''
            item["company"]=''
            item["website"]=''
            item["province"]=''
            item["headquarters"]=''
            item["industry_b"]=''
            item["welfare"]=''
            item['工商注册号']=''
            item['组织机构代码']=''
            item['统一信用代码']=''
            item['经营状态']=''
            item['行业']=''
            item['企业类型']=''
            item['法定代表人']=''
            item['营业期限']=''
            item['注册资本']=''
            item['核准日期']=''
            item['登记机关']=''
            item['企业地址']=''
            item['经营范围']=''
            item['企业联系电话']=''
            item['电子邮箱']=''
            item['主要人员']=''
            item['股东信息']=''
            item['热招职位']=''
        
            item["website"]=response.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[2]/div/a/text()').extract_first()
            item["url"]=response.url
            item["company"]=response.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/span/text()').extract_first().strip()
            item["province"]=province
            t=soup.find('div',class_="base").text
            if re.search('总部地点',t):
                item["headquarters"]=t[re.search('总部地点',t).end()+1:re.search('总部地点\S*',t).end()]
            if re.search('所属行业',t):
                item["industry_b"]=t[re.search('所属行业',t).end()+1:re.search('所属行业\S*',t).end()]
            if re.search('公司福利',t):
                item["welfare"]=t[re.search('公司福利',t).end()+1:re.search('公司福利\S*',t).end()]
            if soup.find('div',class_="gszc"):
                for t in soup.find('div',class_="gszc").div.find_all('td',class_="tr-title"):
                    item[t.text[:-1]]=t.next_sibling.next_sibling.text
            t=soup.find('div',class_="qynb").find_all('td')
            for tdn in range(len(t)):
                if t[tdn].text=='电子邮箱：':
                    item["电子邮箱"]=t[tdn+1].text
                elif t[tdn].text=='企业联系电话：':
                    item["企业联系电话"]=t[tdn+1].text

            for t in soup.find('div',class_="gszc").find_all('h2')[1:]:
                if t.text=='主要人员':
                    st=''
                    for td in t.next_sibling.next_sibling.find_all('td',class_="tr-title"):
                        st+=td.text+td.next_sibling.next_sibling.text+';'
                    item["主要人员"]=st[:-1]
                    
                elif t.text=='股东信息':
                    st=''
                    if len(t.next_sibling.next_sibling.find_all('tr'))>1:
                        for tr in t.next_sibling.next_sibling.find_all('tr')[1:]:
                            for td in tr.find_all('td'):
                                st+=td.text+','
                            st=st[:-1]+';'
                    item["股东信息"]=st[:-1]
            st=''
            for a in soup.find('div',class_="position").find_all('a'):
                if not a.span:
                    break
                st+=a.span.text+','
                for p in a.find_all('p'):
                    st+=p.text+','
                st=st[:-1]+';'
            item["热招职位"]=st[:-1]
            yield item
        #filename = 'a.txt'
        #with open(filename, 'wb') as f:
        #    f.write(response.body)