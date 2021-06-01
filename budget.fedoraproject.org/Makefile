include ../Makefile.in

# no translation
pullpos: ;

$(LANGUAGES): % : | static rss-cache po/%.mo data/templates/translations.html
	$(PYTHON) $(BUILDDIR)/build.py -o out -i data/content -l $@ -p po -b $(BASEPATH)

