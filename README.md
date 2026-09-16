# Recommendation API

A movie recommendation engine written in Python, built from first principles.

## Status

**Phase 1 — core catalogue logic**

| Feature | Status |
|---|---|
| Filter by release year | done |
| Filter by minimum rating | next |
| Filter by genre | planned |

## Usage

```python
from core import filter_by_year
from data.movies import MOVIES

filter_by_year(MOVIES, 2017)