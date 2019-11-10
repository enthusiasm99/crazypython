class Cell:
    @property
    def state(self):
        return self._state  #"_state" 相当于一个变量的名字，可以换成"aastate" 、"bb"
    
    @state.setter
    def state(self, value):
        if 'alive' in value.lower():
            self._state = 'alive'
        else :
            self._state = 'dead'
    
    @property
    def is_dead(self):
        return not self._state.lower == 'alive'

c = Cell()
c.state = 'Alive'
print(c.state)
print(c.is_dead)