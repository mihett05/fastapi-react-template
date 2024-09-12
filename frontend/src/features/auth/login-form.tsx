import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';
import { z } from '~/shared/i18n';
import { Form, FormTextField } from '~/shared/ui/forms';

type LoginFormProps = {};

const LoginSchema = z.object({
  username: z.string().min(1),
  password: z.string().min(1),
});

function LoginForm({}: LoginFormProps) {
  const methods = useForm({
    defaultValues: {
      username: '',
      password: '',
    },
    resolver: zodResolver(LoginSchema),
  });

  return (
    <Form onSubmit={methods.handleSubmit((data) => {})} {...methods}>
      <FormTextField name="username" label="Логин" />
      <FormTextField name="password" label="Пароль" type="password" />
    </Form>
  );
}

export default LoginForm;
