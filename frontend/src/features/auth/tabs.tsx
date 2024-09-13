import TabContext from '@mui/lab/TabContext';
import TabList from '@mui/lab/TabList';
import TabPanel from '@mui/lab/TabPanel';
import { Box, Tab } from '@mui/material';
import { SyntheticEvent, useState } from 'react';
import { LoginForm } from './login-form';
import { RegisterForm } from './register-form';

function AuthTabs() {
  const [tab, setTab] = useState('login');

  const handleChange = (_: SyntheticEvent, newTab: string) => {
    setTab(newTab);
  };

  const onAuth = () => {
    window.location.pathname = '/';
  };

  return (
    <Box sx={{ width: '100%', typography: 'body1' }}>
      <TabContext value={tab}>
        <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
          <TabList onChange={handleChange} aria-label="lab API tabs example" variant="fullWidth">
            <Tab label="Логин" value="login" />
            <Tab label="Регистрация" value="register" />
          </TabList>
        </Box>
        <TabPanel value="login">
          <LoginForm onSucess={onAuth} />
        </TabPanel>
        <TabPanel value="register">
          <RegisterForm onSucess={onAuth} />
        </TabPanel>
      </TabContext>
    </Box>
  );
}

export default AuthTabs;
