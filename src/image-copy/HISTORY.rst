.. :changelog:

Release History
===============

0.2.12
++++++
* Fix the issue that the "--target-subscription" input by user is ignored.

0.2.11
++++++
* Fix the issue that command ended with an error when copying image to multiple locations.

0.2.10
++++++
* Fix the issue that the hyper_v_generation used for copying image is None when showing resource.

0.2.9
++++++
* Fix the issue that the hyper_v_generation is always V1 when copying the image.

0.2.8
++++++
* Remove unused --subscription parameter

0.2.7
++++++
* Fix copying failure when location of source resource group and source image are different.

0.2.6
++++++
* Add validation on temporary resource group.

0.2.5
++++++
* Fix a bug of --tags.

0.2.4
++++++
* Fix copying an image originally created from a blob (create a snapshot with the source storage account id)

