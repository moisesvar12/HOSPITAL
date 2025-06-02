from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.models import User
from aplication.security.models import UserFaceDescriptor
from aplication.security.forms.face_login import FaceRegisterForm
import numpy as np
import json
import logging

logger = logging.getLogger(__name__)

def face_register_form(request):
    """Vista para mostrar el formulario de registro facial"""
    form = FaceRegisterForm()
    return render(request, 'security/face_register.html', {'form': form})

def face_login_form(request):
    """Vista para mostrar el formulario de login facial"""
    return render(request, 'security/face_login.html')

@csrf_exempt
def register_face(request):
    """Vista para procesar el registro facial"""
    if request.method == 'POST':
        form = FaceRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            face_data = form.cleaned_data['face_data']
            
            # Procesar y guardar los datos
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password(User.objects.make_random_password())
                user.save()

            # Guardar el descriptor facial
            UserFaceDescriptor.objects.update_or_create(
                user=user,
                defaults={'face_descriptor': face_data}
            )
            return JsonResponse({
                'success': True,
                'message': 'Registro facial completado con éxito'
            })

        # Si los datos no son válidos
        return JsonResponse({
            'success': False,
            'message': 'Datos inválidos. Revisa el formulario.'
        }, status=400)
    
    return JsonResponse({
        'success': False,
        'message': 'Método no permitido. Por favor, use POST.'
    }, status=405)

@csrf_exempt
def face_login(request):
    """Vista para procesar el login facial"""
    if request.method != 'POST':
        return JsonResponse({
            'success': False,
            'message': 'Método no permitido. Por favor, use POST.'
        }, status=405)

    try:
        data = json.loads(request.body)
        username = data.get('username')
        face_descriptor = np.array(data.get('faceDescriptors', []))

        if not username or not face_descriptor.any():
            return JsonResponse({
                'success': False,
                'message': 'Se requiere un nombre de usuario y una imagen facial'
            }, status=400)

        # Buscar usuario y su descriptor facial
        user = User.objects.filter(username=username).first()
        if not user:
            return JsonResponse({
                'success': False,
                'message': 'Usuario no encontrado'
            }, status=404)

        stored_descriptor = UserFaceDescriptor.objects.filter(user=user).first()
        if not stored_descriptor:
            return JsonResponse({
                'success': False,
                'message': 'No se encontraron datos faciales para este usuario'
            }, status=404)

        # Comparar descriptores faciales
        stored_array = np.array(json.loads(stored_descriptor.face_descriptor))
        distance = np.linalg.norm(face_descriptor - stored_array)

        # Umbral de similitud
        SIMILARITY_THRESHOLD = 0.6

        if distance < SIMILARITY_THRESHOLD:
            login(request, user)
            return JsonResponse({
                'success': True,
                'message': 'Inicio de sesión exitoso',
                'redirect_url': '/core/'  # Ajusta esta URL a tu página principal
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'El rostro no coincide con el registro'
            }, status=401)

    except Exception as e:
        logger.error(f"Error en face_login: {str(e)}")
        return JsonResponse({
            'success': False,
            'message': f'Error del servidor: {str(e)}'
        }, status=500)
