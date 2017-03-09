import pytest
import textwrap
import os
import sys


@pytest.fixture
def test_apps(monkeypatch):
    monkeypatch.syspath_prepend(
        os.path.abspath(os.path.join(
            os.path.dirname(__file__), 'test_apps'))
    )


@pytest.fixture
def test_configs(monkeypatch):
    monkeypatch.syspath_prepend(
        os.path.abspath(os.path.join(
            os.path.dirname(__file__), 'test_configs'))
    )


@pytest.fixture
def modules_tmpdir(tmpdir, monkeypatch):
    """A tmpdir added to sys.path."""
    rv = tmpdir.mkdir('modules_tmpdir')
    monkeypatch.syspath_prepend(str(rv))
    return rv


@pytest.fixture
def modules_tmpdir_prefix(modules_tmpdir, monkeypatch):
    monkeypatch.setattr(sys, 'prefix', str(modules_tmpdir))
    return modules_tmpdir


@pytest.fixture
def purge_module(request):
    def inner(name):
        request.addfinalizer(lambda: sys.modules.pop(name, None))
    return inner


@pytest.fixture
def install_egg(modules_tmpdir, monkeypatch):
    """Generate egg from package name inside base and put the egg into
    sys.path"""
    def inner(name, base=modules_tmpdir):
        if not isinstance(name, str):
            raise ValueError(name)
        base.join(name).ensure_dir()
        base.join(name).join('__init__.py').ensure()

        egg_setup = base.join('setup.py')
        egg_setup.write(textwrap.dedent("""
        from setuptools import setup
        setup(name='{0}',
              version='1.0',
              packages=['site_egg'],
              zip_safe=True)
        """.format(name)))

        import subprocess
        subprocess.check_call(
            [sys.executable, 'setup.py', 'bdist_egg'],
            cwd=str(modules_tmpdir)
        )
        egg_path, = modules_tmpdir.join('dist/').listdir()
        monkeypatch.syspath_prepend(str(egg_path))
        return egg_path
    return inner
