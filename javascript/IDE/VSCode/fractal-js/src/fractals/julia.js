import { ITERATIONS, COMPLEX_C } from "../core/paramMacros";

/** Julia set fractal implementation */
export const Julia = {
  name: "Julia",
  schema: {
    ...ITERATIONS(),
    ...COMPLEX_C(),
  },

  iterate(x, y, maxIterations, params) {
    let zx = x;
    let zy = y;
    const cx = params.cReal;
    const cy = params.cImag;
    let i = 0;

    while (zx * zx + zy * zy <= 4 && i < maxIterations) {
      const xt = zx * zx - zy * zy + cx;
      zy = 2 * zx * zy + cy;
      zx = xt;
      i++;
    }

    return i;
  },
};
