import { configureStore } from '@reduxjs/toolkit';

import { api } from '~/shared/api/api';
import { usersSlice } from './slices/users';

export const store = configureStore({
  reducer: {
    [api.reducerPath]: api.reducer,
    [usersSlice.reducerPath]: usersSlice.reducer,
  },
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(api.middleware),
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
