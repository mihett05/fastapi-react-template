import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';
import { usePostAuthRegisterMutation } from '~/shared/api/api';
import { setToken } from '~/shared/api/tokens';
import { z } from '~/shared/i18n';
import { useAppDispatch } from '~/shared/store/hooks';
import { setUser } from '~/shared/store/slices/users';

const RegisterSchema = z
  .object({
    email: z.string().min(1),
    password: z.string().min(1),
    passwordAgain: z.string().min(1),
  })
  .refine((data) => data.password === data.passwordAgain, 'Пароли должны совпадать');

export function useRegister(onSuccess?: () => void) {
  const dispatch = useAppDispatch();
  const [register, registerRequest] = usePostAuthRegisterMutation();
  const methods = useForm({
    defaultValues: {
      email: '',
      password: '',
      passwordAgain: '',
    },
    resolver: zodResolver(RegisterSchema),
  });

  const onRegister = async (data: z.infer<typeof RegisterSchema>) => {
    const response = await register({
      userCreate: {
        email: data.email,
        password: data.password,
      },
    });

    if (!response.error) {
      setToken(response.data.accessToken);
      dispatch(setUser(response.data.user));
      onSuccess?.();
    } else {
      methods.setError('email', {
        message: 'Не удалось создать пользователя',
      });
    }
  };

  return {
    isLoading: registerRequest.isLoading,
    methods,
    onRegister,
  };
}
