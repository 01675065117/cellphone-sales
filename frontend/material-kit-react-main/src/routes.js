import { Navigate, useRoutes } from 'react-router-dom';
// import { lazy } from 'react';
// layouts
import DashboardLayout from './layouts/dashboard';
import SimpleLayout from './layouts/simple';
// project import
// import Loadable from './components/Loadable';
// import MinimalLayout from './layouts/MinimalLayout/MinimalLayout';
//
import BlogPage from './pages/BlogPage';
import UserPage from './pages/UserPage';
import LoginPage from './pages/LoginPage';
import SignupPage from './pages/SignupPage';
import Page404 from './pages/Page404';
import ProductsPage from './pages/ProductsPage';
import AlbumPage from './pages/AlbumPage';
import DashboardAppPage from './pages/DashboardAppPage';

// ----------------------------------------------------------------------
// render - login
// const LoginForm = Loadable(lazy(() => import('./pages/LoginPage')));
// const SignupForm = Loadable(lazy(() => import('./pages/SignupPage')));

export default function Router() {
  const routes = useRoutes([
    {
      path: '/dashboard',
      element: <DashboardLayout />,
      children: [
        { element: <Navigate to="/dashboard/app" />, index: true },
        { path: 'app', element: <DashboardAppPage /> },
        { path: 'user', element: <UserPage /> },
        { path: 'products', element: <ProductsPage /> },
        { path: 'blog', element: <BlogPage /> },
      ],
    },
    // {
    //   path: '/',
    //   element: <MinimalLayout />,
    //   children: [
    //       {
    //           path: 'login',
    //           element: <LoginForm />
    //       },
    //       {
    //           path: 'signup',
    //           element: <SignupForm />,
    //           index : false
    //       }
    //   ],
    // },
    
    {
      path: 'signup',
      element: <SignupPage />,
    },
    {
      path: 'login',
      element: <LoginPage />,
    },
    {
      path: 'album',
      element: <AlbumPage />,
    },
    {
      element: <SimpleLayout />,
      children: [
        { element: <Navigate to="/dashboard/app" />, index: true },
        { path: '404', element: <Page404 /> },
        { path: '*', element: <Navigate to="/404" /> },
      ],
    },
    {
      path: '*',
      element: <Navigate to="/404" replace />,
    },
  ]);

  return routes;
}
