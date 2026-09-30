# CS661 - Big Data Visual Analytics  
## Social Media Engagement Pattern Visualization and Starbucks Customer Segmentation

### Project Overview

This project presents a visualization-based analysis of long-term social media engagement patterns using a large-scale Facebook dataset containing religious posts. The system explores how user interaction changes over time through interactive visual analytics built with D3.js and processed using big data tools.

The project focuses on identifying engagement behavior, temporal trends, and comparative performance across categories using metrics such as likes, comments, and shares.

### Live Demo

https://socialmediaengagementpattern.netlify.app

---

## Features

- Analysis of Facebook post engagement data from 2010 to 2020
- Interactive visualizations for:
  - Likes
  - Comments
  - Shares
- Time-series analysis of engagement activity
- Comparative category-based analysis
- Exploratory visual analytics using D3.js
- Big data preprocessing using PySpark

---

## Technology Stack

| Layer | Technologies |
|-------|--------------|
| Frontend | HTML, CSS, JavaScript |
| Visualization | D3.js v7 |
| Data Processing | Python, PySpark |
| Hosting | Netlify |

---

## Dataset Information

- Source: Public Facebook religious post dataset
- Dataset Size: Approximately 400,000 records
- Fields Used:
  - Post Type
  - Posted Date
  - Likes
  - Comments
  - Shares
  - Page Category

---

## Visualization Modules

### Engagement Over Time
Displays interaction trends across multiple years using time-series visualizations.

### Category Comparison
Compares engagement metrics between different page categories.

### Temporal Analysis
Examines periodic spikes and behavioral changes in engagement activity.

---

## Project Structure

```bash
socialmediaengagement/
│
├── data/                 # Dataset files
├── scripts/              # Python and PySpark preprocessing scripts
├── visualizations/       # D3.js visualization modules
├── index.html            # Main application entry
├── style.css             # Styling files
├── app.js                # Visualization logic
└── README.md
