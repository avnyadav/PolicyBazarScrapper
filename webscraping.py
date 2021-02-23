import time
from selenium import webdriver

browser=webdriver.Chrome()
url="https://www.google.com/"
browser.get(url)

"""
<input class="gLFyf gsfi" maxlength="2048" name="q" type="text"
 jsaction="paste:puy29d" aria-autocomplete="both" aria-haspopup="false"
autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" 
title="Search" value="" aria-label="Search" data-ved="0ahUKEwiIqtzvi_nuAhVe63MBHUr1AhYQ39UDCAQ">

"""

name="q"

search_el=browser.find_element_by_name(name=name)
print(search_el)

search_el.send_keys("ineuron")

"""
<input class="gNO89b" value="Google Search"
 aria-label="Google Search" name="btnK"
  type="submit" data-ved="0ahUKEwiokaKSjvnuAhVk7XMBHWp0DPIQ4dUDCAs">
"""

submit_btn_el=browser.find_element_by_css_selector("input[type='submit']")

time.sleep(4)
print(submit_btn_el.get_attribute('name'))
submit_btn_el.click()


