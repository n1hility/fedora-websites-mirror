#!/bin/bash
tmpdir=`mktemp -d`

outfile=$tmpdir/index.html
finalfile=/srv/people/site/index.html
cat <<EOM>>$outfile
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Fedora Project</title>
    <link rel="stylesheet" type="text/css" media="all" href="http://fedoraproject.org/static/css/fedora.css" />
    <!--[if lt IE 7]>
    <style type="text/css">
        #wrapper
        {
            height: 100%;
            overflow: visible;
        }
    </style>
    <![endif]-->
    <style type="text/css">
        table {
            width: 50%
        }

        #content
        {
            margin-left: 2ex!important;
            height: auto;
        }

        td, th
        {
            width: 50%;
            border: none!important;
            padding: 0.5ex 2ex!important;
        }

        tr.userinfo:hover
        {
            background-color: #E8E8E8;
        }

        tr.userinfo
        {
            border-bottom: 1px solid #c8c8c8;
        }

        #admincontact
        {
            border-top: 1px solid #CCCCCC;
            margin-top: 2ex;
            padding-top: 0.5ex;
        }

    </style>
  </head>
  <body>
    <div id="wrapper">
      <div id="head">
        <h1><a href="http://fedoraproject.org/index.html">Fedora</a></h1>
      </div>
      <div id="content">
        <h2>Fedora People</h2>
        <p><a href="http://fedoraproject.org/wiki/Infrastructure/fedorapeople.org">FAQ</a> covers the details on how to use your public space.</p>
        <table>
          <tr>
            <th>Home Page</th>
            <th>Name</th>
          </tr>
EOM

users=`getent passwd | sort| cut -d: -f1,6 | grep '/home/fedora/'`
for useranddir in $users
   do
    user=`echo $useranddir| cut -d: -f1`
    homedir=`echo $useranddir| cut -d: -f2`
    name="`getent passwd $user | cut -d: -f5`"
    if [ -d $homedir/public_html/ ]; then
     cat <<EOM>> $outfile
 <tr class="userinfo">
    <td><a href="http://${user}.fedorapeople.org">$user</a></td>
    <td>$name</td>
 </tr>
EOM
    fi
   done
   
cat << EOM>> $outfile
        </table>
        <div id="admincontact">
          Contact: <a href="mailto:admin at fedoraproject.org">admin at fedoraproject.org</a><br />
          <ul id="sponsors">
            <li><a href="http://linux.dell.com"><img src="http://torrent.fedoraproject.org/images/poweredby_horizontal_lr.gif" alt="Powered by Dell" width="106" height="35"/></a></li>
            <li><a href="http://www.internetx.com/"><img src="http://fedoraproject.org/static/images/sponsors/internetx.png" width="122" height="47" alt="InterNet X" /></a></li>
          </ul>
        </div>
      </div>
    </div>
    <div id="bottom">
      <div id="footer">
        <p class="copy">
        &copy; 2010 Red Hat, Inc. and others.
        Please send any comments or corrections to the <a href="mailto:webmaster@fedoraproject.org">websites team</a>.
        </p>
        <p class="disclaimer">
        The Fedora Project is maintained and driven by the community and sponsored by Red Hat.  This is a community maintained site.  Red Hat is not responsible for content.
        </p>
        <ul>
          <li class="first"><a href="http://fedoraproject.org/wiki/Legal:Main">Legal</a></li>
          <li><a href="http://fedoraproject.org/wiki/Legal:Trademark_guidelines">Trademark Guidelines</a></li>
        </ul>
      </div>
    </div>
  </body>
</html>
EOM

cp -f $outfile  $finalfile
chgrp web $finalfile
chmod g+w $finalfile

