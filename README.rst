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

    app = app_factory(config, 'project-name')
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

Now, what if you want to add a few extensions to your project?
In your configuration file (FLASK_CONFIG), set a variable
called **EXTENSIONS** with the full path to your extension.

.. code:: python

    # file: extensions.py
    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy()

    # config/dev.py
    EXTENSIONS = [
        'extensions.db'
    ]  # and that's it!

Your extension will be loaded and initialized for you.

Config
======

You're advised to create a python module to work as your project configuration.
DEV, TEST or PROD specific configurations should be loaded through **FLASK_CONFIG**.

That said, there are a few quite helpful configurations Empty will recognize
by default. See the list below:

- BLUEPRINTS - a list (['blog', 'messages',...]) or dictionary ({'blog': dict(**options), 'messages': dict(**options), ...}) describing which blueprints to load. Blueprints are loaded **by name** from an option **apps/** folder in your project root (preferably) or directly from the project root. 
- EXTENSIONS - a list with the path to your extension instances. Something like this: ['extensions.db'] where 'extensions' is a module and db is an instance of your extension. If you define an "<EXT_INSTANCE_NAME>_init_kwargs" function where your extension instance is, its output will be used as extra arguments to your extension initialization routine.
- BP_MODULES - list of modules  uto loaded from your blueprints. The default value is: ``('admin', 'models', 'schemas', 'views', 'api')``

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
