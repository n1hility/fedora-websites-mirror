# NOTE

The getfedora.org sources now live in [a new repository](https://pagure.io/fedora-web/websites/)
and are built with Flask and Frozen-Flask.
The other sites remain in *this* current repository that you are looking at right now.

---------------------------------------------------------------------------------------------------

This is the Fedora Websites GIT repo used to build the websites starting
from the F24 release cycle.

History of previous commits is still available in the [old repo on Fedora Hosted](https://git.fedorahosted.org/cgit/fedora-web.git/). **For more information please read the [documentation](https://docs.pagure.org/fedora-websites/) and the [Fedora Websites pages on the Fedora Wiki](https://fedoraproject.org/wiki/Websites)**

### Contributing
If you like to help the websites team but are not actually a member, you 
can easily file Pull Requests. Fork this repository, make your changes and
submit them here. Check of the [Fedora Websites wiki](https://fedoraproject.org/wiki/Websites#Join_the_Websites_Team) for details on how to
become a member of the websites team. 

Translations are handled by the Fedora [localization team](https://fedoraproject.org/wiki/L10N) on [Zanata](https://fedora.zanata.org/project/view/fedora-web).

### Websites
This repository contains the sources for the following Fedora Websites:

* http://alt.fedoraproject.org
* http://arm.fedoraproject.org
* http://boot.fedoraproject.org
* http://budget.fedoraproject.org
* http://fedoracommunity.org
* http://fedorahosted.org
* http://fedorapeople.org
* http://fedoraproject.org
* http://flocktofedora.org
* http://fudcon.fedoraproject.org
* http://labs.fedoraproject.org
* http://mirrors.fedoraproject.org
* http://spins.fedoraproject.org
* http://start.fedoraproject.org

### Getting started

**WARNING:** DO NOT execute the following steps as root, just use your normal user:

#### 1. Setup your system

    sudo dnf install git gettext python-genshi python-lxml python-setuptools python-dateutil \
    python-dogpile-cache babel python-feedparser fedfind python-requests python2-babel

    sudo dnf groups install 'Web Server'

#### 2. Clone the fedora-websites repo

    git clone https://pagure.io/fedora-websites.git

#### 3. Enter the directory of the website you want to work on
For example, if you want to work on getfedora.org, use:

    cd fedora-websites/getfedora.org

#### 4. Launch a test instance

    make en test

#### 5. Stop the test instance

    make stoptest

**Note:** if you have caching problems you can clean the instance even more:

    make veryclean
