# Bokeh Server Request

## Project Details

Name: Bokeh
Website: https://bokeh.org/


## Request October 2021

### Requester

- Bryan Van de Ven <bryan@bokeh.org>

### Request Details

1. Please provide a brief description of your project's specific needs for AWS credits:

We use: S3, Cloudfront, Elastic Beanstalk, Simple Email Service, Elastic Container Registry, and EC2. These all support the various properties under the bokeh.org domain, but the most critical is S3/Cloudfront for the BokehJS CDN. Without this, most Bokeh plots everywhere stop working.

1. Please provide us with an estimated cost for meeting those needs (in U.S. Dollars):

It has been in the ~1800 USD/yr including the stabilizd traffic from JHU  Bokeh content at https://coronavirus.jhu.edu/data/animated-world-map However we would like headroom to absorb any unexpected spikes in CDN usage, and to move on some new initiatives, and request 3000 USD/yr.

1. Are any of these needs particularly urgent or important? If so, please explain.

We would like to invest time to implement more automation/chat-ops around our CI and releases to reduce the time burden on maintainers for these tasks. 

7. Additional Comments:

No response
