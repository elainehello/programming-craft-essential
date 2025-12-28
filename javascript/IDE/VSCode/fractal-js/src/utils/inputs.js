export function createInputHandler(canvas, coordinates, onUpdate) {
  let isDragging = false;
  let lastMouseX = 0;
  let lastMouseY = 0;
  let keys = new Set();

  // Mouse events for panning
  function onMouseDown(e) {
    isDragging = true;
    lastMouseX = e.clientX;
    lastMouseY = e.clientY;
    canvas.style.cursor = "grabbing";
  }

  function onMouseMove(e) {
    if (!isDragging) return;

    const deltaX = e.clientX - lastMouseX;
    const deltaY = e.clientY - lastMouseY;

    // Pan the view
    const panScale = coordinates.scale / canvas.width;
    coordinates.center.x -= deltaX * panScale;
    coordinates.center.y -= deltaY * panScale;

    lastMouseX = e.clientX;
    lastMouseY = e.clientY;

    onUpdate();
  }

  function onMouseUp() {
    isDragging = false;
    canvas.style.cursor = "grab";
  }

  // Zoom with mouse wheel
  function onWheel(e) {
    e.preventDefault();
    const zoomFactor = e.deltaY > 0 ? 1.1 : 0.9;
    coordinates.scale *= zoomFactor;
    // renderisation
    onUpdate();
  }

  // Keyboard navigation
  function onKeyDown(e) {
    keys.add(e.code);

    switch (e.code) {
      case "Equal":
      case "NumpadAdd":
        // Zoom in with +/=
        coordinates.scale *= 0.9;
        // renderisation
        onUpdate();
        break;
      case "Minus":
      case "NumpadSubtract":
        // Zoom out with -
        coordinates.scale *= 1.1;
        // renderisation
        onUpdate();
        break;
      case "KeyR":
        // Reset view with 'R'
        coordinates.center.x = -0.5;
        coordinates.center.y = 0;
        coordinates.scale = 3.0;
        // renderisation
        onUpdate();
        break;
    }
  }

  function onKeyUp(e) {
    keys.delete(e.code);
  }

  // Continuous movement with arrow keys
  function updateContinuous() {
    let moved = false;
    const moveSpeed = coordinates.scale * 0.02;

    if (keys.has("ArrowLeft") || keys.has("KeyA")) {
      coordinates.center.x -= moveSpeed;
      moved = true;
    }
    if (keys.has("ArrowRight") || keys.has("KeyD")) {
      coordinates.center.x += moveSpeed;
      moved = true;
    }
    if (keys.has("ArrowUp") || keys.has("KeyW")) {
      coordinates.center.y -= moveSpeed;
      moved = true;
    }
    if (keys.has("ArrowDown") || keys.has("KeyS")) {
      coordinates.center.y += moveSpeed;
      moved = true;
    }
    // if true - renderise fractal
    if (moved) {
      onUpdate();
    }

    requestAnimationFrame(updateContinuous);
  }

  // Event listeners
  canvas.addEventListener("mousedown", onMouseDown);
  canvas.addEventListener("mousemove", onMouseMove);
  canvas.addEventListener("mouseup", onMouseUp);
  canvas.addEventListener("mouseleave", onMouseUp);
  canvas.addEventListener("wheel", onWheel);

  window.addEventListener("keydown", onKeyDown);
  window.addEventListener("keyup", onKeyUp);

  // Continuous update loop
  updateContinuous();

  // Cleanup function
  return function cleanup() {
    canvas.removeEventListener("mousedown", onMouseDown);
    canvas.removeEventListener("mousemove", onMouseMove);
    canvas.removeEventListener("mouseup", onMouseUp);
    canvas.removeEventListener("mouseleave", onMouseUp);
    canvas.removeEventListener("wheel", onWheel);

    window.removeEventListener("keydown", onKeyDown);
    window.removeEventListener("keyup", onKeyUp);
  };
}
