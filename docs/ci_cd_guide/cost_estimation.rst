*****
Cost Estimation and Prediction
*****

One of the biggest concerns when transitioning from free to paid CI/CD is understanding and predicting costs. This section will help you estimate what you might spend and how to optimize.

Understanding CI Costs
======================

Most CI services charge based on:

- **Compute time:** The number of CPU minutes (or hours) your builds consume
- **Parallelization:** Running multiple jobs simultaneously multiplies costs
- **Hardware tier:** Premium hardware (GPUs, more memory) costs more
- **Build frequency:** How often builds run (per commit, per PR, scheduled, etc.)
- **Data transfer:** Some services charge for artifact storage or transfer

Basic Cost Calculation
=====================

Here's a simple formula to estimate your monthly CI costs:

.. code-block:: text

    Monthly Cost = (CPUs × Cost per CPU-minute) × Total Build Minutes per Month

Example Calculation
^^^^^^^^^^^^^^^^^^^

Let's say you have a Python project with these characteristics:

- **Build frequency:** Every commit and pull request
- **Average commits:** 20 per day
- **Average PRs:** 5 per day (each PR runs tests multiple times = 2 test runs per PR on average)
- **Test duration:** 10 minutes
- **Matrix:** Test on Python 3.9, 3.10, 3.11, 3.12 (4 parallel jobs)

Monthly calculation:

.. code-block:: text

    Daily builds: (20 commits + 5 PR runs × 2) × 4 matrix jobs = 120 builds/day
    Monthly builds: 120 × 30 = 3,600 builds
    Total CPU-minutes: 3,600 × 10 = 36,000 CPU-minutes
    
    If charged $0.008 per CPU-minute:
    Monthly cost = 36,000 × $0.008 = $288/month

Factors That Drive Costs Up
=============================

**Testing Frequency**
   Every commit is more expensive than just pull requests:
   
   - Nightly runs: Usually cheapest
   - Pull request runs: Medium cost
   - Every commit: Most expensive (multiple commits per day)
   - Multiple runs per PR: Very expensive

**Matrix Builds**
   Testing on multiple Python versions, OS platforms, or architectures multiplies costs:
   
   - Testing on 2 Python versions: 2× cost
   - Testing on 3 OS (Linux, macOS, Windows): 3× cost
   - Both = 6× cost!

**Build Duration**
   Longer tests cost more:
   
   - 5-minute tests: Relatively cheap
   - 30-minute tests: Significant cost
   - 2-hour tests: Very expensive; consider running only nightly

**Hardware Requirements**
   Specialized hardware costs more:
   
   - Standard CPUs: Baseline cost
   - GPUs: 3-10× more expensive
   - Exotic architectures: Highly variable

**Parallelization**
   Running jobs in parallel costs more immediately (but saves real time):
   
   - 1 job at a time: Minimum cost
   - 4 parallel jobs: ~4× cost

Cost Optimization Strategies
============================

**Reduce Testing Frequency**

   Instead of testing every commit:
   
   - Test pull requests only (saves commits between PRs)
   - Use a matrix filter to skip redundant jobs
   - Run expensive tests only on certain events

**Optimize Your Test Matrix**

   Don't test every combination if you don't need to:
   
   - Test only supported Python versions
   - Test on main OSes during development, full matrix on release
   - Skip optional dependencies tests in routine CI
   - Example strategy:
      - Per-commit/PR: Linux with main Python version
      - Nightly: Full matrix across platforms/versions

**Cache Dependencies**

   Caching saves both time and CI minutes:
   
   - Cache pip/conda packages
   - Cache compiled artifacts
   - Cache Docker images
   - Example: If tests normally take 30 minutes but 20 minutes is dependency installation, caching can cut cost in half

**Use Cheaper Hardware**

   Only use expensive hardware when needed:
   
   - Standard CPU for unit tests
   - GPU only for tests that actually need it
   - Consider conditional job runs

**Batch Work into Nightly Runs**

   For expensive operations:
   
   - Move long tests to nightly runs
   - Run on fewer platforms nightly
   - Reserve peak testing for focused areas

**Parallelize Intelligently**

   Don't parallelize everything:
   
   - Some tests can't run in parallel (database tests)
   - Parallel builds take more resources but less real time
   - Find the sweet spot: parallel enough for speed, but not excessive

**Profile Your Builds**

   Understand where time is spent:
   
   - Which tests are slowest?
   - What can be optimized or parallelized?
   - Can slow tests be run less frequently?

Vendor-Specific Tips
====================

**GitHub Actions**
   - Use ``matrix`` strategically; each combination multiplies cost
   - Use conditional job execution to skip unnecessary jobs
   - Set jobs to cancel on new commit to avoid wasted build time
   - Self-hosted runners for heavy workloads can reduce costs

**CirrusCI**
   - Free tier has generous credits for open source
   - Only pay for usage above credits
   - Custom pools can reduce per-job costs at scale

**UbiCloud**
   - Negotiate volume pricing through NumFOCUS
   - Similar to GitHub Actions but better pricing for high-volume users

Estimating Your Costs
====================

To estimate your costs accurately:

1. **Monitor your current usage** (free tier if available)
2. **Count your daily builds** (commits × matrix jobs)
3. **Measure your average build time**
4. **Get the vendor's pricing:**
   
   - Per-minute rates? Per-VM-hour? Per-month fixed?
   - Are there different rates for different hardware?
   - Do they offer free tiers or open source discounts?

5. **Calculate:** (Builds/month) × (Matrix size) × (Build duration) × (Price/unit)
6. **Add buffer:** Add 20-30% for overhead and spikes

Example Vendor Pricing (as of 2025)
===================================

.. note::
   
   Pricing changes frequently. Always check current vendor pricing.

**GitHub Actions**
   - Free: 2,000 minutes/month per account
   - Paid: ~$0.24 per 1,000 CPU-minutes (Linux)
   - GPUs: $0.90+ per minute

**CirrusCI**
   - Free tier: $100 credit/month for open source
   - Paid: $0.045 per CPU-minute (approximately)
   - Open source discounts available

**UbiCloud**
   - ~$0.04-0.07 per CPU-minute (negotiable)
   - Better rates for committed volume

Requesting Funding from NumFOCUS
================================

If you've estimated your costs and need help funding CI/CD:

1. Prepare a summary:
   
   - Current testing strategy
   - Hardware requirements
   - Estimated monthly cost
   - Why paid CI is needed
   - Which vendor(s) you've chosen

2. Contact the Infrastructure Committee
3. Submit a request through the NumFOCUS process
4. The committee can help with:
   
   - Negotiating with vendors
   - Setting up billing through NumFOCUS
   - Optimizing your CI to reduce costs

