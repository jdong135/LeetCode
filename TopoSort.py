strings = ['A = 3 + 4', 'B = A - 6', 'C = A + B - -5']
graph = {}
to_eval = {}
for string in strings:
    expressions = string.split(' ')
    left = expressions[0]
    to_eval[left] = expressions[2:]
    for variable in expressions[2:]:
        if variable.isalpha():
            if left in graph:
                graph[left].append(variable)
            else:
                graph[left] = [variable]

def topoSort(graph):
    output = []
    visited = set() # added to output
    cycle = set() # not added to output, in current path
    def visit(node):
        if node in cycle:
            return False
        if node in visited:
            return True
        cycle.add(node)
        if node in graph:
            for child in graph[node]:
                if visit(child) == False:
                    return False
        cycle.remove(node)
        visited.add(node)
        output.append(node)
        # graph[child] = []
        return True
    
    for node in graph:
        if not visit(node):
            return []
    return output

eval_order = topoSort(graph)
res = {}
for var, exp in to_eval.items():
    value = 0
    
    res[var] = value
