import { zodResolver } from '@hookform/resolvers/zod';
import { FetchBaseQueryError } from '@reduxjs/toolkit/query/react';
import { useForm } from 'react-hook-form';
import { usePostAuthLoginMutation } from '~/shared/api/api';
import { setToken } from '~/shared/api/tokens';
import { z } from '~/shared/i18n';
import { useAppDispatch } from '~/shared/store/hooks';
import { setUser } from '~/shared/store/slices/users';

const LoginSchema = z.object({
  email: z.string().min(1),
  password: z.string().min(1),
});

export function useLogin(onSuccess?: () => void) {
  const dispatch = useAppDispatch();
  const [login, loginRequest] = usePostAuthLoginMutation();
  const methods = useForm({
    defaultValues: {
      email: '',
      password: '',
    },
    resolver: zodResolver(LoginSchema),
  });

  const onLogin = async (data: z.infer<typeof LoginSchema>) => {
    const response = await login({
      userAuthenticate: {
        email: data.email,
        password: data.password,
      },
    });

    if (!response.error && response.data) {
      setToken(response.data.accessToken);
      dispatch(setUser(response.data.user));
      onSuccess?.();
    } else if (
      (response.error as FetchBaseQueryError).status &&
      (response.error as FetchBaseQueryError).status === 401
    ) {
      ['email', 'password'].forEach((name) => {
        methods.setError(name as 'email' | 'password', {
          message: 'Не верный E-Mail или пароль',
        });
      });
    } else {
      methods.setError('email', {
        message: 'Не удалось сделать запрос',
      });
    }
  };

  return {
    isLoading: loginRequest.isLoading,
    methods,
    onLogin,
  };
}
