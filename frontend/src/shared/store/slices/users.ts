import { PayloadAction, createSlice } from '@reduxjs/toolkit';
import { UserRead } from '~/shared/api/api';

type UsersState = {
  user: UserRead | null;
};

const initialState: UsersState = {
  user: null,
};

export const usersSlice = createSlice({
  name: 'users',
  initialState,
  reducers: {
    setUser(state, action: PayloadAction<UserRead>) {
      state.user = action.payload;
    },
  },
});

export const { setUser } = usersSlice.actions;
