import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    selected_website = select_website()
    
    if selected_website == "BOSS 直聘":
        from crawlers.boss_zhipin.config import jobs, experience, degree, citys
        from crawlers.boss_zhipin.crawler import BossZhipinCrawler
        
        # Initialize the browser and start the crawler
        browser = init_browser()
        boss_crawler = BossZhipinCrawler(browser, jobs, experience, degree, citys)
        boss_crawler.login()
        
        search_lists = boss_crawler.get_search_lists()
        for search_url in search_lists:
            boss_crawler.get_jobs_lists(*search_url)
        
        logging.info(f"[{selected_website}] 爬虫成功完成")
        browser.quit()
    else:
        logging.warning(f"目前不支持的爬取网站: {selected_website}")

def select_website() -> str:
    print("请选择要爬取的网站：")
    print("1. BOSS 直聘")
    choice = input("请输入选项编号（例如 1）：")
    
    if choice == '1':
        return "BOSS 直聘"
    else:
        logging.warning("无效输入，默认选择 BOSS直聘")
        return "BOSS 直聘"

def init_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)
