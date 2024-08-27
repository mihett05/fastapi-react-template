import { baseApi as api } from './base';

const injectedRtkApi = api.injectEndpoints({
  endpoints: (build) => ({
    postAuthJwtLogin: build.mutation<PostAuthJwtLoginApiResponse, PostAuthJwtLoginApiArg>({
      query: (queryArg) => ({ url: `/auth/jwt/login`, method: 'POST', body: queryArg.login }),
    }),
    postAuthJwtLogout: build.mutation<PostAuthJwtLogoutApiResponse, PostAuthJwtLogoutApiArg>({
      query: () => ({ url: `/auth/jwt/logout`, method: 'POST' }),
    }),
    postAuthRegister: build.mutation<PostAuthRegisterApiResponse, PostAuthRegisterApiArg>({
      query: (queryArg) => ({ url: `/auth/register`, method: 'POST', body: queryArg.userCreate }),
    }),
    postAuthForgotPassword: build.mutation<
      PostAuthForgotPasswordApiResponse,
      PostAuthForgotPasswordApiArg
    >({
      query: (queryArg) => ({
        url: `/auth/forgot-password`,
        method: 'POST',
        body: queryArg.bodyAuthResetForgotPassword,
      }),
    }),
    postAuthResetPassword: build.mutation<
      PostAuthResetPasswordApiResponse,
      PostAuthResetPasswordApiArg
    >({
      query: (queryArg) => ({
        url: `/auth/reset-password`,
        method: 'POST',
        body: queryArg.bodyAuthResetResetPassword,
      }),
    }),
    postAuthRequestVerifyToken: build.mutation<
      PostAuthRequestVerifyTokenApiResponse,
      PostAuthRequestVerifyTokenApiArg
    >({
      query: (queryArg) => ({
        url: `/auth/request-verify-token`,
        method: 'POST',
        body: queryArg.bodyAuthVerifyRequestToken,
      }),
    }),
    postAuthVerify: build.mutation<PostAuthVerifyApiResponse, PostAuthVerifyApiArg>({
      query: (queryArg) => ({
        url: `/auth/verify`,
        method: 'POST',
        body: queryArg.bodyAuthVerifyVerify,
      }),
    }),
    getAuthUsersMe: build.query<GetAuthUsersMeApiResponse, GetAuthUsersMeApiArg>({
      query: () => ({ url: `/auth/users/me` }),
    }),
    patchAuthUsersMe: build.mutation<PatchAuthUsersMeApiResponse, PatchAuthUsersMeApiArg>({
      query: (queryArg) => ({ url: `/auth/users/me`, method: 'PATCH', body: queryArg.userUpdate }),
    }),
    getAuthUsersById: build.query<GetAuthUsersByIdApiResponse, GetAuthUsersByIdApiArg>({
      query: (queryArg) => ({ url: `/auth/users/${queryArg.id}` }),
    }),
    patchAuthUsersById: build.mutation<PatchAuthUsersByIdApiResponse, PatchAuthUsersByIdApiArg>({
      query: (queryArg) => ({
        url: `/auth/users/${queryArg.id}`,
        method: 'PATCH',
        body: queryArg.userUpdate,
      }),
    }),
    deleteAuthUsersById: build.mutation<DeleteAuthUsersByIdApiResponse, DeleteAuthUsersByIdApiArg>({
      query: (queryArg) => ({ url: `/auth/users/${queryArg.id}`, method: 'DELETE' }),
    }),
    postAuthJwtRefresh: build.mutation<PostAuthJwtRefreshApiResponse, PostAuthJwtRefreshApiArg>({
      query: (queryArg) => ({
        url: `/auth/jwt/refresh`,
        method: 'POST',
        cookies: { refresh: queryArg.refresh },
      }),
    }),
  }),
  overrideExisting: false,
});
export { injectedRtkApi as api };
export type PostAuthJwtLoginApiResponse = /** status 200 Successful Response */ BearerResponse;
export type PostAuthJwtLoginApiArg = {
  login: BodyAuthAuthJwtLogin;
};
export type PostAuthJwtLogoutApiResponse = /** status 200 Successful Response */ any;
export type PostAuthJwtLogoutApiArg = void;
export type PostAuthRegisterApiResponse = /** status 201 Successful Response */ UserRead;
export type PostAuthRegisterApiArg = {
  userCreate: UserCreate;
};
export type PostAuthForgotPasswordApiResponse = /** status 202 Successful Response */ any;
export type PostAuthForgotPasswordApiArg = {
  bodyAuthResetForgotPassword: BodyAuthResetForgotPassword;
};
export type PostAuthResetPasswordApiResponse = /** status 200 Successful Response */ any;
export type PostAuthResetPasswordApiArg = {
  bodyAuthResetResetPassword: BodyAuthResetResetPassword;
};
export type PostAuthRequestVerifyTokenApiResponse = /** status 202 Successful Response */ any;
export type PostAuthRequestVerifyTokenApiArg = {
  bodyAuthVerifyRequestToken: BodyAuthVerifyRequestToken;
};
export type PostAuthVerifyApiResponse = /** status 200 Successful Response */ UserRead;
export type PostAuthVerifyApiArg = {
  bodyAuthVerifyVerify: BodyAuthVerifyVerify;
};
export type GetAuthUsersMeApiResponse = /** status 200 Successful Response */ UserRead;
export type GetAuthUsersMeApiArg = void;
export type PatchAuthUsersMeApiResponse = /** status 200 Successful Response */ UserRead;
export type PatchAuthUsersMeApiArg = {
  userUpdate: UserUpdate;
};
export type GetAuthUsersByIdApiResponse = /** status 200 Successful Response */ UserRead;
export type GetAuthUsersByIdApiArg = {
  id: string;
};
export type PatchAuthUsersByIdApiResponse = /** status 200 Successful Response */ UserRead;
export type PatchAuthUsersByIdApiArg = {
  id: string;
  userUpdate: UserUpdate;
};
export type DeleteAuthUsersByIdApiResponse = /** status 204 Successful Response */ void;
export type DeleteAuthUsersByIdApiArg = {
  id: string;
};
export type PostAuthJwtRefreshApiResponse = /** status 200 Successful Response */ BearerResponse;
export type PostAuthJwtRefreshApiArg = {
  refresh: string | null;
};
export type BearerResponse = {
  access_token: string;
  token_type: string;
};
export type ErrorModel = {
  detail:
    | string
    | {
        [key: string]: string;
      };
};
export type ValidationError = {
  loc: (string | number)[];
  msg: string;
  type: string;
};
export type HttpValidationError = {
  detail?: ValidationError[];
};
export type BodyAuthAuthJwtLogin = {
  grant_type?: string | null;
  username: string;
  password: string;
  scope?: string;
  client_id?: string | null;
  client_secret?: string | null;
};
export type UserRead = {
  id: number;
  email: string;
  is_active?: boolean;
  is_superuser?: boolean;
  is_verified?: boolean;
};
export type UserCreate = {
  email: string;
  password: string;
  is_active?: boolean | null;
  is_superuser?: boolean | null;
  is_verified?: boolean | null;
};
export type BodyAuthResetForgotPassword = {
  email: string;
};
export type BodyAuthResetResetPassword = {
  token: string;
  password: string;
};
export type BodyAuthVerifyRequestToken = {
  email: string;
};
export type BodyAuthVerifyVerify = {
  token: string;
};
export type UserUpdate = {
  password?: string | null;
  email?: string | null;
  is_active?: boolean | null;
  is_superuser?: boolean | null;
  is_verified?: boolean | null;
};
export const {
  usePostAuthJwtLoginMutation,
  usePostAuthJwtLogoutMutation,
  usePostAuthRegisterMutation,
  usePostAuthForgotPasswordMutation,
  usePostAuthResetPasswordMutation,
  usePostAuthRequestVerifyTokenMutation,
  usePostAuthVerifyMutation,
  useGetAuthUsersMeQuery,
  usePatchAuthUsersMeMutation,
  useGetAuthUsersByIdQuery,
  usePatchAuthUsersByIdMutation,
  useDeleteAuthUsersByIdMutation,
  usePostAuthJwtRefreshMutation,
} = injectedRtkApi;
