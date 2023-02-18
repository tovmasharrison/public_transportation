def upload_profile_image(instance, filename):
    return f"images/{instance.user.username}/{filename}"