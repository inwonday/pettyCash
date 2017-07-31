def rough(request=None):
    if request.method == 'POST':
        data = request.POST.dict()
        print data
        username = data.get('username', None)
        passwordOld = data.get('passwordOld', None)
        passwordNew = data.get('passwordNew', None)
        passwordConfirm = data.get('passwordNewConfirm', None)
        if passwordNew == passwordConfirm:
            user = authenticate(username=username, password=passwordOld)
            if user is not None:
                print passwordNew
                user.set_password(passwordNew)
                user.save()
                print  authenticate(username=username, password=passwordOld)
                print 'all godod'
                return redirect('login')
        return render(request, 'bwi/rough.html')
    else:
         return render(request, 'bwi/rough.html')
