#!/usr/bin/python
import sys

languages = [("en", "en"),]

linguasfile = sys.argv[1]
linguas = open(linguasfile)
for l in linguas:
    lang = l.strip()
    if lang and not lang.startswith('#'):
        code = lang.lower().replace('_', '-')
        languages.append((lang, code))
linguas.close()

print '# Define the correct MIME type for specific languages'
for lang in ['bn', 'el', 'nb', 'pl', 'es', 'tr', 'sr', 'si', 'pt']:
    print 'AddType text/html .%s' % (lang)

print ' '

for (lang, code) in languages:
    print 'AddLanguage %s .%s' % (code, lang)

print '''
LanguagePriority en
ForceLanguagePriority Prefer Fallback

AddDefaultCharset utf-8

RewriteEngine on
'''

lang_regex = '|'.join(zip(*languages)[0])
print 'RewriteCond %%{QUERY_STRING} ^lang=(%s)$' % lang_regex
print 'RewriteRule ^(?:/(?:%s))?(/.*)$ /%%1$1? [R=301]' % lang_regex
print 'AliasMatch ^(?:/(?:%s))(/.*)?$ @DOCUMENTROOT@$1' % lang_regex

print '''
<Directory @DOCUMENTROOT@>
  Options MultiViews
'''

for (lang, code) in languages:
    print '  SetEnvIf Request_URI ^/%s/ prefer-language=%s' % (lang, code)

print '</Directory>'
