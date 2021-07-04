#!/bin/env python

import ConfigParser, sys, os
import langtable

'''
This script takes the contents of the website-specific LINGUAS file, constructs an options menu for the languages contained therein.
It takes as argument the translations.ini relative path, the LINGUAS file relative path, and the output template name
'''

language_map = ConfigParser.ConfigParser()
language_map.readfp(open(sys.argv[1]))

banned = language_map.get('Banned', 'lang_code')

languages = [('en', 'English')]
with open(sys.argv[2], 'r') as linguas: # Linguas is where available languages are stored
    for lang in linguas:
        lang = lang.strip()
        if lang and not lang.startswith('#') and not lang in banned:
            languages.append((lang, langtable.language_name(languageId=lang).encode('utf-8')))
languages = sorted(languages)

with open(sys.argv[3], 'w') as output: # Output is a genshi template
    output.write('''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml"
	  xmlns:py="http://genshi.edgewall.org/"
	  xmlns:xi="http://www.w3.org/2001/XInclude"
	  py:strip="">

	<!-- This file is generated, don't edit here -->

	''')

    output.write('''
    <div class="dropup language-header">
      <span class="fa fa-language fa-lg"></span>
      <a class="dropdown-toggle" href="#" role="button" id="langSelect" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
        Change Language
      </a>
      <div class="dropdown-menu dropdown-menu-right language-menu" aria-labelledby="langSelect">
        <ul class="list-unstyled text-center" id="languagelist">
    ''')

    for l_code, l_name in languages:
        output.write('<li><a href="/'+ l_code +'/">'+ l_name +'</a></li>')

    output.write("""
        </ul>
      </div>
    </div>
	""")
    output.write('</html>')
