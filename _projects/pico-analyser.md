---
layout: page
title: Pico Electrochemical Analyser
description: A low-cost, high-precision potentiostat/galvanostat built with the Raspberry Pi Pico.
importance: 1
category: Engineering & Chemistry
related_publications: false
images:
  lightbox2: true
---

## Overview

This project involves the design and implementation of an electrochemical testing circuit capable of performing **Electrical Impedance Spectroscopy (EIS)** and **Cyclic Voltammetry (CV)**. By leveraging the Raspberry Pi Pico's dual-core RP2040, the system handles real-time signal generation and high-speed data acquisition for chemical sensing applications.

---

## Hardware Architecture

The core of the system is a custom analog front-end designed to interface with a standard three-electrode setup (Working, Reference, and Counter electrodes).

### 1. Transimpedance Amplifier (TIA)
To measure the low-level currents generated during redox reactions, I implemented a TIA stage. The output voltage is defined by:

$$V_{out} = -I_{cell} \times R_f$$

where $R_f$ is the feedback resistor. I utilized a switching resistor bank to allow for auto-ranging sensitivity across different chemical concentrations.

### 2. Signal Generation
The Pico generates the excitation waveforms (triangular for CV, sinusoidal for EIS) using an external R-2R DAC or filtered PWM, ensuring low noise floor for sensitive measurements.

---

## Software and Control

The firmware is written in **C** for maximum performance during ADC sampling, with a **Python**-based desktop interface for real-time plotting and data logging.

* **Firmware:** Utilizes PIO (Programmable I/O) for jitter-free signal generation.
* **Processing:** Fast Fourier Transform (FFT) is performed on-device to extract impedance parameters during EIS runs.

---

## Future Development

* Integration of a Bluetooth module for wireless field testing.
* Optimizing the TIA for nano-ampere range measurements.
* Developing a custom PCB in KiCad to replace the current breadboard prototype.

---

## Gallery

<a href="https://cdn.photoswipe.com/photoswipe-demo-images/photos/1/img-2500.jpg" data-lightbox="roadtrip"><img src="https://cdn.photoswipe.com/photoswipe-demo-images/photos/1/img-200.jpg" /></a>
<a href="https://cdn.photoswipe.com/photoswipe-demo-images/photos/2/img-2500.jpg" data-lightbox="roadtrip"><img src="https://cdn.photoswipe.com/photoswipe-demo-images/photos/2/img-200.jpg" /></a>
<a href="https://cdn.photoswipe.com/photoswipe-demo-images/photos/3/img-2500.jpg" data-lightbox="roadtrip"><img src="https://cdn.photoswipe.com/photoswipe-demo-images/photos/3/img-200.jpg" /></a>

---

<!-- <div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/pico_setup.jpg" title="Pico Prototype" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/cv_plot.jpg" title="Cyclic Voltammetry Plot" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Left: The current prototype setup at JCU. Right: Sample data output showing a standard Ferricyanide redox couple.
</div> -->