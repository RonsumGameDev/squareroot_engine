# Sqrt Engine: Digit-by-Digit Square Root Calculator

This is a pure Python implementation of the classic **long division method** for calculating square roots — precise, decimal-based, and educational.

> 🔥 Authored by [Saksham "Ronsum" Dwivedi](https://github.com/RonsumGameDev)

## Features
- No floating point rounding errors
- Compute square roots to *N* digits of precision
- Educational debug logs
- No external dependencies

## Usage

```python
from sqrt_engine import sqroot

print(sqroot(69, places=20, debug=True))
