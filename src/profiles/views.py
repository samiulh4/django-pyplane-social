from django.shortcuts import render
from .models import Profile,Relationship
from .forms import ProfileModelForm

# Create your views here.


def my_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True
    context = {
        'profile': profile,
        'form': form,
        'confirm': confirm,
    }
    return render(request, 'profiles/myprofile.html', context)
# End -:- my_profile_view    


def invites_received_view(request):
    profile = Profile.objects.get(user=request.user)
    qs = Relationship.objects.invatations_received(profile)
    # results = list(map(lambda x: x.sender, qs))
    # is_empty = False
    # if len(results) == 0:
    #     is_empty = True
    context = {
        'qs': qs,
        #'is_empty': is_empty,
    }
    return render(request, 'profiles/my_invites.html', context)
 # End -:- invites_received_view



def profiles_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles(user)
    context = {'qs': qs}
    return render(request, 'profiles/profile_list.html', context)
# end -:- profiles_list_view()


def invite_profiles_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles_to_invite(user)
    context = {'qs': qs}
    return render(request, 'profiles/to_invite_list.html', context)
# end -:- invite_profiles_list_view()  