import {
  Box,
  Button,
  List,
  ListItem,
  ListItemText,
  styled,
  TextField,
  Typography,
} from '@mui/material';

const ChatPageContainer = styled(Box)({
  display: 'flex',
  flexDirection: 'column',
});

const ChatMessagesContainer = styled(Box)({
  flex: 1,
  overflowY: 'auto',
  padding: 16,
});

// const ChatInputContainer = styled('div')({
//   padding: 16,
// });

const ChatInput = styled(TextField)(({ theme }) => ({
  flex: 1,
  marginRight: theme.spacing(1),
}));

const SendButton = styled(Button)(({ theme }) => ({
  marginLeft: theme.spacing(1),
}));

interface IMessages {
  sender: string;
  content: string;
  date: string;
}

interface IMessagesProps {
  messages: IMessages[];
  newMessage: string;
  handleSendMessage: () => void;
  setNewMessage: React.Dispatch<React.SetStateAction<string>>;
}

const Chat = (props: IMessagesProps) => {
  const { messages, newMessage, handleSendMessage, setNewMessage } = props;
  return (
    <ChatPageContainer>
      <ChatMessagesContainer>
        <List>
          {messages.map((message, index) => (
            <ListItem key={index}>
              <ListItemText
                primary={message.sender}
                secondary={
                  <Box display="flex" justifyContent="space-between">
                    <Typography variant="body1">{message.content}</Typography>
                    <Typography variant="caption" color="secondary">
                      {message.date}
                    </Typography>
                  </Box>
                }
                sx={{
                  backgroundColor:
                    message.sender === 'Me' ? 'rgba(167, 219, 127, .1)' : 'rgba(127, 219, 207, .1)',
                }}
              />
            </ListItem>
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
