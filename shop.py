#Задание 4
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
# driver.find_element_by_id('menu-item-40').click()
# driver.find_element_by_xpath("//img[@title='Mastering HTML5 Forms']").click()
# header = driver.find_element_by_css_selector('.product_title.entry-title')
# header_get_text = header.text
# assert header_get_text == "HTML5 Forms"
# driver.quit()

#Задание 5
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
# driver.find_element_by_id('menu-item-40').click()
# driver.find_element_by_link_text('HTML').click()
# items = driver.find_element_by_css_selector('.cat-item.cat-item-19.current-cat > span.count')
# items_get_text = items.text
# assert items_get_text == "(3)"
# driver.quit()

#Задание 6
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
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
# driver.find_element_by_id('menu-item-40').click()
# default_sort = driver.find_element_by_xpath("//option[@value='menu_order']")
# default_sort_get_text = default_sort.text
# assert default_sort_get_text == "Default sorting"
# sort1 = driver.find_element_by_class_name("orderby")
# select = Select(sort1)
# select.select_by_visible_text("Sort by price: high to low")
# sort2 = driver.find_element_by_xpath("//option[@value='price-desc']")
# sort2_get_text = sort2.text
# assert sort2_get_text == "Sort by price: high to low"
# driver.quit()

#Задание 7
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get('https://practice.automationtesting.in/')
# driver.find_element_by_id('menu-item-40').click()
# driver.find_element_by_css_selector("img[title='Android Quick Start Guide']").click()
# book_old_price = driver.find_element_by_css_selector(".price > del > span")
# book_old_price_text = book_old_price.text
# book_new_price = driver.find_element_by_css_selector(".price > ins > span")
# book_new_price_text = book_new_price.text
# assert book_old_price_text == "₹600.00"
# assert book_new_price_text == "₹450.00"
# book_cover = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_cover.click()
# book_cover_close = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# book_cover_close.click()
# driver.quit()

#Задание 8
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get('https://practice.automationtesting.in/')
# driver.find_element_by_id('menu-item-40').click()
# driver.find_element_by_xpath("//a[@data-product_id='182']").click()
# items = driver.find_element_by_css_selector("span.cartcontents")
# items_text = items.text
# assert items_text == "1 item"
# price = driver.find_element_by_css_selector("a > span.amount")
# price_text = price.text
# assert price_text == "₹180.00"
# driver.find_element_by_css_selector('li >a.wpmenucart-contents').click()
# subtotal = WebDriverWait(driver, 20).until(
#     EC.text_to_be_present_in_element((By.XPATH, "//td[@data-title='Subtotal'"), "180"))
# total = WebDriverWait(driver, 20).until(
#     EC.text_to_be_present_in_element((By.XPATH, "//td[@data-title='Total'"), "183.60"))
# driver.quit()

#Задание 9
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get('https://practice.automationtesting.in/')
# driver.find_element_by_id('menu-item-40').click()
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_xpath("//a[@data-product_id='182']").click()
# time.sleep(3)
# driver.find_element_by_xpath("//a[@data-product_id='180']").click()
# time.sleep(3)
# driver.find_element_by_css_selector("a.wpmenucart-contents").click()
# time.sleep(3)
# driver.find_element_by_xpath("//a[@data-product_id='182']").click()
# time.sleep(3)
# driver.find_element_by_link_text("Undo?").click()
# time.sleep(3)
# driver.find_element_by_css_selector("tr:nth-child(2) > td > div > input").clear()
# time.sleep(3)
# select = Select(driver.find_element_by_css_selector("tr:nth-child(2) > td > div > input"))
# select.select_by_value("3")
# #Ошибка~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# time.sleep(3)
# driver.find_element_by_name('update_cart').click()
# time.sleep(3)
# quantity = driver.find_element_by_css_selector("tr:nth-child(2) > td > div > input")
# quantity_true = quantity.get_attribute("3")
# assert quantity_true == "3"
# time.sleep(3)
# driver.find_element_by_name('apply_coupon').click()
# time.sleep(3)
# failed = driver.find_element_by_css_selector(".woocommerce-error > li")
# failed_text = failed.text
# assert failed_text == "Please enter a coupon code."
# driver.quit()

#Задание 10
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get('https://practice.automationtesting.in/')
# driver.find_element_by_id('menu-item-40').click()
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_xpath("//a[@data-product_id='182']").click()
# time.sleep(3)RussКггыф
# driver.find_element_by_css_selector("a.wpmenucart-contents").click()
# time.sleep(3)
# driver.find_element_by_css_selector(".checkout-button.button.alt.wc-forward").click()
# time.sleep(3)
# first_name = driver.find_element_by_id('billing_first_name')
# first_name.send_keys('Denis')
# last_name = driver.find_element_by_id('billing_last_name')
# last_name.send_keys('Denisov')
# email = driver.find_element_by_id('billing_email')
# email.send_keys('d.moskovskiy@mail.ru')
# phone = driver.find_element_by_id('billing_phone')
# phone.send_keys('8787878787')
# time.sleep(3)

# driver.find_element_by_id("s2id_billing_country").click()
# time.sleep(3)
# driver.find_element_by_id('s2id_autogen1_search').click()
# time.sleep(3)
# driver.find_element_by_link_text("Russia").click()
# time.sleep(3)
# # Ошибка ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# # element = driver.find_element_by_id('billing_country')
# # select = Select(element)
# # select.select_by_value("RU")
# # И так Ошибка ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# address = driver.find_element_by_id('billing_address_1')
# address.send_keys('Lenina Street')
# city = driver.find_element_by_id('billing_city')
# city.send_keys('Las Vegas')

# # Если бы Russia, тогда было бы так
# county = driver.find_element_by_id('billing_state')
# county.send_keys('Tver County')
# postcode = driver.find_element_by_id('billing_postcode')
# postcode.send_keys('1234567')


