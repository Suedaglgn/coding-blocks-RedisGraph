def add_node(Rnode):
    """
    A method that adds node to graph without replication
    """
    query = f"""
    MERGE {str(Rnode)}
    """


def add_edge(src_node, dst_node, relation):
    """
    A method that adds edge to graph without replication
    """
    query = f"""
    MATCH (a  {src_node.toString()})
    MATCH (b {dst_node.toString()}) 
    MERGE (a)-[e:{relation}]->(b) 
    ON CREATE SET e.prop2 = 'cur-time'
    """


def get_nodes(param_str):
    """
    Query to find nodes
    """
    base_query = f"""
                MATCH p = (nodes {param_str})
                RETURN nodes
                """


def get_all_nodes(self):
    """
    A method that get all nodes from given graph
    """
    query = """
    MATCH p = (a)
    RETURN p
    """


def get_all_edges(self):
    """
    A method that get all edges from graph
    """
    query = """
    MATCH p = (a)-[]->(b)
    RETURN p
    """


def get_all_children(self, query_params):
    """
    A method that retrive all children of specific node that defined in query params
    @query_params: filter query string to match root node
    """
    query = f"""
    MATCH p = (l {query_params})-[*0..]->(m) 
    return m
    """
