#!/usr/bin/env python
# -*- coding: utf-8 -*-
#=======================================================================
#
# ca_prng.py
# ---------
# Fast and simple ca_prng conformant cellular automata model in
# Python. This model is actually implented as a general 1D CA class
# and the rule and size of the CA array is provided as parameters.
# 
# 
# Author: Joachim Strömbergson
# Copyright (c) 2008, Kryptologik
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
# 
#     * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials
#       provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY Kryptologik ''AS IS'' AND ANY EXPRESS
# OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL Kryptologik BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
# GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#=======================================================================

#-------------------------------------------------------------------
# Python module imports.
#-------------------------------------------------------------------
import sys
import math
import optparse


#-------------------------------------------------------------------
# class CellularAutomata()
# 
# This class implements a 1D cellular automata. The class expects
# to be initalized with an array of arbitrary length with initial
# cell state values (0 or 1) as well as an array with update rules.
# 
# The update rule is expected to contain eight values (0 or 1)
# that define the update value for a cell given by the current
# state of the cell and two nearest neighbours. Note that nearest
# neighbour is calculated with wrap around, that is the cell
# array is treated as a ring.
#-------------------------------------------------------------------
class CellularAutomata():
    def __init__(self, rule, init_state, verbosity):
        self.my_rule = rule
        self.my_state = init_state
        self.verbose = verbosity

        
    def print_state(self):
        """Print the current state of the cellular automata."""
        print(self.my_state)

        
    def update_ca_state(self):
        """Update the cells in the cellular automata array."""

        # Create a new CA array to store the updated state.
        new_state = [x for x in range(len(self.my_state))]

        # For each cell we extract three consequtive bits from the
        # current state and use wrap around at the edges.
        for curr_bit in range(len(self.my_state)):
            if curr_bit == 0:
                bit_left = self.my_state[-1]
                bit_mid = self.my_state[0]
                bit_right = self.my_state[1]
            elif curr_bit == (len(self.my_state) - 1):
                bit_left = self.my_state[(curr_bit - 1)]
                bit_mid = self.my_state[curr_bit]
                bit_right = self.my_state[0]
            else:
                bit_left = self.my_state[(curr_bit - 1)]
                bit_mid = self.my_state[curr_bit]
                bit_right = self.my_state[(curr_bit + 1)]
            
            # Use the extraxted bits to calculate an index for
            # the update rule array and update the cell.
            rule_index = 4 * bit_left + 2 * bit_mid + bit_right
            if self.verbose:
                print("rule_index = %d " % rule_index)
            new_state[curr_bit] = self.my_rule[rule_index]
            
        # Replace the old state array with the new array.
        self.my_state = new_state
    
    def return_cur_state(self):
        return self.my_state


#-------------------------------------------------------------------
# main()
#
# Main function.
#-------------------------------------------------------------------
def ca_prng(init_pattern_data, load_init_state, update_rule, load_update_rule, next_pattern):

    my_init_state = [0 for i in range(32)]
    my_update_rules = [0, 0, 0, 1, 1, 1, 1, 0] #rule 30
    prng_data = 0
    if load_update_rule == 1:
        j = bin(update_rule).replace('0b','').zfill(8)
        m = list(j)
        for l in range(len(m)):
            m[l] = int(m[l])
        my_update_rule = m
    if load_init_state == 1:
        j = bin(init_pattern_data).replace('0b','').zfill(32)
        m = list(j)
        for l in range(len(m)):
            m[l] = int(m[l])
        my_init_rule = m
    my_ca = CellularAutomata(my_update_rules, my_init_state, False)

    if (next_pattern == 1):
        my_ca.update_ca_state()
        prng = my_ca.return_cur_state()
        for l in range(len(prng)):
            prng[l] = str(prng[l])
        prng_data = int(''.join(prng),2)
        
    
    return prng_data
    

     