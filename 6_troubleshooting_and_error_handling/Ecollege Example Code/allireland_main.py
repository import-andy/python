# -- Imports --

import allireland as ai

# -- Function definations --

def display_instructions():
    '''Displays the program instructions and options list'''

    print('Entering your letter choice will show you the stats.')
    print('Enter A to show a list of all competing counties.')
    print('Enter B to show which team has won the most titles.')    
    print('Enter C to show table of all counties and how many titles they have won.')
    print('Enter D to show a list of all counties who have won a chosen amount of titles.')
    print('Enter E to show number of titles by province.')
    print('Enter F to add a title to a particular county.')
    print()


def get_userchoice():
    '''retruns the validated user choice letter'''
    bad_input = True

    while(bad_input):
        try:
            option = input("Enter option A - F. Press Q to quit: ")
            option = option.lower()
            if option not in ('a', 'b', 'c', 'd', 'e', 'f', 'q'): 
                raise ValueError
            bad_input = False 
        except ValueError:
            print('You must enter option A - F or press Q to quit:')

    return option


# A 1
def showallcounties():
    '''returns a set of all counties from the four provinces'''
    allcounties = ai.connacht.union(ai.leinster, ai.munster, ai.ulster)
    return allcounties

# 2 B
def most_titles(dict_table):
    '''
    Calculates which team has won the most championship titles

    returns: a tuple with the name of the top team and the amount of titles they have won
    '''
    topteam = list(dict_table.keys())[0]
    toptitle_amount = list(dict_table.values())[0]
    
    for team, numtitle in dict_table.items():       
        if numtitle > toptitle_amount:
            topteam = team
            toptitle_amount = numtitle

    return (topteam, toptitle_amount)


# C
def display_league_table():
    '''Displays a table list of counties and their titles form most to least'''
    copy_allireland_winners = dict()
    for team, titles in ai.allireland_winners.items():
        copy_allireland_winners[team] = titles

    while len(copy_allireland_winners) !=0:
        next_team = most_titles(copy_allireland_winners) 
        print(f'{next_team[0]} : {next_team[1]}')
        del copy_allireland_winners[next_team[0]]

            
# 2 province wins
def province_wins(province):
    '''Takes in a set of counties and returns the total title wins from that set'''
    total = 0
    for team in province:
        total += ai.allireland_winners[team]

    return total   


# 2 number of title
def counties_with_titlecount(titlecount):
    '''
    Takes in a number of titles and returns a tuple of all the counties who have won that many titles

    titlecount: the number of titles to check each county for
    '''
    countylist = []
    for team, titles in ai.allireland_winners.items():
        if titles == titlecount:
            countylist.append(team)

    return tuple(countylist)


# E
def increment_numtitles(county):
    '''increments a counties titles by 1

    county: The county to increment
    '''
    county = county.strip().title()
    if county not in ai.allireland_winners.keys():
        raise ValueError('This is not a valid county')
    else:
        ai.allireland_winners[county] += 1


# -- End of function definations --

# -- Main Program -- 
print('Welcome to All Ireland Stats!\n')
display_instructions()        

run_program = True

while(run_program):

    option = get_userchoice()

    if option == 'a':
        # A to show a list of all competing counties.
        for c in sorted(showallcounties()):
            print(c + ',', end=' ')
        print('\n')

    elif option == 'b':
        # B to show which team has won the most titles.
        team, titleamount = most_titles(ai.allireland_winners)
        print(f'{team} has won the most titles with {titleamount} in total')
        print()

    elif option == 'c':
        # C to show table of all counties and how many titles they have won.
        print('Team : Titles')
        print('-------------')
        display_league_table()
        print()

    elif option == 'd':
        # D to show a list of all counties who have won a chosen amount of titles.
        numtitles = int(input("Enter number of titles: "))
        print('Counties that won', numtitles, 'titles:')
        for c in counties_with_titlecount(numtitles):
            print(c.title())
        print()

    elif option == 'e':
        # E to show number of titles by province.
        print('Connact has won ' + str(province_wins(ai.connacht)) + ' titles')
        print('Leinster has won ' + str(province_wins(ai.leinster)) + ' titles')
        print('Munster has won ' + str(province_wins(ai.munster)) + ' titles')
        print('Ulster has won ' + str(province_wins(ai.ulster)) + ' titles')
        print()

    elif option == 'f':
        # F to add a title to a particular county.
        county_badinput = True
        while(county_badinput == True):
            countyentered = input("Please enter the latest All Ireland Champion: ")
            try:
                increment_numtitles(countyentered)
            except ValueError as ve:
                print(ve)
            else:
                county_badinput = False

    elif option == 'q':
        # Q Quits the program
        print('Thanks for using All Ireland Stats, goodbye!')
        run_program = False

