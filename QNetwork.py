'''
Created on May 8, 2017

@author: jejje
'''

import tensorflow as tf
import numpy as np
class QNetwork(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.g = tf.Graph()
        self.sess = tf.InteractiveSession(graph=self.g) #,config=tf.ConfigProto(log_device_placement=True))
        self.state_placeholder = tf.placeholder(tf.float32, [1,10],name="States")
        self.learning_rate_ph = tf.placeholder(tf.float32, name="Learning_rate")
        self.learning_rate = 1
        self.Q_target = tf.placeholder(tf.float32, [1,1],name="Q_targets")
        self.gamma = 0.99
        self.NeuralNetwork(10)
        self.setLossFunction()
        self.predict = tf.argmax(self.Qout,1)
        self.sess.run(tf.global_variables_initializer())

    def NeuralNetwork(self, HIDDEN_UNITS_L1, NUM_INPUTS=10, NUM_OUTPUTS=1):
        with self.g.as_default():

            weights_1 = tf.Variable(tf.truncated_normal([NUM_INPUTS, HIDDEN_UNITS_L1]),name="w1")
            biases_1 = tf.Variable(tf.zeros([HIDDEN_UNITS_L1]), name="b1")
            layer_1_outputs = tf.nn.tanh(tf.matmul(self.state_placeholder, weights_1,name="Input_W1_Mul") + biases_1,name="L1")

            weights_2 = tf.Variable(tf.truncated_normal([HIDDEN_UNITS_L1, NUM_OUTPUTS]),name="w2")
            biases_2 = tf.Variable(tf.zeros([NUM_OUTPUTS]),name="b2")
            self.Qout = tf.add(tf.matmul(layer_1_outputs, weights_2,name="L1_W2_Mul"),biases_2,name="output")

    def setLossFunction(self):
        
        loss_function = tf.reduce_sum(tf.square(tf.subtract(self.Qout, self.Q_target)))
        self.train_op = tf.train.AdamOptimizer(self.learning_rate).minimize(loss_function)
        
    def train(self, curr_state, next_state, reward, allActions, terminal):
        with self.g.as_default():
            if terminal:
                targetQ = np.asarray(reward).reshape(1,1)
            else:
                maxQ,_ = self.getMaxQvalue(next_state, allActions)
                targetQ = reward + self.gamma*maxQ
            
            feed_dict={self.Q_target          : targetQ,
                       self.state_placeholder : np.asarray(curr_state).reshape(1,10),
                       self.learning_rate_ph  : self.learning_rate} 
            for _ in range(1):
                self.sess.run(self.train_op,feed_dict)
        return True
    
    def getQValue(self, state):
        with self.g.as_default():
            return self.sess.run(self.Qout,feed_dict={self.state_placeholder: state})

    def reduceLearningRate(self):
        self.learning_rate *= 0.999
        
    def getMaxQvalue(self, state, allActions):
        with self.g.as_default():
            maxQvalue = -1e10
            bestAction = 0
            for action in allActions:
                input = np.asarray(state+[action])
                input = input.reshape(1,10)
                currQvalue = self.sess.run(self.Qout,feed_dict={self.state_placeholder: input})
                if currQvalue>maxQvalue:
                    maxQvalue=currQvalue
                    bestAction = action
            return maxQvalue, bestAction
    