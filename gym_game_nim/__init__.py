from gym.envs.registration import register

register(id='game_nim-v0',
         entry_point='gym_game_nim.envs:GameNimEnv')
