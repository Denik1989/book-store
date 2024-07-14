#Задание 2
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get('https://practice.automationtesting.in/')
# driver.find_element_by_id('menu-item-50').click()
# email = driver.find_element_by_id('reg_email')
# email.send_keys("d.moskovskiy@mail.ru")
# time.sleep(3)
# password = driver.find_element_by_id('reg_password')
# password.send_keys("4tg13ocv789tzl")
# time.sleep(3)
# driver.find_element_by_name('register').click()
# driver.quit()


#Задание 3
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get('https://practice.automationtesting.in/')
# driver.find_element_by_id('menu-item-50').click()
# username = driver.find_element_by_id('username')
# username.send_keys("d.moskovskiy@mail.ru")
# time.sleep(3)
# password = driver.find_element_by_id('password')
# password.send_keys("4tg13ocv789tzl")
# time.sleep(3)
# driver.find_element_by_name('login').click()
# element = driver.find_element_by_link_text("Logout")
# element_get_text = element.text
# assert element_get_text == "Logout"
# driver.quit()
