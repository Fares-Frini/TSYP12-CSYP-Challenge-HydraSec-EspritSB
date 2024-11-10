<p align="center">
  <a href="" rel="noopener">
 <img src="images/tsyp_img1.png" alt="Project logo"></a>
</p>
<h3 align="center">HydraSec:</span> Empowering Cyber Defense with Intelligent Swarm Protection.
</h3>
<p align="center">
  <img src="images/logo_cs.png" alt="Project logo" width="200">
</p>

<div align="center">
</div>
---

<p align=""><i> <span style="color: #ff4500;">HydraSec</span> is an AI-powered cybersecurity solution utilizing a swarm-based defense approach, leveraging a microservices architecture with Docker and Kubernetes to deliver scalable, adaptive, and real-time threat detection and mitigation across diverse data sources.
    <br> <i>
</p>

## 📝 <span style="color: #007acc;">Table of Contents</span>
- [📚 <span style="color: #007acc;">Documentation</span>](#documentation)
- [💻 <span style="color: #007acc;">Interfaces</span>](#interfaces)
- [🛡️ <span style="color: #007acc;">SIEM</span>](#siem)
- [🛠️ <span style="color: #007acc;">Security_Tools</span>](#sectools)
- [🤖 <span style="color: #007acc;">AI_Models</span>](#ai_models)
- [⚙️ <span style="color: #007acc;">System d'Exploitations</span>](#sysexp)
- [🏗️ <span style="color: #007acc;">Architecture and Infrastructure</span>](#architecture_infrastructure)


## 📚 <span style="color: #007acc;">Documentation</span> <a name = "documentation"></a>
In this work, we have provided an in-depth exploration of the scientific aspects underpinning our solution, including comprehensive explanations of the employed AI models, their functioning, and the architectural design that supports them. [<span style="color: #ff4500;">Research_Paper</span>](https://github.com/Fares-Frini/TSYP12-CSYP-Challenge/tree/main/AI_Models)<br> Additionally, we documented the entire process through a detailed report that outlines how each model was trained, optimized, and evaluated. This report also features data visualizations and step-by-step breakdowns of the workflow, offering a transparent and thorough view of the methodologies and outcomes achieved in our implementation. [<span style="color: #ff4500;">Report</span>](https://github.com/Fares-Frini/TSYP12-CSYP-Challenge/tree/main/AI_Models)

## 💻 <span style="color: #007acc;">Interfaces</span> <a name = "interfaces"></a>
In our visualization efforts, we utilized the <span style="color: #007acc;">Grafana dashboard</span>, a flexible, user-friendly, and intuitive tool designed for displaying diverse data metrics. Grafana's capabilities allow for efficient monitoring and real-time alerting, providing deep insights into system health, security incidents, and various data streams. This enables streamlined data analysis, making it a crucial component for visualizing and understanding our models' outputs and system behavior. [<span style="color: #ff4500;">Here</span>](https://github.com/Fares-Frini/TSYP12-CSYP-Challenge/tree/main/Interfaces)

## 🛡️ <span style="color: #007acc;">SIEM</span> <a name = "siem"></a>
We leveraged <span style="color: #007acc;">Wazuh</span>, a Security Information and Event Management (SIEM) tool, to provide comprehensive security monitoring and threat detection. Wazuh's capabilities include log data aggregation, monitoring of system activity, and real-time alerting for potential threats. Its robust analysis tools enable the identification of security incidents, helping ensure system integrity and compliance. This integration enhances visibility across the infrastructure and supports rapid, data-driven decision-making to counter cyber threats effectively. [<span style="color: #ff4500;">Here</span>](https://github.com/Fares-Frini/TSYP12-CSYP-Challenge/tree/main/SIEM)

## 🛠️ <span style="color: #007acc;">Security Tools</span> <a name = "sectools"></a>
A key part of our solution is integrating with pre-existing tools and the broader cybersecurity ecosystem to ensure a coherent and resilient workflow. Tools such as <span style="color: #007acc;">Snort</span> play an essential role, offering network intrusion detection and prevention capabilities. By incorporating Snort, we enhance our ability to analyze network traffic, detect suspicious patterns, and generate alerts in real-time. This integration supports seamless interoperability with other components, strengthening overall security and fostering a unified, layered defense strategy. [<span style="color: #ff4500;">Here</span>](https://github.com/Fares-Frini/TSYP12-CSYP-Challenge/tree/main/Security_Tools)

## 🤖 <span style="color: #007acc;">AI_Models</span> <a name = "ai_models"></a>
We utilize advanced AI models to enhance cybersecurity detection and response. <span style="color: #007acc;">Reinforcement Learning</span> is applied for endpoint protection, allowing the system to learn and adapt dynamically to new threats. <span style="color: #007acc;">Generative Adversarial Networks (GANs)</span> are employed for malware generation and detection, improving the model's ability to recognize evolving threats. <span style="color: #007acc;">Long Short-Term Memory (LSTM)</span> networks analyze network traffic patterns, detecting anomalous activities in real-time.<br>Additionally, <span style="color: #007acc;">NLP with Data Augmentation</span> is used for phishing email detection, while <span style="color: #007acc;">Unsupervised Learning</span> aids in identifying IP profiling anomalies, enabling more effective threat identification without labeled data.
 [<span style="color: #ff4500;">Here</span>](https://github.com/Fares-Frini/TSYP12-CSYP-Challenge/tree/main/AI_Models)

## ⚙️ <span style="color: #007acc;">System d'Exploitations</span> <a name = "sysexp"></a>
To evaluate the efficiency of our solution, we conducted extensive testing using various <span style="color: #007acc;">Linux environments</span>. We employed <span style="color: #007acc;">Kali Linux</span> for simulating different types of cyberattacks due to its robust suite of penetration testing tools. Additionally, we utilized <span style="color: #007acc;">Metasploitable</span>, a deliberately vulnerable Linux machine, to simulate real-world attack scenarios. This testing approach allowed us to assess the system's detection and response capabilities comprehensively, ensuring robust performance against diverse threats in controlled conditions.
 [<span style="color: #ff4500;">Here</span>](https://github.com/Fares-Frini/TSYP12-CSYP-Challenge/tree/main/Ses)
 
 ## 🏗️<span style="color: #007acc;"> Architecture and Infrastructure</span>
  <a name = "architecture_infrastructure"></a>
 
 - Network Architecture :
  <img src="/images/architecture.png" alt="Architecture and Infrastructure" width="500" align="center">
  
- DMZ Architecture :
 <img src="/images/DMZ.png" alt="Architecture and Infrastructure" width="500" align="center">

| **Step**     | **Description**                                                                                                                                              |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1 + 2**    | Users gain access to **Elasticsearch** after successful authorization through **pfSense**.                                                                  |
| **3**        | **Wazuh** retrieves relevant data from the database server (**FreeNAS**).                                                                                   |
| **4**        | After analyzing the retrieved data, **Wazuh** communicates with **Grafana** to display visualized results.                                                  |
| **5**        | Concurrently, **Wazuh** sends data to the **Windows server**, which processes it using various AI models, including:                                        |
|              | • **Endpoints Protection** using Reinforcement Learning                                                                                                      |
|              | • **Malware Generation and Detection** with GAN                                                                                                             |
|              | • **Network Traffic Analysis** using LSTM                                                                                                                   |
|              | • **Phishing Mail Detection** through Data Augmentation and NLP                                                                                             |
|              | • **IP Profiling Detection** using Unsupervised Learning                                                                                                    |
| **6**        | If any anomalies or threats are detected, **Wazuh** responds by updating the **database server (FreeNAS)**.                                                 |
| **7**        | The detected anomalies are sent to **Grafana** for real-time visualization and monitoring.                                                                  |



 


