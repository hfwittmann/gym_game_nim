# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:39:32 2016

@author: hfwittmann
"""

import numpy as np
from unittest import TestCase

# seed for reproducibility
np.random.seed(168)

from gym_game_nim.envs.game_nim_env import GameNimEnv


class TestSanity(TestCase):
    def testTakeWay(self):
        
        G = GameNimEnv()
        
        # the default MaxHeapSize is 100
        self.assertTrue(G.maxHeapSize, 100)

        # prototype for assertion error test
        # https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
        with self.assertRaises(AssertionError) as context0:
            
            # cause assertionError
            assert False, 'My assertion error message'
        
        # https://stackoverflow.com/questions/284043/outputting-data-from-unit-test-in-python
        self.assertTrue('My assertion error' in str(context0.exception), 'Message if test goes wrong')
        # end : prototype

        # produce assertion errors
        G.reset()    
        # use first heap
        firstHeap = G.state[0]
    
        # produce failures to check asserts are working
        # 1 failure
        with self.assertRaises(AssertionError) as context:
            # use wrong type for action (action should be a list of 2 values)
            G.step(0)            
        self.assertTrue('Wrong type' in str(context.exception), str(context.exception))
        
        # 2 failure
        with self.assertRaises(AssertionError) as context:
           # use wrong list length for action (action should be a list of 2 values)
            G.step([0])            
        self.assertTrue('Wrong length' in str(context.exception), str(context.exception))
    
        # 3 failure
        with self.assertRaises(AssertionError) as context:
            # try to take more than is in the first heap to cause error            
            G.step([0, firstHeap + 1])            
        self.assertTrue('Heap is not big enough' in str(context.exception), str(context.exception))
        
    
        # now perform a correct action: take the first heap        
        state, reward, done, info = G.step([0, firstHeap])
        
        self.assertTrue( all(state == [0, 58, 46])) # first heap has vanished
        self.assertEqual(reward, 0) # reward is 0, as there are still other heaps left
        self.assertEqual(done, False) # game ist not finished, as there are still other heaps left
        
        
        # test winning position
        G.setHeapsStartingPositions(heaps=[1,0,0])
        
        action = [0, 1] # take one bean from 0-heap (meaning the first heap, due to 0-indexing)
        
        state, reward, done, _ = G.step(action)
        self.assertTrue ( np.all(np.array(state) == 0) , 'Position should be final position (=[0,0,0]), but is {}'.format(state))
        self.assertEqual(reward, 1, 'Reward should be one (=instant win)')
        
        
        
 # for simple debugging do : self = TestSanity()