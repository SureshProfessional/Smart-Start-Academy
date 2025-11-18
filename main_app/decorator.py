from django.shortcuts import redirect

def logout_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:            
            return redirect('/school-page') 
        return view_func(request, *args, **kwargs)
    return wrapper