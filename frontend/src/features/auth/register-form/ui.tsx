import { Button } from '@mui/material';
import { Form, FormTextField } from '~/shared/ui/forms';
import { useRegister } from './hooks';

type RegisterFormProps = {
  onSucess?: () => void;
};

function RegisterForm({ onSucess }: RegisterFormProps) {
  const { isLoading, methods, onRegister } = useRegister(onSucess);

  return (
    <Form loading={isLoading} onSubmit={methods.handleSubmit(onRegister)} {...methods}>
      <FormTextField name="email" label="Логин" />
      <FormTextField name="password" label="Пароль" type="password" />
      <FormTextField name="passwordAgain" label="Повторите пароль" type="password" />
      <Button type="submit" variant="contained">
        Создать аккаунт
      </Button>
    </Form>
  );
}

export default RegisterForm;
