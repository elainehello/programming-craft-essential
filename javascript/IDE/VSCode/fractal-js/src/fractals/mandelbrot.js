import { ITERATIONS } from "../core/paramMacros.js";

/** Mandelbrot fractal implementation */
export const Mandelbrot = {
  name: "Mandelbrot",
  schema: {
    ...ITERATIONS(),
  },

  iterate(x0, y0, maxIterations, params) {
    let x = 0;
    let y = 0;
    let i = 0;

    while (x * x + y * y <= 4 && i < maxIterations) {
      const xt = x * x - y * y + x0;
      y = 2 * x * y + y0;
      x = xt;
      i++;
    }

    return i;
  },
};
