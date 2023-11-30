# Copyright (c) The University of Edinburgh 2014
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
See grouping_alltoone.py
Only different is that this test give TestProducer a stateful property
"""

from dispel4py.examples.graph_testing import testing_PEs as t
from dispel4py.workflow_graph import WorkflowGraph


def testAlltoOne():
    """
    Creates a graph with two consumer nodes and a global grouping.

    :rtype: the created graph
    """
    graph = WorkflowGraph()
    prod = t.TestProducer()
    prod.numprocesses = 1
    prod.stateful = "nature"
    cons1 = t.TestOneInOneOut()
    cons2 = t.TestOneInOneOut()
    cons1.numprocesses = 5
    cons2.numprocesses = 5
    graph.connect(prod, "output", cons1, "input")
    cons2.inputconnections["input"]["grouping"] = "global"
    graph.connect(cons1, "output", cons2, "input")
    return graph


""" important: this is the graph_variable """
graph = testAlltoOne()
