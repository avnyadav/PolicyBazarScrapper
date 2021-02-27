from MongoDBOperation import MongoDBOperation
from conf import mobile_number, name,Age_range,Gender
from selenium import webdriver
import time
import functions as usful_funct
from selenium.webdriver.support.select import Select
import json
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains


def getPolicyBazarHealthPreimumDetail(name,person_age,child_ages,mobile_number,gender="Male",n_child=0):
    """
    :param name: Accept Name of person
    :param person_age: Age of person
    :param child_ages: list of age of children
    :param gender: Accept gender of person Male or Female default value is Male
    :param mobile_number: Mobile number of person
    :param n_child: number of children
    :return: dataframe containing all files


    """
    try:
        if person_age<18:
            raise Exception("Person age should be greater than or equal 18")

        if gender not in ["Male","Female"]:
            raise Exception("Gender should mail or female")

        if n_child!=len(child_ages):
            raise Exception("Number of children and no of ages received for child is not matched")

        invalid_child_ages=[]
        for child_age in child_ages:
            if person_age-child_age<18:
                invalid_child_ages.append(child_age)

        if len(invalid_child_ages)>0:
            raise Exception("Parent age "+str(person_age)+" should be greater than child age by atleast 18 year from his child age ",invalid_child_ages)





        url = "https://health.policybazaar.com/?pq=health0&utm_content=home_v10"
        browser = webdriver.Chrome()  #opening google chrome
        browser.maximize_window() #maximizing window
        browser.get(url) # requesting url specified page
        time.sleep(5) #waiting for 5 second to load page

        #by default on webpage gender Male is selected if gender is Female the below block will be executed
        if gender=="Female":
            radio_gender_btn_name = 'gender'
            radio_btn_gender_option_el = browser.find_elements_by_name(radio_gender_btn_name) #selecting radio buttons of gender
            time.sleep(2) #waiting for 2 seconds
            usful_funct.selectRadioButton(browser, radio_btn_gender_option_el, 2) # calling a function to select gender female

        #selecting input text box of person
        input_box_name = "name"
        input_name_el = browser.find_element_by_name(input_box_name)

        #selecting input text box of person
        input_box_mobile_no = "number"
        input_mob_el = browser.find_element_by_name(input_box_mobile_no)

        #inserting name and mobile number of person
        input_name_el.send_keys(name)
        input_mob_el.send_keys(mobile_number)

        #getting continue buttong from webpage and clicking on it to proceed towards next page
        continue_btn = browser.find_element_by_css_selector("input[type='submit']")
        continue_btn.click()

        #waiting for next page to load
        time.sleep(5)

        #selecting last option of probile to provide detail option about family
        like_to_insure = 'profile'
        radio_like_to_insure_option_el = browser.find_elements_by_name(like_to_insure)
        like_to_insure_value = '6'
        usful_funct.selectRadioButton(browser, radio_like_to_insure_option_el, like_to_insure_value)

        time.sleep(5)

        #selcting self checkbox
        my_family="full"
        myself=browser.find_elements_by_class_name(my_family)[0]
        myself.click()
        select_age = Select(browser.find_element_by_class_name("select_family_box"))
        select_age.select_by_index(person_age-18+1)
        time.sleep(2)

        #updating children information
        if len(child_ages)>0:
            my_family="kids"
            #selecting son check box
            kids=browser.find_elements_by_class_name(my_family)[0]
            kids.click()
            time.sleep(3)
            #getting child increment button +
            increse_child_count=browser.find_elements_by_class_name("circle_kids")
            for increase_btn in increse_child_count:
                if increase_btn.text=='+':

                    for child in range(0,n_child-1):
                        increase_btn.click()
                        time.sleep(2)
            #getting select option for age of all child
            child_age_els=browser.find_elements_by_class_name("select_family_box_kid")
            child_ages_index=0

            #selecting age of each child
            for child_age_el in child_age_els:
                select_age = Select(child_age_el)
                select_age.select_by_index(child_ages[child_ages_index]+1)
                child_ages_index=child_ages_index+1


        #moving to next page
        continue_btn = browser.find_element_by_css_selector("input[type='submit']")
        continue_btn.click()


        #selecting pune city
        city="Pune"

        radio_btn_pune=browser.find_elements_by_name(city)
        usful_funct.selectRadioButton(browser,radio_btn_pune,"309")
        time.sleep(3)
        medication="ped_button"

        #selecting no option for medication
        div_btn_no=browser.find_elements_by_class_name(medication)[1]
        div_btn_no.click()
        i=0
        final_df=[]
        data_df=[]
        while i!=5:
            try:
                #print(data_df)
                time.sleep(3)
                data=browser.find_elements_by_class_name("quotes_more_plans")
                data_df=[]
                for d in data:
                    #print(d.click())
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
                                'Person_age':person_age,
                                'No_of_child':n_child,
                                'Child_ages':child_ages,
                                'Gender':gender,
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



                btn = browser.find_element_by_class_name("call-to-action2")
                btn.click()

            except Exception as e:
                try:
                    btn = browser.find_element_by_class_name("call-to-action2")
                    btn.click()
                except Exception as e:
                    pass
                i=i+1

        browser.close()
        return final_df
    except Exception as e:
        raise e


"""
mgdb=MongoDBOperation()
database_name="PolicyBazar"
collection_name="policy"
if len(final_df)>0:
    print("inserted")
    mgdb.insertDataFrame(database_name,collection_name,pd.DataFrame(final_df))
    pd.DataFrame(final_df).to_csv("PolicyBazarData.csv")
"""






if __name__=="__main__":
    try:
        trackers=usful_funct.getTracker()
        is_header_required=True
        idx=0
        for tracker in trackers:
            print(tracker)
            if tracker['is_processed']==0:
                df = getPolicyBazarHealthPreimumDetail(tracker['name'],
                                                       person_age=tracker['person_age'],
                                                       child_ages=tracker['child_ages'],
                                                        mobile_number=tracker['mobile_number'],
                                                        gender=tracker['gender'],
                                                       n_child=tracker['child_count'])
                if is_header_required and idx==0:
                    pd.DataFrame(df).to_csv("PolicyBazarCompleteData.csv",mode="a+")
                    is_header_required=False
                else:
                    pd.DataFrame(df).to_csv("PolicyBazarCompleteData.csv", header=None,mode="a+")

                trackers[idx]['is_processed']=1
            idx += 1
            with open('data.txt', 'w') as f:
                json.dump(trackers, f, ensure_ascii=False,indent=4)



        """
        df=getPolicyBazarHealthPreimumDetail(name, person_age=29, child_ages=[8,4], mobile_number=mobile_number,
                                          gender="Female", n_child=2)
        pd.DataFrame(df).to_csv("PolicyBazarDemo.csv")
        """
    except Exception as e:
        with open('data.txt', 'w') as f:
            json.dump(trackers, f, ensure_ascii=False,indent=4)
        print(trackers)
        print(str(e))


