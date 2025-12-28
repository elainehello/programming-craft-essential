/** Computes fractal data for each pixel and stores in buffer */
export function computeFractal({
  width,
  height,
  coordinates,
  fractal,
  parameters,
  buffer,
}) {
  const maxIterations = parameters.maxIterations;

  for (let py = 0; py < height; py++) {
    for (let px = 0; px < width; px++) {
      const { x, y } = coordinates.pixelToComplex(px, py, width, height);

      const iterations = fractal.iterate(x, y, maxIterations, parameters);

      // Store iteration count for rendering
      buffer[py * width + px] = iterations;
    }
  }
}
