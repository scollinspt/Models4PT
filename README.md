# Models4PT

**Models4PT** 

Built on the cytoscape.js framework (see below)

---

## **About Models4PT**

Models4PT will be a dynamic tool for creating and analyzing graphical causal models tailored to the needs of physical therapy clinicians and researchers. It integrates into the Clinical Inquiry Network, which seeks to enhance clinical reasoning, causal modeling, and evidence-informed practice in physical therapy. This initiative includes:

1. **Stats4PT**:  
   A statistical education and guidance platform for physical therapy.  
   [Learn more here](https://peripateticpt.substack.com/p/welcome-to-stats4pt).

2. **The Clinical Inquiry Fellowship**:  
   A program for advancing clinical reasoning and critical inquiry in PT practice.  
   [Learn more here](https://peripateticpt.substack.com/p/clinical-inquiry-fellowship).

3. **Collaborative Tools**:  
   A suite of resources to model complex patient cases, integrate research findings, and explore clinical reasoning frameworks.

---

## **Enhancements in Progress**

### **Transition to a PT-Focused Tool**
- Adapting the platform to address physical therapy-specific use cases.
- Adding customizable templates and libraries for common PT causal models.

### **Integration of Bhaskar’s Critical Realist Framework**
- Explicit modeling of the **empirical, actual, and real domains** in causal modeling.
- Support for latent variables and deeper structural analysis (including hierarchical models - see below).

### **Expanded Inference Methodologies**
To support comprehensive clinical reasoning, Models4PT will integrate options for probabilistic causal inference models, including:
1. **Induction (Statistical Inference)**:  
   - Analyzing patterns and generalizations from data to support clinical decisions.
2. **Deduction (Probability Logic)**:  
   - Exploring deterministic and probabilistic relationships between variables.
3. **Abduction (Bayesian Inference)**:  
   - Generating hypotheses and evaluating their likelihood using Bayesian methods.

### **Improved User Experience**
- Enhanced saving/loading functionality using local storage and, eventually, backend storage for collaborative workflows.
- Streamlined interfaces for creating, modifying, and exporting models.

### **Planned Extensions**
1. Hosting the platform at **models4pt.com** to provide a publicly accessible, PT-centric tool.
2. Adding features to:
   - Identify and visualize confounders relevant to PT interventions and research.
   - Automate suggestions for evidence-based adjustments to causal models.
3. Integration into broader clinical reasoning education and consulting services.

### Hierarchical Model Support

Models4PT is preparing to support hierarchical causal models. This functionality will allow nodes to reference submodels, enabling multilevel causal reasoning and integration of critical realist perspectives.

**Key Objectives**:
- Extend variable metadata to include submodel references.
- Prepare the backend database for hierarchical relationships.
- Ensure algorithms like adjustment set calculation and d-separation are hierarchy-ready.
- Add placeholders in the interface for hierarchical metadata.

**Future Goals**:
This feature will support advanced use cases, including nested causal systems and multilevel analyses, while preserving compatibility with current core functionality.

---

## **Running the GUI Locally**

To test or use the current version of Models4PT locally:
1. Clone the repository.
2. Open `gui/dags.html` in a modern web browser.
3. Follow the instructions in the GUI for saving/loading models.

---
## Credits & Attribution

This project integrates [Cytoscape.js](https://js.cytoscape.org/) for interactive neuromechanical modeling and visualization.  
It also utilizes the following Cytoscape.js extensions:  
- [cytoscape-dagre](https://github.com/cytoscape/cytoscape.js-dagre) (for hierarchical layouts)  
- [cytoscape-cola](https://github.com/cytoscape/cytoscape.js-cola) (for force-directed graph layout)  

Cytoscape.js is developed by the [Cytoscape Consortium](https://cytoscape.org/) and licensed under the [MIT License](https://github.com/cytoscape/cytoscape.js/blob/master/LICENSE).  

---

## **Contact**

For questions about this project or collaboration opportunities, please contact:
- **Sean Collins, PT, ScD**  
  [Peripatetic PT](https://peripateticpt.substack.com/)  
  [Stats4PT](https://peripateticpt.substack.com/p/welcome-to-stats4pt)  
  [Clinical Inquiry Fellowship](https://peripateticpt.substack.com/p/clinical-inquiry-fellowship)  

  Updated as of January 21, 2025
