What have we here?
==================

Empty is a soft wrapper around the amazing Flask web framework; it
adds new pre-defined configuration which makes it easier to create
robuts projects.

What comes packed?
==================

- Looks up blueprints in a apps/ folder inside your project root. You may now have your blueprints better organized.
- Loads extensions automagically.
- Loads blueprint modules automagically.
- Gives you *configure_* methods loaded in the right order, that you may simply override.
- Has a few pre-built filters (**date** and **datetime**, for now)

Usage
=====

Creating your firs Empty application is quite simple. Just do the following:

.. code:: python

    from empty import app_factory
    import config  # your config module

    # config can also be None; no problem
    app = app_factory('project-name', config)
    app.run()

    # or
    from empty import Empty
    import config  # your config module

    app = Empty('project-name')
    app.configure(config)
    app.run()

All nice and cuzzy. Now, imagine you would like to load custom
configuration rules in your application. To do that,
just define a environment variable called **FLASK_CONFIG**
pointing to the configuration file, which can be a python file.

.. code:: python

    FLASK_CONFIG=config/dev.py
    # or
    FLASK_CONFIG=config/testing.py

Blueprints
==========

For Empty to load your blueprints for you, make sure
the blueprint instance can be imported directly from
the blueprint package or module. A good suggestion
could be to declare your blueprint instance like this:

    apps/myblueprint
    .. __init__.py (import blueprint instance here)
    .. bp.py (declare blueprint instance here)

Then, in your config module/object/whatever, declare
you wish to load your blueprint, like this:

.. code:: python

    # loading it this way, url_prefix will be /myblueprint
    BLUEPRINTS = ['myblueprint']
    # like this, you can provide custom configuration
    BLUEPRINTS = [
        ('myblueprint', {
            # .. blueprint configuration goes here ..
        })
    ]

Extensions
==========

Flask extensions are a great way to shorten your work.
To load extensions with Empty, create a module,
declare your extensions there and load them through
your configuration.

.. code:: python

    # file: extensions.py
    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy()

    # config.py
    EXTENSIONS = [
        'extensions.db'
    ]  # and that's it!

The code above loads and initializes the extensions for you.
Some extensions, like flask-security, may require extra
arguments (besides app) to load properly. For these cases,
declare a function besides your extension instance in the
following manner:

.. code:: python

    def <extension_instance_name>_init_kwargs():
        return ext_kwargs

**ext_kwargs** should be a dict with the necessary extra
**init_app** parameters.


Click support
=============

- (planned) command to make it easy to create a new blueprint
- (planned) command to list your routes

Integrations
------------

Empty integrates quite with with many projects, but there are few that
are just too good! Adding them to empty would probably go against the
whole idea of something that doesn't get in your way. So, what we'll do
is to describe a few easy-to-follow recipes with empty on how to
create the most common setups. These recipes are **WIP**, of now.

Recipes
=======

**WIP**
