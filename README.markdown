bottle-sessions
=

bottle-sessions is a sessions library derived from [gae-session](https://github.com/dound/gae-sessions) for [Bottle python framework](http://bottlepy.org/docs/dev/) for ALL session sizes.  It is extremely fast, lightweight (one file), and easy to use. 



Advantages:
-
 * __Lightweight__: One short file and references to very popular Python libraries.
 * __Fast and Efficient__
     - Uses secure cookies for small sessions to minimize overhead.
     - Uses memcache to minimize read times for larger sessions.
     - Minimizes number of database query() by compactly storing all values in one field.
     - Frequency of writes is minimized by *only writing if there is a change*,
       and *only once per request* (when the response is being sent).
     - Session data is lazily loaded - if you don't use the session for a
       request, zero overhead is added.
 * __Secure__: Protected against session hijacking, session fixation, tampering
   with session data, and XSS attacks.
 * __High Availability__ is ensured by persisting changes to the datastore.
     - If you don't need this, you can use <code>set\_quick()</code> and
       <code>pop\_quick()</code> and data will only be changed in memcache.
 * __Simple to Use__
     - Easily installed as WSGI Middleware.
     - Session values are accessed via a dictionary interface.
     - The session automatically initializes when you first assign a value.
       Until then, no cookies are set and no writes are done.
     - Sessions expire automatically (based on a lifetime you can specify).
     - Thread-safe.


Requirements.txt
-
Python : 2.7.3<br/>
MySQL-python : 1.2.4c1<br/>
SQLAlchemy : 0.7.9<br/>

Limitations:
-
  * Limited to 1MB of data in a session.  (to fit in a single memcache entry)


Installation
-

_*DETAILED SETUP INSTRUCTIONS TO BE ADDED*_


Small sessions are stored in __secure__ cookies.  The required `cookie_key`
parameter is used to sign cookies with an HMAC-SHA256 signature.  This enables
gae-sessions to notice if any change is made to the data by the client (in which
case it is discarded).  The data itself is stored as a base64-encoded, pickled
Python dictionary - *tech savvy users could view the values* (though they cannot
change them).  If this is an issue for your application, then disable the use of
cookies for storing data for small sessions by calling SessionMiddleware with
`cookie_only_threshold=0`.

The default session lifetime is 7 days.  You may configure how long a session
lasts by calling `SessionMiddleware` with a `lifetime` parameter, e.g.,
`lifetime=datetime.timedelta(hours=2))`.

If you want ALL of your changes persisted ONLY to memcache, then create the
middleware with `no_datastore=True`.  This will result in faster writes but your
session data might be lost at any time!  If cookie-only sessions have not been
disabled, then small sessions will still be stored in cookies (this is faster
than memcache).

You will also want to create a cronjob to periodically remove expired sessions
from the datastore. <code>*CRON JOB EXAMPLE TO BE ADDED*</code>


If you *only* want session information (including the session ID) to be sent
from the client when the user accesses the server over SSL (i.e., when accessing
URLs prefixed with "https"), then you will need to manually start the session by
calling [`start(ssl_only=True)`](http://dound.com/myprojects/gae-sessions/docs/html/docindex.html#gaesessions.Session.start).
An existing session cannot be converted to or from an SSL-only session.  Use
this option with care - remember that if this option is used, a user's browser
will *not* send any session cookies when requesting non-https URLs.


Example Usage
-
_*EXAMPLES TO BE ADDED*_

Author
-

_Author_: [gae-session](https://github.com/dound/gae-sessions), [David Underhill](http://www.dound.com) <br/>
_Author_: [Sung-Taek, Kim](http://twitter.com/stkim1)
_Updated_: 2012-Jan-15 (v1.0.0)  
_License_: Apache License Version 2.0