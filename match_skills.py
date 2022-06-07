"""
The purpose of this file it to read the official skills from the jobspikr API
and compare them to the skills I have in my database.
We need a txt file called my_skills.txt with a dump of skills from my database.
"""

with open('jobpikr_skills.txt') as f:
    lines = f.readlines()
    list_of_skills = [line.strip() for line in lines]

with open('my_skills.txt') as g:
    my_lines = g.readlines()
    list_of_my_skills = [my_line.strip() for my_line in my_lines]

matched_skills = [skill for skill in list_of_my_skills if skill in list_of_skills]
print(matched_skills)