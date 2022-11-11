class SingletonMeta(object):

    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        
        return class_._instance

class SingletonGetJson(SingletonMeta):

    def getToken(tk, obj):
        clave = None
        if tk == 'token 1':
            clave = obj['token1']
        elif tk == 'token 2':
            clave = obj['token2']
        else:
            return 'token ' + tk + ' no existe'

        return clave
            
