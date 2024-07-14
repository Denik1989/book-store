#Задание 1

# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get('https://practice.automationtesting.in/')
# driver.execute_script("window.scrollBy(0, 600);")
# driver.find_element_by_xpath("//img[@title='Selenium Ruby']").click()
# driver.find_element_by_class_name("reviews_tab").click()
# driver.find_element_by_class_name("star-5").click()
# time.sleep(3)
# review = driver.find_element_by_id('comment')
# review.send_keys("Nice book!")
# time.sleep(3)
# name = driver.find_element_by_id('author')
# name.send_keys("Denis")
# time.sleep(3)
# email = driver.find_element_by_id('email')
# email.send_keys("d.moskovskiy@mail.ru")
# time.sleep(3)
# driver.find_element_by_id("submit").click()
# driver.quit()
