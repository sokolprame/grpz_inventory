/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './**/templates/**/*.html', // ��� ������� Django
        './static/css/input.css',   // �������� Tailwind ����
    ],
    theme: {
        extend: {},
    },
    plugins: [],
};
