# Manufacturing KPI Calculator

## Overview

The Manufacturing KPI Calculator is a simple web-based tool designed to help users calculate key performance indicators (KPIs) commonly used in manufacturing and business analysis. These metrics allow engineers, managers, and analysts to evaluate production efficiency, equipment performance, and business profitability.

The application provides an easy-to-use interface where users can input operational data and instantly calculate important performance metrics.

This project was developed as a demonstration of how manufacturing metrics can be analysed using a lightweight web application.

---

## Features

### Manufacturing KPIs

The manufacturing section allows users to calculate important production metrics:

**First Pass Yield (FPY)**
Measures the proportion of products that are manufactured correctly without requiring rework.

Formula:
FPY = Good Units / Total Units

**Overall Equipment Effectiveness (OEE)**
Evaluates the efficiency of manufacturing equipment by combining three factors:

* Availability
* Performance
* Quality

Formula:
OEE = Availability × Performance × Quality

---

### Business KPIs

The business section includes financial performance indicators:

**Return on Investment (ROI)**
Measures how profitable an investment is relative to its cost.

Formula:
ROI = Net Profit / Investment

**Revenue Growth**
Measures the rate at which revenue increases over time.

Formula:
Revenue Growth = (Current Revenue − Previous Revenue) / Previous Revenue

---

## Technology Stack

This project was built using:

* **Python**
* **Flask** – Web framework for handling routes and backend logic
* **HTML** – Structure of the web pages
* **CSS** – Basic styling and layout
* **Jinja2** – Template rendering within Flask

---

## Project Structure

```
project/
│
├── app.py
│
├── templates/
│   ├── index.html
│   ├── productionquality.html
│   └── business.html
│
└── static/
    └── (optional CSS files)
```

---

## Installation

1. Clone the repository

```
git clone https://github.com/yourusername/manufacturing-kpi-calculator.git
```

2. Navigate to the project directory

```
cd manufacturing-kpi-calculator
```

3. Install Flask

```
pip install flask
```

4. Run the application

```
python app.py
```

---

## Usage

1. Open a browser and go to:

```
http://127.0.0.1:5000
```

2. Navigate to the desired section:

* Manufacturing KPIs
* Business KPIs

3. Enter the required values and click **Calculate** to view the result.

---

## Purpose of the Project

This project demonstrates:

* Basic web application development using Flask
* Implementation of manufacturing performance metrics
* Integration of backend calculations with frontend user interfaces

It is intended as a learning project and a demonstration of applying engineering concepts within a simple web tool.

---

## Possible Future Improvements

Potential enhancements include:

* Additional manufacturing KPIs (Cycle Time, Throughput, Scrap Rate)
* Graphical dashboards for KPI visualization
* Data storage for tracking historical performance
* Improved UI design and responsiveness
* Input validation and error handling

---

## License

This project is intended for educational purposes and personal learning.

