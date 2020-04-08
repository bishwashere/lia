from bs4 import BeautifulSoup as bsoup4
import urllib2
import json
import urllib
import cookielib
import re
import time
import datetime

SEARCH_LOCATION = "Iowa, United States"
SEARCH_KEYWORD = "Software Engineer"
MAX_JOB_CYCLE = 20


cookie = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

java_regex = re.compile('( |^)?java( |$|.|,)', re.I)
javascript_regex = re.compile('( |^)?(javascript|JS)( |$|.|,)', re.I)
json_regex = re.compile('( |^)?json( |$|.|,)', re.I)
soap_regex = re.compile('( |^)?soap( |$|.|,)', re.I)
css_regex = re.compile('( |^)?css( |$|.|,)', re.I)
sql_regex = re.compile('( |^)?sql( |$|.|,)', re.I)
git_regex = re.compile('( |^)?git( |$|.|,)', re.I)
nosql_regex = re.compile('( |^)?nosql( |$|.|,)', re.I)
spring_regex = re.compile('( |^)?spring( |$|.|,)', re.I)
unittest_regex = re.compile('( |^)?unit( )?test', re.I)
agile_regex = re.compile('( |^)?agile( |$|.|,)', re.I)
cicd_regex = re.compile('( |^)?ci\/cd( |$|.|,)', re.I)
python_regex = re.compile('( |^)?python( |$|.|,)', re.I)
react_regex = re.compile('( |^)?react( |$|.|,)', re.I)
docker_regex = re.compile('( |^)?docker( |$|.|,)', re.I)
postgres_regex = re.compile('( |^)?postgres( |$|.|,)', re.I)
aws_regex = re.compile('( |^)?aws( |$|.|,)', re.I)
kanban_regex = re.compile('( |^)?kanban( |$|.|,)', re.I)
maven_regex = re.compile('( |^)?maven( |$|.|,)', re.I)
bamboo_regex = re.compile('( |^)?bamboo( |$|.|,)', re.I)
aspnet_regex = re.compile('( |^)?asp\.net( |$|.|,)', re.I)
dotnet_regex = re.compile('( |^)?dot( )?net( |$|.|,)', re.I)
ajax_regex = re.compile('( |^)?ajax( |$|.|,)', re.I)
angular_regex = re.compile('( |^)?angular( |$|.|,)', re.I)
csharp_regex = re.compile('( |^)?c\#( |$|.|,)', re.I)
jsp_regex = re.compile('( |^)?jsp( |$|.|,)', re.I)
cobol_regex = re.compile('( |^)?cobol( |$|.|,)', re.I)
devops_regex = re.compile('( |^)?dev( )?ops?( |$|.|,)', re.I)
azure_regex = re.compile('( |^)?azure( |$|.|,)', re.I)
windows_regex = re.compile('( |^)?windows( |$|.|,)', re.I)
jquery_regex = re.compile('( |^)?jquery( |$|.|,)', re.I)


print datetime.datetime.now()
print "Analyzing for:"
print "\tLocation: %s" % SEARCH_LOCATION
SEARCH_LOCATION = urllib.quote(SEARCH_LOCATION)

print "\tKeyword: %s" % SEARCH_KEYWORD
SEARCH_KEYWORD = urllib.quote(SEARCH_KEYWORD)
print "\tLooking at: %d" % (MAX_JOB_CYCLE*25) + " jobs (as analysis sample)"

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

java_match_count = 0
javascript_match_count = 0
json_match_count = 0
soap_match_count = 0
css_match_count = 0
sql_match_count = 0
git_match_count = 0
nosql_match_count = 0
spring_match_count = 0
unittest_match_count = 0
agile_match_count = 0
cicd_match_count = 0
python_match_count = 0
react_match_count = 0
docker_match_count = 0
postgres_match_count = 0
aws_match_count = 0
kanban_match_count = 0
maven_match_count = 0
bamboo_match_count = 0
aspnet_match_count = 0
dotnet_match_count = 0
ajax_match_count = 0
angular_match_count = 0
csharp_match_count = 0
jsp_match_count = 0
cobol_match_count = 0
devops_match_count = 0
azure_match_count = 0
windows_match_count = 0
jquery_match_count = 0


total_jobs = 0

for job_details_link in job_description_a_tag_list:
	job_detail_link = job_details_link['href'] # job_detail_link = job_description_a_tag_list[0]['href']
	job_detail_handler = opener.open(job_detail_link)
	job_details_html = job_detail_handler.read()

	job_details_soup = bsoup4(job_details_html, 'html.parser')
	job_description_text = job_details_soup.find('section', {'class':'description'}).text

	java_match = java_regex.search(job_description_text)
	javascript_match = javascript_regex.search(job_description_text)
	json_match = json_regex.search(job_description_text)
	soap_match = soap_regex.search(job_description_text)
	css_match = css_regex.search(job_description_text)
	sql_match = sql_regex.search(job_description_text)
	git_match = git_regex.search(job_description_text)
	nosql_match = nosql_regex.search(job_description_text)
	spring_match = spring_regex.search(job_description_text)
	unittest_match = unittest_regex.search(job_description_text)
	agile_match = agile_regex.search(job_description_text)
	cicd_match = cicd_regex.search(job_description_text)
	python_match = python_regex.search(job_description_text)
	react_match = react_regex.search(job_description_text)
	docker_match = docker_regex.search(job_description_text)
	postgres_match = postgres_regex.search(job_description_text)
	aws_match = aws_regex.search(job_description_text)
	kanban_match = kanban_regex.search(job_description_text)
	maven_match = maven_regex.search(job_description_text)
	bamboo_match = bamboo_regex.search(job_description_text)
	aspnet_match = aspnet_regex.search(job_description_text)
	dotnet_match = dotnet_regex.search(job_description_text)
	ajax_match = ajax_regex.search(job_description_text)
	angular_match = angular_regex.search(job_description_text)
	csharp_match = csharp_regex.search(job_description_text)
	jsp_match = jsp_regex.search(job_description_text)
	cobol_match = cobol_regex.search(job_description_text)
	devops_match = devops_regex.search(job_description_text)
	azure_match = azure_regex.search(job_description_text)
	windows_match = windows_regex.search(job_description_text)
	jquery_match = jquery_regex.search(job_description_text)

	if java_match:
		java_match_count += 1
	if javascript_match:
		javascript_match_count += 1
	if json_match:
		json_match_count += 1
	if css_match:
		css_match_count += 1
	if sql_match:
		sql_match_count += 1
	if git_match:
		git_match_count += 1
	if soap_match:
		soap_match_count += 1
	if nosql_match:
		nosql_match_count += 1
	if spring_match:
		spring_match_count += 1
	if unittest_match:
		unittest_match_count += 1
	if agile_match:
		agile_match_count += 1
	if cicd_match:
		cicd_match_count += 1
	if python_match:
		python_match_count += 1
	if react_match:
		react_match_count += 1
	if docker_match:
		docker_match_count += 1
	if postgres_match:
		postgres_match_count += 1
	if aws_match:
		aws_match_count += 1
	if kanban_match:
		kanban_match_count += 1
	if maven_match:
		maven_match_count += 1
	if bamboo_match:
		bamboo_match_count += 1
	if aspnet_match:
		aspnet_match_count += 1
	if dotnet_match:
		dotnet_match_count += 1
	if ajax_match:
		ajax_match_count += 1
	if angular_match:
		angular_match_count += 1
	if csharp_match:
		csharp_match_count += 1
	if jsp_match:
		angular_match_count += 1
	if cobol_match:
		cobol_match_count += 1
	if devops_match:
		devops_match_count += 1
	if azure_match:
		azure_match_count += 1
	if windows_match:
		windows_match_count += 1
	if jquery_match:
		jquery_match_count += 1

	total_jobs+=1

job_batch_count = 25
while job_batch_count<(MAX_JOB_CYCLE*25):

	# job more list
	job_list_more_handler = opener.open("https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=%s&location=%s&trk=homepage-basic_jobs-search-bar_search-submit&redirect=false&start=%s" % (SEARCH_KEYWORD, SEARCH_LOCATION, job_batch_count))
	job_list_html = job_list_more_handler.read()

	# job details
	job_list_soup = bsoup4(job_list_html ,'html.parser')
	job_description_a_tag_list = job_list_soup.find_all('a', {'class': 'result-card__full-card-link'})

	for job_details_link in job_description_a_tag_list:
		job_detail_link = job_details_link['href'] # job_detail_link = job_description_a_tag_list[0]['href']
		job_detail_handler = opener.open(job_detail_link)
		job_details_html = job_detail_handler.read()

		job_details_soup = bsoup4(job_details_html ,'html.parser')
		job_description_text = job_details_soup.find('section', {'class':'description'}).text

		java_match = java_regex.search(job_description_text)
		javascript_match = javascript_regex.search(job_description_text)
		json_match = json_regex.search(job_description_text)
		soap_match = soap_regex.search(job_description_text)
		css_match = css_regex.search(job_description_text)
		sql_match = sql_regex.search(job_description_text)
		git_match = git_regex.search(job_description_text)
		nosql_match = nosql_regex.search(job_description_text)
		spring_match = spring_regex.search(job_description_text)
		unittest_match = unittest_regex.search(job_description_text)
		agile_match = agile_regex.search(job_description_text)
		cicd_match = cicd_regex.search(job_description_text)
		python_match = python_regex.search(job_description_text)
		react_match = react_regex.search(job_description_text)
		docker_match = docker_regex.search(job_description_text)
		postgres_match = postgres_regex.search(job_description_text)
		aws_match = aws_regex.search(job_description_text)
		kanban_match = kanban_regex.search(job_description_text)
		maven_match = maven_regex.search(job_description_text)
		bamboo_match = bamboo_regex.search(job_description_text)
		aspnet_match = aspnet_regex.search(job_description_text)
		dotnet_match = dotnet_regex.search(job_description_text)
		ajax_match = ajax_regex.search(job_description_text)
		angular_match = angular_regex.search(job_description_text)
		csharp_match = csharp_regex.search(job_description_text)
		jsp_match = jsp_regex.search(job_description_text)
		cobol_match = cobol_regex.search(job_description_text)
		devops_match = devops_regex.search(job_description_text)
		azure_match = azure_regex.search(job_description_text)
		windows_match = windows_regex.search(job_description_text)
		jquery_match = jquery_regex.search(job_description_text)

		if java_match:
			java_match_count += 1
		if javascript_match:
			javascript_match_count += 1
		if json_match:
			json_match_count += 1
		if css_match:
			css_match_count += 1
		if sql_match:
			sql_match_count += 1
		if git_match:
			git_match_count += 1
		if soap_match:
			soap_match_count = 1
		if nosql_match:
			nosql_match_count = 1
		if spring_match:
			spring_match_count = 1
		if unittest_match:
			unittest_match_count = 1
		if agile_match:
			agile_match_count = 1
		if cicd_match:
			cicd_match_count += 1
		if python_match:
			python_match_count += 1
		if react_match:
			react_match_count += 1
		if docker_match:
			docker_match_count += 1
		if postgres_match:
			postgres_match_count += 1
		if aws_match:
			aws_match_count += 1
		if kanban_match:
			kanban_match_count += 1
		if maven_match:
			maven_match_count += 1
		if bamboo_match:
			bamboo_match_count += 1
		if aspnet_match:
			aspnet_match_count += 1
		if dotnet_match:
			dotnet_match_count += 1
		if ajax_match:
			ajax_match_count += 1
		if angular_match:
			angular_match_count += 1
		if csharp_match:
			csharp_match_count += 1
		if jsp_match:
			angular_match_count += 1
		if cobol_match:
			cobol_match_count += 1
		if devops_match:
			devops_match_count += 1
		if azure_match:
			azure_match_count += 1
		if windows_match:
			windows_match_count += 1
		if jquery_match:
			jquery_match_count += 1

		total_jobs+=1

	job_batch_count += 25


print "Number of jobs asking for:"
print "\tJAVA: %d" % java_match_count
print "\tJavaScript: %d" % javascript_match_count
#print "\tJSON: %d" % json_match_count
#print "\tCSS: %d" % css_match_count
print "\tSQL: %d" % sql_match_count
print "\tGIT: %d" % git_match_count
#print "\tSOAP: %d" % soap_match_count
#print "\tNoSQL: %d" % nosql_match_count
#print "\tSpring: %d" % spring_match_count
#print "\tUnit Test: %d" % unittest_match_count
#print "\tAgile: %d" % agile_match_count
print "\tCI/CD: %d" % cicd_match_count
print "\tPython: %d" % python_match_count
print "\tReact: %d" % react_match_count
print "\tDocker: %d" % docker_match_count
print "\tPostgres: %d" % postgres_match_count
print "\tAWS: %d" % aws_match_count
print "\tKanban: %d" % kanban_match_count
print "\tMaven: %d" % maven_match_count
print "\tBamboo: %d" % bamboo_match_count
print "\tASP.Net: %d" % aspnet_match_count
print "\tDot Net: %d" % dotnet_match_count
print "\tAJAX: %d" % ajax_match_count
print "\tAngular: %d" % angular_match_count
print "\tC#: %d" % csharp_match_count
print "\tJSP: %d" % jsp_match_count
print "\tCOBOL: %d" % cobol_match_count
print "\tDev Ops: %d" % devops_match_count
print "\tAzure: %d" % azure_match_count
print "\tWindows: %d" % windows_match_count
print "\tjQuery: %d" % jquery_match_count

