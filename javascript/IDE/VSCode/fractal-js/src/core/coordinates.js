/** Creates coordinate system for mapping pixels to complex plane */
export function createCoordinates({
  center = { x: -0.5, y: 0 },
  scale = 3.0,
} = {}) {
  return {
    center: { ...center },
    scale,

    // Maps a pixel coordinate to the complex plane
    pixelToComplex(px, py, width, height) {
      const aspect = width / height;

      const x = this.center.x + (px / width - 0.5) * this.scale * aspect;

      const y = this.center.y + (py / height - 0.5) * this.scale;

      return { x, y };
    },
  };
}
