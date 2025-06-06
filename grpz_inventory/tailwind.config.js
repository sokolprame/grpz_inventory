module.exports = {
    content: [
        './templates/**/*.html', // ��� HTML-������� � �������� ����� templates
        './users/templates/**/*.html', // ������� � ���������� users
        './components/templates/**/*.html', // ������� � ���������� components
        './warehouses/templates/**/*.html', // ������� � ���������� warehouses
        './orders/templates/**/*.html', // ������� � ���������� orders
        './suppliers/templates/**/*.html', // ������� � ���������� suppliers
        './stock_operations/templates/**/*.html', // ������� � ���������� stock_operations
        './audit/templates/**/*.html', // ������� � ���������� audit
        './static/js/**/*.js'
    ],
    theme: {
        extend: {},
    },
    plugins: [],
};