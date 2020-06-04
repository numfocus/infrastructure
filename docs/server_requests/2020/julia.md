# Julia Server Request

## Project Details

Name: Julia
Website: julialang.org


## Request April 2020

### Requester

- Keno Fischer <keno@juliacomputing.com>
- Viral Shah <viral@juliacomputing.com>

### Request Details

- 6x m5d.2xlarge Windows (3x win32, 3x win64 CI) - $33,480.72
- 9x m5d.2xlarge Non-Windows (3x each linux32, linux64, freebsd64 CI) - $21,207.96
- 3x c6g.4xlarge (linuxaarch64 CI) - ~$10k probably (AWS hasn't released pricing yet)
- 2x m5d.4xlarge (PkgEval and BinaryBuilder) - $8,024.16
- Data Transfer (projected - currently between $1k-$2k a month, but note that everything high-volume is cached on our global CDN): $3k/month - $36k total
- Data Storage (projected - currently fairly low, but we're about to start storing crash dumps and we're abusing GitHub releases for binary artifact storage) - $500/month - $6 total
Which roughly adds up to $100k. There's obviously slack in the Data Transfer/Storage allocations. We've managed to keep that fairly low, since we've been building out a global CDN infrastructure, which has kept cost growth down there for the past few months. However, I think we're pretty much at the end of what we can do there, so I expect it to start growing again.
Our allocation for this year was $50k, but we'll run out before it's up - which is why I was talking to Amazon about getting us some extra credits for this year and renewing for next year.
