Description -> created new bitmap index for kaggle and pwc and measured it indiviually
(i couldnt do it with openml.)
I am getting this error: 

SR175: Uniqueness violation : Violating unique index RDF_QUAD_GPOS on table DB.DBA.RDF_QUAD. Transaction killed.
at line 3 of Top-Level:
CREATE BITMAP INDEX RDF_QUAD_PGOS ON DB.DBA.RDF_QUAD (G, P, O, S) PARTITION (O VARCHAR (-1, 0hexffff))




With only one index (OGPS ) created by default, if the graph is always given, as with one or more FROM or FROM NAMED clauses, and there are no patterns where only graph and predicate are given, then the default indices should be sufficient. If predicate and graph are given but subject is not, then it is sometimes useful to add:

Making the PGOS index can help in some cases even if it is not readily apparent from the queries that one is needed. This is so, for example, if the predicate by itself is selective; i.e., there is a predicate that occurs in only a few triples.

CREATE BITMAP INDEX RDF_QUAD_GPOS
  ON DB.DBA.RDF_QUAD (G, P, O, S) 
  PARTITION (O VARCHAR (-1, 0hexffff));
  


 