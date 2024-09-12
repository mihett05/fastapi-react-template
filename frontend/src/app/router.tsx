import { createBrowserRouter } from 'react-router-dom';
import ChatPage from '~/pages/chat';
import ChatsPage from '~/pages/chats';
import LoginPage from '~/pages/login';

export const router = createBrowserRouter([
  {
    path: '/auth/login',
    element: <LoginPage />,
  },
  {
    path: '/chats',
    element: <ChatsPage />,
    children: [
      {
        path: '/chats/:chatId',
        element: <ChatPage />,
      },
    ],
  },
]);
