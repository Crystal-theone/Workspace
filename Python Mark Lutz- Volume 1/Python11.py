import re

match = re.match('Uzair[ \t]*(.*)Tariq','Uzair Sample Tariq')
print(match.group(1))
