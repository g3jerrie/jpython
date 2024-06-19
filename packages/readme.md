# Package

Physically, a package is a folder/directory comprising of related files and methods.
From business point of view, a package consists of related business functions and modules specific to an aspect of business

For example:

All activities related to business functions including data operations/business rules/working with the entities should be entitled to the package called model.

Any activities related to user interactions -> should be in the package called view.

All activities related to coordinating/controlling the entire program should be in the package called controller.

This defines a popular architecture called MVC framework.

A package can have sub-packages/files etc.

Each package/sub-package should have a file named __init__.py

How does Python locate packages: by an Environment variable called PYTHONPATH
