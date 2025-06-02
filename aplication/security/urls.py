from django.urls import path
from aplication.security.views import auth,menu,module,grupos_modulos,profile,face_login,user


app_name = "security"
urlpatterns = []
# security
urlpatterns += [
    path('auth/login',auth.signin,name="auth_login"),
    path('auth/logout',auth.signout,name='auth_logout'),
    path('auth/change_password',auth.change_password,name='auth_change_password'),
    path('auth/register',auth.signup,name='auth_register'),
    path('profile/', profile.view_profile, name='view_profile'),
    path('profile/edit/', profile.edit_profile, name='edit_profile'),
    path('switch-profile/<int:profile_id>/', profile.switch_profile, name='switch_profile'),


    # URLs de categoria
    path('menu_list/', menu.MenuListView.as_view(), name='menu_list'),
    path('menu_create/', menu.MenuCreateView.as_view(), name='menu_create'),
    path('menu_update/<int:pk>/', menu.MenuUpdateView.as_view(), name='menu_update'),
    path('menu_delete/<int:pk>/', menu.MenuDeleteView.as_view(), name='menu_delete'),   


    #Urls Reconocimiento Facial
    
    path('register/', face_login.face_register_form, name='face_register_form'),
    path('login/', face_login.face_login_form, name='face_login_form'),
    path('register_face/', face_login.register_face, name='register_face'),
    path('face_login/', face_login.face_login, name='face_login'),

    #urls de modulos
    path('module_list/', module.ModuleListView.as_view(), name='module_list'),
    path('module_create/', module.ModuleCreateView.as_view(), name='module_create'),
    path('module_update/<int:pk>/', module.ModuleUpdateView.as_view(), name='module_update'),
    path('module_delete/<int:pk>/', module.ModuleDeleteView.as_view(), name='module_delete'),    

    #urls de grupos-modulos-permisos
    path('groupmodulepermission_list/', grupos_modulos.GroupModulePermissionListView.as_view(), name='groupmodulepermission_list'),
    path('groupmodulepermission_create/', grupos_modulos.GroupModulePermissionCreateView.as_view(), name='groupmodulepermission_create'),
    path('groupmodulepermission_update/<int:pk>/', grupos_modulos.GroupModulePermissionUpdateView.as_view(), name='groupmodulepermission_update'),
    path('groupmodulepermission_delete/<int:pk>/', grupos_modulos.GroupModulePermissionDeleteView.as_view(), name='groupmodulepermission_delete'),    

    # urlls de usuarios
    path('users_list/', user.UsersListView.as_view(), name='users_list'),
    path('users_create/', user.UserCreateView.as_view(), name='users_create'),
    path('users_update/<int:pk>/', user.UserUpdateView.as_view(), name='users_update'),
    path('users_delete/<int:pk>/', user.UserDeleteView.as_view(), name='users_delete'),    

]

