"""

  Use this for running the VESPA service from Apache.
  This script provides the WSGI entry point for Flask apps.

 ----------------------------------------------------------------------------
  Required steps for mod-wsgi implementation:

   1) Configure apache config (/etc/httpd/conf/httpd.conf) with this section:
      <IfModule wsgi_module>
         ## Tell mod_wsgi where to find "flask" module for import
         WSGIPythonPath /opt/rh/rh-python36/root/usr/lib64/python3.6/site-packages
         ## Tell mod_wsgi which <app>.wsgi file to use
         WSGIScriptAlias /vespa /home/wfanselow/Vespa/vespa_flask.wsgi
         ## Configure directoty-access to <app>.wsgi for apache
         <Directory /home/wfanselow/Vespa>
           Options FollowSymLinks
           AllowOverride None
           Require all granted
         </Directory>
       </IfModule>
 
   2) The standard apache mod_wsgi.so is typcially compiled for python 2.7. This can be
      seen by restarting apache server and tailing /var/log/httpd/error_log and looking for
      this line (notice python version):
       >> [mpm_prefork:notice] [pid 123] ... Apache/2.4.6 ... PHP/5.4.16 mod_wsgi/3.4 Python/2.7.5 configured -- resuming normal operations
      The python version of mod_wsgi.so can also be seen with "ldd /usr/lib64/httpd/modules/mod_wsgi.so".
      So, we installed a version of mod_wsgi which uses python3.6 with these 3 steps.
        a) Install new mod_wsgi with pip3 ( #pip3 install mod-wsgi )
           This creates the file:  
            /opt/rh/rh-python36/root/usr/lib64/python3.6/site-packages/mod_wsgi/server/mod_wsgi-py36.cpython-36m-x86_64-linux-gnu.so
        b) Back up old mod_wsgi.so 
          # mv /usr/lib64/httpd/modules/mod_wsgi.so /usr/lib64/httpd/modules/mod_wsgi.so.python27
        c) Symlink standard mod_wsgi.so path to the new mod_wsgi.so 
          # ln -s /opt/rh/rh-python36/root/usr/lib64/python3.6/site-packages/mod_wsgi/server/mod_wsgi-py36.cpython-36m-x86_64-linux-gnu.so /usr/lib64/httpd/modules/mod_wsgi.so
      Now restart and apache and verify the version info in /var/log/httpd/error_log
       
 ----------------------------------------------------------------------------

"""
import sys
import os

## Set location of the <flask-app>.py directory (does not have to be current dir)
BASE_DIR = '/home/wfanselow/Vespa/app'

## Set some app environment vars
os.environ['FLASK_ENV'] = 'development'
os.environ['BASE_DIR'] = BASE_DIR 

## Put path to jdwe_flask.py on top of python path so it is found.
sys.path.insert(0, BASE_DIR) 

## Import our Flask.app context for the WSGI process. 
## NOTICE!!! mod_wsgi requires that the WSGI application entry point be called 'application'. 
## If you want to call it something else then you would need to configure mod_wsgi explicitly 
## to use the other name.
from app.vespa_flask import app as application
