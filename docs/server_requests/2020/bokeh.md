# Bokeh Server Request

## Project Details

Name: Bokeh
Website: https://bokeh.org/


## Request April 2020

### Requester

- Bryan Van de Ven <bryan@bokeh.org>

### Request Details

1. Please provide a brief description of your project's specific needs for AWS credits:

We use: S3, Cloudfront, Elastic Beanstalk, Simple Email Service, and EC2. These all support the various properties under the bokeh.org domain, but the most critical is S3/Clooudfront for the BokehJS CDN. Without this, most Bokeh plots everywhere stop working.

1. Please provide us with an estimated cost for meeting those needs (in U.S. Dollars):

It had been in the ~1300 USD/yr range however JHU has included Bokeh content at https://coronavirus.jhu.edu/data/animated-world-map which has more than doubled our daily Cloudfront spend. Not sure how long it will continue, but at this rate it would be closer to 3000 USD/yr

1. Are any of these needs particularly urgent or important? If so, please explain.

As mentioned, coronavirus.jhu.edu has added some Bokeh plots which as more than doubled our CDN requests in the the last week.

7. Additional Comments:

No response
