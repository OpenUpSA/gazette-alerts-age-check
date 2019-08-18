Gazette Alerts Age Check
========================

Automated check to inform us when gazette search alerts aren't going out to users.

This is a [serverless framework](https://serverless.com/) project that sets up
an HTTP endpoint which should be monitored by a standard website uptime check,
e.g. [UptimeDoctor](http://www.uptimedoctor.com/).

Each time the endpoint is called, it checks whether alert emails have been
received in an email inbox within a specified amount of time.

A 500 error response is given if no alert emails were received in the specified
time.

A 200 error response is given otherwise.

Installation
------------

Deploy the lambda function and set up an endpoint triggering it:

```
serverless deploy
```

Set up an HTTP uptime check once per hour to email you upon an error.

AWS Lambda Cost estimate
------------------------

    0.128 *      24 * 30    * 0.5       = 46 GB seconds per month
      GB     hours / month    seconds
