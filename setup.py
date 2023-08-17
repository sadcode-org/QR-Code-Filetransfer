import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='code-filetransfer',
    version='2.1',
    author='VanGans',
    author_email='oppicialxz@gmail.com',
    description='Transfer files over WiFi between your computer and your smartphone from the terminal',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sadcode-org/QR-Code-Filetransfer',
    packages=setuptools.find_packages(),
    scripts=['code-filetransfer/code-filetransfer'],
    install_requires=['qrcode']
)
