from bs4 import BeautifulSoup
import smtplib
#email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# system date and time manipulation
import datetime
now = datetime.datetime.now()
import requests
#email content placeholder

content = ""

#extraction Hacker News Stories

def extract_news(url):
    print("Extracting Hacker News Stories....")
    cnt = ''
    cnt += ('<b>HN Top Stores:</b>\n' + '<br>' + '-'*50 + '<br>')
    # use the first three lines to create a body in cnt
    response = requests.get(url)
    # gets the content of the url and stores in the "request" variable 
    content = response.content
    # stores the content of "response" var in local var "content" using the methond .content
    soup = BeautifulSoup(content, 'html.parser')
    '''
    using HTML parse to make "soup" funtion to grab HACKERNEWS article list
    method 'soup.findall' targets 'td - tablecell' tag with attributes
    "class : 'title'" and "valign: "
    the enumerate for loop will create a modified numbered list for the email body
    to help houses the content of the website
    it is top stop once it hits the "MORE" tag in the website
    '''
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        # cnt += (tag.text if tag.text != 'More' else '')
        cnt += ((str(i+1)+' :: '+tag.text + "\n" + '<br>') if tag.text != 'More' else '')
        #print(tag.prettify) #find all('span', attrs={'class':'sitestr'}))
    return(cnt)

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br> __________ </br>')
content += ('<br><br>End of Message')

print(content)
#Email Authentication
print("Composing Email")
#update your email details

SERVER = 'smtp.gmail.com'
PORT = 587
TO = 'sapkota.5620@gmail.com'
FROM = 'freak5620@gmail.com'
PASS = '##################'

# fp = open(file_name, 'rb')
# create a text/plain message
# msg = MIMEText('')
msg = MIMEMultipart()

#msg.add_header('Content-Disposition', 'attachment', filename='empty.txt')
#Create a dynamic email subject and header

msg['Subject'] = 'Top News Storries -HN [Automated Email]' + '' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['Top'] = TO
#attaching the web scraped content to this msg object using MIMEText
msg.attach(MIMEText(content, 'html'))
#fp.close()

print('Initialize Server.....')
print(msg.as_string())
server = smtplib.SMTP(SERVER, PORT)
#server = smtplin.SMTP_SSL('smtp.gmail.com', 465)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())
print('Email sent..')
server.quit()
