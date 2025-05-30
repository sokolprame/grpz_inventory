npx tailwindcss initmodule.exports = {
    content: [
        './static/css/styles.css',
        './**/templates/**/*.html', // Обновлённый паттерн для всех приложений
    ],
    theme: {
        extend: {},
    },
    plugins: [],
};