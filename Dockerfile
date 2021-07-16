FROM fedora:30
MAINTAINER Rick Elrod <relrod@redhat.com>

WORKDIR /opt/oldrepo/

RUN  dnf install -y git gettext python-genshi python-lxml python-setuptools \
     python-dateutil python-dogpile-cache babel python-feedparser fedfind \
     python-requests python2-babel python-langtable findutils make httpd

EXPOSE 5000
