module.exports = {
    content: [
        './templates/**/*.html', // Все HTML-шаблоны в корневой папке templates
        './users/templates/**/*.html', // Шаблоны в приложении users
        './components/templates/**/*.html', // Шаблоны в приложении components
        './warehouses/templates/**/*.html', // Шаблоны в приложении warehouses
        './orders/templates/**/*.html', // Шаблоны в приложении orders
        './suppliers/templates/**/*.html', // Шаблоны в приложении suppliers
        './stock_operations/templates/**/*.html', // Шаблоны в приложении stock_operations
        './audit/templates/**/*.html', // Шаблоны в приложении audit
        './static/js/**/*.js'
    ],
    theme: {
        extend: {},
    },
    plugins: [],
};