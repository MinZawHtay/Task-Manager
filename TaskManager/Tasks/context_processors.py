def global_data(request):
    theme = None

    if request.user.is_authenticated:
        try:
            theme = request.user.profile.theme
        except:
            theme = 'light'

    return {
        'theme': theme
    }