import { defineConfig } from 'vite';
import tailwindcss from '@tailwindcss/postcss';
import autoprefixer from 'autoprefixer';

export default defineConfig({
    build: {
        outDir: 'static/dist',
        rollupOptions: {
            input: 'static/js/main.js',
            output: {
                entryFileNames: '[name].js', // Имя для JS-файлов (main.js)
                assetFileNames: 'styles.css' // Имя для CSS-файлов
            }
        }
    },
    css: {
        postcss: {
            plugins: [tailwindcss(), autoprefixer()]
        }
    }
});