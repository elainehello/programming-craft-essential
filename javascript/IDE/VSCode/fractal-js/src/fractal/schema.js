import { ITERATIONS, COMPLEX_C } from "../core/paramMacros";

/** Parameter configurations for different fractal types */
export const FractalSchemas = {
  mandelbrot: {
    ...ITERATIONS(),
  },

  julia: {
    ...ITERATIONS,
    ...COMPLEX_C(),
  },

  burningShip: {
    ...ITERATIONS(300),
  },
};
