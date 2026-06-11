#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:01:24 2022

@author: julio
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere

n=2
qc=QuantumCircuit(n)
#qc.h(0) #Se aplica la compuerta de Hadamard al primer quibit, pone al primer qubit en una superposicion
qc.cx(0,1)# se aplica la compuerta CNOT, el primer qubit es el qubit de control
#qu.x(1)#se aplica la compuerta NOT al segundo qubit, es decir sigmaZ
statevec=Statevector.from_instruction(qc).data
print(statevec)
qc.draw(output='mpl')
print(qc.draw(output='text'))
plot_state_qsphere(statevec)