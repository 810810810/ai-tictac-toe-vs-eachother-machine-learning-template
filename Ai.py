import configparser
import numpy as np
import random

class TicTacToeAI:
    def __init__(self, player, config_file):
        self.player = player
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.discount_factor = float(self.config['learning']['discount_factor'])
        self.learning_rate = float(self.config['learning']['learning_rate'])
        self.epsilon = float(self.config['learning']['epsilon'])
        self.q_table = {}

    def get_q_value(self, state, action):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(9)
        return self.q_table[state][action]

    def update_q_value(self, state, action, reward, next_state):
        q_value = self.get_q_value(state, action)
        next_max_q = np.max(self.q_table[next_state])
        new_q_value = (1 - self.learning_rate) * q_value + self.learning_rate * (reward + self.discount_factor * next_max_q)
        self.q_table[state][action] = new_q_value

    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, 8)
        else:
            return np.argmax(self.q_table[state])

    def learn(self, state, action, reward, next_state):
        self.update_q_value(state, action, reward, next_state)

    def get_move(self, state):
        action = self.choose_action(state)
        return action // 3, action % 3

