from conf import mobile_number,name
from selenium import webdriver
import time
import json
import numpy as np
from selenium.webdriver.common.action_chains import ActionChains

def getNextChildAge(parent_age,current_child_age,parent_child_age_diff=18):
    try:
        n_child_possible = (parent_age - current_child_age-parent_child_age_diff) // 2
        if n_child_possible > 0 and current_child_age==0:
            child_age =  parent_age - parent_child_age_diff-current_child_age-1
        elif current_child_age!=0:
            diff=np.random.randint(2,5)
            if current_child_age-diff>0:
                child_age=current_child_age-diff
            else:
                child_age=-1
        else:
            child_age = -1
        return child_age
    except Exception as e:
        raise Exception(str(e))


def getNumberOfChildAndAges(parent_age,parent_child_age_diff=18):
    """
    :param parent_age: parent age
    :param parent_child_age_diff: default 18
    :return: tuples of (n_child,child_age_list)
    """
    try:
        if parent_age<18:
            raise Exception("Parent age must be greater than 18")
        child_ages=[]
        current_child_age=0
        if parent_age - parent_child_age_diff > 0 and parent_age < 81:
            while current_child_age!=-1 and len(child_ages)<4:
                current_child_age=getNextChildAge(parent_age,current_child_age,parent_child_age_diff)
                if current_child_age!=-1:
                    child_ages.append(current_child_age)
        updated_age=[]
        for age in child_ages:
            if age>21:
                updated_age.append(age%21)
        child_ages=updated_age
        return len(child_ages), child_ages
    except Exception as e:
        raise Exception(str(e))


def getTracker():
    """

    :return: List of tracker
    """
    try:
        with open('data.txt', 'r') as d:
            res = json.load(d)
        return res
    except Exception as e:
        raise Exception(str(e))


def selectRadioButton(browser,radio_button_els,value):
    try:

        n_button=len(radio_button_els)
        for i in range(n_button):
            #print(radio_button_els[i].get_attribute('value'))
            if radio_button_els[i].get_attribute('value')==str(value):
                browser.implicitly_wait(10)
                ActionChains(browser).move_to_element(radio_button_els[i]).click(radio_button_els[i]).perform()
                #print("not visible")
                return True
    except Exception as e:
        raise Exception("File funtions.py throw a exception from method selectRadioButton"+str(e))



def getRadionOptionsValue(radio_button_els):
    try:
        data=[]
        idx=0
        for r in radio_button_els:
            data.append(r.get_attribute('value'))
            idx=idx+1
        return data
    except Exception as e:
        raise str(e)



