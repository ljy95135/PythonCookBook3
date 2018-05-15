import shutil

print(shutil.get_archive_formats())
shutil.unpack_archive('Python-3.3.0.tgz')
shutil.make_archive('py33', 'zip', 'Python-3.3.0')
