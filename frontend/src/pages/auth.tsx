import { Container, Paper } from '@mui/material';
import AuthTabs from '~/features/auth/tabs';
import Layout from '~/shared/ui/layout';

function AuthPage() {
  return (
    <Layout>
      <Container maxWidth="sm">
        <Paper
          sx={{
            my: 5,
            py: 1,
          }}
        >
          <AuthTabs />
        </Paper>
      </Container>
    </Layout>
  );
}

export default AuthPage;
