import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

from IPython.core.debugger import set_trace
    
class GameNimEnv(gym.Env):
    metadata = {'render.modes':['human'] }
    
    def __init__(self):

        # initialize with max heapsizes 100
        self.setMaxHeapSize()
        return None
    
    def setMaxHeapSize(self, MaxHeapSize=100):
     
        self.MaxHeapSize = MaxHeapSize
        # Remarks
        # the action_space are two numbers:
        # the first coordinate is the heap from which the beans are taken
        # the second coordinate is the number of beans taken
        self.action_space = spaces.Box(np.array([0, 1]), np.array([3, self.MaxHeapSize])) 
        # low and high are arrays of the same shape

    def _step(self, action):
    
        reward = 0
        done = False
        

        assert isinstance(action, list), 'Wrong type.' + \
            "Type is: {}. Should be <class 'list'>".format(type(action))
        
        assert len(action) == 2, 'Wrong length.' + \
            'Length is:{}. Should by 2'.format(len(action))
            
        
        heapnumber = action[0]
        beansnumber = action[1]
        
        heapsize = self.state[heapnumber]
        
        assert heapsize>=beansnumber, 'Heap is not big enough' + \
            "Heap number is: {}. You tried to take {}, but there are only {} beans in this heap".format(heapnumber, beansnumber, heapsize)

        
        self.state[heapnumber] += - beansnumber
        
        if np.all(self.state == 0):
            
            reward = -1 # this is for the misère variant. Otherwise reward = 1
            done = True
        
        return np.array(self.state), reward, done, {}
    
    def _reset(self):
        
        
        # the starting position are three random-sized heaps (of beans)
        self.state = np.random.randint(self.MaxHeapSize, size=(3,))
        
        print('starting in state:', self.state)
        
        return None
    
    def _render(self, mode='human', close=False):
        
        if close:
            return
        
        print ("current state:", self.state)
        
        return None
