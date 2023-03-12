def upload_profile_image(instance, filename):
    """ Path to store uploaded images """

    return f"images/{instance.user.username}/{filename}"


def default_profile_image():
    """ Path for default images """

    return "static/user/image/default_profile.jpg"
