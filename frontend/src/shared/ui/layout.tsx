import { CssBaseline } from '@mui/material';
import React from 'react';
import Header from './header';

type LayoutProps = {
  children?: React.ReactNode;
};

function Layout({ children }: LayoutProps) {
  return (
    <>
      <CssBaseline />
      <Header />
      {children}
    </>
  );
}

export default Layout;
