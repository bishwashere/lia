from bs4 import BeautifulSoup as bsoup4
import urllib2
import json
import urllib
import cookielib
import re
import time
import datetime
from difflib import SequenceMatcher

from variables import SEARCH_LOCATION, SEARCH_KEYWORD, MAX_JOB_CYCLE
from variables import COUNTER_DICT, KEYWORD_LIST

cookie = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

total_jobs = 0
duplicate_job_count = 0
error_count = 0
all_keywords_regex_list = list()
for item in KEYWORD_LIST:
	(keyword, regex) = item
	COUNTER_DICT[keyword] = 0


def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

def hit_link_and_parse_description(job_description_a_tag_list):
	global total_jobs
	global duplicate_job_count
	global KEYWORD_LIST
	global COUNTER_DICT
	global error_count
	global all_keywords_regex_list
	job_description_text = ''


	for job_details_link in job_description_a_tag_list:
		total_jobs+=1
		job_detail_link = job_details_link['href'] # job_detail_link = job_description_a_tag_list[0]['href']
		try:
			job_detail_handler = opener.open(job_detail_link)
		except Exception:
			error_count+=1
			continue

		job_details_html = job_detail_handler.read()
		job_details_soup = bsoup4(job_details_html, 'html.parser')
		job_description_text_temp = job_details_soup.find('section', {'class':'description'}).text
		if similar(job_description_text_temp, job_description_text) < 0.80:
			# Check if same job description is repeated in order which is seen many times in LinkedIn job posting.
			job_description_text=job_description_text_temp
		else:
			duplicate_job_count+=1
			continue

		for item in KEYWORD_LIST:
			(keyword, regex) = item
			keyword_regex = re.compile(regex, flags=re.I)
			keyword_match = keyword_regex.search(job_description_text)
			if keyword_match:
				COUNTER_DICT[keyword] = COUNTER_DICT[keyword]+1
			all_keywords_regex_list.append(keyword)
		else:
			all_keyword_regex = re.compile(' | '.join(all_keywords_regex_list), flags=re.I)
			if not all_keyword_regex.search(job_description_text):
				print job_detail_link

print datetime.datetime.now()
print "Analyzing for:"
print "\tLocation: %s" % SEARCH_LOCATION
SEARCH_LOCATION = urllib.quote(SEARCH_LOCATION)

print "\tKeyword: %s" % SEARCH_KEYWORD
SEARCH_KEYWORD = urllib.quote(SEARCH_KEYWORD)

print "\tLTry to get: %d" % (MAX_JOB_CYCLE*25) + " jobs"

main_link = "https://www.linkedin.com/jobs/search?location=%s" % SEARCH_LOCATION +"&redirect=false&keywords=%s&trk=homepage-basic_recent-search" % SEARCH_KEYWORD
job_list_handler = opener.open(main_link)
job_list_html = job_list_handler.read()

# job details
job_list_soup = bsoup4(job_list_html, 'html.parser')

latest_post_date_list = job_list_soup.find_all('time', {'class': 'job-result-card__listdate--new'})
if latest_post_date_list:
	latest_post_date = datetime.datetime.strptime("2020-01-01", '%Y-%m-%d')
	for item in latest_post_date_list:
		post_date = datetime.datetime.strptime(item['datetime'], '%Y-%m-%d')
		if latest_post_date < post_date:
			latest_post_hour = item.text
else:
	latest_post_date_list = job_list_soup.find_all('time', {'class': 'job-result-card__listdate'})
	if latest_post_date_list:
		latest_post_date = datetime.datetime.strptime("2020-01-01", '%Y-%m-%d')
		for item in latest_post_date_list:
			post_date = datetime.datetime.strptime(item['datetime'], '%Y-%m-%d')
			if latest_post_date < post_date:
				latest_post_hour = item.text

#print "\t(last job posted: " + latest_post_hour + ")"

job_description_a_tag_list = job_list_soup.find_all('a', {'class': 'result-card__full-card-link'})
hit_link_and_parse_description(job_description_a_tag_list)

job_batch_count = 25
while job_batch_count<(MAX_JOB_CYCLE*25):
	job_batch_count += 25

	# job more list
	job_list_more_handler = opener.open("https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=%s&location=%s&trk=homepage-basic_jobs-search-bar_search-submit&redirect=false&start=%s" % (SEARCH_KEYWORD, SEARCH_LOCATION, job_batch_count))
	job_list_html = job_list_more_handler.read()

	# job details
	job_list_soup = bsoup4(job_list_html ,'html.parser')
	job_description_a_tag_list = job_list_soup.find_all('a', {'class': 'result-card__full-card-link'})
	hit_link_and_parse_description(job_description_a_tag_list)

print "Analysed: %d" % total_jobs + " jobs (duplicate job post or URL unresponsive)"
print "Got: %d" % duplicate_job_count + " duplicate job posting"
print "Got: %d" % error_count + " HTTP Request denied error"


total_keyword_hit = 0
print "Number of jobs asking for:"
for key, value in sorted(COUNTER_DICT.items(), key=lambda item: item[1], reverse=True):
	if value != 0 and  value >= 5:
		print "\t"+key.upper()+": %d" % value
		total_keyword_hit+=value

print "Total keywords hit: %s" % total_keyword_hit

