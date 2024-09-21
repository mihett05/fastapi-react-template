import { List, styled } from '@mui/material';
import { Link } from 'react-router-dom';
import ChatItem from './chat-item';

const ChatListContainer = styled(List)(({ theme }) => ({
  height: '80vh',
  padding: theme.spacing(2),
}));

interface IChat {
  id: number;
  name: string;
  lastMessage: string;
  lastMessageTime: string;
}

interface IChatList {
  chats: IChat[];
}

const ChatList = ({ chats }: IChatList) => {
  return (
    <ChatListContainer>
      {chats.map((chat) => (
        <Link to={`/chats/${chat.id}`} style={{ textDecoration: 'none' }} key={chat.id}>
          <ChatItem
            name={chat.name}
            lastMessage={chat.lastMessage}
            lastMessageTime={chat.lastMessageTime}
          />
        </Link>
      ))}
    </ChatListContainer>
  );
};

export default ChatList;
