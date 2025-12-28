import { ITERATIONS } from "../core/paramMacros";

/** Burning Ship fractal implementation */
export const BurningShip = {
  name: "Burning Ship",
  schema: {
    ...ITERATIONS(),
  },

  iterate(x0, y0, maxIterations, params) {
    let x = 0;
    let y = 0;
    let i = 0;

    while (x * x + y * y <= 4 && i < maxIterations) {
      const xt = x * x - y * y + x0;
      y = Math.abs(2 * x * y) + y0;
      x = Math.abs(xt);
      i++;
    }

    return i;
  },
};
