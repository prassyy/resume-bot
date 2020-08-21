#!/usr/bin/python

import slate3k as slate
import os

def addSummary(file, title, skillsFound, skillsMissing):
	file.write(title + '\n' + 'Skills found: ')
	for skill in skillsFound:
		file.write(skill + ', ')

	file.write('\nSkills Missing: ')
	for skill in skillsMissing:
		file.write(skill + ', ')
	file.write('\n\n')


#Open Keywords txt and load them in a list
keywords = set()
with open('keywords.txt', 'r') as fin: 
	for line in fin.readlines():
		keywords.add(line.rstrip().lower())
	fin.close()

#Open the summary csv file 
summary = open('summary.txt', 'w')

#open each pdf file in feed folder
for file in (f for f in os.scandir('feed/') if f.name.endswith('.pdf')):
	skillsFound = set()
	with open('feed/' + file.name, "rb") as resume:
		pdf_resume = slate.PDF(resume)
		for fragments in pdf_resume:
			pageText = fragments.lower()

			#look for occurrence of every phrase in keywords list and add them in a skills found dictionary if it exists
			for keyword in keywords:
				if pageText.count(keyword) > 0:
					skillsFound.add(keyword)
		resume.close()

	# Also create a skills not found list - (keywords - skills found)
	skillsMissing = keywords.difference(skillsFound)
	# In summary csv file create a new entry against the filename(candidate name) - and add the skills found and skills not found lists
	addSummary(summary, file.name, skillsFound, skillsMissing)
	print('Finished crawling through ' + file.name)

#save and close the summary file
summary.close()
print('Crawling done!')