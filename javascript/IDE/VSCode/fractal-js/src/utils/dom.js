export function bindNumberInput(input, onChange) {
    input.addEventListener('input', () => {
        onChange();
    });
}