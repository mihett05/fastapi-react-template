import { Box, Button, List, styled, TextField } from '@mui/material';
import ChatMessage from './chat-message';

const ChatPageContainer = styled(Box)({
  display: 'flex',
  flexDirection: 'column',
});

const ChatMessagesContainer = styled(Box)({
  flex: 1,
  overflowY: 'auto',
  padding: 16,
});

const ChatInput = styled(TextField)(({ theme }) => ({
  flex: 1,
  marginRight: theme.spacing(1),
}));

const SendButton = styled(Button)(({ theme }) => ({
  marginLeft: theme.spacing(1),
}));

interface IMessage {
  sender: string;
  content: string;
  date: string;
}

interface IMessageProps {
  messages: IMessage[];
  newMessage: string;
  handleSendMessage: () => void;
  setNewMessage: React.Dispatch<React.SetStateAction<string>>;
}

const Chat = (props: IMessageProps) => {
  const { messages, newMessage, handleSendMessage, setNewMessage } = props;
  return (
    <ChatPageContainer>
      <ChatMessagesContainer>
        <List>
          {messages.map((message, index) => (
            <ChatMessage message={message} key={index} />
          ))}
        </List>
      </ChatMessagesContainer>
      <Box display="flex" alignItems="center">
        <ChatInput value={newMessage} onChange={(e) => setNewMessage(e.target.value)} fullWidth />
        <SendButton onClick={handleSendMessage} variant="contained" color="primary">
          Send
        </SendButton>
      </Box>
    </ChatPageContainer>
  );
};

export default Chat;
