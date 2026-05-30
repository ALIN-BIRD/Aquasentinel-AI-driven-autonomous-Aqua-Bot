# AquaSentinel: Autonomous Water Quality Hub 🌊

**🏆 Awarded Best Hardware Implementation out of 30+ Engineering Groups**

An Edge-AI enabled, real-time autonomous water quality monitoring, evaluation, and mitigation system built on the Raspberry Pi Pico W.

## 🚀 Features
* **Multi-Sensor Data Fusion Matrix:** Evaluates pH, Turbidity, Dissolved Oxygen (DO), Temperature, and Water Level simultaneously.
* **Edge-AI Soft Inference Logic:** Executes local forward-propagation math using a neural network weight matrix entirely on-chip to assess contamination risk factors.
* **Automated Closed-Loop Mitigation:** Triggers dual-channel isolated optocoupler relays to engage industrial purge and aeration pumps when parameter boundary anomalies are logged.
* **Failsafe System Guard Watchdog:** Monitors hardware lines; if a probe is physically disconnected or fails, the core system enters a hard safety lockout state within 5 seconds to protect the actuators.
* **Remote Alerting Pipelines:** Integrates with SMTP endpoints via lightweight network sockets to dispatch instantaneous hazard updates to administrative control screens.

## 🗺️ Pin Mappings & Architecture

| Module Component | Microcontroller Pin (RP2040) | Interface Type |
| :--- | :--- | :--- |
| **I2C OLED Display (SSD1306)** | GP0 (SDA), GP1 (SCL) | I2C Port 0 |
| **Water Purge Pump Relay** | GP15 | Digital Output |
| **Air Aerator Pump Relay** | GP14 | Digital Output |
| **System Alert Buzzer** | GP13 | PWM Tone Output |
| **Ultrasonic Depth Sensor** | GP17 (Trig), GP18 (Echo) | Pulse timing input |
| **Analog pH Sensor Module** | GP26 | ADC Channel 0 |
| **Analog Turbidity Sensor** | GP27 | ADC Channel 1 |
| **Analog Dissolved Oxygen (DO)** | GP28 | ADC Channel 2 |
| **DS18B20 Temp Sensor** | GP21 | OneWire Protocol |

## 🛠️ Software Stack
* **Language:** MicroPython
* **Core Libraries:** `machine`, `network`, `usocket`, `ubinascii`, `onewire`, `ds18b20`
