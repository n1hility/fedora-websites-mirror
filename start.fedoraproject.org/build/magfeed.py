import codecs
import os
import sys
import feedparser

FedMag = ['https://fedoramagazine.org/feed']

html = """
<!DOCTYPE html>
<html lang="en"
  xmlns="http://www.w3.org/1999/xhtml"
  xmlns:py="http://genshi.edgewall.org/"
  xmlns:xi="http://www.w3.org/2001/XInclude"
  py:strip="">
"""

for feed in map(feedparser.parse, FedMag):
    for item in feed["items"][:5]:
        # Date format: '%a, %d %b %Y %H:%M:%S +0000'
        # removing '[...]' from the summary, so its cleaner
        summary = item.summary.rstrip(' [&#8230;]').replace("&#8217;", "'").replace("&#8217", "'")
        item.title = item.title.replace("&", "&#38;")
        # find the first image enclosure
        for image_enclosure in item.enclosures:
            if image_enclosure.get('type') == 'image/jpg':
                break

        html += """
        <div class="hidden-xs col-sm-1 top-margin">
			<p class="month">%s</p>
			<p class="day">%s</p>
		</div>
        <div class="col-xs-12 col-sm-11 white">
        	<div class="row">
        		<div class="col-xs-1 col-sm-1 hidden-xs">
        		<img src="%s" />
        		</div>
        		<div class="col-xs-11 col-sm-10">
					  <a class="title" href="%s"><h3>%s</h3></a>
				</div>
        		<div class="hidden-xs col-sm-1 comments pull-right">
					<i class="fa fa-fw fa-comment comment-icon"></i>%s
				</div>
        	</div>
        	<div class="row">
        		<div class="col-xs-12 col-sm-11 col-sm-offset-1">
        		<p>%s...</p>
				<a href="%s" class="pull-right readme">Read more ...</a>
        		</div>
        	</div>
		</div>
        """ % (item.updated.split()[2], item.updated.split()[1], image_enclosure.href.replace("&", "&#38;"), item.links[0]['href'], item.title,
			item.slash_comments, summary, item.links[0]['href'])
#print item.content
#break
html += """
</html>"""

with codecs.open('data/templates/magfeed.html', 'w', 'utf8') as f:
    f.write(html)
