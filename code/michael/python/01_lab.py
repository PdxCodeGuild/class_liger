# Career Game
# Thank you for playing Career Game. Our complex algorithm has determined that you are most
# suited for a career as a {occupation} working {bedtime} to {waketime}, {favorite_day} to 
# {favorite_day}, {favorite_number} weeks per year. Your salary will be ${cost_of_last_meal}
# every other {time_period}. You will work in {worst_place} and your commute will be 
# {minutes_to_disneyland} minutes each way.

print("""Hello, we are going to play Career Game today to determine your ideal career! Our
proprietary algorithm will calculate some complex data points to make sure you get connected 
to the career you are most suited for!""")

occupation = input("\nWhat is the worst job possible in your opinion: ")
bedtime = input('\nWhen do you typically go to bed: ')
waketime = input('\nWhen do you typically wake up: ')
favorite_day = input('\nWhat is the best day of week to relax and have fun: ')
favorite_number = input('\nWhat is your favorite number: ')
cost_of_last_meal = input('\nHow much did your most recent meal cost in dollars: ')
time_period = input('\nName a unit of time: ')
worst_place = input('\nWhat is the worst place to visit: ')
minutes_to_disneyland = input('\nHow many minutes would it take you to drive to Disneyland: ')

print(f'''Thank you for playing Career Game. Our complex algorithm has determined that you are most
suited for a career as a {occupation} working {bedtime} to {waketime}, {favorite_day} to 
{favorite_day}, {favorite_number} weeks per year. Your salary will be ${cost_of_last_meal}
every other {time_period}. You will work in {worst_place} and your commute will be 
{minutes_to_disneyland} minutes each way. Enjoy your new career! You start tomorrow :)''')