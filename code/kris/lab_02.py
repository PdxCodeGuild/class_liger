print("\nHello there! Before we look for job postings, we need to get some information from you.")
hair_color = input("\nFirst, what is the color of your hair: ")
height = input("\nWhat is your height in inches (ex: 66): ")
fav_color = input("\nWhat is your favorite color: ")
city = input('\nWhere do you live?: ')
height = int(height)
# print(hair_color,height,fav_color,city)
transportation = input("\nDo you have a car? (y/n): ")
transportation = transportation.lower()

print("\nI think we found a job for you! Take a look!")
if transportation == 'y':
    print(f'''Looking a chef in {city}, who wouldn't mind wearing a {fav_color} uniform,
must be between {height - 1} and {height + 1} inches, and must drive to work every day! ''')
else:
    print(f'''Looking a chef in {city}, who wouldn't mind wearing a {fav_color} uniform,
must be between {height - 1} and {height + 1} inches, and must use company vehicle! ''')