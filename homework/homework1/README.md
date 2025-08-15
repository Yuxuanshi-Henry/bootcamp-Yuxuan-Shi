# Credit Card Fraud Detection Optimization  
**Stage:** Problem Framing & Scoping (Stage 01)  

### Problem Statement  
Reduce undetected fraudulent transactions while maintaining acceptable false positive rates for cardholders. Most systems miss new fraud patterns, causing financial losses.

### Stakeholder & User  
- **Stakeholder:** VP
- **User:** Fraud Operations Team
- **Decision Window:** Model updates quarterly; transaction decisions in real-time.  

### Useful Answer & Decision  
- **Type:** Predictive  
- **Artifact:** Fraud probability score per transaction
- **Decision Trigger:** Block transaction if probability > threshold

### Assumptions & Constraints  
- Fraud patterns stable within updating cycles
- Data available: 3 months historical transactions (easy to get for investment banks)
- Max 1s added latency for scoring
- Systematic volatility stays stable within updating cycles

### Known Unknowns / Risks  
- Model instability with new fraud patterns
- Data gaps in cross-border transactions
- Concept drift over time

### Lifecycle Mapping  
| Goal → Stage → Deliverable |  
|----------------------------|  
| Define fraud detection gap → Stage 01 → This scoping doc |

### Repo Plan  
Folders: /data/, /src/, /notebooks/, /docs/  
Updates: Weekly commits  