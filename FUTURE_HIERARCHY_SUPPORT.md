# Future Hierarchy Support in Models4PT

## Overview

Models4PT aims to integrate advanced causal modeling functionality, including support for hierarchical models. Hierarchical models will allow nodes to represent submodels, enabling multilevel causal reasoning and critical realist perspectives.

This document outlines the plans for preparing the backend, metadata, and algorithms to support hierarchy while deferring the front-end implementation to a later stage.

---

## Current Plan

### 1. **Extend Metadata for Variables**
- **Objective**: Prepare variables (nodes) to store references to submodels.
- **Implementation**:
  - Add a `submodel` property to variable definitions.
  - Example:
    ```javascript
    const node = {
        id: "Node1",
        type: "exposure",
        domain: "empirical",
        submodel: null // or an ID like "subModelA"
    };
    ```

---

### 2. **Prepare Backend Database**
- **Objective**: Enable the database to store hierarchical relationships between models.
- **Schema Design**:
  - **Models Table**:
    - `model_id`: Primary key for the model.
    - `model_data`: Serialized model data (JSON).
  - **Hierarchy Table**:
    - `parent_id`: ID of the parent model.
    - `child_id`: ID of the submodel.

---

### 3. **Adapt Algorithms**
- **Objective**: Ensure core algorithms can handle hierarchical models.
- **Initial Approach**:
  - Update algorithms for adjustment sets, d-separation, and path analyses to recognize hierarchical relationships.
  - Example: Skip or log submodels in initial implementation.
  - Use recursive logic for future expandability.

---

### 4. **Front-End Placeholders**
- **Objective**: Add placeholders in the interface for hierarchical metadata without implementing full functionality.
- **Details**:
  - Display submodel references when showing variable metadata.
  - Example:
    ```javascript
    function displayVariableInfo(node) {
        console.log("Variable ID:", node.id);
        console.log("Domain:", node.domain);
        if (node.submodel) {
            console.log("This node references a submodel:", node.submodel);
        }
    }
    ```

---

### 5. **Document the Hierarchy Logic**
- **Objective**: Provide a clear roadmap for how hierarchy will function in the future.
- **Key Considerations**:
  - Interaction of submodels with:
    - Adjustment sets.
    - Path analyses.
    - Bias and causal effects.
  - Data flow between parent and submodels.

---

## Benefits of This Approach

- **Future-Proofing**: Core systems are designed to support hierarchy without delaying current development.
- **Incremental Development**: Enables focus on core features while laying the groundwork for hierarchy.
- **Minimal Rework**: Reduces effort when hierarchy functionality is added in future phases.

---

## Next Steps

1. **Update Variable Data Structure**:
   - Add the `submodel` property to node definitions.
2. **Plan the Database Schema**:
   - Design and document tables for models and hierarchical relationships.
3. **Algorithm Assessment**:
   - Identify algorithms needing updates for hierarchy support.
4. **Front-End Preparation**:
   - Add placeholders for submodel metadata in the interface.