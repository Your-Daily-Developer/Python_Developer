a=input("Enter a list of numbers separated by space: ")
b=list(map(int,a.split()))

separator=0
for i in b:
    if i%2==0:
        separator=i+separator
    else:
        continue

print(separator)

a=input("Enter a sentence:")
b=a.split()
Counter=0
c=set(b)
for i in c:
    if i in b:
        Counter+=1
        print(Counter,"=",i)
    else:
        continue

a=input("Enter:")
counter=0
builder=0
gainer=0
for i in a:
    if i=="!" or i=="`" or i=="^" or i=="~" or i=="," or i=="." or i=="*" or i=="&" or i=="$" or i=="@" or i=="#" or i=="(" or i==")" or i=="<" or i==">" or i=="=" or i=="+" or i=="-" or i=="_" or i=="[" or i=="]" or i=="|" or i=="{" or i=="}" or i=="/" or i=="?" or i==" " :
        counter=counter+1
    elif i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0":
        builder=builder+1
    else:
        gainer=gainer+1

print(counter,builder,gainer)

My_file=open("Textforhtml.exe","a")
print("Textforhtml.exe")
print(My_file.read())
My_file.close()

string=input("Enter a sentence: ")
counter=0
for i in string:
    if i=="e":
        counter+=1
    else:
        continue
correct=counter
answer=int(input("Enter the number of e in the sentence:"))
if answer==correct:
    print("Correct")
else:
    print("Incorrect")


#bro you are giving hints on the easy question this is not fair and no hints for the difficult one:
a=input("Enter a list numbers (eg. 12 34 45 ): ")
b=list(map(int,a.split()))
counter=0
for i in b:
    if i%2==0:
        counter=counter+i
    else:
        continue

print("The sum of the even numbers will be ",counter)


b=input("Enter a sentence:")
collector=0
for i in b:
    if i.lower() in "aeiou":
        continue
    else:
        print(i+"",end="")






time_calculator=0

activities_and_time_in_minutes={
    "Coding":40,
    "Entertainment":45,
    "Typing":5,
    "Whispering":60

}

for i in activities_and_time_in_minutes.keys():
    if i==int():
        time_calculator=time_calculator+int(i)
    else:
        continue



Required=input("Input what you have to find \n""A)Potential Difference or (V)\n" "B)Current flowing through the conductor (I)\n" "C)Resistance of the conductor (R)\n""FRO WHATEVER YOU HAVE TO FIND PUT VALUES AS\n" "V OR R OR I:" )
if Required.upper() != "V" and Required.upper() != "R" and Required.upper() != "I":
    print("Enter the values as guided")
elif Required.upper()=="V":
    Values = float(input("Enter the value of I"))
    Values3 = float(input("Enter the value of R"))
    print(Values*Values3)
elif Required.upper()=="R":
    Values2 = float(input("Enter the value of V"))
    Values = float(input("Enter the value of I"))
    print(Values/Values2)
elif Required.upper()=="I":
    Values2 = float(input("Enter the value of V"))
    Values3 = float(input("Enter the value of R"))
    print(Values2/Values3)
else:
    print("Please Follow The Instructions!!")

    new_skill = input("Enter your desired skill:")
    old_skills = ["Python", "CSS", "HTML"]
    while new_skill.lower() != "exit":
        new_skill = input("Enter your desired skill:")

        old_skills.append(new_skill)

    print(old_skills)
    print("You have earned " + str(len(old_skills)) + " skills")

    roadmap = {
        "Python": 5,
        "Web_Dev": 3,
        "AI_Consulting": 2
    }

    roadmap["Cybersecurity"] = 1

    print(roadmap)

    roadmap["Chess"] = 9
    print(roadmap)

import datetime

date=datetime.date(2026,1,25)
today=datetime.date.today()
print(date)
print(today)

time=datetime.time(12,24,34)
now=datetime.datetime.now()
print(now)
print(time)


now=now.strftime("%H: %M: %S %m-%d-%Y")
print(now)

target_datetime=datetime.datetime(200,2,3,4,5)
current_datetime=datetime.datetime.now()

if target_datetime > current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")

old_skills=["Python","CSS","HTML"]
print(len(old_skills))


for i in range(1,21):
    is_special=False
    if i%3==0:
        is_special=True
        print(i,"-"' Special')

    else:
        is_special=False
        print(i,"-"' Normal Number')


for i in range(1,11):
    is_special=False

    if i==3:
        is_special=True

    if is_special==True:
        print("You are great ")
    print(i)

    for i in range(1, 11):
        for j in range(1, 4):
            print("!", end="-")
        print()

        for i in range(1, 4):  # Manager: i becomes 1, then 2, then 3
            for j in range(i):  # Worker: Runs 'i' times
                print(i, end=" ")  # STAMP the Manager's number
            print()  # Move to next line

            for i in range(1, 6):  # Manager: Row 1 to 5
                if i % 2 != 0:  # Logic: If 'i' is ODD (1, 3, 5)
                    for j in range(i):  # Worker runs 'i' times
                        print(i, end=" ")  # Print the Number
                else:  # Logic: If 'i' is EVEN (2, 4)
                    for j in range(i):  # Worker runs 'i' times
                        print("*", end=" ")  # Print the Star
                print()  # Manager moves to next line

                for i in range(1, 6):
                    if i % 2 != 0:  # Manager checks: Is this row ODD?
                        for j in range(i):
                            print(1, end=" ")
                    else:  # Manager checks: If NOT odd (meaning EVEN)
                        for j in range(i):
                            print(0, end=" ")
                    print()  # Manager moves to a new line

                    import datetime as gpt

                    print(gpt.datetime.now())
                    print(gpt.timedelta(minutes=1))
                    print(gpt.time(10, 23, 22))
                    print(gpt.datetime.today())
                    print(gpt.datetime.now())
                    print(gpt.datetime.now())
                    print(gpt.datetime.now().year)
                    print(gpt.date.today())

                    target = gpt.datetime(2030, 1, 1)
                    time_left = target - gpt.datetime.today()
                    print(time_left)
                    print(gpt.datetime.now().strftime("%dth of %A-%B-%Y"))
                    print(gpt.datetime.today().strftime("%d-%m-(%B)-Y" + " %I-%M pm %A "))

                    for i in range(1, 6):
                        for j in range(1, 6 - i):
                            print("-", end="")

                        for k in range(i + 1):
                            print("*" * k, end="")
                        print()

                        for i in range(1, 6):

                            if i == 1 or i == 5:
                                for j in range(1, 6):
                                    print("*", end="")
                            elif i == 2 or i == 3 or i == 4:
                                for j in range(1, 3):
                                    print("*" + " ", end=" ")

                            print()

                            for i in range(1, 6):
                                for j in range(1, 6):
                                    if (i + j) % 2 == 0:
                                        print("*", end=" ")
                                    else:
                                        print("#", end=" ")
                                print()

                                user = input("Enter the numbers (eg. 200 200 400):")
                                modify = list(map(int, (user.split())))
                                new_list = []
                                for i in modify:
                                    if i < 500:
                                        modify.remove(i)
                                    else:
                                        new_list.append(f"{i * 10 / 100:2f}")

                                print(new_list)

                                password = input("Enter your password: ")
                                i = ""
                                counter = 0
                                for i in password:
                                    if i == "@":
                                        counter += 1
                                if counter > 0 and len(password) > 8:
                                    print("Strong")
                                else:
                                    print("Weak")

                                    a = input('Enter your name:')
                                    for i in a[::-1]:
                                        print(i, end="")

                                        asset = ["Gold", "Stocks", "Crypto"]
                                        value = [50000, 80000, 1200000]
                                        for i, a in zip(asset, value):
                                            print(f"Asset:  {i:<10} | Value:  {a:,.2f}")

                                            scores = [85, 92, 78, 60, 95]

                                            for i in scores:
                                                if i > 90:
                                                    print("Legendary Performance!")
                                                elif 80 >= i >= 90:
                                                    print("Solid 10CR Effort!")
                                                else:
                                                    print("Hard Work Needed.")


                                                    def current_earning(monthly_salary):
                                                        if monthly_salary >= 1000000000:
                                                            return "You are doing great earn more Manas!!"
                                                        else:
                                                            return "You need to add more efforts brother to win!!"


                                                    earning = int(input("Enter your current monthly salary:"))
                                                    print(current_earning(earning))

                                                    my_watch = {
                                                        "Brand": "Casio",
                                                        "Dial Color": "Sunray, Blue",
                                                        "Registered": True
                                                    }

                                                    my_watch["Price"] = 8000
                                                    print(my_watch)

                                                    dev_profile = {
                                                        "Skills": ["Python", "HTML", "CSS"],
                                                        "Targets": {"Money": "10CR", "Grade": "11th"},
                                                        "Health Status": "Recovering"

                                                    }

                                                    print("Targeting  " + dev_profile["Targets"]["Money"] + " in " +
                                                          dev_profile["Targets"]["Grade"] + " grade" + " with " +
                                                          dev_profile["Skills"][0] + " skills.")


                                                    def money_needed(income):
                                                        if income < 10_00_00_000:
                                                            return 10_00_00_000 - income
                                                        else:
                                                            return "You are doing great!!"


                                                    earnings = int(input("Enter the earnings: "))

                                                    print(f"You need {money_needed(earnings):,} to reach your goal")

                                                    lakhs = [20, 45, 13, 34]
                                                    doubled_lakhs = []

                                                    for i in lakhs:
                                                        doubled_lakhs.append(i * 2)

                                                    print(doubled_lakhs)

                                                    earnings_2027 = {
                                                        "Freelance_Web": {"amount": 50000, "status": "Ready"},
                                                        "Python_Bot": {"amount": 120000, "status": "Pending"},
                                                        "App_Sub": {"amount": 30000, "status": "Ready"},
                                                        "Crypto_Trade": {"amount": 80000, "status": "Pending"}
                                                    }
                                                    pending_projects = []
                                                    bank_balance = 0
                                                    for keys, values in earnings_2027.items():
                                                        if earnings_2027[keys]["status"] == "Pending":
                                                            pending_projects.append(earnings_2027[keys]["amount"])
                                                        else:
                                                            bank_balance = bank_balance + earnings_2027[keys]["amount"]

                                                    print(pending_projects)
                                                    print(bank_balance)

                                                    a = input()
                                                    total = 0
                                                    for i in a:
                                                        total = total + int(i)

                                                    print(total)

                                                    a = int(input())
                                                    if a % 2 == 0:
                                                        print("Armstrong")
                                                    else:
                                                        print("Not Armstrong")

                                                        a = input('Enter numbers separated by a space')
                                                        b = list(map(int, a.split()))
                                                        print(max(b))

                                                        income_dictionary = {
                                                            "Freelancer": 10000,
                                                            "Apple": 40000,
                                                            "Samsung": 39000,
                                                            "D.R.D.O": 100000,
                                                            "I.S.R.O": 1000000,

                                                        }
                                                        Amount = 0
                                                        for values in income_dictionary.values():
                                                            if values > 100000:
                                                                print(f"This is a High-Value stream!! #{values:,}💸💸")
                                                            else:
                                                                print("This is a Low-Value stream!!")
                                                                password = "1245manas"
                                                                user = input("Enter your password: ")
                                                                trials = 5
                                                                counter = 0
                                                                while user != password:
                                                                    user = input("Enter your password: ")
                                                                    counter = counter + 1

                                                                    if trials - 1 == counter:
                                                                        print("No, more attempts left!!")
                                                                        break
                                                                    elif user == password:
                                                                        print("Welcome back !")

                                                                        my_collection = []

                                                                        Casio_MTD = {
                                                                            "Model": "AD23KDG23",
                                                                            "Dial_color": "Blue",
                                                                            "is_registered": True,

                                                                        }

                                                                        if Casio_MTD["is_registered"] == True:
                                                                            print("Protected")
                                                                        else:
                                                                            print("Not protected")

                                                                        my_collection.append(Casio_MTD)
                                                                        wealth_portfolio = []
                                                                        Asset1 = {
                                                                            "Name": "Casio MTD",
                                                                            "Value": 8000,
                                                                            "Type": "Physical"

                                                                        }
                                                                        Asset2 = {
                                                                            "Name": "Freelance Project",
                                                                            "Value": 150000,
                                                                            "Type": "Digital"
                                                                        }
                                                                        Asset3 = {
                                                                            "Name": "SaaS Subscription",
                                                                            "Value": 500000,
                                                                            "Type": "Digital"
                                                                        }

                                                                        wealth_portfolio.append(Asset1)
                                                                        wealth_portfolio.append(Asset2)
                                                                        wealth_portfolio.append(Asset3)
                                                                        total_value = 0
                                                                        for values in wealth_portfolio:
                                                                            total_value += values["Value"]
                                                                            if values["Type"] == "Digital":
                                                                                print(values["Name"])
                                                                                wealth_portfolio = []
                                                                                Asset1 = {
                                                                                    "Name": "Casio MTD",
                                                                                    "Value": 8000,
                                                                                    "Type": "Physical"

                                                                                }
                                                                                Asset2 = {
                                                                                    "Name": "Freelance Project",
                                                                                    "Value": 150000,
                                                                                    "Type": "Digital"
                                                                                }
                                                                                Asset3 = {
                                                                                    "Name": "SaaS Subscription",
                                                                                    "Value": 500000,
                                                                                    "Type": "Digital"
                                                                                }

                                                                                wealth_portfolio.append(Asset1)
                                                                                wealth_portfolio.append(Asset2)
                                                                                wealth_portfolio.append(Asset3)
                                                                                for asset in wealth_portfolio:
                                                                                    if asset["Value"] > 100000:
                                                                                        print(asset["Name"],
                                                                                              asset["Value"])

                                                                                total_value = 0

                                                                                name = input(
                                                                                    "Enter the name for the asset:")
                                                                                value = int(input(
                                                                                    "Enter the value for the asset:"))
                                                                                Asset4 = {
                                                                                    name: value

                                                                                }
                                                                                wealth_portfolio.append(Asset4)

                                                                                print(wealth_portfolio)

                                                                                limit = int(input(
                                                                                    "Enter how many times you will be entering numbers: "))
                                                                                Group = []

                                                                                while limit > 0:
                                                                                    number = int(
                                                                                        input("Enter a number: "))
                                                                                    Group.append(number)
                                                                                    limit -= 1

                                                                                Even_summer = 0
                                                                                Even_counter = 0
                                                                                Odd_summer = 0
                                                                                Odd_counter = 0

                                                                                for i in Group:
                                                                                    if i % 2 == 0:
                                                                                        Even_counter += 1
                                                                                        Even_summer += i
                                                                                    else:
                                                                                        Odd_counter += 1
                                                                                        Odd_summer += i

                                                                                print(
                                                                                    f"The total number of even numbers is: {Even_counter} their sum is: {Even_summer}")
                                                                                print(
                                                                                    f"The total number of even numbers is: {Odd_counter} their sum is: {Odd_summer}")

                                                                                assets = ["Casio", "Bitcoin", "Gold"]
                                                                                web_tags = []
                                                                                for asset in assets:
                                                                                    if asset == "Bitcoin":

                                                                                        web_tags.append(
                                                                                            f"<h1 class='Crypto' > {asset} </h1>")
                                                                                    else:
                                                                                        web_tags.append(
                                                                                            f"<h1> {asset} </h1>")

                                                                                print(web_tags)

                                                                                portfolio = {"Casio": 12000,
                                                                                             "Bitcoin": 4500000,
                                                                                             "Gold": 60000}
                                                                                my_list = []
                                                                                for x, y in portfolio.items():
                                                                                    if y > 1_000_000:
                                                                                        my_list.append(
                                                                                            f"<h1> class='Whale'> {x} - VIP Asset </h1> ")
                                                                                    else:
                                                                                        my_list.append(
                                                                                            f"<h1 class='Standard'> {x} </h1>")
                                                                                        raw_data = [" casio ",
                                                                                                    "bitcoin", " GOLD ",
                                                                                                    "Ethereum "]
                                                                                        clean_data = []
                                                                                        for x in raw_data:
                                                                                            if x == "bitcoin":
                                                                                                clean_data.append(
                                                                                                    "💰 Bitcoin (King)")
                                                                                            else:
                                                                                                clean_data.append(x)
                                                                                                print(clean_data)
                                                                                                profits = [100, 5000,
                                                                                                           20, 1000000]
                                                                                            net_profit = 0
                                                                                            for i in profits:
                                                                                                if i < 100:
                                                                                                    continue
                                                                                                elif i > 10000:
                                                                                                    net_profit = net_profit + i * 0.7
                                                                                                else:
                                                                                                    net_profit = net_profit + i * 0.9
                                                                                            print(net_profit)

                                                                                            new_investments = [
                                                                                                " apple ", "tesla",
                                                                                                " MICROSOFT "]
                                                                                            amounts = [500, 1500000, 50]
                                                                                            html_list = []
                                                                                            new_amounts = []
                                                                                            for i in new_investments:
                                                                                                x = i.strip().capitalize()
                                                                                                if x == "Microsoft":
                                                                                                    html_list.append(
                                                                                                        f"<h1>{x}</h1>")
                                                                                                elif x == "Apple":
                                                                                                    html_list.append(
                                                                                                        f"<h1>{x}</h1>")

                                                                                            for i in amounts:
                                                                                                if i < 100:
                                                                                                    continue
                                                                                                elif i > 1000000:
                                                                                                    new_amounts.append(
                                                                                                        i * 0.7)
                                                                                                else:
                                                                                                    new_amounts.append(
                                                                                                        i * 0.9)

                                                                                            print(
                                                                                                f"Here are the new amounts: {new_amounts} and here is the new list {html_list}")
                                                                                            numbers = [2, 3, 4]
                                                                                            counter = 0
                                                                                            for num in numbers:
                                                                                                void = 1
                                                                                                for i in range(1,
                                                                                                               num + 1):
                                                                                                    void = void * i

                                                                                                counter = counter + void

                                                                                            print(counter)

                                                                                            numbers = [2, 3, 4]
                                                                                            storer = 0
                                                                                            counter = 0
                                                                                            for i in numbers:
                                                                                                storer = 1
                                                                                                for j in range(1,
                                                                                                               i + 1):
                                                                                                    storer = storer * j
                                                                                                    if storer >= 10:
                                                                                                        storer = storer % 2
                                                                                                        storer = storer // 2
                                                                                                counter = counter + storer
                                                                                            print(counter)

                                                                                            n = int(input())
                                                                                            total = 0
                                                                                            new_number = 1
                                                                                            while n > 0:
                                                                                                total = n % 10

                                                                                                factorial = total * 1
                                                                                                new_number = new_number * factorial
                                                                                                n = n // 10
                                                                                            print(new_number)
                                                                                            items = ["Watch", "Phone"]
                                                                                            prices = [12000, 50000]
                                                                                            for i in range(len(items)):
                                                                                                print(
                                                                                                    f"{items[i]} costs {prices[i]}")

                                                                                                assets = ["Casio",
                                                                                                          "Bitcoin",
                                                                                                          "Ethereum",
                                                                                                          "Dogecoin"]
                                                                                                values = [12000,
                                                                                                          8500000,
                                                                                                          250000, 8000]

                                                                                                for i in range(
                                                                                                        len(assets)):
                                                                                                    name = assets[i]
                                                                                                    value = values[i]

                                                                                                    if value > 100000:
                                                                                                        print(
                                                                                                            f"<div class='whale-card'> {name} </div>")
                                                                                                    else:
                                                                                                        print(
                                                                                                            f"<div class='small-card'> {name} </div>")

                                                                                                        assets = [
                                                                                                            "Casio MTD-135D",
                                                                                                            "Bitcoin",
                                                                                                            "Ethereum",
                                                                                                            "Gold (100g)",
                                                                                                            "Dogecoin",
                                                                                                            "Real Estate Fund"]
                                                                                                        values = [12000,
                                                                                                                  8500000,
                                                                                                                  240000,
                                                                                                                  650000,
                                                                                                                  15,
                                                                                                                  1200000]

                                                                                                        for i in range(
                                                                                                                len(assets)):
                                                                                                            name = \
                                                                                                            assets[i]
                                                                                                            value = \
                                                                                                            values[i]

                                                                                                            if value > 500000:
                                                                                                                print(
                                                                                                                    f"<div class='gold-glow'> {name}-{value} </div>'")
                                                                                                            elif 50000 <= value <= 500000:
                                                                                                                print(
                                                                                                                    f"<div class='silver-card'> {name}-{value} </div>")
                                                                                                            else:
                                                                                                                print(
                                                                                                                    f"<div class='standard-card'> {name}-{value} </div>")

                                                                                                                a = int(
                                                                                                                    input(
                                                                                                                        "Enter a number:"))
                                                                                                                gainer = 0
                                                                                                                while a > 0:
                                                                                                                    digit = a % 10
                                                                                                                    gainer = gainer + digit
                                                                                                                    a = a // 10
                                                                                                                print(
                                                                                                                    f"You earned {gainer}")































