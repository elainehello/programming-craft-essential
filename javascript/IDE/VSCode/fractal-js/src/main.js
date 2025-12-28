import { fractals } from "./fractals/index.js";
import { createRenderer } from "./core/renderer.js";
import { createCoordinates } from "./core/coordinates.js";
import { computeFractal } from "./core/engine.js";
import { bindNumberInput } from "./utils/dom.js";
import { createInputHandler } from "./utils/inputs.js";
import "./style.css";

const canvas = document.createElement("canvas");
document.body.appendChild(canvas);

const renderer = createRenderer(canvas);
renderer.resize();

// Get controls from HTML
const realInput = document.querySelector("#real");
const imagInput = document.querySelector("#imag");
const fractalSelect = document.querySelector("#fractal-select");

// Move these outside the function
const coordinates = createCoordinates();
let buffer = new Array(canvas.width * canvas.height);
let currentFractal = "julia";
let isRendering = false;

function getCurrentFractal() {
  return fractals[currentFractal];
}

function getParameters() {
  const fractal = getCurrentFractal();
  const params = {
    maxIterations: 200,
  };

  // Add fractal-specific parameters
  if (currentFractal === "julia") {
    params.cReal = Number(realInput.value) || -0.7;
    params.cImag = Number(imagInput.value) || 0.27015;
  }

  return params;
}

function updateControlsVisibility() {
  const juliaControls = document.querySelector(".julia-controls");
  if (juliaControls) {
    juliaControls.style.display = currentFractal === "julia" ? "block" : "none";
  }
}

function render() {
  if (isRendering) return;
  isRendering = true;

  // Resize buffer if canvas size changed
  if (buffer.length !== canvas.width * canvas.height) {
    buffer = new Array(canvas.width * canvas.height);
  }

  const fractal = getCurrentFractal();
  const parameters = getParameters();

  // Show loading state
  canvas.style.opacity = "0.7";

  // Use requestAnimationFrame for smooth rendering
  requestAnimationFrame(() => {
    computeFractal({
      width: canvas.width,
      height: canvas.height,
      coordinates,
      fractal,
      parameters,
      buffer,
    });

    renderer.render(buffer, parameters.maxIterations);

    canvas.style.opacity = "1";
    isRendering = false;
  });
}

// Setup input handling
const inputCleanup = createInputHandler(canvas, coordinates, render);

// Handle fractal selection
fractalSelect.addEventListener("change", (e) => {
  currentFractal = e.target.value;
  updateControlsVisibility();
  render();
});

// Bind controls Julia Set
bindNumberInput(realInput, render);
bindNumberInput(imagInput, render);

// Handle window resize
window.addEventListener("resize", () => {
  renderer.resize();
  render();
});

// Set initial fractal and render
currentFractal = fractalSelect.value || "julia";
updateControlsVisibility();
canvas.style.cursor = "grab";

// Initial render
render();

// Cleanup on page unload
window.addEventListener("beforeunload", () => {
  inputCleanup();
});
