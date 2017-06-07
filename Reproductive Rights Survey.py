import random #I'm thinking I'll need random lib for some rng
import time #Might need this?
import pygame #Considering using a graphical interface with pygame, not required#

countryIndex = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan",
"Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia" "Bosnia and Herzegovina,", "Botswana,", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burma", "Burundi",
"Cambodia", "Cameroon", "Cabo Verde", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Democratic Republic of the Congo", "The Republic of Congo",
"Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Curacao", "Cyprus", "Czechia", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor",
"Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "The Gambia",
"Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Holy See", "Honduras", "Hong Kong",
"Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya",
"Kiribati", "North Korea", "South Korea", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
"Lithuania", "Luxembourg", "Macau", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania",
"Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Namibia", "Nauru", "Nepal", "Netherlands",
"New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", " Oman", "Pakistan", "Palau", "Palestinian Territories", "Panama", "Papua New Guinea",
"Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
"Samoa", "San Marino", "San Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Sint Maarten",
"Slovakia", "Slovenia", "Solomon Islands", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden",
"Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan",
"Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Yemen", "Vietnam",
"Zambia", "Zimbabawe"]
continentIndex = ["Africa", "Antarctica", "Asia", "Australia", "Europe", "North America", "South America"]
#Instead of doing this Just make one big multi line List because this is bad
print("Welcome to our Reproductive Rights Survey, made by Marcus Wong and Henry Ramos!")
print("Here, we will ask you a variety of questions in order to inform you about Women's Reproductive Rights around the world.")


username = input("First, let's start with your name: ")
print("Nice to meet you," , username)
print("Okay, so now we'll pick a continent. Please be sure to capitalize the name! I.E Asia instead of asia.")
continentChoice = input("What continent is the country in? If you don't know, pick any!:  ")


if continentChoice == continentIndex[0]:
    print("So you'd like to learn more about ",continentIndex[0], "huh? Interesting!")
elif continentChoice == continentIndex[1]:
    print("So you'd like to learn more about",continentIndex[1], "huh? Cool choice!")
elif continentChoice == continentIndex[2]:
    print("So you'd like to learn more about",continentIndex[2], "huh? Alright!")
elif continentChoice == continentIndex[3]:
    print("So you'd like to learn more about",continentIndex[3], "huh? Cool choice!")
elif continentChoice == continentIndex[4]:
    print("So you'd like to learn more about",continentIndex[4], "huh? Let's do it!")
elif continentChoice == continentIndex[5]:
    print("So you'd like to learn more about",continentIndex[5], "huh? That's where we live!")
elif continentChoice == continentIndex[6]:
    print("So you'd like to learn more about",continentIndex[6], "huh? Interesting!")
else:
    print("Something went wrong, please make sure you spelled and formatted the continent properly!")
asia = ["Afghanistan", "Azerbaijan", "Armenia", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China", "Cyprus"]
asia2 = ["Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait"]
asia3 = ["Kyrgyzstan", "Laos", "Lebanon","Malaysia", "Maldives", "Mongolia", "Myanmar", "Burma", "Nepal", "North Korea"]
asia4 = ["Oman", "Pakistan", "Palestine", "Philippines", "Qatar", "Russia", "Saudi Araia", "Singapore", "South Korea", "Sri Lanka"]
asia5 = ["Syria", "Taiwan", "Tajikistan", "Thailand", "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"]
countryChoice = input("Which country in your chosen continent would you like to learn about?:")
if countryChoice == asia[]:
    print("So you chose", asia[])
