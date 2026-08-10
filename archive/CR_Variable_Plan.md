# Models4PT Critical Realism Variable Plan

## Overview
This document outlines the integration of Bhaskar's critical realism domains into the variable metadata system for Models4PT, while maintaining and enhancing DAGitty’s core functionalities such as exposure, outcome, adjusted, selected, and unobserved variables.

## Key Concepts
1. **Bhaskar's Domains**:
    - **Empirical**: Observable and measurable variables.
    - **Actual**: Events that occur but are not necessarily observed.
    - **Real**: Underlying mechanisms or structures that generate events.

2. **Existing DAGitty Categories**:
    - **Exposure**: Variables marked as causes.
    - **Outcome**: Variables marked as effects.
    - **Adjusted**: Variables adjusted for in analysis.
    - **Selected**: Variables marked as selected.
    - **Unobserved**: Variables considered latent or not directly measured.

## Variable Metadata Structure
Each variable in Models4PT will include:
- **Domain**: Empirical, Actual, or Real.
- **Function**: Cause (exposure), Effect (outcome), Adjusted, Selected, or Unobserved.

## Plan for Implementation
### Phase 1: Metadata Framework
1. Add a `domain` property to nodes with three possible values: `Empirical`, `Actual`, or `Real`.
2. Retain existing categories (`Exposure`, `Outcome`, etc.) and ensure they remain functional with DAGitty's algorithms.
3. Update the graphical interface to allow assignment of both domain and function metadata for each variable.

### Phase 2: GUI Enhancements
1. Modify the **Variable Properties Panel** to include:
    - Domain selection (dropdown menu).
    - Function assignment (checkboxes or toggles).
2. Adjust the coloring logic to visually represent both domain and function:
    - Example: Color nodes based on domain (Empirical, Actual, Real) with additional markers for functions like exposure or outcome.

### Phase 3: Algorithm Adjustments
1. Update adjustment set and testable implication algorithms to respect the new metadata:
    - Allow algorithms to handle variables across domains and their implications on causal paths.
2. Ensure backward compatibility with existing DAGitty features.

### Phase 4: Database and Backend Preparation
1. Design database schema to store domain and function metadata for variables.
2. Allow for retrieval of models with these new properties for analysis and visualization.

### Phase 5: Documentation and Education
1. Update user documentation to explain the new variable metadata and its significance in critical realism.
2. Provide examples demonstrating how to utilize these features in clinical and research contexts.

## Future Considerations
1. **Dynamic Domain Assignment**:
    - Incorporate rules or machine-learning approaches to suggest domains based on data or context.
2. **Hierarchy and Submodels**:
    - Ensure the new metadata system integrates seamlessly with future plans for hierarchical modeling.
3. **Interactive Visualizations**:
    - Enable users to toggle between different domain representations and analyze implications.

## Summary
Integrating Bhaskar’s critical realism domains into Models4PT enhances its capacity to model complex causal structures while retaining the core functionalities of DAGitty. This structured plan ensures that new features are robust, intuitive, and valuable for clinical research.