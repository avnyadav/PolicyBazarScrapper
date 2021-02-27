from conf import mobile_number, name, Age_range, Gender
from selenium import webdriver
import time
import json
import numpy as np
from selenium.webdriver.common.action_chains import ActionChains

def getNextChildAge(parent_age,current_child_age,parent_child_age_diff=18):
    try:
        if current_child_age==0:
            n_child_possible = (parent_age - current_child_age-parent_child_age_diff) // 2
        else:
            n_child_possible=(current_child_age-1)//2
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


        for index in range(len(child_ages)):
            if child_ages[index]>21:
                child_ages[index]=child_ages[index]%21

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


def generateData():
    tracker=[]
    idx=0
    for person_age in Age_range:
        for gender in Gender:
            n_child, child_ages = getNumberOfChildAndAges(person_age)

            for child_count in range(n_child + 1):
                print(" currently runing for --> name :{0} person age :{1} child ages: {2}"
                      " mobile number: {3}"
                      " gender: {4}"
                      " n_child:{5}".format(name
                                            , person_age, child_ages[:child_count], mobile_number, gender, child_count)
                      )
                tracker.append({'name':name,'person_age':person_age,

                               'child_ages':child_ages[:child_count],
                                'mobile_number':mobile_number,
                                'gender':gender,
                                'child_count':child_count
                               ,'is_processed':0})
    with open('data.txt', 'w') as f:
        json.dump(tracker, f, ensure_ascii=False,indent=4)




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



if __name__=="__main__":
    print(getNumberOfChildAndAges(24))

    generateData()