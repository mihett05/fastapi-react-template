import { baseApi as api } from './base';
const injectedRtkApi = api.injectEndpoints({
  endpoints: (build) => ({
    getAuthMe: build.query<GetAuthMeApiResponse, GetAuthMeApiArg>({
      query: () => ({ url: `/auth/me` }),
    }),
    postAuthLogin: build.mutation<PostAuthLoginApiResponse, PostAuthLoginApiArg>({
      query: (queryArg) => ({
        url: `/auth/login`,
        method: 'POST',
        body: queryArg.userAuthenticate,
      }),
    }),
    postAuthRegister: build.mutation<PostAuthRegisterApiResponse, PostAuthRegisterApiArg>({
      query: (queryArg) => ({ url: `/auth/register`, method: 'POST', body: queryArg.userCreate }),
    }),
    postAuthRefresh: build.mutation<PostAuthRefreshApiResponse, PostAuthRefreshApiArg>({
      query: (queryArg) => ({
        url: `/auth/refresh`,
        method: 'POST',
        cookies: { refresh: queryArg.refresh },
      }),
    }),
  }),
  overrideExisting: false,
});
export { injectedRtkApi as api };
export type GetAuthMeApiResponse = /** status 200 Successful Response */ UserRead;
export type GetAuthMeApiArg = void;
export type PostAuthLoginApiResponse = /** status 200 Successful Response */ UserWithToken;
export type PostAuthLoginApiArg = {
  userAuthenticate: UserAuthenticate;
};
export type PostAuthRegisterApiResponse = /** status 200 Successful Response */ UserWithToken;
export type PostAuthRegisterApiArg = {
  userCreate: UserCreate;
};
export type PostAuthRefreshApiResponse = /** status 200 Successful Response */ string;
export type PostAuthRefreshApiArg = {
  refresh: string | null;
};
export type UserRead = {
  id: number;
  email: string;
  isActive: boolean;
  isSuperuser: boolean;
};
export type UserWithToken = {
  accessToken: string;
  user: UserRead;
};
export type ValidationError = {
  loc: (string | number)[];
  msg: string;
  type: string;
};
export type HttpValidationError = {
  detail?: ValidationError[];
};
export type UserAuthenticate = {
  email: string;
  password: string;
};
export type UserCreate = {
  email: string;
  password: string;
};
export const {
  useGetAuthMeQuery,
  useLazyGetAuthMeQuery,
  usePostAuthLoginMutation,
  usePostAuthRegisterMutation,
  usePostAuthRefreshMutation,
} = injectedRtkApi;
