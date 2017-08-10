# Overview
This is a project to automatically generate property website based on flask framework. 

# Run the project
```
cd /path/to/backendnew
virtualenv -p python2.7 venv
source venv/bin/activate
pip install -r requirement.txt
```
To run locally

```
python manage.py runserver
```
To deploy in apache server, you need to install 
mod_wsgi module for apache and then add these lines to 'httpd.conf'(configuration file of apache).

```
WSGIScriptAlias / /path/to/backendnew/my.wsgi
WSGIPythonHome /path/to/backendnew/venv
WSGIPythonPath /path/to/backendnew

<Directory /path/to/backendnew>
    Order deny,allow
    Allow from all
    <Files my.wsgi>
    Order deny,allow
    Allow from all
    </Files>
</Directory>
```

# Usage

Agents can login the website, upload images for their own properties. Before publishing the webiste,
They need to buy a domain for a property and then point the domain to 208.64.255.119. After publishing the webiste, anyone can visit the domain bought by the agent to watch the property website.