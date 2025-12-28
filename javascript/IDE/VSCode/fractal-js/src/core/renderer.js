export function createRenderer(canvas) {
    const ctx = canvas.getContext('2d');

    let width = 0;
    let height = 0;

    function resize() {
        width = window.innerWidth;
        height = window.innerHeight;
        canvas.width = width;
        canvas.height = height;
    }

    function iterationToColor(iter, maxIterations) {
        const colorBlack = [0, 0, 0];

        if (iter === maxIterations) {
            return colorBlack;
        }

        // Gradient rgb (red, green, blue)
        const t = iter / maxIterations;
        const r = Math.floor(9 * (1 - t) * t * t * t * 255);
        const g = Math.floor(15 * (1 - t) * (1 - t) * t * t * 255);
        const b = Math.floor(8.5 * (1 - t) * (1 - t) * (1 - t) * t * 255);
        const rgbColor = [r, g, b];

        return rgbColor;
    }

    function render(buffer, maxIterations) {
        const imageData = ctx.createImageData(width, height);
        const data = imageData.data;

        for (let i = 0; i < buffer.length; i++) {
            const [r, g, b] = iterationToColor(buffer[i], maxIterations);
            const idx = i * 4;
            data[idx] = r;
            data[idx + 1] = g;
            data[idx + 2] = b;
            data[idx + 3] = 255; // alpha
        }
        ctx.putImageData(imageData, 0, 0);
    }
    return { resize, render };
}