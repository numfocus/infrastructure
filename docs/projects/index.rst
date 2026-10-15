=====================
Services for Projects
=====================

This document contains information on the infrastructure services NumFOCUS offers to its supported projects.

Request a <subdomain>.pydata.org
--------------------------------

If your project wants to use a pydata.org subdomain, please create a `pydata.org subdomain issue <https://github.com/numfocus/infrastructure/issues/new?template=pydata_subdomain.yaml>`__

Request a custom domain
-----------------------

If your project wants a custom domain managed by NumFOCUS, please create a `custom domain issue <https://github.com/numfocus/infrastructure/issues/new?template=custom_domain.yaml>`__

Request hosting for a static site
---------------------------------

Small static site
~~~~~~~~~~~~~~~~~

GitHub Pages is the recommended way to host static websites which don't exceed `GitHub Pages quotas <https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits#usage-limits>`__:

-  1 GB storage
-  100 GB bandwidth per month (soft limit)
-  10 builds per hour (soft limit)

To set up GitHub Pages you can push the built website to a new repository or a branch of your existing repository, and configure it to be served at ``https://github.com/<your-org>/<your-repo>/settings/pages``

It supports a default ``.github.io`` subdomain, or a custom domain.

Using GitHub Pages you have total control of your website, and there is no cost to NumFOCUS in money or time.

Bigger static site
~~~~~~~~~~~~~~~~~~

If you need static hosting that exceeds GitHub Pages quotas, please create a `static hosting issue <https://github.com/numfocus/infrastructure/issues/new?template=static_hosting.yaml>`__

Request performance benchmarks for your project
-----------------------------------------------

Running benchmarks and keeping a history for your project can be tricky, since CI hardware can be different at every run, and comparisons among versions wouldn't be meaningful.

You can request dedicated hardware to run `asv <https://asv.readthedocs.io/>`__ benchmarks and publish the results.

If your project wants its benchmarks to be published, please create a `benchmarks issue <https://github.com/numfocus/infrastructure/issues/new?template=benchmarks.yaml>`__

Other requests
--------------

For infrastructure needs not covered above, please open a `project request issue <https://github.com/numfocus/infrastructure/issues/new?template=project_requests.yaml>`__.

.. toctree::
   :maxdepth: 2
   :caption: Project Requests:

   Historical project requests <requests_2020/index>
