from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class Website:
    def __init__(self, name, domainName):
        self.name = name
        self.domainName = domainName


def searchBugCrowd(driver, bugCrowd_URL, websites):
    driver.get(bugCrowd_URL)
    sites = driver.find_elements_by_class_name('program-container')
    for i in sites:
        bugBounty = "no"
        if i.find_elements_by_tag_name('th')[2].get_attribute('class') == "yes":
            bugBounty = "yes"
            name = \
            i.find_elements_by_tag_name('th')[0].find_elements_by_tag_name('a')[
                0].get_attribute('text')
            websites.append(Website(name, ""))
        else:
            continue
    return websites


def searchHackerOne(driver, hackerOne_URL, websites):
    driver.get(hackerOne_URL)
    sites = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]').find_elements_by_class_name("program")
    while len(sites) == 0:
        sites = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]').find_elements_by_class_name("program")
    for site in sites:
        name = site.find_element_by_class_name('program__profile').find_element_by_tag_name('ul').find_element_by_tag_name('li').text[14:]
        websites.append(Website(name, ""))
    return websites

def main():
    websites = list()
    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": r"C:\Users\b1n4ry\Desktop\Music",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    #options.add_argument('headless')
    #options.add_argument('window-size=1920x1080')
    #options.add_argument("disable-gpu")

    driver = webdriver.Chrome(options=options,
                              executable_path='C:\\Users\\b1n4ry\\Downloads\\chromedriver_win32(3)\\chromedriver')

    bugCrowd_URL = "https://www.bugcrowd.com/bug-bounty-list/"
    hackerOne_URL = "https://hackerone.com/bug-bounty-programs"
    websites = searchBugCrowd(driver, bugCrowd_URL, websites)
    websites = searchHackerOne(driver, hackerOne_URL, websites)
    for i in websites:
        print(i.name)


main()
