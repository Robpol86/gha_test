"""pytest conftest."""
from pathlib import Path

import pytest
from sphinx.testing.path import path
from sphinx.testing.util import SphinxTestApp

pytest_plugins = "sphinx.testing.fixtures"  # pylint: disable=invalid-name


@pytest.fixture(scope="session")
def rootdir() -> path:
    """Used by sphinx.testing, return the directory containing all test docs."""
    return path(__file__).parent.abspath() / "test_docs"


@pytest.fixture(name="sphinx_app")
def _sphinx_app(app: SphinxTestApp) -> SphinxTestApp:
    """Instantiate a new Sphinx app per test function."""
    app.build()
    yield app


@pytest.fixture()
def outdir(sphinx_app: SphinxTestApp) -> Path:
    """Return the Sphinx output directory with HTML files."""
    return Path(sphinx_app.outdir)
