"""Focused correctness checks for the curated CSP and probabilistic routines.

Run from the repository root: python verify_algorithms.py
Loads definitions from notebooks without running their large experiments.
"""
import ast
import itertools
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent

def definitions(path, namespace):
    for cell in json.loads(path.read_text())['cells']:
        if cell['cell_type'] != 'code': continue
        tree = ast.parse(''.join(cell['source']))
        tree.body = [n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.ClassDef,ast.Import,ast.ImportFrom))]
        exec(compile(tree,str(path),'exec'),namespace)

def clues(line):
    groups=[];count=0
    for v in list(line)+[0]:
        if v:count+=1
        elif count:groups.append(count);count=0
    return tuple(groups)

def check_csp():
    folder = ROOT/'notebooks/03_constraint_solving'
    sys.path.insert(0,str(folder))
    ns={}
    definitions(folder/'nonogram_csp_solver_comparison.ipynb',ns)
    options=[(),(1,),(2,)]
    solver_pairs=[('solve_baseline','ValuesState'),('solve_forward_check','DomainValuesState'),('solve_mrv','MRVState'),('solve_ac3_mrv','MRVState')]
    for specification in itertools.product(options,repeat=4):
        rows=specification[:2];cols=specification[2:]
        expected=False
        for bits in itertools.product([0,1],repeat=4):
            a=np.array(bits).reshape(2,2)
            if all(clues(a[i])==rows[i] and clues(a[:,i])==cols[i] for i in range(2)):
                expected=True;break
        for solver,state_class in solver_pairs:
            csp=ns['build_nonogram_csp'](rows,cols)
            state=ns[state_class](csp)
            result=ns[solver](csp,state,ns['StepLogger']())
            assert result==expected,(solver,specification,result,expected)
            if result:
                assert all(clues(state.assignment[i])==rows[i] and clues(state.assignment[:,i])==cols[i] for i in range(2))
            if hasattr(state,'num_remaining_values'):
                assert all(state.num_remaining_values[c]==len(state.domains[c]) for c in csp.variables)
    print('PASS: 324 CSP checks across all 81 two-by-two clue combinations; solutions and MRV counts verified.')

def check_bayes():
    p=ROOT/'notebooks/04_probabilistic_reasoning/bayesian_network_inference_and_decisions.ipynb'
    cells=json.loads(p.read_text())['cells'];ns={}
    for c in cells:
        if c['cell_type']=='code' and 'NETWORK_CPTS = {' in ''.join(c['source']):exec(''.join(c['source']),ns)
    definitions(p,ns)
    assignments=[dict(zip(ns['VARIABLES'],bits)) for bits in itertools.product([False,True],repeat=6)]
    assert np.isclose(sum(ns['joint_probability'](a) for a in assignments),1)
    for query in ns['VARIABLES']:
        for evidence_var in ns['VARIABLES']:
            if evidence_var==query:continue
            for val in (False,True):
                ev={evidence_var:val}
                selected=[a for a in assignments if a[evidence_var]==val]
                expected=sum(ns['joint_probability'](a) for a in selected if a[query])/sum(ns['joint_probability'](a) for a in selected)
                assert np.isclose(ns['exact_posterior'](query,ev),expected)
    print('PASS: joint normalization and 60 posterior queries checked against direct joint sums.')

if __name__=='__main__':
    check_csp()
    check_bayes()
