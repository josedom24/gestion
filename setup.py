from setuptools import setup

setup(name='django 1.7 on Red Hat Openshift',
    version='1.3',
    description='django on OpenShift',
    author='',
    author_email='',
    url='https://github.com/jfmatth/openshift-django17',
    install_requires=['django-tinymce','django-easy-pdf','xhtml2pdf>=0.0.6','reportlab>=2.7,<3'],
)
