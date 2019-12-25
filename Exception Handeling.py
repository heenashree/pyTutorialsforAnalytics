dict_1 = {'Name':'Heenashree', 'Practice': 'CnD', 'Skills':'Python'}
list_1 = [1,2,3,4,5,6]
try:
    #1/0
    #print(dict_1['test'])
    #list_1[7]
    #print(x)
    print("this")
    try:
            print("test")
    except:
            print("none")

except ZeroDivisionError:
    print("This is errored out for zero division error")
except KeyError:
    print("This is a key error")
except IndexError:
    print("This is index error")
except NameError:
    print("Variable not defined")
except:
    print("")
else:
    print("If there is no error then execute this")
finally:
    print("This will always run")



