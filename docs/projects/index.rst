=====================
Services for projects
=====================

NumFOCUS provides domains, hosting, and benchmarking infrastructure for supported projects.

Request a <subdomain>.pydata.org
--------------------------------

To request a pydata.org subdomain, open a `PyData subdomain request <https://github.com/numfocus/infrastructure/issues/new?template=pydata_subdomain.yaml>`__.

Request a custom domain
-----------------------

To request a custom domain managed by NumFOCUS, open a `custom domain request <https://github.com/numfocus/infrastructure/issues/new?template=custom_domain.yaml>`__.

Request hosting for a static site
---------------------------------

Small static site
~~~~~~~~~~~~~~~~~

Use GitHub Pages for static websites within the `GitHub Pages limits <https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits#usage-limits>`__:

-  1 GB storage
-  100 GB bandwidth per month (soft limit)
-  10 builds per hour (soft limit)

Push the built website to a repository or branch, then configure publishing at ``https://github.com/<your-org>/<your-repo>/settings/pages``

GitHub Pages supports a default ``.github.io`` address or a custom domain.

Your project manages its own site, with no hosting charges to NumFOCUS.

Bigger static site
~~~~~~~~~~~~~~~~~~

For sites that exceed those limits, open a `static hosting request <https://github.com/numfocus/infrastructure/issues/new?template=static_hosting.yaml>`__.

Request performance benchmarks for your project
-----------------------------------------------

CI hardware can vary between runs, making benchmark results difficult to compare.

You can request dedicated hardware to run `asv <https://asv.readthedocs.io/>`__ benchmarks and publish the results.

To request benchmark hosting, open a `benchmark request <https://github.com/numfocus/infrastructure/issues/new?template=benchmarks.yaml>`__.

Other requests
--------------

For other infrastructure needs, open a `project request <https://github.com/numfocus/infrastructure/issues/new?template=project_requests.yaml>`__.

.. toctree::
   :maxdepth: 2
   :caption: Historical requests

   Historical project requests <requests_2020/index>
