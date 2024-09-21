import { useEffect, useState } from 'react';
import { useParams } from 'react-router';
import Chat from '~/features/chat/chat';

interface IMessages {
  sender: string;
  content: string;
  date: string;
}

const ChatPage = () => {
  const chatId = useParams();
  const [messages, setMessages] = useState<IMessages[]>([]);
  const [newMessage, setNewMessage] = useState('');

  useEffect(() => {
    const mockMessages = [
      { sender: 'SENDER', content: 'Hello!', date: '12:30' },
      { sender: 'SENDER', content: 'How are you?', date: '12:30' },
    ];
    setMessages(mockMessages);
  }, [chatId]);

  const handleSendMessage = () => {
    setMessages([
      ...messages,
      { sender: 'Me', content: newMessage, date: (new Date() as Date).toString() },
    ]);
    setNewMessage('');
  };

  return (
    <Chat
      messages={messages}
      newMessage={newMessage}
      handleSendMessage={handleSendMessage}
      setNewMessage={setNewMessage}
    />
  );
};

export default ChatPage;
