***********************
Performance Benchmarking
***********************

For performance-critical projects like NumPy, SciPy, and other scientific packages, performance benchmarking is essential. This section covers benchmarking fundamentals and how to set it up in CI/CD.

Why Benchmark in CI?
====================

Performance regressions can sneak in silently:

- A seemingly innocent refactor slows things down
- A dependency change impacts speed
- Compiler optimizations are lost in a rewrite
- Memory usage grows unexpectedly

Running benchmarks in CI helps catch these issues before they reach users. For scientific Python projects, performance is often as important as correctness.

Benchmarking Fundamentals
=========================

**What to Measure**

   - Execution time (runtime)
   - Memory usage
   - Memory allocation patterns
   - CPU cache efficiency (for advanced use cases)

**When to Measure**

   - Every commit (if fast)
   - Every PR (common for expensive benchmarks)
   - Nightly (for comprehensive or very expensive benchmarks)
   - On releases (for historical tracking)

**How to Handle Variance**

   Benchmarks are inherently variable:
   
   - Run multiple iterations and report mean, stddev
   - Account for system noise
   - Use statistical methods to determine if regression is real
   - Set reasonable thresholds for alerts (e.g., >5% regression)

**Hardware Consistency**

   Benchmark results are hardware-dependent:
   
   - Run on consistent hardware (same CPU, memory, storage)
   - Document the hardware used
   - Don't compare benchmarks from different hardware
   - Avoid dynamic environments when possible (use bare metal for precise benchmarks)

Benchmarking Frameworks
======================

**airspeed velocity (asv)**
   A long-standing Python benchmarking tool
   
   - **Best for:** Long-term performance tracking
   - **Pros:**
      - Tracks performance history over time
      - Web interface for visualization
      - Can track multiple Python versions and configurations
      - Good documentation and examples
   - **Cons:**
      - Older codebase
      - Can be complex to set up initially
   - **Usage:** Great for projects with long performance histories (NumPy, SciPy)

**codspeed.io**
   Modern CI-native benchmarking
   
   - **Best for:** Modern Python projects wanting easy CI integration
   - **Pros:**
      - Free for open source (commercial otherwise)
      - Easy GitHub/GitLab integration
      - Beautiful dashboards
      - Works with pytest
   - **Cons:**
      - Proprietary (not open source)
      - Focused on execution time, not memory
   - **Usage:** Easy setup for projects just starting benchmarking

**pytest-benchmark**
   Lightweight benchmarking within pytest
   
   - **Best for:** Projects already using pytest
   - **Pros:**
      - Minimal setup
      - Integrates with pytest
      - Good statistical handling
      - JSON output for analysis
   - **Cons:**
      - Less suitable for long-term tracking
      - Minimal visualization
   - **Usage:** Good starting point before more complex systems

**Memory Profilers**
   For memory-focused projects
   
   - **memory_profiler:** Line-by-line memory tracking
   - **tracemalloc:** Python's built-in memory tracking
   - **Scalene:** Modern Python profiler
   - **Best for:** Memory-intensive code
   - **Usage:** Often run on a subset of code or nightly

Machine Requirements for Benchmarking
=====================================

**Why Machine Consistency Matters**

   Benchmark results vary with:
   
   - CPU model and frequency
   - Memory speed and configuration
   - Disk speed (can affect I/O tests)
   - Background processes
   - System load
   - Power settings (CPU scaling, turbo boost)

**Options for Consistent Hardware**

   **Shared CI Service (e.g., GitHub Actions)**
   
   - Pros: Simple, no maintenance
   - Cons: Variable hardware, can't control OS scheduling
   - Use for: Trend tracking over time (noise averages out)

   **Dedicated Bare Metal**
   
   - Pros: Consistent results, controlled environment
   - Cons: Expensive, requires maintenance
   - Use for: High-precision benchmarking, regression detection

   **Custom Hardware Pool**
   
   - Pros: Better control than shared CI, less expensive than full bare metal
   - Cons: Still requires management
   - Use for: Projects with significant benchmarking needs

**Setting Up Consistent CI**

   If using shared CI (GitHub Actions, CirrusCI):
   
   - Document the runner type you're using
   - Run benchmarks multiple times and use statistical analysis
   - Track trends over time; absolute numbers are less reliable
   - For regression detection, focus on relative change

   If using dedicated hardware:
   
   - Disable CPU frequency scaling
   - Minimize background processes
   - Pin benchmarks to specific CPUs if possible
   - Monitor for system updates affecting results
   - Keep benchmarks short to minimize thermal variance

Setting Up Benchmarks in CI
============================

**Basic asv Setup**

   .. code-block:: yaml

       # .github/workflows/benchmark.yml
       name: Benchmark
       on: [pull_request]
       jobs:
         benchmark:
           runs-on: ubuntu-latest
           steps:
             - uses: actions/checkout@v3
             - name: Set up Python
               uses: actions/setup-python@v4
               with:
                 python-version: '3.11'
             - name: Install dependencies
               run: |
                 pip install asv
             - name: Run benchmarks
               run: asv run

**Basic codspeed Setup**

   .. code-block:: yaml

       # .github/workflows/benchmark.yml
       name: Benchmark
       on: [pull_request]
       jobs:
         benchmark:
           runs-on: ubuntu-latest
           steps:
             - uses: actions/checkout@v3
             - name: Set up Python
               uses: actions/setup-python@v4
               with:
                 python-version: '3.11'
             - uses: CodSpeedHQ/action@v1
               with:
                 token: ${{ secrets.CODSPEED_TOKEN }}

**pytest-benchmark in CI**

   .. code-block:: yaml

       # .github/workflows/benchmark.yml
       name: Benchmark
       on: [pull_request]
       jobs:
         benchmark:
           runs-on: ubuntu-latest
           steps:
             - uses: actions/checkout@v3
             - name: Set up Python
               uses: actions/setup-python@v4
               with:
                 python-version: '3.11'
             - name: Install dependencies
               run: pip install pytest pytest-benchmark
             - name: Run benchmarks
               run: pytest --benchmark-only

Interpreting Benchmark Results
==============================

**What's a Real Regression?**

   A small variation might be noise:
   
   - < 2%: Noise, ignore
   - 2-5%: Likely real but small; consider if worth addressing
   - 5-10%: Real regression, should investigate
   - > 10%: Significant regression, must investigate

**Statistical Approaches**

   Don't rely on single runs:
   
   - Run benchmarks multiple times (5-10 runs minimum)
   - Report mean and standard deviation
   - Use statistical tests (t-test) for comparison
   - Track confidence intervals

**Comparing Branches**

   When comparing PR vs. main:
   
   - Ideally run on same hardware
   - Run multiple times if using shared CI
   - Account for system variance
   - Focus on consistent patterns, not single outliers

Best Practices for Benchmarking
==============================

1. **Start simple:** Use pytest-benchmark to begin
2. **Measure what matters:** Focus on user-visible performance
3. **Hardware matters:** Document your hardware or account for variance
4. **Run regularly:** Nightly or per-PR depending on cost
5. **Track history:** Store results for long-term trending
6. **Set thresholds:** Define what's a regression vs. noise
7. **Investigate regressions:** Don't just alert, actually fix issues
8. **Share results:** Make benchmarks visible to developers
9. **Optimize selectively:** Run full benchmarks nightly, quick tests per-PR
10. **Include memory:** If memory usage matters, benchmark it too

Benchmark CI Cost Considerations
=================================

Benchmarking adds CI cost because:

- Benchmarks run code many times (multi-second builds become multi-minute)
- Need to account for variance (multiple runs)
- May need specialized hardware
- Results must be stored and tracked

To minimize cost:

- Run quick benchmarks per-PR
- Run comprehensive benchmarks nightly
- Use conditional jobs to skip benchmarks for non-performance changes
- Cache dependencies aggressively
- Consider running only on main branch for cost control

Resources
=========

- `airspeed velocity documentation <https://asv.readthedocs.io/>`_
- `codspeed.io <https://codspeed.io/>`_
- `pytest-benchmark <https://pytest-benchmark.readthedocs.io/>`_
- `Python performance tips <https://wiki.python.org/moin/PythonSpeed/PerformanceTips>`_

