import numpy as np

name = "Avnish Jane"
mobile_number = "8998787690"
Age = range(18, 101)
Gender = ['Male', 'Female']
Child = range(0, 5)


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



if __name__=="__main__":
    try:
        print(getNumberOfChildAndAges(60))
    except Exception as e:
        print(str(e))