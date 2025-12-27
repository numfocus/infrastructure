===================
AWS Account Details
===================

Projects are giving sub-organizational accounts to the main NumFOCUS organization account.
For the sub-org account a group email will be made and the project's infrastructure team will be responsible for all emails and warnings to that account.

Account Creation
----------------

Let's run through an example, first we create a email group <project_name>-aws-admin@numfocus.org.

.. image:: google_group_creation.png
   :width: 600

Then we create an aws subaccount aws-<project_name>.

.. image:: AWSSubAccountCreation.png
   :width: 600

That account will be used to create a root level password.

The requester will be provided an admin account in the sub-organizational account.
These account details will be sent via a separate email.

From there it is up to the requester to use AWS console to create what they need.
NumFOCUS will monitor budgets and correspond accordingly.
