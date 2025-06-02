from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from aplication.security.forms.perfil import UserProfileForm, UserEditForm
from ..models import UserProfile

@login_required
def view_profile(request):
    data = {"title1": "IC - Perfil",
            "title2": "Perfil de Usuario"}
    
    user = request.user
    form = UserProfileForm(instance=user)
    # Renderiza la plantilla 'security/profile.html' en lugar de 'core/profile.html'
    return render(request, 'core/profile.html', {'form': form, **data})

@login_required
def edit_profile(request):
    data = {"title1": "IC - Perfil",
            "title2": "Editar Perfil"}
    
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('security:view_profile')
    else:
        form = UserEditForm(instance=user)
    # Renderiza la plantilla 'security/update_profile.html' en lugar de 'core/update_profile.html'
    return render(request, 'core/update_profile.html', {'form': form, **data})

@login_required
def switch_profile(request, profile_id):
    profile = get_object_or_404(UserProfile, id=profile_id, user=request.user)
    print(f"Switch Profile - Profile ID: {profile_id}, User: {request.user}")
    request.session['active_profile_id'] = profile.id
    print(f"Switch Profile - Active Profile ID Set: {profile.id}")
    print(f"Switch Profile - Session: {request.session.items()}")
    return redirect('security:view_profile')
