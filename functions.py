from conf import Mobile_Number,Name
from selenium import webdriver
import time
import json
from selenium.webdriver.common.action_chains import ActionChains


def selectRadioButton(browser,radio_button_els,value):
    try:

        n_button=len(radio_button_els)
        for i in range(n_button):
            print(radio_button_els[i].get_attribute('value'))
            if radio_button_els[i].get_attribute('value')==str(value):
                browser.implicitly_wait(10)
                ActionChains(browser).move_to_element(radio_button_els[i]).click(radio_button_els[i]).perform()
                print("not visible")
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



