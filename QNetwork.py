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


    def __init__(self, params):
        '''
        Constructor
        '''
        self.g = tf.Graph()
        self.sess = tf.InteractiveSession(graph=self.g) #,config=tf.ConfigProto(log_device_placement=True))
        self.state_placeholder = tf.placeholder(tf.float32, [None, 9],name="Board_states")
        self.Q_value_placehoalder = tf.placeholder(tf.float32, [1], name="Q_value")
        self.gamma = 0.99
        self.NeuralNetwork(10)
        
    def NeuralNetwork(self, HIDDEN_UNITS_L1, NUM_INPUTS=9, NUM_OUTPUTS=1):
        with self.g.as_default():

            weights_1 = tf.Variable(tf.truncated_normal([NUM_INPUTS, HIDDEN_UNITS_L1]),name="w1")
            biases_1 = tf.Variable(tf.zeros([HIDDEN_UNITS_L1]), name="b1")
            layer_1_outputs = tf.nn.tanh(tf.matmul(self.state_placeholder, weights_1,name="Input_W1_Mul") + biases_1,name="L1")

            weights_2 = tf.Variable(tf.truncated_normal([HIDDEN_UNITS_L1, NUM_OUTPUTS]),name="w2")
            biases_2 = tf.Variable(tf.zeros([NUM_OUTPUTS]),name="b2")
            self.ff_NN_train = tf.add(tf.matmul(layer_1_outputs, weights_2,name="L1_W2_Mul"),biases_2,name="output")
            
            loss_function = tf.reduce_mean(tf.square(tf.subtract(self.ff_NN_train, self.Q_value_placehoalder)))
            self.loss = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss_function)


    def calculateDiscReturn(self, reward, num_steps):
        rollout_return = np.zeros(num_steps)
        rollout_return[-1] = reward
        running_add = 0
        for i in reversed(xrange(0, num_steps)):
            running_add = running_add*self.gamma + rollout_return[i]
            
        return rollout_return
        
    def train(self, discReturn):
        
        
        
        return None
