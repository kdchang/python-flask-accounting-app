from fabric.api import local

def test():
    local('python -m unittest discover')
