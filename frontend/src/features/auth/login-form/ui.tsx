import { Button } from '@mui/material';
import { Form, FormTextField } from '~/shared/ui/forms';
import { useLogin } from './hooks';

type LoginFormProps = {
  onSucess?: () => void;
};

function LoginForm({ onSucess }: LoginFormProps) {
  const { isLoading, methods, onLogin } = useLogin(onSucess);

  return (
    <Form loading={isLoading} onSubmit={methods.handleSubmit(onLogin)} {...methods}>
      <FormTextField name="email" label="Логин" />
      <FormTextField name="password" label="Пароль" type="password" />
      <Button type="submit" variant="contained">
        Войти
      </Button>
    </Form>
  );
}

export default LoginForm;
