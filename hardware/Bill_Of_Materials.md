# Bill of Materials (BOM): AquaSentinel Node Hardware Matrix

This document provides a comprehensive component breakdown for the award-winning AquaSentinel localized Industrial IoT (IIoT) edge node deployment. 

---

## 1. Core Processing & User Interface Layer

| Component Item | Description | Operational Role | Qty | Estimated Cost (INR) |
| :--- | :--- | :--- | :--- | :--- |
| **Raspberry Pi Pico W** | Dual-core ARM Cortex-M0+ microcontroller @ 133MHz, 2MB onboard Flash, integrated CYW43439 2.4GHz Wi-Fi module. | Main execution core hosting the localized embedded machine learning weights, watchdog timers, and background networking threads. | 1 | ₹650 |
| **SSD1306 I2C OLED Display** | 0.96-inch monochrome display panel, 128x64 pixel matrix, driven via monospaced hexadecimal character mapping arrays. | Local Human-Machine Interface (HMI) tracking real-time sensor streams and local AI classification threat indices. | 1 | ₹250 |

---

## 2. Advanced Multi-Sensor Parameter Matrix

| Component Item | Description | Operational Role | Qty | Estimated Cost (INR) |
| :--- | :--- | :--- | :--- | :--- |
| **Analog pH Sensor Kit** | Probe assembly with onboard signal conditioning board (pH 0-14 tracking range, standard analog voltage mapping curve). | Measures chemical variations and boundary shifts to detect contamination or dangerous acidic/alkaline spikes. | 1 | ₹1,200 |
| **Analog Turbidity Sensor** | Photoelectric liquid clarity analyzer module (0V to 3.3V operational envelope corresponding to water muddiness). | Quantifies suspended particles and particulate suspension levels by assessing light transmission constraints. | 1 | ₹450 |
| **Analog Dissolved Oxygen (DO) Module** | Galvanic electrochemical DO sensing probe with signal-amplification circuit board. | Maps localized oxygen tension values to track environmental stability and oxygen depletion risk indexes. | 1 | ₹1,800 |
| **DS18B20 OneWire Temp Sensor** | Waterproof stainless steel probe housing utilizing a digital 1-Wire interface. | Feeds high-precision thermal profiles to the local AI optimization engine for background calibration parameters. | 1 | ₹150 |
| **HC-SR04 Ultrasonic Sensor** | Dual-transceiver ultrasonic distance measurement module tailored for fluid depth parameters. | Monitors target fluid surface elevation boundaries to flag storage overflow anomalies or low-volume pump depletion. | 1 | ₹120 |

---

## 3. Power Distribution & Closed-Loop Actuation Layer

| Component Item | Description | Operational Role | Qty | Estimated Cost (INR) |
| :--- | :--- | :--- | :--- | :--- |
| **2-Channel Relay Board** | 5V low-level trigger mechanical relay module featuring complete onboard optocoupler isolation arrays. | Electrically isolates the low-voltage RP2040 processing lines from high-voltage inductive pump transients. | 1 | ₹180 |
| **12V DC Fluid Purge Pump** | High-flow micro submersible inductive motor pump assembly. | Closed-loop hazard mitigation actuator tasked with flushing compromised volume contents out of the central tank. | 1 | ₹350 |
| **12V DC Water Aerator Pump** | Low-noise air-injection motor pump designed for localized oxygen enrichment. | Engages automatically when DO parameters slip past safe minimums to correct hypoxia. | 1 | ₹300 |
| **LM2596 Buck Converter** | High-efficiency step-down DC-DC switching voltage regulator module. | Scales external 12V battery inputs down to stable 5V rails to feed the microcontroller and display circuits. | 1 | ₹110 |
| **Piezoelectric Active Buzzer** | Standard 5V high-frequency audible alarm element mapped to a dedicated hardware PWM channel. | Generates pulsed alarm frequencies locally during anomalous hazard triggers or watchdog sensor disconnect faults. | 1 | ₹30 |
| **Miscellaneous Lab Assets** | Premium solderless breadboards, solid-core jumper wires, 1N4007 flyback suppression diodes, and terminal blocks. | Secures electrical continuity across modular hardware nodes. | - | ₹200 |

---

## 📊 Summary of Implementation Logistics
* **Total Discovered Components:** 11 active subsystems
* **Aggregated Prototyping Cost:** ~₹5,800
* **System Power Profiling:** Dual-rail infrastructure (12V DC for active inductive pump loads / 5V DC step-down for digital sensor logic processing paths).