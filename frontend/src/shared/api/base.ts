import {
  BaseQueryFn,
  createApi,
  FetchArgs,
  fetchBaseQuery,
  FetchBaseQueryError,
} from '@reduxjs/toolkit/query/react';
import { getToken, refreshToken } from './tokens';

const tokenBaseQuery: BaseQueryFn<string | FetchArgs, unknown, FetchBaseQueryError> = async (
  args,
  api,
  extraOptions,
) => {
  const fetchQuery = fetchBaseQuery({
    baseUrl: import.meta.env.VITE_BASE_API_URL,
    credentials: 'include',
    prepareHeaders: (headers) => {
      if (headers.has('Authorization')) {
        return headers;
      }

      const token = getToken();
      if (token !== null) {
        headers.set('Authorization', `Bearer ${token}`);
      }

      return headers;
    },
  });

  const response = await fetchQuery(args, api, extraOptions);

  let token = getToken();
  if (response.error && token !== null) {
    try {
      token = await refreshToken();
    } catch (_: Error) {
      window.location = '/';
    }
    const headers = {
      Authorization: `Bearer ${token!}`,
    };
    if (typeof args === 'string') {
      return fetchQuery(
        {
          url: args,
          headers: {
            ...headers,
          },
        },
        api,
        extraOptions,
      );
    } else {
      return fetchQuery(
        {
          ...args,
          headers: {
            ...args.headers,
            ...headers,
          },
        },
        api,
        extraOptions,
      );
    }
  }

  return response;
};

export const baseApi = createApi({
  baseQuery: tokenBaseQuery,
  endpoints: () => ({}),
});
