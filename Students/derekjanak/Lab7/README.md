Lab 7

Background:

In this lab, we designed and built simple phase shifter circuits, then took measurements of
their S-matrices.  We also took S-parameter measurements on a milled Wilkinson power divider
circuit of the design discussed in class.  The performance and design of this circuit was
later modeled in HFSS simulation.

Application:

In high frequency power electronics, power dividers are essential to provide power to various
components while avoiding reflections, which waste power and generate unwanted circuit noise
and transients.  The Wilkinson power divider is designed as both a divider and a combiner that
is capable both of providing power to the two output ports and of recieving power from these
ports.  This power splitter design has the advantage of having isolated output ports; that is,
an excitation at port 2 does not disturb the circuit output at port 3.

Phase shifters are also very important tools within high frequency circuits.  These
devices can be applied in situations when phase matching is needed at inputs or 
outputs of circuits.  The phase shifter designed in lab is a basic proof of concept
that has limited applications.  An adjustable phase shifter design will be discussed
in a later lab.

Design:

The design of the Wilkinson power divider is primarily based on symmetry.  The circuit consists
of an input port connected to a transmission line with a normalized characteristic impedance of 1.
This line terminates in two quarter wave transformers which connect to output ports with normalized
characteristic impedance equal to 1.  The two quarter wave transformers are bridged by a SMD
resistor of value 2Z0, resulting in an even 3 dB power split.  To accomplish this, the quarter
wave sections are curved to form a circular pattern in order to avoid strong coupling effects;
this also results in additional reactance which requires a slight compensation in length.  The
output ports also curve outward from the resistor in order to avoid coupling.  The analysis of
the circuit is carried out using even/odd mode analysis.

The phase shifter designed in this lab utilized lengths of transmission line to shift the phase
of the output.  An initial line was established in order to determine a reference phase; then
the original line was cut and two phase shifting circuit routes were tested.  These routes
consisted of a line running parallel to the original line but offset.  The two connecting
segments of transmission line were chosen to be quarter wavelength sections for one phase
shifting circuit and eigth wavelength sections for the other; this resulted in shifts of 
180 degrees and 90 degrees, respectively.  Special care was taken to space these lines widely in
order to minimize coupling and to keep the additional line length within the reference frame.


Procedure:

First, the Wilkinson power divider S-parameters were measured using the network analyzer;
this required measurements taken at each of the two output ports with respect to the input
port.  The data from these measurements was saved and is included in the data plots.

Next, students designed and constructed the phase shifter.  The students established a reference
microstrip line of characteristic impedance 50 ohms on 62 mil FR4 and soldered SMA connectors 
onto both ends.  The reference line was measured and the phase shift was recorded.  The reference
line was then cut at two points, and a perpendicular quarter wavelength lines were attached at
each of the breaks.  These lines were connected with a section of transmission line running parallel
to the original line.  This resulted in a new line with an electrical length 180 degrees greater
than the original line.  Measurements  were taken to confirm the phase shift of the circuit, and
the results are shown in the plots below.  The same procedure was repeated utilizing eight
wavelength offset line segments to achieve phase shifts of 90 degrees.

Results:

See plot images for data.

Conclusion:

In this lab, the student applied knowledge from lecture to the analysis of a pre-fabricated
Wilkinson power divider, as well as to the design and construction of two phase shifter circuits.
The lab was fairly straightforward, with the only difficulties being encountered in simulation
of the Wilkinson power divider, where it was necessary to adjust the length of the quarter
wavelength sections in order to compensate for reactance due to the unusual geometry of the lines.
Ultimately, this lab progressed smoothly and resulted in a greater understanding of power
transmission and phase shifting within high frequency circuits.

Hindsight:

I would have liked to learn more about the design of various power dividers, and even to have
fabricated my own design.  It would also have been beneficial to investigate a circuit designed
to produce an uneven power division.  However, I feel that this lab was extremely well designed
and that it was beneficial in reinforcing the foundations of high frequency design.

Reflection:

The most challenging aspects of this lab were not theoretical; on the contrary, the most
difficult portions were the actual fabrication of the circuits.  The circuits were created
from strips of copper tape which were layed on the substrate.  At the high temperatures needed
for soldering, the adhesive binding the tape to the substrate began to fail, making it difficult
to create good connections.  The greatest benefit of this lab was in designing the actual phase
shifting circuits, because this reinforced and demonstrated the concepts discussed in class.
I personally felt that my understanding of high frequency design considerations improved after
the completion of this lab.