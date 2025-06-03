/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './**/templates/**/*.html', // все шаблоны Django
        './static/css/input.css',   // исходный Tailwind файл
    ],
    theme: {
        extend: {},
    },
    plugins: [],
};
