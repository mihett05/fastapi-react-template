import { TextField } from '@mui/material';
import { HTMLInputTypeAttribute } from 'react';
import { FieldValues, Path, useController, useFormContext } from 'react-hook-form';

type FormTextFieldProps<T extends FieldValues> = {
  name: Path<T>;
  label: string;
  type?: HTMLInputTypeAttribute;
  multiline?: boolean;
  fullWidth?: boolean;
};

function FormTextField<T extends FieldValues>({
  name,
  label,
  type = 'text',
  multiline = false,
  fullWidth = false,
}: FormTextFieldProps<T>) {
  const { control } = useFormContext();
  const { field, fieldState } = useController({
    control,
    name,
  });

  return (
    <TextField
      label={label}
      type={type}
      {...field}
      error={fieldState.error !== undefined}
      helperText={fieldState.error && fieldState.error.message}
      multiline={multiline}
      fullWidth={fullWidth}
    />
  );
}

export default FormTextField;
