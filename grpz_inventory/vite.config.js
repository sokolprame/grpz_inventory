import { defineConfig } from 'vite';

   export default defineConfig({
     build: {
       outDir: 'static/dist',
       assetsDir: '',
       emptyOutDir: true,
       manifest: true,
       rollupOptions: {
         input: {
           main: './static/css/styles.css',
         },
       },
     },
   });