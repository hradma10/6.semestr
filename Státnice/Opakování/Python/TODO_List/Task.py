class Task: 
    def __init__(self, id, name, content):
        self._id = id
        self._name = name
        self._active = True
        self._content = content

    def get_id(self):
        return self._id

    def set_name(self, name):
        if len(self._name):
            self._name = ""
        else:
            self._name = name
    
    def get_name(self):
        return self._name
    
    def set_active(self, state):    
        self._active = state
    
    def get_active(self):
        return self._active
    
    def set_content(self, content):    
        self._content = content
    
    def get_content(self):
        return self._content
    
