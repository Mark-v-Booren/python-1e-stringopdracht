# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Gullit 32'
# Van Basten 54'
scorerName1 = 'Ruud Gullit'
scorerName2 = 'Marco an Basten'
goal1 = '32'
goal2 = '54'


report = f'{scorerName1} scored in the {goal1}nd minute and \n{scorerName2} scored in the {goal2}th minute!'

print(report)

player = 'Hans van Breukelen'
playerName = player.split()
firstName = playerName[0]
lastName = playerName[-1]
nameShort = firstName[0] +'. van ' + playerName[-1]

lastNamelenght = len(lastName)

chantLen = len(firstName)
chantName = (firstName+"!") * chantLen
goodChant= chantName[-1] != ''

print(firstName, lastName, lastNamelenght, nameShort, chantName, goodChant) 
