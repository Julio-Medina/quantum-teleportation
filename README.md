# Introduction to Quantum Circuits and Quantum Teleportation

This repository contains a short LaTeX article introducing the basic mathematical and physical ideas behind quantum circuits, quantum computation, Bell states, Bell-state measurement, and the quantum teleportation protocol.

The document was originally written in Spanish and later translated into English. The article is intended as a compact educational introduction for students with some background in linear algebra, quantum mechanics, or mathematical physics.

## Overview

Quantum computing is built on the representation of information through quantum states. Instead of classical bits, which take values `0` or `1`, quantum computation uses qubits, which may exist in superpositions of computational basis states. This allows quantum circuits to manipulate amplitudes through unitary transformations and to exploit uniquely quantum effects such as interference and entanglement.

The article develops these ideas gradually, starting from Dirac notation and single-qubit states, then moving toward measurement, quantum gates, multipartite states, Bell states, Bell measurements, and finally the teleportation protocol.

## Main topics covered

- Origins of quantum computing and Feynman's motivation for quantum simulation
- Classical bits versus quantum bits
- Dirac notation: kets, bras, inner products, and outer products
- Qubit representation in the computational basis
- Quantum measurement and Born's rule
- Single-qubit gates, including Pauli matrices and the Hadamard gate
- Tensor products and multipartite quantum states
- Two-qubit gates, especially the CNOT gate
- Quantum entanglement and Bell states
- Bell-state preparation circuits
- Bell-state measurement
- Quantum teleportation with classical communication and feed-forward corrections

## Repository structure

A typical version of this repository may contain:

```text
.
├── Quantum_Teleportation.tex          # Original Spanish LaTeX article
├── Quantum_Teleportation_EN.tex       # English translated version
├── README.md                          # Project documentation
├── classicalNOT.png                   # Classical NOT gate diagram
├── basic_CNOT_circuit.png             # CNOT circuit diagram
├── Bell_states_creation.png           # Bell-state preparation circuit
├── Bell_measurement.png               # Bell-state measurement circuit
└── teletransportation_protocol.png    # Quantum teleportation protocol diagram
```

The exact file names may vary depending on how the repository is organized. The LaTeX source expects the image files to be available in the same directory as the `.tex` file.

## Core mathematical ideas

### Qubits

The computational basis states are represented as

$$
|0\rangle =
\begin{pmatrix}
1 \\
0
\end{pmatrix},
\qquad
|1\rangle =
\begin{pmatrix}
0 \\
1
\end{pmatrix}.
$$

A general normalized qubit can be written as

$$
|\psi\rangle = \alpha |0\rangle + \beta |1\rangle,
\qquad
|\alpha|^2 + |\beta|^2 = 1.
$$

### Born's rule

If a state $|\psi\rangle$ is measured in a basis containing the state $|x\rangle$, the probability of obtaining the outcome associated with $|x\rangle$ is

$$
P(x) = |\langle x | \psi \rangle|^2.
$$

This rule connects the abstract vector-space description of quantum states with experimentally observed probabilities.

### Bell states

The article introduces the maximally entangled Bell basis:

$$
|\psi^{00}\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle),
$$

$$
|\psi^{01}\rangle = \frac{1}{\sqrt{2}}(|01\rangle + |10\rangle),
$$

$$
|\psi^{10}\rangle = \frac{1}{\sqrt{2}}(|00\rangle - |11\rangle),
$$

$$
|\psi^{11}\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle).
$$

These states are central to quantum information theory because they represent simple examples of entangled two-qubit systems.

### Quantum teleportation

The teleportation protocol allows Alice to transmit an unknown quantum state to Bob using a shared entangled pair, a Bell-state measurement, two classical bits of communication, and a correction operation applied by Bob.

If Alice wants to send the state

$$
|\phi\rangle_S = \alpha |0\rangle_S + \beta |1\rangle_S,
$$

and Alice and Bob share the Bell state

$$
|\psi^{00}\rangle_{AB} = \frac{1}{\sqrt{2}}(|00\rangle_{AB} + |11\rangle_{AB}),
$$

then the full three-qubit state can be decomposed in the Bell basis of Alice's two qubits as

$$
|\phi\rangle_S |\psi^{00}\rangle_{AB}=\frac{1}{2}\left[|\psi^{00}\rangle_{SA}|\phi\rangle_B+|\psi^{01}\rangle_{SA}\sigma_x|\phi\rangle_B+|\psi^{10}\rangle_{SA}\sigma_z|\phi\rangle_B+|\psi^{11}\rangle_{SA}\sigma_x\sigma_z|\phi\rangle_B\right].
$$

After Alice performs the Bell-state measurement, Bob's qubit collapses into one of four related states. Alice sends Bob two classical bits indicating her measurement result, and Bob applies the corresponding correction:

| Alice's Bell measurement result | Bob's state before correction | Bob's correction |
| --- | --- | --- |
| $|\psi^{00}\rangle$ | $|\phi\rangle$ | $I$ |
| $|\psi^{01}\rangle$ | $\sigma_x|\phi\rangle$ | $\sigma_x$ |
| $|\psi^{10}\rangle$ | $\sigma_z|\phi\rangle$ | $\sigma_z$ |
| $|\psi^{11}\rangle$ | $\sigma_x\sigma_z|\phi\rangle$ | $\sigma_z\sigma_x$ |

This does not clone the original state. Alice's measurement destroys her local copy of the unknown state, while Bob reconstructs it using the classical information and the shared entanglement resource.

## Bell-state measurement note

The Bell-state measurement circuit in the article is interpreted in the context of the teleportation protocol, where the measurement outcome is tied to built-in classical feed-forward correction logic. This is the standard operational viewpoint used in quantum teleportation and entanglement swapping.

A bare inverse Bell-basis circuit can be written differently depending on the chosen convention for the ordering of gates, qubits, and Bell-state labels. For this reason, the interpretation of the Bell-state measurement block should be kept consistent with the teleportation correction table.

## How to compile the article

To compile the English version with `pdflatex`, run:

```bash
pdflatex Quantum_Teleportation_EN.tex
pdflatex Quantum_Teleportation_EN.tex
```

Running the command twice helps resolve references and labels.

You can also use `latexmk`:

```bash
latexmk -pdf Quantum_Teleportation_EN.tex
```

To clean auxiliary files generated by LaTeX:

```bash
latexmk -c
```

## LaTeX dependencies

The article uses common LaTeX packages:

```latex
\usepackage[english]{babel}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{bbold}
\usepackage{graphicx}
\usepackage{hyperref}
```

If `bbold` is not available in your LaTeX distribution, install the corresponding package or replace `\mathbb{1}` with another identity-operator notation such as `I` or `\mathbf{1}`.

## Suggested project purpose

This repository can be used as:

- A short educational article on quantum circuits and teleportation
- A LaTeX reference for basic quantum-computing notation
- A starting point for a more complete tutorial on quantum information
- A foundation for future code implementations using Qiskit, PennyLane, Cirq, or another quantum-computing framework

## Possible future improvements

- Add a Qiskit implementation of the teleportation circuit
- Add a numerical simulation of the protocol using state vectors
- Include Bloch-sphere visualizations for one-qubit states
- Add exercises after each section
- Expand the discussion of Bell inequalities, CHSH inequalities, and experimental tests of nonlocality
- Add a section on noisy channels and error correction in teleportation experiments

## References

The article cites several standard references in quantum computation and quantum mechanics, including:

- Richard P. Feynman, *Simulating Physics with Computers*
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information*
- N. David Mermin, *Quantum Computer Science: An Introduction*
- J. J. Sakurai, *Modern Quantum Mechanics*
- J. S. Bell, *On the Einstein Podolsky Rosen Paradox*
- Qiskit Textbook

## Author

**Julio A. Medina**  
Universidad de San Carlos  
School of Physical and Mathematical Sciences  
Master's Program in Physics
