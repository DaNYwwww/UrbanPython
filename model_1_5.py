immutable_var=9,8.1,True,"Hello World!"
print(immutable_var)
#immutable_var[0]=1
#Нельзя изменять кортеж так, как это неизменяемый класс
mutable_list = [9,8.1,True, "!dlroW olleH","Modified"]
print(mutable_list)
mutable_list[1]=100.1
print(mutable_list)
