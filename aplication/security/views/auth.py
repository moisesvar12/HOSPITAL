from datetime import datetime, timedelta, timezone
import uuid
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django .contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# from .forms import CustomUserCreationForm, CustomUserUpdateForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from aplication.security.forms.signup import CustomUserCreationForm
from django.urls import reverse
#Valida correo

import random
import string
from django.conf import settings
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

from aplication.security.models import PasswordResetCode, ValidationCode


 
# # PAGUINACION
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# # ----------------- Perfil -----------------
# def profile(request):
#     data = {"title1": "IC - Perfil",
#             "title2": "Perfil de Usuario"}
#     return render(request, 'core/profile.html', data)

# #  Actualizar perfil 
# def update_profile(request):
#     data = {"title1": "IC - Actualizar Perfil",
#             "title2": "Actualizar Perfil"}
#     if request.method == 'POST':
#         form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, '¡Tu perfil ha sido actualizado exitosamente!')
#             return redirect('profile')
#     else:
#         form = CustomUserUpdateForm(instance=request.user)
    
#     return render(request, 'core/update_profile.html', {'form': form, **data})

# # ----------------- Registro -----------------
# def signup(request):
#     data = {"title1": "IC - Registro",
#             "title2": "Registro de Usuarios"}

#     if request.method == "GET":
#         form = CustomUserCreationForm()
#         return render(request, "registration/signup.html", {"form": form, **data})
#     elif request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # login(request, user)
#             messages.success(
#                 request, '¡Registro exitoso! Por favor, inicia sesión.')
#             return redirect("signin")
#         else:
#             # Manejo de errores específicos
#             if form.errors:
#                 error_messages = []
#                 for field in form:
#                     for error in field.errors:
#                         error_messages.append(f"{field.label}: {error}")
#                 for error in form.non_field_errors():
#                     error_messages.append(error)
#                 data["errors"] = error_messages

#             return render(request, "registration/signup.html", {"form": form, **data})

# # ----------------- Cerrar Sesion -----------------
@login_required
def signout(request):
    logout(request)
    return redirect("core:home")

# # ----------------- Iniciar Sesion -----------------
def signin(request):
    
    data = {"title1": "Login",
            "title2": "Inicio de Sesión"}
    if request.method == "GET":
        # Obtener mensajes de éxito de la cola de mensajes
        success_messages = messages.get_messages(request)
        return render(request, "security/auth/signin.html", {
            "form": AuthenticationForm(),
            "success_messages": success_messages,  # Pasar mensajes de éxito a la plantilla
            **data
        })
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("core:home")
            else: 
                return render(request, "security/auth/signin.html", {
                    "form": form,
                    "error": "El usuario o la contraseña son incorrectos",
                    **data
                })
        else:
            return render(request, "security/auth/signin.html", {
                "form": form,
                 "error": "Datos invalidos",
                **data
            })


# # ----------------- CAMBIO DE CONTRASEÑA -----------------
# @login_required
# def change_password(request):
#     data = {
#         "title1": "Change Password",
#         "title2": "Cambio de Contraseña"
#     }
#     if request.method == "POST":
#         form = PasswordChangeForm(user=request.user, data=request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Mantener la sesión del usuario después de cambiar la contraseña
#             messages.success(request, "Tu contraseña ha sido cambiada exitosamente.")
#             return redirect("home")  # Redirigir a la página de inicio
#         else:
#             messages.error(request, "Por favor corrige los errores a continuación.")
#             return render(request, "security/auth/change_password.html", {
#                 "form": form,
#                 **data
#             })
#     else:
#         form = PasswordChangeForm(user=request.user)
#         return render(request, "security/auth/change_password.html", {
#             "form": form,
#             **data
#         })


def generate_validation_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        
        if 'request_code' in request.POST:
            # Generar el código de validación
            validation_code = generate_validation_code()
            request.session['validation_code'] = validation_code
            
            # Enviar el código por correo
            send_mail(
                'Código de Validación',
                f'Tu código de validación es: {validation_code}',
                settings.DEFAULT_FROM_EMAIL,
                [request.user.email],
                fail_silently=False,
            )
            messages.info(request, 'Código de validación enviado a tu correo electrónico.')
            return render(request, 'security/auth/change_password.html', {
                'form': form,
                'title1': 'Change Password',
                'title2': 'Cambio de Contraseña',
                'code_sent': True
            })
        
        if 'change_password' in request.POST:
            validation_code = request.POST.get('validation_code')
            session_code = request.session.get('validation_code')
            
            if validation_code != session_code:
                messages.error(request, 'El código de validación es incorrecto.')
                return render(request, 'security/auth/change_password.html', {
                    'form': form,
                    'title1': 'Change Password',
                    'title2': 'Cambio de Contraseña'
                })
            
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Mantener la sesión del usuario después de cambiar la contraseña
                messages.success(request, 'Tu contraseña ha sido cambiada exitosamente.')
                # Limpiar el código de validación de la sesión
                del request.session['validation_code']
                return redirect('home')  # Redirigir a la página de inicio
            else:
                messages.error(request, 'Por favor corrige los errores a continuación.')
        
        return render(request, 'security/auth/change_password.html', {
            'form': form,
            'title1': 'Change Password',
            'title2': 'Cambio de Contraseña'
        })
    
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'security/auth/change_password.html', {
            'form': form,
            'title1': 'Change Password',
            'title2': 'Cambio de Contraseña'
        }) 
    
    
# ----------------- Registro -----------------
def signup(request):
    data = {"title1": "IC - Registro",
            "title2": "Registro de Usuarios"}

    if request.method == "GET":
        form = CustomUserCreationForm()
        return render(request, "security/auth/signup.html", {"form": form, **data})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)  # Añadir request.FILES aquí
        if form.is_valid():
            user = form.save()
            messages.success(request, '¡Registro exitoso! Por favor, inicia sesión.')
            return redirect(reverse('security:auth_login'))
        else:
            if form.errors:
                error_messages = []
                for field in form:
                    for error in field.errors:
                        error_messages.append(f"{field.label}: {error}")
                for error in form.non_field_errors():
                    error_messages.append(error)
                data["errors"] = error_messages

            return render(request, "security/auth/signup.html", {"form": form, **data})

# def signup(request):
#     data = {"title1": "IC - Registro", "title2": "Registro de Usuarios"}

#     if request.method == "GET":
#         form = CustomUserCreationForm()
#         return render(request, "security/auth/signup.html", {"form": form, **data})
#     elif request.method == "POST":
#         form = CustomUserCreationForm(request.POST, request.FILES)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             try:
#                 # Validar la existencia del correo electrónico con registros MX
#                 is_valid_email = validate_email(email, verify=True, check_mx=True)

#                 if not is_valid_email:
#                     form.add_error('email', 'La dirección de correo electrónico no es válida o no existe.')
#                     return render(request, "security/auth/signup.html", {"form": form, **data})

#                 user = form.save()
#                 messages.success(request, '¡Registro exitoso! Por favor, inicia sesión.')
#                 return redirect(reverse('security:auth_login'))
#             except Exception as e:
#                 print(f"Error al validar el correo electrónico: {e}")
#                 form.add_error('email', 'Ocurrió un error al intentar validar la dirección de correo electrónico.')
#                 return render(request, "security/auth/signup.html", {"form": form, **data})
#         else:
#             if form.errors:
#                 error_messages = []
#                 for field in form:
#                     for error in field.errors:
#                         error_messages.append(f"{field.label}: {error}")
#                 for error in form.non_field_errors():
#                     error_messages.append(error)
#                 data["errors"] = error_messages

#             return render(request, "security/auth/signup.html", {"form": form, **data})
