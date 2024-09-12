import { createBrowserRouter } from 'react-router-dom';
import LoginPage from '~/pages/login';

export const router = createBrowserRouter([
  {
    path: '/auth/login',
    element: <LoginPage />,
  },
]);
