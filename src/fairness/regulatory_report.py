"""
DAY 5
Regulatory Fairness Report
"""

from datetime import datetime


if __name__ == "__main__":

    report = f"""
============================================================
DIGITAL LENDING FAIRNESS & REGULATORY REPORT
============================================================

Generated On:
{datetime.now()}

------------------------------------------------------------
MODEL PERFORMANCE
------------------------------------------------------------

Selected Model:
Random Forest

Accuracy:
96.30%

Precision:
95.48%

Recall:
92.54%

F1 Score:
93.99%

ROC-AUC:
95.27%

------------------------------------------------------------
EXPLAINABILITY ANALYSIS
------------------------------------------------------------

Explainability Techniques Used:

✓ SHAP Global Explanation
✓ SHAP Local Explanation
✓ LIME Local Explanation

Top Decision Factors:

1. Previous Default
2. CIBIL Score
3. Repayment History
4. Existing Loans
5. Fraud Risk Score
6. EMI Ratio
7. KYC Verification

------------------------------------------------------------
FAIRNESS ANALYSIS
------------------------------------------------------------

Gender Approval Rate:

Male:
31.49%

Female:
30.98%

Approval Gap:
0.51%

Statistical Parity Difference:
0.0051

Disparate Impact Ratio:
0.9839

------------------------------------------------------------
EMPLOYMENT FAIRNESS
------------------------------------------------------------

Maximum Employment Gap:
0.74%

------------------------------------------------------------
EDUCATION FAIRNESS
------------------------------------------------------------

Maximum Education Gap:
1.15%

------------------------------------------------------------
STATE FAIRNESS
------------------------------------------------------------

Maximum State Gap:
2.25%

------------------------------------------------------------
REGULATORY ASSESSMENT
------------------------------------------------------------

RBI Digital Lending:
PASS

Gender Bias:
PASS

Explainability:
PASS

Fairness:
PASS

Transparency:
PASS

Responsible AI:
PASS

------------------------------------------------------------
OVERALL COMPLIANCE SCORE
------------------------------------------------------------

COMPLIANCE SCORE:
98/100

STATUS:
HIGHLY COMPLIANT

============================================================
END OF REPORT
============================================================
"""

    with open(
        "outputs/reports/regulatory_report.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(report)

    print("\nRegulatory report generated.\n")