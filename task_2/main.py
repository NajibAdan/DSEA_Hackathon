from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Firefox()
def to_csv(list):
    with open('results.csv', 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
        wr.writerows(list)
def main(url):
    postings = []
    for i in range(0,40,10):
        driver.get(url+str(i))

        results = driver.find_elements(By.CLASS_NAME,'resultContent')
        
        for result in results:
            job_title = result.find_element(By.CLASS_NAME,'jobTitle').text.replace(',','')
            company = result.find_element(By.CLASS_NAME,'companyName').text.replace(',','')
            location = result.find_element(By.CLASS_NAME,'companyLocation').text.replace(',','').replace('\n','')
            salary = result.find_elements(By.CLASS_NAME,'estimated-salary-container')
            if salary:
                salary = salary[0].text.replace(',','')
            else:
                salary = None
            postings.append([job_title,company,location,salary])
    to_csv(postings)

if __name__=="__main__":
    url = 'https://www.indeed.com/jobs?q=data+scientist&start='
    main(url)