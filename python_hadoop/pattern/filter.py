#!/usr/bin/env python

import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        body = line[4]
        body_without_last_char = body[:-1]
        if len(re.findall("\.|\?|!", body_without_last_char)) > 0:
            continue
        else:
            writer.writerow(line)



test_text = """
import webapp2

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

month_abbvs = dict((m[:3].lower(), m) for m in months)

def valid_month(month): if month:

def valid_day(day): if day and day.isdigit():

def valid_year(year): if year and year.isdigit(): year = int(year) if year &gt; 1900 and year &lt;= 2020: return year

class MainHandler(webapp2.RequestHandler):

    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(form)
    def post(self):
        self.response.out.write(""Thanks for your Birthday info!"")

app = webapp2.WSGIApplication([('/', MainHandler)], #url mapping section
                              debug=True)
</code></pre>"	"question"	"\N"	"\N"	"2012-05-16 12:47:48.980972+00""0"	""	"6128269"	"100001071"	"2012-05-16 14:23:50.689135+00""6026126"	"\N"	"\N"	"362"	"f"


"""
# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()
