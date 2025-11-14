thonpython
class FilterEngine:
    """Apply filters to review datasets."""

    def apply_filters(self, reviews, rating_min=None, language=None):
        filtered = reviews

        if rating_min is not None:
            filtered = [r for r in filtered if r.get("rating", 0) >= rating_min]

        if language is not None:
            filtered = [r for r in filtered if r.get("language") == language]

        return filtered