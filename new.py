import datetime as gpt

print(gpt.datetime.now())
print(gpt.timedelta(minutes=1))
print(gpt.time(10,23,22))
print(gpt.datetime.today())
print(gpt.datetime.now())
print(gpt.datetime.now())
print(gpt.datetime.now().year)
print(gpt.date.today())

target=gpt.datetime(2030,1,1)
time_left=target-gpt.datetime.today()
print(time_left)
print(gpt.datetime.now().strftime("%dth of %A-%B-%Y"))
print(gpt.datetime.today().strftime("%d-%m-(%B)-Y"+" %I-%M pm %A "))