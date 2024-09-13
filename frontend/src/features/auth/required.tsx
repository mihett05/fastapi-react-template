import { Box, CircularProgress, Typography } from '@mui/material';
import { ReactNode, useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router';
import { useLazyGetAuthMeQuery } from '~/shared/api/api';
import { getToken } from '~/shared/api/tokens';
import { routes } from '~/shared/routes';
import { useAppSelector } from '~/shared/store/hooks';
import { setUser } from '~/shared/store/slices/users';

type AuthRequiredProps = {
  children?: ReactNode;
};

function AuthRequired({ children }: AuthRequiredProps) {
  const dispatch = useDispatch();
  const user = useAppSelector((state) => state.users.user);
  const [getUser, getUserRequest] = useLazyGetAuthMeQuery();
  const navigate = useNavigate();

  useEffect(() => {
    const token = getToken();
    console.log(user, token);
    if (!user && !token) {
      navigate(routes.auth());
    } else if (!user && token) {
      (async () => {
        const response = await getUser();
        if (!response.isError && response.data) {
          dispatch(setUser(response.data));
        } else {
          navigate(routes.auth());
        }
      })();
    }
  }, [user]);

  if (user) {
    return children;
  }

  return (
    <Box
      sx={{
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, 50%)',
      }}
    >
      {getUserRequest.isLoading ? (
        <CircularProgress />
      ) : (
        <Typography color="error">Эта страница требует аутентификации</Typography>
      )}
    </Box>
  );
}

export default AuthRequired;
