"""."""
from .api import API


class CatApi(API):
    """CatApi class."""

    def __init__(self, *args, **kwargs):
        """Cat object init."""
        super().__init__(*args, **kwargs)

    def search(self, search_term):
        """."""
        pass
