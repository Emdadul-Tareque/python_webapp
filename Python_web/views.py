from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    error = {}
    if request.method == 'POST':
        phone_number = request.POST.get('phone')
        name = request.POST.get('name')
        email = request.POST.get('email')

        if not len(phone_number) == 11:
            error['phone'] = "ফোন নাম্বারটি ভুল"
        if len(name) <= 2:
            error['name'] = "নাম অবশ্যই দুই অক্ষরের বেশি হতে হবে"
        if not email:
            error['email'] = "ইমেল ফিল্ডটি পূরণ করুন"

        success = request.method == "POST" and not error

    return render(request, 'index.html', context={'error': error, 'success': success})
