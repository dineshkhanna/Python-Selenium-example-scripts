def google_trends(search_word):
	from selenium import webdriver
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.common.exceptions import TimeoutException
	from selenium.webdriver.firefox.firefox_profile import 
FirefoxProfile
	import time
	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.download.folderList", 2)
	
profile.set_preference("browser.download.manager.showWhenStarting", 
False)
	profile.set_preference("browser.download.dir", 'C:\\Python27')
	profile.set_preference("browser.helperApps.neverAsk.saveToDisk", 
"text/csv")
	driver = 
webdriver.Firefox(firefox_profile=profile,executable_path=r'C:\\Python27\\geckodriver.exe')
	
driver.get("https://trends.google.com/trends/explore?date=all&geo=TH&q="+ 
search_word)
	time.sleep(7)
	lst = 
driver.find_elements_by_css_selector(".widget-actions-item.export")
	lst[0].click()
	
google_trends("technology")
