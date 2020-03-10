from selenium import webdriver
import time

def get_adress_by_inn(inn_list):
    adress_list = []
    driver = webdriver.Chrome('chromedriver')
    driver.get('https://egrul.nalog.ru/index.html')
    time.sleep(2)
    search_elem = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/div[1]/div[1]/div/div[1]/div/div/input')
    for inn in inn_list:
        search_elem.clear()
        search_elem.send_keys(inn)
        search_elem.submit()
        time.sleep(2)
        adress = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[4]/div/div[3]/div').text
        if adress:
            adress_list.append(adress)
        else:
            adress_list.append('н/д')
    return adress_list