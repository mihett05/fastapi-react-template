import { Button, ListItem, ListItemText, Typography } from '@mui/material';

interface IMessage {
  message: {
    sender: string;
    content: string;
    date: string;
  };
}

const mockButtons = [{ text: 'hueta' }, { text: 'lorem ipsum' }, { text: 'eshkin kot eprst' }];

const ChatMessage = ({ message }: IMessage) => {
  return (
    <ListItem sx={{ display: 'block' }}>
      <ListItemText
        primary={message.sender}
        secondary={
          <span style={{ display: 'flex', justifyContent: 'space-between' }}>
            <Typography component="span" variant="body1">
              {message.content}
            </Typography>
            <Typography component="span" variant="caption" color="secondary">
              {message.date}
            </Typography>
          </span>
        }
        sx={{
          backgroundColor:
            message.sender === 'Me' ? 'rgba(167, 219, 127, .1)' : 'rgba(127, 219, 207, .1)',
        }}
      />
      {mockButtons.map((button, index) => (
        <Button key={index} variant="outlined">
          {button.text}
        </Button>
      ))}
    </ListItem>
  );
};

export default ChatMessage;
