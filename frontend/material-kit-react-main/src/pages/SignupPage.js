import { Link } from 'react-router-dom';

// material-ui
import { Grid, Stack, Typography } from '@mui/material';

// project import
import SignupForm from '../sections/auth/signup/SignupForm';
import AuthWrapper from '../sections/auth/AuthWrapper';

// ================================|| REGISTER ||================================ //

const SignupPage = () => (
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
                    <Typography variant="h3">Sign up</Typography>
                    <Typography component={Link} to="/login" variant="body1" sx={{ textDecoration: 'none' }} color="primary">
                        Already have an account?
                    </Typography>
                </Stack>
            </Grid>
            <Grid item xs={12}>
                <SignupForm />
            </Grid>
        </Grid>
    </AuthWrapper>
);

export default SignupPage;
