
def funcionModuloI(dividendo, divisor):
    """
    Compute the integer‑style modulo (remainder) of ``dividendo`` divided by ``divisor``.
    
    This helper mirrors the behaviour of the ``%`` operator but adds explicit
    validation and a richer error message. It works with any objects that
    implement the ``__mod__`` protocol (e.g. ``int``, ``float``, ``Decimal``,
    ``Fraction``) and returns a result of the same type as the operation would
    produce in native Python.

    -----------------------------------------------------------------------
    Description
    -----------------------------------------------------------------------
    The modulo operation finds the remainder after integer division:

        dividendo = divisor * q + r   where 0 <= r < |divisor|

    In Python the sign of the result follows the sign of the divisor, which
    makes the operation *floor* based rather than *truncation* based.  This
    function simply forwards to the built‑in ``%`` operator after checking for
    division‑by‑zero and providing a clearer exception when the operands do not
    support the modulo operation.

    -----------------------------------------------------------------------
    Parameters
    -----------------------------------------------------------------------
    dividendo : int, float, Decimal, Fraction, or any type supporting ``%``
        The numerator (the value to be divided).

    divisor : int, float, Decimal, Fraction, or any type supporting ``%``
        The denominator.  Must not be zero; otherwise a ``ZeroDivisionError`` is
        raised.

    -----------------------------------------------------------------------
    Returns
    -----------------------------------------------------------------------
    result : same type as the native ``%`` operation
        The remainder after dividing ``dividendo`` by ``divisor``.  The result
        satisfies ``0 <= result < abs(divisor)`` when ``divisor`` is non‑zero.

    -----------------------------------------------------------------------
    Raises
    -----------------------------------------------------------------------
    ZeroDivisionError
        If ``divisor`` equals ``0`` (or ``0.0`` etc.).

    TypeError
        If either argument does not implement the ``__mod__`` method required
        for the ``%`` operator.

    -----------------------------------------------------------------------
    Edge Cases & Notes
    -----------------------------------------------------------------------
    * **Negative numbers** – The result always has the sign of the divisor.
      Example: ``funcionModuloI(-7, 4)`` returns ``1`` because ``-7 = 4*(-2) + 1``.
    * **Floating‑point operands** – The function works with ``float`` and other
      numeric types, but be aware of the usual floating‑point rounding errors.
    * **Non‑numeric types** – Objects that overload ``__mod__`` (e.g. custom
      classes, ``numpy.ndarray``) can be used as long as they follow the same
      contract as Python’s built‑in ``%``.
    * **Zero divisor** – Unlike ``%`` which raises ``ZeroDivisionError`` on its
      own, this function checks first to provide a consistent, easy‑to‑understand
      message.

    -----------------------------------------------------------------------
    Examples
    -----------------------------------------------------------------------
    >>> funcionModuloI(10, 3)
    1
    >>> funcionModuloI(10.5, 2)
    0.5
    >>> funcionModuloI(-7, 4)
    1
    >>> funcionModuloI(7, -4)
    -1
    >>> from fractions import Fraction
    >>> funcionModuloI(Fraction(7, 3), Fraction(2, 5))
    Fraction(1, 15)

    -----------------------------------------------------------------------
    See Also
    -----------------------------------------------------------------------
    * Python's ``%`` operator documentation: https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations
    * ``math.fmod`` – provides a C‑style remainder that follows the sign of the
      dividend rather than the divisor.
    """
    # -------------------------------------------------------------------
    # Guard against division by zero
    # -------------------------------------------------------------------
    if divisor == 0:
        raise ZeroDivisionError("divisor cannot be zero")

    # -------------------------------------------------------------------
    # Perform the modulo operation; let Python raise TypeError if unsupported
    # -------------------------------------------------------------------
    try:
        result = dividendo % divisor
    except TypeError as exc:
        raise TypeError(
            "Both arguments must support the '%' operator (e.g., int, float, Decimal, Fraction)."
        ) from exc

    return result


import unittest
from decimal import Decimal
from fractions import Fraction

# Import the function to be tested.
# Assuming it is defined in a module named `modulo_func.py`.
# If the function lives in the same file, you can omit the import.
from modulo_func import funcionModuloI


class TestFuncionModuloI(unittest.TestCase):
    """Test suite for the `funcionModuloI` helper."""

    # -----------------------------------------------------------------
    # Basic functionality tests
    # -----------------------------------------------------------------
    def test_integer_modulo(self):
        self.assertEqual(funcionModuloI(10, 3), 1)
        self.assertEqual(funcionModuloI(0, 5), 0)
        self.assertEqual(funcionModuloI(5, 5), 0)

    def test_negative_dividend(self):
        # Result follows the sign of the divisor
        self.assertEqual(funcionModuloI(-7, 4), 1)   # -7 = 4*(-2) + 1
        self.assertEqual(funcionModuloI(-7, -4), -3)  # -7 = -4*2 + -3

    def test_negative_divisor(self):
        self.assertEqual(funcionModuloI(7, -4), -1)   # 7 = -4*(-2) + -1

    def test_float_modulo(self):
        self.assertAlmostEqual(funcionModuloI(10.5, 2), 0.5)
        self.assertAlmostEqual(funcionModuloI(-5.2, 3.0), 0.8)

    def test_decimal_modulo(self):
        a = Decimal('10.75')
        b = Decimal('0.6')
        self.assertEqual(funcionModuloI(a, b), Decimal('0.55'))

    def test_fraction_modulo(self):
        a = Fraction(7, 3)   # 7/3
        b = Fraction(2, 5)   # 2/5
        self.assertEqual(funcionModuloI(a, b), Fraction(1, 15))

    # -----------------------------------------------------------------
    # Edge‑case tests
    # -----------------------------------------------------------------
    def test_large_numbers(self):
        large = 10 ** 100
        self.assertEqual(funcionModuloI(large + 123, large), 123)

    def test_zero_dividend(self):
        self.assertEqual(funcionModuloI(0, 7), 0)
        self.assertEqual(funcionModuloI(0, -3), 0)

    def test_one_as_divisor(self):
        self.assertEqual(funcionModuloI(12345, 1), 0)
        self.assertEqual(funcionModuloI(-12345, 1), 0)

    # -----------------------------------------------------------------
    # Error handling tests
    # -----------------------------------------------------------------
    def test_zero_divisor_raises(self):
        with self.assertRaises(ZeroDivisionError):
            funcionModuloI(10, 0)

    def test_non_numeric_type_raises(self):
        class NoMod:
            pass

        with self.assertRaises(TypeError):
            funcionModuloI(NoMod(), 3)

        with self.assertRaises(TypeError):
            funcionModuloI(5, NoMod())

    def test_mixed_unsupported_types(self):
        # int % list triggers TypeError
        with self.assertRaises(TypeError):
            funcionModuloI(5, [1, 2, 3])

    # -----------------------------------------------------------------
    # Compatibility with objects that overload __mod__
    # -----------------------------------------------------------------
    def test_custom_mod_operator(self):
        class ModWrapper:
            def __init__(self, value):
                self.value = value

            def __mod__(self, other):
                # simple wrapper that delegates to the underlying int
                return self.value % other

        wrapper = ModWrapper(17)
        self.assertEqual(funcionModuloI(wrapper, 5), 2)

    # -----------------------------------------------------------------
    # Floating‑point rounding edge case
    # -----------------------------------------------------------------
    def test_float_precision_edge(self):
        # 0.1 cannot be represented exactly; modulo should still be close.
        result = funcionModuloI(0.3, 0.1)
        self.assertAlmostEqual(result, 0.0, places=7)


if __name__ == "__main__":
    unittest.main()