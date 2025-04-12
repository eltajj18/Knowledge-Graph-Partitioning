from SPARQLBurger.SPARQLQueryBuilder import *

# Create an object of class SPARQLSelectQuery and set the limit for the results to 100
select_query = SPARQLSelectQuery(distinct=True, limit=100)

# Add a prefix
prefixes = [
    Prefix(prefix="", namespace="http://w3id.org/mlso#"),
    Prefix(prefix="ov", namespace="http://open.vocab.org/terms/"),
    Prefix(prefix="mls", namespace="http://www.w3.org/ns/mls#"),
    Prefix(prefix="owl", namespace="http://www.w3.org/2002/07/owl#"),
    Prefix(prefix="rdf", namespace="http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
    Prefix(prefix="sdo", namespace="https://w3id.org/okn/o/sd#"),
    Prefix(prefix="xml", namespace="http://www.w3.org/XML/1998/namespace"),
    Prefix(prefix="xsd", namespace="http://www.w3.org/2001/XMLSchema#"),
    Prefix(prefix="adms", namespace="http://www.w3.org/ns/adms#"),
    Prefix(prefix="dcat", namespace="http://www.w3.org/ns/dcat#"),
    Prefix(prefix="foaf", namespace="http://xmlns.com/foaf/0.1/"),
    Prefix(prefix="mlso", namespace="http://w3id.org/mlso/"),
    Prefix(prefix="prov", namespace="http://www.w3.org/ns/prov#"),
    Prefix(prefix="rdfs", namespace="http://www.w3.org/2000/01/rdf-schema#"),
    Prefix(prefix="skos", namespace="http://www.w3.org/2004/02/skos/core#"),
    Prefix(prefix="fabio", namespace="http://purl.org/spar/fabio/"),
    Prefix(prefix="schema", namespace="http://schema.org/"),
    Prefix(prefix="dcterms", namespace="http://purl.org/dc/terms/"),
    Prefix(prefix="edamontology", namespace="http://edamontology.org/"),
]

for prefix in prefixes:
    select_query.add_prefix(prefix=prefix)

# Add the variables we want to select
select_query.add_variables(variables=["?person", "?age"])

# Create a graph pattern to use for the WHERE part and add some triples
where_pattern = SPARQLGraphPattern()
where_pattern.add_triples(
    triples=[
        Triple(subject="?person", predicate="rdf:type", object="ex:Person"),
        Triple(subject="?person", predicate="ex:hasAge", object="?age"),
        Triple(subject="?person", predicate="ex:address", object="?address"),
    ]
)

# Set this graph pattern to the WHERE part
select_query.set_where_pattern(graph_pattern=where_pattern)

# Group the results by age
select_query.add_group_by(
    group=GroupBy(
        variables=["?age"]
    )
)

# Print the query we have defined
print(select_query.get_text())
                      