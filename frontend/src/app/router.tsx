import { createBrowserRouter } from 'react-router-dom';
import AuthPage from '~/pages/auth';
import ChatPage from '~/pages/chat';
import ChatsPage from '~/pages/chats';

export const router = createBrowserRouter([
  {
    path: '/auth',
    element: <AuthPage />,
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
