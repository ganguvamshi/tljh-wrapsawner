from setuptools import setup


setup (
    name="tljh-wrapspawner",
    author="vamshidhar gangu",
    author_email = 'ganguvamshi@gmail.com',
    version="0.0.1",
    license="GPL-3.0 license",
    url="https://github.com/ganguvamshi/tljh-wrapsawner",
    entry_points = {"tljh": ["wrapspawner = tljh_wrapspawner"]},
    py_modules=['tljh_wrapspawner']
)
