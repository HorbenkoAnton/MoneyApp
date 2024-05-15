#Building app from zero is pretty hard task so I think I'll split it

#First of all what I want from this app. 

'''It's simple program to help me track my monthly expenses.'''

# Key purpose just store info about my expenses.
# Additional purpose give some stats and help with analitics.(but it's later)

#I want to have some categories of expenses and whole expenses number(sum of all categories). 
#Be able to control categories, control amount of money I add.
#Also I want auth system.I want each user to have their own exenses list.

#Also I want cool name and logo design 😎😎😎
#I already have idea for a name if I named folder MoneyApp and it's sound like MoneyUp.
#(that's pretty chill and and reveals whole program purpose i think)
#And logo might be something like coin with an arrow pointing upwords 

#Some kind of blocks I probably need:
#Authentication
#Expenses
# *extend later*
#(something like notifications, and other features gonna be later now let's keep it simple)

#Models?I think
#category: name, owner;
#exepnse: name,amount,description(optional), category, date, owner; 

#UserProfile: name, expenses ,categories;

#step by step:
#database setup
#apps creation
#models
#serializers
#views
#urls