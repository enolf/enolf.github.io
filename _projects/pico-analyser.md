---
layout: page
title: Pico Electrochemical Analyser
description: A low-cost, high-precision potentiostat/galvanostat built with the Raspberry Pi Pico.
img: assets/img/12.jpg
importance: 1
category: Engineering & Chemistry
related_publications: false
---

Every project has a beautiful feature showcase page.
It's easy to include images in a flexible 3-column grid format.
Make your photos 1/3, 2/3, or full width.

To give your project a background in the portfolio page, just add the img tag to the front matter like so:

    ---
    layout: page
    title: project
    description: a project with a background image
    img: /assets/img/12.jpg
    ---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/1.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/3.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Caption photos easily. On the left, a road goes through a tunnel. Middle, leaves artistically fall in a hipster photoshoot. Right, in another hipster photoshoot, a lumberjack grasps a handful of pine needles.
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    This image can also have a caption. It's like magic.
</div>

You can also put regular text between your rows of images, even citations {% cite einstein1950meaning %}.
Say you wanted to write a bit about your project before you posted the rest of the images.
You describe how you toiled, sweated, _bled_ for your project, and then... you reveal its glory in the next row of images.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    You can also have artistically styled 2/3 + 1/3 images, like these.
</div>

The code is simple.
Just wrap your images with `<div class="col-sm">` and place them inside `<div class="row">` (read more about the <a href="https://getbootstrap.com/docs/4.4/layout/grid/">Bootstrap Grid</a> system).
To make images responsive, add `img-fluid` class to each; for rounded corners and shadows use `rounded` and `z-depth-1` classes.
Here's the code for the last row of images above:

{% raw %}

```html
<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
```

{% endraw %}

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