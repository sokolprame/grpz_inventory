import { defineConfig } from 'vite';
import tailwindcss from '@tailwindcss/postcss';
import autoprefixer from 'autoprefixer';

export default defineConfig({
    build: {
        outDir: 'static/dist',
        assetsDir: '',
        emptyOutDir: true,
        manifest: true,
        rollupOptions: {
            input: { main: './static/css/styles.css' }, // �������� � main2 �� main
            output: {
                entryFileNames: '[name].css', // ������ ������� main.css
                assetFileNames: '[name].[ext]',
            },
        },
    },
    css: {
        postcss: {
            plugins: [tailwindcss(), autoprefixer()],
        },
    },
    root: './',
    server: { watch: { usePolling: true } },
});