# Electrical engineering coursework

Course notes and original study examples organized around electrical engineering at Toronto Metropolitan University.

Start with [circuit analysis](courses/ELE202/), [electronic circuits](courses/ELE404/), [digital systems](courses/COE328/), or [software systems](courses/COE318/). The [Python examples](examples/) calculate resistor-divider loading and the response of an ideal RC low-pass filter.

Each course page links to an official TMU course description. The examples were prepared for this repository; they are study illustrations rather than submitted assignments or measured hardware results.

## Circuits, electronics, and digital design

| Course | Subject |
| --- | --- |
| [ELE 202](courses/ELE202/) | Electric Circuit Analysis |
| [ELE 302](courses/ELE302/) | Electric Networks |
| [ELE 401](courses/ELE401/) | Electric and Magnetic Fields |
| [ELE 404](courses/ELE404/) | Electronic Circuits I |
| [COE 328](courses/COE328/) | Digital Systems |

## Programming and software

| Course | Subject |
| --- | --- |
| [COE 318](courses/COE318/) | Software Systems |
| [COE 428](courses/COE428/) | Engineering Algorithms and Data Structures |
| [CPS 118](courses/CPS118/) | Introductory Programming for Scientists |
| [CPS 188](courses/CPS188/) | Computer Programming Fundamentals |

## Mathematics

| Course | Subject |
| --- | --- |
| [MTH 110](courses/MTH110/) | Discrete Mathematics I |
| [MTH 140](courses/MTH140/) | Calculus I |
| [MTH 141](courses/MTH141/) | Linear Algebra |
| [MTH 240](courses/MTH240/) | Calculus II |
| [MTH 312](courses/MTH312/) | Differential Equations and Vector Calculus |
| [MTH 314](courses/MTH314/) | Discrete Mathematics for Engineers |

## Physics, chemistry, and materials

| Course | Subject |
| --- | --- |
| [PCS 125](courses/PCS125/) | Physics: Waves and Fields |
| [PCS 211](courses/PCS211/) | Physics: Mechanics |
| [PCS 224](courses/PCS224/) | Solid State Physics |
| [CHY 102](courses/CHY102/) | General Chemistry |
| [MTL 200](courses/MTL200/) | Materials Science Fundamentals |

## Engineering practice and economics

| Course | Subject |
| --- | --- |
| [CEN 100](courses/CEN100/) | Introduction to Engineering |
| [CEN 800](courses/CEN800/) | Law and Ethics in Engineering Practice |
| [CMN 432](courses/CMN432/) | Communication in the Engineering Professions |
| [ECN 801](courses/ECN801/) | Principles of Engineering Economics |
| [ECN 440](courses/ECN440/) | Economic Issues in Financial Markets |

## Run the circuit examples

The calculations use the Python standard library. From the repository root:

```bash
python examples/circuits.py
```

The example README explains the equations, units, model assumptions, and test commands. [courses.json](courses.json) provides the course catalog as structured data.
