#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 17:57:05 2022

@author: julio
"""
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere

n=2
qc=QuantumCircuit(n)
#qc.x(0)
#qc.x(1)
qc.cx(0,1)
qc.h(0)
qc.x(0)
qc.x(1)
statevec=Statevector.from_instruction(qc).data
print(statevec)
qc.draw(output='mpl')
print(qc.draw(output='text'))
plot_state_qsphere(statevec)