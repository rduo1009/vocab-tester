#!/usr/bin/env python3

try:
    from icecream import ic  # type: ignore
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa: E731
