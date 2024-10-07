import logging
from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By

class BossZhipinCrawler:
    def __init__(self, browser, jobs,  experience, degree, citys,):
        self.browser = browser
        self.jobs = jobs
        self.experience = experience
        self.degree = degree
        self.citys = citys
        self.selected_website = "BOSS 直聘"

    def login(self):
        self.browser.get('https://login.zhipin.com/')
        logging.info(f"[{self.selected_website}] Please scan qrcode to login {self.selected_website}")
        sleep(30)
        self.browser.refresh()

    def get_search_lists(self):
        urls = []
        for job in self.jobs:
            for city_code, city_name in self.citys.items():
                url = f'https://www.zhipin.com/web/geek/job?position=100102&city={city_code}&experience={self.experience}&degree={self.degree}'
                urls.append((url, f"{city_name}_{job}.xlsx"))
        return urls

    def get_jobs_lists(self, search_url: str, name: str):
        self.browser.get(search_url)
        logging.info(f"[{self.selected_website}] Sleep")
        sleep(6)
        logging.info(f"[{self.selected_website}] Wake Up")

        page_num_tags = self.browser.find_elements(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/a')
        logging.info(f"[{self.selected_website}] Capture page labels, length: {len(page_num_tags)}")
        if not page_num_tags:
            sleep(20)
            page_num_tags = self.browser.find_elements(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/a')

        try:
            page_num = int(page_num_tags[-2].text) if len(page_num_tags) > 3 else 1
            logging.info(f"[{self.selected_website}] Information total {page_num} pages, url: {search_url}")
            
            for page in range(1, page_num):
                logging.info(f"[{self.selected_website}] Crawling page {page+1}.")
                url = f"{search_url}&page={page+1}"
                self.browser.get(url)
                sleep(7)
                lis = self.browser.find_elements(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/ul/li')
                info = {
                    '公司': [], '岗位': [], '薪资': [], '福利': [], '经验要求': [],
                    '学历要求': [], '加分项目': [], '所属行业': [], '位置': [], '公司规模': []
                }
                
                for li in lis:
                    job_info = self.extract_job_info(li)
                    for key, value in job_info.items():
                        info[key].append(value)
                    
                    logging.info(f"[{self.selected_website}] [公司]: {job_info['公司']} [岗位]: {job_info['岗位']} "
                                 f"[薪资]: {job_info['薪资']} [福利]: {job_info['福利']} "
                                 f"[经验要求]: {job_info['经验要求']} [学历要求]: {job_info['学历要求']} "
                                 f"[加分项目]: {job_info['加分项目']} [所属行业]: {job_info['所属行业']} "
                                 f"[位置]: {job_info['位置']} [公司规模]: {job_info['公司规模']}")
                
                self.save_data(name, pd.DataFrame(info))
        except Exception as e:
            logging.error(f"[{self.selected_website}] Error occurred: {e}", exc_info=True)

    def extract_job_info(self, li) -> dict:
        job_name = li.find_element(By.CLASS_NAME, 'job-name').text
        salary = li.find_element(By.CLASS_NAME, 'salary').text
        addr = li.find_element(By.CLASS_NAME, 'job-area').text
        tag_list = li.find_elements(By.CLASS_NAME, 'tag-list')
        tag_list1 = [i for i in tag_list[0].find_elements(By.TAG_NAME, 'li') if i.text.strip()]
        tag_list2 = [i for i in tag_list[1].find_elements(By.TAG_NAME, 'li') if i.text.strip()]
        experience, degree = tag_list1[0].text, tag_list1[1].text
        excess = ', '.join([x.text for x in tag_list2])
        company_name = li.find_element(By.CLASS_NAME, 'company-name').text
        industry = li.find_element(By.CLASS_NAME, 'company-tag-list').find_elements(By.TAG_NAME, 'li')[0].text
        welfare = li.find_element(By.CLASS_NAME, 'info-desc').text
        company_tag_list = li.find_element(By.CLASS_NAME, 'company-tag-list')
        company_people = next((x.text for x in company_tag_list.find_elements(By.TAG_NAME, 'li') if "人" in x.text), "无")

        return {
            '公司': company_name, '岗位': job_name, '薪资': salary, '福利': welfare,
            '经验要求': experience, '学历要求': degree, '加分项目': excess,
            '所属行业': industry, '位置': addr, '公司规模': company_people
        }

    def save_data(self, name: str, new_data: pd.DataFrame):
        try:
            data = pd.read_excel(name)
        except FileNotFoundError:
            data = pd.DataFrame({
                '公司': [], '岗位': [], '薪资': [], '福利': [], '经验要求': [],
                '学历要求': [], '加分项目': [], '所属行业': [], '位置': [], '公司规模': []
            })
        save = pd.concat([data, new_data], axis=0)
        save.to_excel('./data/' + name, index=False)