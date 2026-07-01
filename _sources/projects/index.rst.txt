=====================
Services for Projects
=====================

This document contains information on the infrastructure services NumFOCUS offers to its supported projects.

Request a <subdomain>.pydata.org
--------------------------------

If your project wants to use a pydata.org subdomain, please create a `pydata.org subdomain issue <https://github.com/numfocus/infrastructure/issues/new?labels=Pydata%2CSubdomain&template=pydata_subdomain.yaml>`__

Request a custom domain
-----------------------

If your project wants to use a pydata.org subdomain, please create a `custom domain issue <https://github.com/numfocus/infrastructure/issues/new?labels=Custom%2CDomain&template=custom_domain.yaml>`__

Request hosting for a static site
---------------------------------

Small static site
~~~~~~~~~~~~~~~~~

GitHub pages is the recommended way to host static websites which don't exceed `GitHub pages quotas <https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages#usage-limits>`__:

-  1 GB storage
-  100 GB bandwidth (soft limit)
-  10 builds per hour (soft limit)

To set up GitHub pages you can push the built website to a new repository or a branch of your existing repository, and configure it to be served at ``https://github.com/<your-org>/<your-repo>/settings/pages``

It supports a default ``.github.io`` subdomain, or a custom domain.

Using GitHub pages you have total control of your website, and there is no cost to NumFOCUS in money or time.

Bigger static site
~~~~~~~~~~~~~~~~~~

If you need static hosting which exceed GitHub pages quotas, please create a `static hosting issue <https://github.com/numfocus/infrastructure/issues/new?labels=Static%2CHosting&template=template=static_hosting.yaml>`__

Request performance benchmarks for your project
-----------------------------------------------

Running benchmarks and keeping a history for your project can be tricky, since CI hardware can be different at every run, and comparisons among versions wouldn't be meaningful.

For this reason, NumFOCUS provides the service of running `asv <https://asv.readthedocs.io/>`__ benchmarks in dedicated hardware, and publish the results at https://pandas.pydata.org/speed/

If your project wants its benchmarks being published, please create a `benchmarks issue <https://github.com/numfocus/infrastructure/issues/new?labels=Benchmarks&template=template=benchmarks.yaml>`__

Other requests
--------------

TBC/TBD

.. toctree::
   :maxdepth: 2
   :caption: Project Requests:

   requests_2020/index
