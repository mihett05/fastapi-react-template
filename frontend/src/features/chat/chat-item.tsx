import { Avatar, ListItem, ListItemAvatar, ListItemText, styled, Typography } from '@mui/material';

const ChatListItem = styled(ListItem)(({ theme }) => ({
  marginBottom: theme.spacing(1),
  '&:hover': {
    backgroundColor: 'rgba(46, 125, 50, .05)',
  },
}));

const ChatListItemText = styled(ListItemText)(() => ({
  flex: 1,
  overflow: 'hidden',
  textOverflow: 'ellipsis',
}));

interface IChatItem {
  name: string;
  lastMessage: string;
  lastMessageTime: string;
}

const ChatItem = ({ name, lastMessage, lastMessageTime }: IChatItem) => {
  return (
    <ChatListItem>
      <ListItemAvatar>
        <Avatar>{name.charAt(0).toUpperCase()}</Avatar>
      </ListItemAvatar>
      <ChatListItemText
        primary={
          <Typography variant="body1" color="black">
            {name}
          </Typography>
        }
        secondary={
          <span style={{ display: 'flex', justifyContent: 'space-between' }}>
            <Typography color="text-primary" variant="caption">
              {lastMessage}
            </Typography>
            <Typography color="secondary" variant="caption">
              {lastMessageTime}
            </Typography>
          </span>
        }
      ></ChatListItemText>
    </ChatListItem>
  );
};

export default ChatItem;
