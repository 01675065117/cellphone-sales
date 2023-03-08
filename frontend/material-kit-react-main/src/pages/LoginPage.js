import { Link } from 'react-router-dom';

// material-ui
import { Grid, Stack, Typography } from '@mui/material';
import MoodIcon from '@mui/icons-material/Mood';
// project import
import LoginForm from '../sections/auth/login/LoginForm';
import AuthWrapper from '../sections/auth/AuthWrapper';

// ================================|| LOGIN ||================================ //

const LoginPage = () => (
    <AuthWrapper>
        <Grid container spacing={3}>
            <Grid item xs={12}>
                <Typography
                    variant="h4"
                    noWrap
                    component="a"
                    href="/album"
                    sx={{
                    mr: 2,
                    display: { xs: 'inline-block', md: 'inline-block' },
                    fontFamily: 'monospace',
                    fontWeight: 2000,
                    letterSpacing: '.3rem',
                    color: 'inherit',
                    textDecoration: 'none',
                    }}
                    >
                        LOGO
                </Typography>
                <Stack direction="row" justifyContent="space-between" alignItems="baseline" sx={{ mb: { xs: -0.5, sm: 0.5 } }}>
                    <Typography variant="h3">Login</Typography>
                    <Typography component={Link} to="/signup" variant="body1" sx={{ textDecoration: 'none' }} color="primary">
                        Don&apos;t have an account?
                    </Typography>
                </Stack>
            </Grid>
            <Grid item xs={12}>
                <LoginForm />
            </Grid>
        </Grid>
    </AuthWrapper>
);

export default LoginPage;