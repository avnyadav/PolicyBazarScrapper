from MongoDBOperation import MongoDBOperation
from conf import Mobile_Number, Name
from selenium import webdriver
import time
import functions as usful_funct
from selenium.webdriver.support.select import Select
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains

url = "https://health.policybazaar.com/?pq=health0&utm_content=home_v10"
print(Mobile_Number, Name)

browser = webdriver.Chrome()

browser.maximize_window()
browser.get(url)

time.sleep(5)

"""
<input type="radio" value="1" name="radio-group-gender" checked="checked" class="radio-group-gender">
<input type="radio" value="2" name="radio-group-gender" class="radio-group-gender">
"""
radio_gender_btn_name = 'gender'
radio_btn_gender_option_el = browser.find_elements_by_name(radio_gender_btn_name)
time.sleep(2)

# called a function to choose radio button possible value is (1,2)
usful_funct.selectRadioButton(browser, radio_btn_gender_option_el, 2)

# selecting

input_box_name = "name"
input_name_el = browser.find_element_by_name(input_box_name)

input_box_mobile_no = "number"
input_mob_el = browser.find_element_by_name(input_box_mobile_no)
print(input_name_el.get_attribute('placeholder'))
print(input_mob_el.get_attribute('placeholder'))

input_name_el.send_keys(Name)
input_mob_el.send_keys(Mobile_Number)

continue_btn = browser.find_element_by_css_selector("input[type='submit']")
continue_btn.click()

time.sleep(3)
like_to_insure = 'profile'
radio_like_to_insure_option_el = browser.find_elements_by_name(like_to_insure)
like_to_insure_value = '6'
usful_funct.selectRadioButton(browser, radio_like_to_insure_option_el, like_to_insure_value)

time.sleep(3)
my_family="full"
myself=browser.find_elements_by_class_name(my_family)[0]
myself.click()


my_family="kids"
kids=browser.find_elements_by_class_name(my_family)[0]
kids.click()
time.sleep(3)
select_age = Select(browser.find_element_by_class_name("select_family_box"))
select_age.select_by_index(3)
time.sleep(2)
increse_child_count=browser.find_elements_by_class_name("circle_kids")
for increase_btn in increse_child_count:
    print("BTN value",increase_btn.text)
    if increase_btn.text=='+':
        increase_btn.click()
time.sleep(2)
child_age_els=browser.find_elements_by_class_name("select_family_box_kid")
for child_age_el in child_age_els:
    select_age = Select(child_age_el)
    select_age.select_by_index(3)

continue_btn = browser.find_element_by_css_selector("input[type='submit']")
continue_btn.click()

city="Pune"

radio_btn_pune=browser.find_elements_by_name(city)
usful_funct.selectRadioButton(browser,radio_btn_pune,"309")
time.sleep(3)
medication="ped_button"

div_btn_no=browser.find_elements_by_class_name(medication)[1]
div_btn_no.click()
i=0
final_df=[]
data_df=[]
while i!=5:
    try:
        print(data_df)
        time.sleep(3)
        data=browser.find_elements_by_class_name("quotes_more_plans")
        data_df=[]
        for d in data:
            print(d.click())
            content=browser.find_elements_by_class_name("quotes_content_desktop")

            for c in content:

                plan_name=c.find_element_by_class_name("quotes_plan_name")

                cover_amount=c.find_element_by_class_name("span_cover_content")
                facility = c.find_element_by_class_name("span_network")
                n_hospital = c.find_element_by_class_name("span_network_content")
                monthly_premium_amount = c.find_element_by_class_name("premium_button")
                annually_premium_amount = c.find_element_by_class_name("annually_premium")

                data_df.append(
                    {
                      'plan_name':plan_name.text,
                        'cover':cover_amount.text,
                        'Facility':facility.text,
                        'No of Hospitals':n_hospital.text,
                        'Monthly charge':monthly_premium_amount.text,
                        'Annually charge':annually_premium_amount.text


                    }
                )
                if len(final_df) < len(data_df):
                    final_df = data_df

            """
            <div class="top_quotes_content"><div class="planContent_container ">
            <span class="quotes_plan_name">Care Advantage - Upto Suite Room </span>
            </div><div class="cover_container">
            <div class="div_cover">
            <span class="span_cover">Cover</span>
            <span class="span_cover_content ">₹ 1Cr</span>
            </div><div class="div_network " id="CashlessHospitalonQuotes">
            <span class="span_network">Cashless Hospitals</span>
            <span class="span_network_content ">270</span></div>
            </div><div class="premium_container ">
            <div class="premium_button" id="ProceedToProduct">₹1,445/month</div>
            <span class="annually_premium">₹ 17,331 annually</span>
            </div><div class="shortlist_container ">
            <div class="Path_shortlist noAnimation coachMark"><img alt="shortlistIcon" class="shortlist_icon"
             src="https://static.pbcdn.in/health-cdn/images/insurer-logo/quotes-logos/shortlist.svg"></div></div></div>
            """



        btn = browser.find_element_by_class_name("call-to-action2")
        btn.click()

    except Exception as e:
        try:
            btn = browser.find_element_by_class_name("call-to-action2")
            btn.click()
        except Exception as e:
            pass
        i=i+1




'''
<div class="box-container full"><div class="field_container">
<div class="checkbox"><label><input id="selfrdo" type="checkbox">
 <span> Spouse</span></label></div></div> <!----></div>
'''
'''
like_to_insure = "chkFamilyMembers"
checkbox_like_to_insure = browser.find_elements_by_class_name(like_to_insure)

value = usful_funct.getRadionOptionsValue(checkbox_like_to_insure)
print(value)

usful_funct.selectRadioButton(browser, checkbox_like_to_insure, value[0])

age = browser.find_element_by_class_name("box-Self")
age_select_el = "chkMemberAge"
select_age = Select(age.find_element_by_class_name(age_select_el))

select_age.select_by_index(3)
continue_btn_name = "btnHealthStep2"
continue_btn_heath2 = browser.find_element_by_class_name(continue_btn_name)
time.sleep(5)
continue_btn_heath2.click()
# continue_btn_heath2.click()
'''
"""
if like_to_insure_value=='Self':

 #   <select class="input_box placeholder chkMemberEldestAge">

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

"""


mgdb=MongoDBOperation()
database_name="PolicyBazar"
collection_name="policy"
if len(final_df)>0:
    print("inserted")
    mgdb.insertDataFrame(database_name,collection_name,pd.DataFrame(final_df))
    pd.DataFrame(final_df).to_csv("PolicyBazarData.csv")










