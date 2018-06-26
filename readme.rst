web2cli
-------

another test to integrate web2py and vuejs

this is a simple test, all files are in the devel folder which is a vue-cli proyect.

Inside devel just run

 $npm run dev

this will generate a bundle file into /static/js and be linked to /views/layout.html

this app has a single table db with a minimal API inside /services/api/person

Why?
----

When trying to write a small SPA found out that the app name is assumed in the url on development, when moving a production server, the app name is no longer used, so it breaks all urls.

Fix
---

After asking in the users mailing list, solution is to set current application as default app in routes.py inside web2py folder.

Since it is web2py's nature to work with multiple apps at the time this would be an spected behaviour, but still should be a way to choose the default app without editing routes.py, using multiple ports it's not an alternative.
