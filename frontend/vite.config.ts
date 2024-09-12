import react from '@vitejs/plugin-react-swc';
import path from 'node:path';
// import { fileURLToPath, URL } from 'node:url';
import { defineConfig } from 'vite';
import svgr from 'vite-plugin-svgr';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react(), svgr()],
  resolve: {
    alias: {
      '~': path.resolve(__dirname, "./src"),
      // '~': fileURLToPath(new URL('./src')),
    },
  },
});
