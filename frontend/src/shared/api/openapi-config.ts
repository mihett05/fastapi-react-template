import type { ConfigFile } from '@rtk-query/codegen-openapi';

import { configDotenv } from 'dotenv';

const {
  parsed: { VITE_BASE_API_URL: baseApiUrl },
} = configDotenv({
  path: '../../../.env.local',
});

const config: ConfigFile = {
  schemaFile: `${baseApiUrl}/openapi.json`,
  apiFile: './base.ts',
  apiImport: 'baseApi',
  outputFile: './api.ts',
  exportName: 'api',
  hooks: {
    lazyQueries: true,
    mutations: true,
    queries: true,
  },
};

export default config;
