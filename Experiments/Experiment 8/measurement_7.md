In Virtuoso, "forcing join order" means telling the query optimizer not to rearrange the order of your triple patterns in a SPARQL query, and instead execute them exactly in the order you wrote them.

Normally, Virtuoso tries to reorder your query patterns to improve performance based on statistics and cardinality estimates. However, sometimes it gets this wrong, especially with:

Very large graphs

Skewed data (some predicates or values appear much more often than others)

Complex joins or optional blocks

To force the join order:
DEFINE sql:select-option "order"
Example
SPARQL
DEFINE sql:select-option "order"
SELECT ?student ?course
WHERE {
  ?student a <http://example.org/GraduateStudent> .
  ?student <http://example.org/takesCourse> ?course .
}


Measuremet -> Use virtuoso_single_named_graph/virtuoso.ini
and new_queries_named_graph_join_order