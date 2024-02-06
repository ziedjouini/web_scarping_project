# 1st step install and import moduls 
# pip/pip3 install lxml
#pip/pip3 install requests
#pip/pip3 install beautifulsoup4
import requests 
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title=[]
company_name=[]
location_name=[]
skills=[]
links=[]
#2nd step use requests to fetch the url 
result=requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

#3rd step save page content/markup
src=result.content
#print(src)

# 4th step create soup objec to parse content 
soup =BeautifulSoup(src, "lxml")
#print(soup)

# 5th step find the elements containing info we need
# job titles, job skills , company names , location names 
job_titles=soup.find_all("h2",{"class":"css-m604qf"})
#print(job_titles)
company_names=soup.find_all("a",{"class":"css-17s97q8"})
#(company_names)
location_names=soup.find_all("span",{"class":"css-5wys0k"})
#print(location_names)
job_skills=soup.find_all("div",{"class":"css-y4udm8"})
#print(job_skills)

# 6th step loop over returned lists to extract needed info into others lists
for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    links.append(job_titles[i].find("a").attrs['href'])
    company_name.append(company_names[i].text)
    location_name.append(location_names[i].text)
    skills.append(job_skills[i].text)
#print(job_skill)
    
#7th step create csv file file and fill it with values 
file_list=[job_title,company_name,location_name,skills,links]
exported=zip_longest(*file_list)
with open("c:\\Users\\ziedj\\Documents\\python programms vs\\jobstutorial.csv" , "w") as myfile:
    wr= csv.writer(myfile)
    wr.writerow(["job title","company name","location","skills","links"])
    wr.writerows(exported)

#8th step to frtch the link of the job and fectch in page details 