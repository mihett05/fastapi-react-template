import { Box } from '@mui/material';
import { useEffect, useState } from 'react';
import { Outlet } from 'react-router';
import ChatList from '~/features/chat/chat-list';
import Layout from '~/shared/ui/layout';

interface IChat {
  id: number;
  name: string;
  lastMessage: string;
  lastMessageTime: string;
}

const ChatsPage = () => {
  const [chats, setChats] = useState<IChat[]>([]);

  useEffect(() => {
    const initChats = [
      {
        id: 1,
        name: 'Eshkin Kot',
        lastMessage: 'Hello world!',
        lastMessageTime: '12:30',
      },
      {
        id: 2,
        name: 'Nikita Guba',
        lastMessage: 'Hello world!',
        lastMessageTime: '12:30',
      },
      {
        id: 3,
        name: 'Sasha Vinokurov',
        lastMessage: 'Hello world!',
        lastMessageTime: '12:30',
      },
      {
        id: 4,
        name: 'Misha Syrtsov',
        lastMessage: 'Hello world!',
        lastMessageTime: '12:30',
      },
    ];
    setChats(initChats);
  }, []);

  return (
    <Layout>
      <Box display="flex">
        <aside style={{ width: '300px' }}>
          <ChatList chats={chats} />
        </aside>
        <main style={{ flex: 1 }}>
          <Outlet />
        </main>
      </Box>
    </Layout>
  );
};

export default ChatsPage;
