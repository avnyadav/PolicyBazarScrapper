from conf import Mobile_Number,Name
from selenium import webdriver
import time
import functions as usful_funct
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.action_chains import ActionChains

url="https://health.policybazaar.com/?pq=health0&utm_content=home_v10"
print(Mobile_Number,Name)



browser=webdriver.Chrome()


browser.get(url)

time.sleep(5)

"""
<input type="radio" value="1" name="radio-group-gender" checked="checked" class="radio-group-gender">
<input type="radio" value="2" name="radio-group-gender" class="radio-group-gender">
"""
radio_gender_btn_name='gender'
radio_btn_gender_option_el=browser.find_elements_by_name(radio_gender_btn_name)
time.sleep(2)

# called a function to choose radio button possible value is (1,2)
usful_funct.selectRadioButton(browser,radio_btn_gender_option_el,2)

# selecting
input_box_name="name"
input_name_el=browser.find_element_by_name(input_box_name)

input_box_mobile_no="number"
input_mob_el=browser.find_element_by_name(input_box_mobile_no)
print(input_name_el.get_attribute('placeholder'))
print(input_mob_el.get_attribute('placeholder'))

input_name_el.send_keys(Name)
input_mob_el.send_keys(Mobile_Number)

continue_btn="CONTINUE"

continue_btn_el=browser.find_element_by_css_selector("input[type='submit']")

if continue_btn_el.get_attribute('value')==continue_btn:
    continue_btn_el.click()

radio_btn_profile_name="profile"
radio_btn_profile_el=browser.find_elements_by_name(radio_btn_profile_name)
usful_funct.selectRadioButton(browser,radio_btn_profile_el,'6')


"""
<input type="text" class="input_box txtName input_right" maxlength="90" placeholder="Full Name">

"""
"""
<input type="tel" autocomplete="off" class="input_box mobNumber input_right" id="name5" placeholder="10 - digit mobile number" minlength="10" maxlength="10" data-country-std-code="91">
"""


"""
<button class="btn btnHealthStep1 btnQuote" data-step="1">View Plans</button>
"""
'''
btn_healthstep1_el=browser.find_element_by_class_name("btnHealthStep1")
btn_healthstep1_el.click()


time.sleep(3)
like_to_insure='radio-group-member'
radio_like_to_insure_option_el=browser.find_elements_by_name(like_to_insure)
like_to_insure_value='family'
usful_funct.selectRadioButton(browser,radio_like_to_insure_option_el,like_to_insure_value)

time.sleep(3)
if like_to_insure_value=='Self':
    """
    <select class="input_box placeholder chkMemberEldestAge">
    """
    print("Hi")
    age_select_el='chkMemberEldestAge'
    select_age=Select(browser.find_element_by_class_name(age_select_el))

    select_age.select_by_index(3)

    possible_age=browser.find_element_by_class_name(age_select_el)
    options=possible_age.find_elements_by_tag_name("option")
    age=[ p.get_attribute("value")  for p in options]
    print(age.index('20'),age.index('24'))
    select_age.select_by_index(age.index('34'))
    time.sleep(1)
    continue_btn_name="btnHealthStep2"
    continue_btn_heath2=browser.find_element_by_class_name(continue_btn_name)
    continue_btn_heath2.click()

    radio_btn_popular_city_name="city"
    radio_btn_popular_city=browser.find_elements_by_name(radio_btn_popular_city_name)
    select_city_name="Pune(Maharashtra)"
    time.sleep(2)
    usful_funct.selectRadioButton(browser,radio_btn_popular_city,select_city_name)
    time.sleep(5)

    radio_btn_is_medication_name="radio-group-ped"
    is_medication_value="0"
    radio_btn_is_medication=browser.find_elements_by_name(radio_btn_is_medication_name)
    usful_funct.selectRadioButton(browser,radio_btn_is_medication,is_medication_value)

    time.sleep(5)

    plan_list_name="quotes_stack"
    insurance_div=browser.find_elements_by_class_name(plan_list_name)
    time.sleep(10)
    try:

        btn=browser.find_element_by_class_name("call-to-action2")
        btn.click()
    except Exception as e:
        pass

    premium_amount=browser.find_elements_by_class_name("premium_button")
    for i in premium_amount:
        print(i.text)
        
        '''










