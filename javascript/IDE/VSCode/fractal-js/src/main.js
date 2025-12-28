import { fractals } from "./fractals/index.js";
import { createRenderer } from "./core/renderer.js";
import { createCoordinates } from "./core/coordinates.js";
import { computeFractal } from "./core/engine.js";
import { bindNumberInput } from "./utils/dom.js";
import "./style.css";

const canvas = document.createElement("canvas");
document.body.appendChild(canvas);

const renderer = createRenderer(canvas);
renderer.resize();

// Get controls from HTML
const realInput = document.querySelector("#real");
const imagInput = document.querySelector("#imag");

// Move these outside the function
const coordinates = createCoordinates();
let buffer = new Array(canvas.width * canvas.height);

function renderJulia() {
  // Resize buffer if canvas size changed
  if (buffer.length !== canvas.width * canvas.height) {
    buffer = new Array(canvas.width * canvas.height);
  }

  const parameters = {
    maxIterations: 200,
    cReal: Number(realInput.value),
    cImag: Number(imagInput.value),
  };

  computeFractal({
    width: canvas.width,
    height: canvas.height,
    coordinates,
    fractal: fractals.julia,
    parameters,
    buffer,
  });
  renderer.render(buffer, parameters.maxIterations);
}

// Bind controls
bindNumberInput(realInput, renderJulia);
bindNumberInput(imagInput, renderJulia);

// Initial render
renderJulia();
