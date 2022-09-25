import requests
import datetime

api_key = '30d4741c779ba94c470ca1f63045390a'



print("________________________________________________________________________________________________________________________________________________")

print("\n")
print(" d888888b d88888b d8888b. .88b  d88. d888888b d8b   db  .d8b.  db           db   d8b   db d88888b  .d8b.  d888888b db   db d88888b d8888b.  ")
print(" `~~88~~' 88'     88  `8D 88'YbdP`88   `88'   888o  88 d8' `8b 88           88   I8I   88 88'     d8' `8b `~~88~~' 88   88 88'     88  `8D  ")
print("    88    88ooooo 88oobY' 88  88  88    88    88V8o 88 88ooo88 88           88   I8I   88 88ooooo 88ooo88    88    88ooo88 88ooooo 88oobY' ")
print("    88    88.     88 `88. 88  88  88   .88.   88  V888 88   88 88booo.      `8b d8'8b d8' 88.     88   88    88    88   88 88.     88 `88. ")
print("    YP    Y88888P 88   YD YP  YP  YP Y888888P VP   V8P YP   YP Y88888P       `8b8' `8d8'  Y88888P YP   YP    YP    YP   YP Y88888P 88   YD  ")


print("________________________________________________________________________________________________________________________________________________")
print("\n")

print("                              Terminal based Weather reporting tool codded in Python - @sakibulalikhan     ")

print("________________________________________________________________________________________________________________________________________________")
print("\n")


user_input = input("Enter City: ") 

weather_data = requests.get(

    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")



e = datetime.datetime.now()

print ("\nToday's date: = %s/%s/%s" % (e.day, e.month, e.year))


if weather_data.json()['cod'] == '404':
    print("\nNo City Found")
else:

    weather = weather_data.json() ['weather'] [0] ['main'] 
    temp = weather_data.json() ['main'] ['temp']
    feels_like = weather_data.json() ['main'] ['feels_like']
    humidity = weather_data.json() ['main'] ['humidity']
    visibility = weather_data.json() ['visibility']
    wind = weather_data.json() ['wind']
    

    print(f"\nThe weather in {user_input} is: {weather}")
    print(f"\nThe temperature in {user_input} is: {temp}ºF and feels like {feels_like}ºF")
    print(f"\nThe humadity in {user_input} is: {humidity}%")
    print(f"\nThe visibility in {user_input} is: {visibility}")
    print(f"\nThe wind speed in {user_input} is: {wind}")
    


print("\n")
print("________________________________________________:HAPPY_WEATHER:________________________________________________")
