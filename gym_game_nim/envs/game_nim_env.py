import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

from IPython.core.debugger import set_trace
    
class GameNimEnv(gym.Env):
    metadata = {'render.modes':['human'] }
    
    def __init__(self):

        # initialize with max heapsizes 100
        self.setNumberOfHeaps()
        self.setMaxHeapSize()
        
        self.setHeapsStartingPositions()
        
        return None

    def setMaxHeapSize(self, maxHeapSize=100):
     
        self.maxHeapSize = maxHeapSize
        self._set_action_space()
 
        return None

    def setNumberOfHeaps(self, numberOfHeaps = 3):
        
        self.numberOfHeaps = numberOfHeaps
        self._set_action_space()
        
        return None

    def setHeapsStartingPositions(self, heaps = None):
        
        # set_trace()
        if heaps:
            self.heaps = np.array(heaps)
            currentMax = np.max(self.heaps)
            if self.maxHeapSize < currentMax:
                self.setMaxHeapSize(currentMax)
            
        
        # the starting position are three random-sized heaps (of beans)
        else:
            self.heaps = np.random.randint(low = 1, high = self.maxHeapSize + 1, size=(self.numberOfHeaps,))
        
        self.reset()
        
        return None

    def _step(self, action):
    
#        set_trace()
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
            "Heap number is: {}. You tried to take {}, but there are only {} beans in this heap. These are the heaps: {}".format(heapnumber, beansnumber, heapsize, self.state)

        
        self.state[heapnumber] += - beansnumber
        
        if np.all(np.array(self.state) == 0):
            
            reward = 1 # this is for the normal variant. The misère variant the reward = - 1. 
            # The winning strategy for the misère variant has an additional complication. thereforw e use the normal variant.
            
            done = True
        
        return self.state, reward, done, {}
    
    def _reset(self):
        
        self.state = self.heaps
        # print('starting in state:', self.state)
        
        return self.state
    
    def _render(self, mode='human', close=False):
        
        if close:
            return
        
        # print ("current state:", self.state)
        
        return None
    
    def _set_action_space(self):
        
        # Remarks
        # the action_space are two numbers:
        # the first coordinate is the heap from which the beans are taken
        # the second coordinate is the number of beans taken
        try:                    
            numberOfHeaps = self.numberOfHeaps
            maxHeapSize = self.maxHeapSize
        
            # low and high are arrays of the same shape
        except AttributeError:
            return None            
        
        self.action_space = spaces.Box(np.array([0, 1]), np.array([numberOfHeaps, maxHeapSize])) 
        
        return None
        
        
        
        