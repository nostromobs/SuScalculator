import datetime

class SuSTest:
    def __init__(self,one,two,three,four,five,six,seven,eight,nine,ten,even,odd,total,grade):
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six
        self.seven = seven
        self.eight = eight
        self.nine = nine
        self.ten = ten
        self.total = total
        self.grade = grade
        
class User:
    def __init__(self,name,score):
        self.name = name
        self.score = score

def GetGrade(_total):
    if _total > 80.3:
        _grade = "A - Fantastic!"
    elif _total > 68 and _total < 80.3:
        _grade = "B - Pretty pretty good!"
    elif _total == 68:
        _grade = "C - Decent!"
    elif _total > 51 and _total < 68:
        _grade = "D - well at least its not a F!"
    elif _total < 51:
        _grade = "F - ouch!"
    return _grade

def GetTotal(_odd,_even):
    _total = 0
    _i = 0
    while _i < 5:
        _odd[_i] -= 1
        _total += _odd[_i]
        _i += 1
    _x = 0
    while _x < 5:
        _even[_x] = 5 - _even[_x]
        _total += _even[_x]
        _x += 1
    _total = _total*2.5
    return _total

def GetTestValues(user,debug,debugTestValues):
    if debug == "true":
        _one = debugTestValues[0]
        _two = debugTestValues[1]
        _three = debugTestValues[2]
        _four = debugTestValues[3]
        _five = debugTestValues[4]
        _six = debugTestValues[5]
        _seven = debugTestValues[6]
        _eight = debugTestValues[7]
        _nine = debugTestValues[8]
        _ten = debugTestValues[9]
    else:
        _one = input("Question 1 score?  ")
        _two = input("Question 2 score?  ")
        _three = input("Question 3 score?  ")
        _four = input("Question 4 score?  ")
        _five = input("Question 5 score?  ")
        _six = input("Question 6 score?  ")
        _seven = input("Question 7 score?  ")
        _eight = input("Question 8 score?  ")
        _nine = input("Question 9 score?  ")
        _ten = input("Question 10 score? ")
    _odd = [int(_one),int(_three),int(_five),int(_seven),int(_nine)]
    _even = [int(_two),int(_four),int(_six),int(_eight),int(_ten)]
    _total = GetTotal(_odd,_even)
    _grade = GetGrade(_total)
    return SuSTest(_one,_two,_three,_four,_five,_six,_seven,_eight,_nine,_ten,_odd,_even,_total,_grade)

def GetNewUser(user,debug,debugKey):
    _userName = "User "+format(user)
    return User(_userName,GetTestValues(user,debug,debugKey))

def GetTotalScore(totalScores):
    _totalScore = 0
    for _score in totalScores:
        _totalScore += _score
    return _totalScore

def GetAverage(total,scale):
    return total/scale

def RunDebug():
    _x = 0
    _totalScores = []
    #WinCon: 80.5
    _test1 = [4,2,5,1,4,2,5,2,5,1] #Score: 87.5
    _test2 = [5,1,4,1,4,1,5,1,5,1] #Score: 95
    _test3 = [5,2,4,2,3,4,4,2,5,4] #Score: 67.5
    _test4 = [5,1,5,1,4,1,4,2,5,2] #Score: 90
    _test5 = [4,1,4,2,3,4,5,3,4,5] #Score: 62.5
    _x += 1
    _user1 = GetNewUser(1,"true",_test1)
    _totalScores.append(_user1.score.total)
    print("**************************************************")
    print(_user1.name)
    print("Total:",_user1.score.total)
    print("Grade:",_user1.score.grade)
    print("**************************************************")
    _user2 = GetNewUser(2,"true",_test2)
    _totalScores.append(_user2.score.total)
    print("**************************************************")
    print(_user2.name)
    print("Total:",_user2.score.total)
    print("Grade:",_user2.score.grade)
    print("**************************************************")
    _user3 = GetNewUser(3,"true",_test3)
    _totalScores.append(_user3.score.total)
    print("**************************************************")
    print(_user3.name)
    print("Total:",_user3.score.total)
    print("Grade:",_user3.score.grade)
    print("**************************************************")
    _user4 = GetNewUser(4,"true",_test4)
    _totalScores.append(_user4.score.total)
    print("**************************************************")
    print(_user4.name)
    print("Total:",_user4.score.total)
    print("Grade:",_user4.score.grade)
    print("**************************************************")
    _user5 = GetNewUser(5,"true",_test5)
    _totalScores.append(_user5.score.total)
    print("**************************************************")
    print(_user5.name)
    print("Total:",_user5.score.total)
    print("Grade:",_user5.score.grade)
    print("**************************************************")
    _total = GetTotalScore(_totalScores)
    _average = GetAverage(_total,5)
    _grade = GetGrade(_average)
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print("Grand Total:",_total)
    print("Overall Grade:",_grade)
    print("Test Average:",_average)
    print("Thank you for using the SuS Calculator!")
    print("Created in Python by Brandon Slater")
    print("**************************************************")

def RunCalculator(scale):
    log = ""
    _x = 0
    _totalScores = []
    while _x < scale:
        _x += 1
        _user = GetNewUser(_x,"calc","")
        _totalScores.append(_user.score.total)
        print("********************"+_user.name+"************************")
        log+="********************"+_user.name+"********************\n"
        print("Total:",_user.score.total)
        log+="Total: "+format(_user.score.total)+"\n"
        print("Grade: "+_user.score.grade[0])
        log+="Grade: "+format(_user.score.grade[0])+"\n"
        print("**************************************************")
        log+="**************************************************"
        _total = GetTotalScore(_totalScores)
        _average = GetAverage(_total,scale)
        _grade = GetGrade(_average)
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    log+="."
    log+="."
    log+="."
    log+="."
    log+="."
    log+="."
    log+="."
    log+="."
    log+="."
    log+="."
    log+="."
    log+="."
    log+="."
    log+="."
    log+="."
    log+="."
    print("********************Results************************")
    log+="********************Results************************"
    print("Grand Total:",_total)
    log+="Grand Total: "+format(_total)+"\n"
    print("Overall Grade:",_grade)
    log+="Overall Grade: "+format(_grade)+"\n"
    print("Test Average:",_average)
    log+="Test Average: "+format(_average)+"\n"
    print("**************************************************")
    log+="**************************************************"
    print(".")
    print(".")
    print(".")
    print("**************************************************")
    print("Thank you for using the System Usability Scale (SuS) Calculator Calculator!")
    print("Created in Python by Brandon Slater")
    print("**************************************************")
    goodbye = input("press enter to exit...")
    return log
    #filename is complete path to file plus name and .txt extension


print('Welcome to the System Usability Scale (SuS) Calculator!')
testName = input("What is the name of your test?")
log = RunCalculator(int(input("How many users are in your test group? ")))
logdate = datetime.datetime.now()
filename = 'SuSResults: '
filename+=testName
filename+=' @ '
filename+=format(logdate)[0:9]
filename+='.txt'
file = open(filename, 'w')
file.write(log)
file.close()
# RunDebug()