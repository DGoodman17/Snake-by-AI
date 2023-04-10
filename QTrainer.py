#Main import block
from agent import Linear_QNet
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os
import torch

#Main code block
class QTrainer:
    def __init__(self, model, lr, gamma):
        #Lerning rate for optimizer
        self.lr = lr
        #Discount rate
        self.gamma = gamma
        #Linear NN defined above
        self.model = model

    def train_step(self, state, action, reward, next_state, done):
        state = torch.tensor(state, dtype=torch.float)
        next_state = torch.unsqueeze(state, 0)
        action = torch.unsqueeze(action, 0)
        reward = torch.unsqueeze(reward, 0)
        done = (done, )

        #if only one peramter to train, then convert to touple of shape (1, x)
        if len(state.shape) == 1:
            #(1, x)
            state = torch.unsqueeze(state, 0)
            next_state = torch.unsqueeze(next_state, 0)
            action = torch.unsqueeze(action, 0)
            reward = torch.unsqueeze(reward, 0)
            done = (done, )
        
        #Predicted Q value with current state
        pred = self.model(state)
        target = pred.clone()
        for idx in range(len(done)):
            Q_new = reward[idx]
            if not done[idx]:
                Q_new = reward[idx] + self.gamma * torch.max(self.model(next_state[idx]))
            target[idx][torch.argmax(action).item()] = Q_new    

    # 2. Q_new = reward + gamma * max(next_predicted Qvalue)
    #pred.clone
    #preds[argmax(action)] = Q_new
        self.optimer.zero_grad()
        loss = self.optimer(target, pred)
        loss.backward()

        self.optimer.step()