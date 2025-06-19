# Sqrt Engine: Digit-by-Digit Square Root Calculator

This is a pure Python implementation of the classic **long division method** for calculating square roots — precise, decimal-based, and educational.

> 🔥 Authored by [Saksham "Ronsum" Dwivedi](https://github.com/RonsumGameDev)
> 🏴 Released under [The Unlicense](https://unlicense.org)

## Features
- No floating point rounding errors
- Compute square roots to *N* digits of precision
- Educational debug logs
- No external dependencies

## Usage

```python
from sqrt_engine import sqroot

# Basic usage
print(sqroot(69))

# With custom decimal places
print(sqroot(2, places=25))

# With debug steps printed
print(sqroot(169, places=15, debug=True))
