
### **Reflection Summary (Brief)**

*   **Methods:** We used **IQR** for its robustness to skewed data and **Z-score** for its statistical basis, with standard thresholds (`1.5*IQR`, `z > 3`). Outliers were handled by **filtering** (removal) and **winsorizing** (capping) to compare strategies.

*   **Assumptions:** We assumed that outliers were likely noise that distorted the underlying data trend. The Z-score method further assumes the data is roughly normal (we actually didn't use it), which is a strong assumption for financial returns.

*   **Impact:** Removing or capping outliers significantly impacted model performance. The regression model on original data showed a more accurate **slope**, a higher **R²**, and lower **error**, demonstrating that outliers were not actually influencing the results. On the contrary, the filtered and winsorized datasets showed degraded performance, indicating that the outliers were not just noise but contained valuable information.

*   **Risks:** The primary risk is **mistaking a true, extreme market event for an error**. By removing it, our model becomes blind to "tail risk" and may be unreliable during market stress.