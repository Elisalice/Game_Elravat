from setuptools import setup

config = {
    'description': 'Игра "Эльрават"',
    'author': 'Алиса Елисеева',
    'author_email': 'alisa.elyseeva@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['gameelravat'],
    'name': 'Game_Elravat',
    'entry_points': {
        'console_scripts': ['elravat = gameelravat.start:start_game']
    } 
}

setup(**config)