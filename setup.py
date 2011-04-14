from setuptools import setup, find_packages
 
version = '0.1'

LONG_DESCRIPTION = """
How to use django-stockroom
----------------------------

``django-stockroom`` is a lightweight, reusable app for implementing and
managing features of online stores in your Django projects. Stockroom provides
product organization, inventory, and shopping cart functionality that can
tweaked through integration into your project; it is not a turn-key e-commerce
solution.

There are 3 steps to setting it up with your projects.

1. List this application in the ``INSTALLED_APPS`` portion of your settings
   file.  Your settings file might look something like::
   
       INSTALLED_APPS = (
           # ...
           'stockroom',
       )

2. Install the stockroom middleware. Your settings file might look something
   like::
   
       MIDDLEWARE_CLASSES = (
           # ...
           'stockroom.middleware.StockroomMiddleware',
       )

3. Add the url mapping to your project's urls.py::

        url(r'^stockroom/', include('stockroom.urls')),


That's it!
"""

setup(
    name='django-stockroom',
    version=version,
    description="django-stockroom is a lightweight, reusable app for implementing and managing features of online stores in your Django projects.",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='commerce,shopping,cart,django',
    author='policus',
    url='https://github.com/policus/django-stockroom',
    install_requires=[
        'PIL',
        'django-piston',
        ],
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
