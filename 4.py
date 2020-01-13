from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
url = "https://sprungmarker.de/"
cloud = []
posts = []
driver.get(url)
if __name__ == "__main__":
#Подсчитать количество постов на главной странице.
#Проверить, что статьи открываются.
#Проверить постраничную навигацию.
    
    for link in driver.find_elements_by_xpath('//h3[@class="entry-title"]/a'):
        posts.append((link.get_attribute("href"), link.text))
    print("Количество постов на главной странице: ",len(posts))

    for p in posts:
        driver.get(p[0])
        if driver.find_element_by_xpath('//h1[@class="entry-title"]').text==p[1]:
            print("Открыта ожидаемая статья ("+p[1]+')')
        else:
            print("ОШИБКА. Открыта не ожидаемая страница")

    driver.get(url)
    for cur_i in range(1,5):
        driver.get(driver.find_element_by_class_name('next.page-numbers').get_attribute('href'))
        if (str(driver.current_url) == ("https://sprungmarker.de/page/"+str(cur_i+1))+"/"):
            print("Переход осуществлен. Открыта страница №", cur_i+1)
    driver.get(url)
    input("\n\nНажмите Enter для закрытия браузера...")
    driver.close()
