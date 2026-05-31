# ImpactIQ

## Multi-Agent AI-Powered Enterprise Change Intelligence Platform

ImpactIQ is an AI-powered platform that helps organizations evaluate enterprise change requests by analyzing business impact, assessing risks, identifying system dependencies, and generating executive-ready reports.

The platform leverages multiple AI agents to provide intelligent decision support before implementing organizational or technical changes.

---

## Features

### Multi-Agent Intelligence

* Impact Analysis Agent
* Risk Assessment Agent
* Training Recommendation Agent
* Risk Scoring Agent

### Enterprise Change Analysis

* Business Impact Analysis
* Technical Impact Assessment
* Risk Prediction
* Dependency Mapping

### Visualization

* Dependency Graph Visualization
* Impact Dashboard
* Risk Metrics

### Reporting

* Executive Summary Generation
* PDF Report Export
* Risk Intelligence Dashboard

### Knowledge Management

* Historical Change Memory
* Similar Change Retrieval
* Context-Aware Recommendations

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Components

* Multi-Agent Architecture
* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)

### Visualization

* NetworkX
* Matplotlib

### Storage

* JSON
* FAISS Vector Store

### Reporting

* PDF Generation

---

## System Workflow

1. User submits a change request.
2. Historical enterprise changes are retrieved.
3. AI agents perform impact and risk analysis.
4. Dependency relationships are identified.
5. Risk score is calculated.
6. Executive summary is generated.
7. PDF report is exported.

---

## Key Capabilities

* Enterprise Change Impact Analysis
* Risk Assessment and Scoring
* Dependency Analysis
* AI-Powered Recommendations
* Executive Reporting
* Change Intelligence Dashboard

---

## Project Structure

```text
AI-CHANGE-IMPACT-ANALYZER/
│
├── backend/
│   ├── graph_engine.py
│   ├── llm_client.py
│   ├── pdf_generator.py
│   ├── rag_store.py
│   └── risk_engine.py
│
├── pages/
│   ├── Landing.py
│   ├── Login.py
│   ├── Register.py
│   └── Dashboard.py
│
├── vectorstore/
├── data/
├── app.py
├── agents.py
├── requirements.txt
└── README.md
```

---

## Installation

```bash
git clone <repository-url>
cd ImpactIQ

pip install -r requirements.txt
streamlit run app.py
```

---

## Future Enhancements

* Real-Time Monitoring
* Interactive Knowledge Graph
* Enterprise API Integration
* Cloud Deployment Support
* Role-Based Access Control
* Advanced Analytics Dashboard

---

## Author

**Poojashri D**

---

## Project Title

**ImpactIQ: A Multi-Agent AI-Powered Enterprise Change Intelligence Platform for Risk Assessment, Impact Analysis, Dependency Mapping, and Decision Support**
