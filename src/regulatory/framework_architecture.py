from graphviz import Digraph

dot = Digraph(
    comment='XDLF Architecture',
    format='png'
)

# Global style
dot.attr(rankdir='TB')
dot.attr('graph',
         bgcolor='white',
         ranksep='0.7',
         nodesep='0.5',
         fontsize='20',
         fontname='Arial')

dot.attr('node',
         shape='box',
         style='rounded,filled',
         fontname='Arial',
         fontsize='14',
         width='3')

# =====================================================
# INPUT
# =====================================================

dot.node(
    'A',
    'Borrower Application Data',
    fillcolor='#D6EAF8'
)

# =====================================================
# PREPROCESSING
# =====================================================

dot.node(
    'B',
    'Data Preprocessing\n'
    '• Cleaning\n'
    '• Encoding\n'
    '• Feature Engineering',
    fillcolor='#D5F5E3'
)

# =====================================================
# MACHINE LEARNING
# =====================================================

with dot.subgraph(name='cluster_ml') as c:

    c.attr(
        label='Machine Learning Layer',
        style='rounded',
        color='gray'
    )

    c.node(
        'LR',
        'Logistic\nRegression',
        fillcolor='#FCF3CF'
    )

    c.node(
        'DT',
        'Decision\nTree',
        fillcolor='#FCF3CF'
    )

    c.node(
        'RF',
        'Random\nForest',
        fillcolor='#FCF3CF'
    )

    c.attr(rank='same')

# =====================================================
# DECISION
# =====================================================

dot.node(
    'D',
    'Loan Decision Engine',
    fillcolor='#FADBD8'
)

# =====================================================
# EXPLAINABILITY
# =====================================================

dot.node(
    'SHAP',
    'SHAP\nGlobal + Local\nExplanation',
    fillcolor='#D4E6F1'
)

dot.node(
    'LIME',
    'LIME\nLocal\nExplanation',
    fillcolor='#D4E6F1'
)

dot.node(
    'EXP',
    'Explainability Layer',
    fillcolor='#D6DBDF'
)

# =====================================================
# FAIRNESS
# =====================================================

dot.node(
    'FAIR',
    'Fairness Assessment\n'
    'SPD | DIR | Bias Metrics',
    fillcolor='#D5F5E3'
)

# =====================================================
# COMPLIANCE
# =====================================================

dot.node(
    'COMP',
    'Regulatory Compliance Engine',
    fillcolor='#F9E79F'
)

# =====================================================
# AUDIT
# =====================================================

dot.node(
    'AUDIT',
    'AI Audit Engine',
    fillcolor='#F5CBA7'
)

# =====================================================
# DASHBOARD
# =====================================================

dot.node(
    'DASH',
    'Governance Dashboard',
    fillcolor='#D7BDE2'
)

# =====================================================
# RBI
# =====================================================

dot.node(
    'RBI',
    'RBI Digital Lending\nCompliance',
    fillcolor='#AED6F1'
)

# =====================================================
# EDGES
# =====================================================

dot.edge('A', 'B')

dot.edge('B', 'LR')
dot.edge('B', 'DT')
dot.edge('B', 'RF')

dot.edge('LR', 'D')
dot.edge('DT', 'D')
dot.edge('RF', 'D')

dot.edge('D', 'SHAP')
dot.edge('D', 'LIME')

dot.edge('SHAP', 'EXP')
dot.edge('LIME', 'EXP')

dot.edge('EXP', 'FAIR')
dot.edge('FAIR', 'COMP')
dot.edge('COMP', 'AUDIT')
dot.edge('AUDIT', 'DASH')
dot.edge('DASH', 'RBI')

# =====================================================
# SAVE
# =====================================================

dot.render(
    'outputs/figures/framework_architecture',
    cleanup=True
)

print("\nFramework architecture saved.")