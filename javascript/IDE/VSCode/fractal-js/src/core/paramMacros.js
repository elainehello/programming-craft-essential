/** Creates a numeric parameter with min/max bounds */
export const NUMBER = ({ min, max, defaultValue }) => ({
  type: "number",
  min,
  max,
  default: defaultValue,
});

/** Controls fractal calculation depth (10-5000 iterations) */
export const ITERATIONS = (defaultValue = 200) =>
  NUMBER({
    min: 10,
    max: 5000,
    defaultValue,
  });

/** Real number parameter for fractal coordinates (-2 to 2) */
export const REAL = (defaultValue = 0) =>
  NUMBER({
    min: -2,
    max: 2,
    defaultValue,
  });

/** Complex constant C for Julia sets (real + imaginary parts) */
export const COMPLEX_C = ({ real = -0.7, imag = 0.27015 } = {}) => ({
  cReal: REAL(real),
  cImag: REAL(imag),
});
