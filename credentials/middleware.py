from django.shortcuts import redirect
from django.http import HttpResponse
class LoginRequiredMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self, request):
        if request.path.startswith("/user/") or request.path.startswith("/manager/"):
             if not request.user.is_authenticated:
                  return redirect("signin")
        if request.path.startswith("/manager/") and request.user.profile.role=="user":
                return HttpResponse("Access denied")
                
        response=self.get_response(request)

        return response