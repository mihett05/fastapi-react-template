import {
  Box,
  Button,
  ButtonProps,
  CircularProgress,
  Dialog,
  DialogContent,
  DialogTitle,
  Typography,
  TypographyProps,
} from '@mui/material';
import React, { FormEvent, useState } from 'react';
import { FieldValues, FormProvider, FormProviderProps } from 'react-hook-form';

interface BaseFormProps<
  TFieldValues extends FieldValues = FieldValues,
  TContext = any,
  TTransformedValues extends FieldValues = TFieldValues,
> extends FormProviderProps<TFieldValues, TContext, TTransformedValues> {
  loading?: boolean;
}

function BaseForm<T extends FieldValues>({ children, loading, ...props }: BaseFormProps<T>) {
  return (
    <FormProvider {...props}>
      <Box
        sx={{
          m: 2,
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-between',
          gap: 2,
        }}
      >
        {loading ? <CircularProgress /> : children}
      </Box>
    </FormProvider>
  );
}

interface FormProps<T extends FieldValues> extends BaseFormProps<T> {
  onSubmit: React.FormEventHandler<HTMLFormElement>;
  title?: string;
  titleProps?: TypographyProps;
  id?: string;
}

export function Form<T extends FieldValues>({
  onSubmit,
  title,
  titleProps,
  children,
  id,
  ...props
}: FormProps<T>) {
  return (
    <Box
      component="form"
      onSubmit={(event) => {
        onSubmit?.(event);
      }}
      id={id}
    >
      {title && <Typography {...titleProps}>{title}</Typography>}
      <BaseForm {...props}>{children}</BaseForm>
    </Box>
  );
}

interface DialogFormProps<T extends FieldValues> extends BaseFormProps<T> {
  onSubmit: React.FormEventHandler<HTMLFormElement>;
  open: boolean;
  setOpen: (open: boolean) => void;
  title?: string;
}

export function DialogForm<T extends FieldValues>({
  open,
  setOpen,
  onSubmit,
  title,
  children,
  ...props
}: DialogFormProps<T>) {
  return (
    <Dialog
      open={open}
      onClose={() => {
        setOpen(false);
        props.reset();
      }}
      PaperProps={{
        component: 'form',
        onSubmit: (event: FormEvent<HTMLFormElement>) => {
          onSubmit?.(event);
          props.reset();
        },
      }}
      keepMounted
    >
      {title && <DialogTitle>{title}</DialogTitle>}
      <DialogContent>
        <BaseForm {...props}>{children}</BaseForm>
      </DialogContent>
    </Dialog>
  );
}

interface OpenDialogFormProps<T extends FieldValues>
  extends Omit<DialogFormProps<T>, 'open' | 'setOpen'> {
  buttonText?: string;
  buttonProps?: ButtonProps;
}

export function OpenDialogForm<T extends FieldValues>({
  buttonText = 'Открыть',
  buttonProps,
  children,
  ...props
}: OpenDialogFormProps<T>) {
  const [open, setOpen] = useState<boolean>(false);
  return (
    <>
      <Button onClick={() => setOpen(true)} {...buttonProps}>
        {buttonText}
      </Button>
      <DialogForm open={open} setOpen={setOpen} {...props}>
        {children}
      </DialogForm>
    </>
  );
}
