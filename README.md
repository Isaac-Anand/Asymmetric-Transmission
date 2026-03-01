# Asymmetric-Transmission
**Internship 2025, Metamaterials and Photonics Lab**

Asymmetric transmission (AT) is a phenomenon where the total transmittance of an electromagnetic wave depends on its propagation direction (forward $+z$ vs. backward $-z$). In the terahertz (THz) regime, this effect is highly desirable for creating nonreciprocal-like devices such as isolators, circulators, and high-efficiency polarization converters without the need for bulky magneto-optical materials.

This project explores the design of anisotropic metamaterials (AMMs) that break structural symmetry to achieve giant AT through cross-polarization conversion. By engineering the unit cell geometry—such as a rectangular spiral—we can precisely control the phase and amplitude of orthogonal wave components.

**KEY FEATURES AND FUNDAMENTAL THEORY**

The Jones Matrix FormalismThe response of a general unit cell to incident radiation is described by the complex Jones Matrix, which relates the incident ($E^i$) and transmitted ($E^t$) electric fields

$$
\begin{pmatrix} 
E_x^t \\ 
E_y^t 
\end{pmatrix} 
= T_{lin} 
\begin{pmatrix} 
E_x^i \\ 
E_y^i 
\end{pmatrix} 
= \begin{pmatrix} 
t_{xx} & t_{xy} \\ 
t_{yx} & t_{yy} 
\end{pmatrix} 
\begin{pmatrix} 
E_x^i \\ 
E_y^i 
\end{pmatrix}
$$

  **Co-polarization coefficients ($t_{xx}, t_{yy}$)**: Transmission where the output state is the same as the input.

  **Cross-polarization coefficients ($t_{yx}, t_{xy}$)**: Transmission where the output state is rotated by $90^\circ$

**CONDITIONS FOR ASYMMETRIC TRANSMISSION**

  For a reciprocal system to exhibit AT, the unit cell must introduce anisotropy. The necessary conditions for AT are:

   **Linear Polarization (LP):** $t_{yx} \neq t_{xy}$ while $t_{xx} = t_{yy}$.

   **Circular Polarization (CP):** $t_{-+} \neq t_{+-}$ while $t_{++} = t_{--}$

**THE AT PARAMETER ($\Delta$)**

The efficiency of the asymmetry is quantified by the AT parameter, defined as the difference in cross-polarization transmittances:

  LP AT Parameter: $\Delta_{lin} = |t_{yx}|^2 - |t_{xy}|^2$.

  CP AT Parameter: $\Delta_{cir} = |t_{-+}|^2 - |t_{+-}|^2$.

**METHODOLOGY AND IMPLEMENTATION**

The core of work and design involved in breaking the mirror symmtery of the unit cell. I have used the a rectangular spiral for this implementation.

  **Spiral Geometry:** The spiral naturally introduces a "handedness" or chirality and breaks the $C_2$ symmetry.

  **Anisotropy Engineering:** The unequal lengths of the spiral arms introduce different phase delays for $x$- and $y$-polarized components, which is the catalyst for polarization conversion

High efficiency is often achieved by stacking multiple layers to form a resonant cavity.  These multiple reflections constructively interfere at specific frequencies, significantly boosting the cross-polarization transmission coefficient ($t_{cross}$) toward unity.

**JUSTIFICATION OF RESULTS**

To validate the research findings, the following metrics are used:

 Cross-Polarization Efficiency: We observe a high cross polarization trnasmission coeffecients, but a lower, almost close to zero, co-polarization transmission coeffecients.

 Parametric Study (Spiral Turns): We investgated the effect of the number of turns on the transmission spectra. We observed that as the number of turns increases, new resonances were developed at the lower frequencies.

 Directional Diode-like Effect: By plotting the AT parameter for forward ($+z$) vs. backward ($-z$) propagation, we justify the AT effect. A large gap between these two curves proves the structure acts as a "one-way" transparent window for specific polarizations.
