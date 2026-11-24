# Definitions, Inference, and Evidence

## Instructional Design

The [site](https://learn-ontology.vercel.app/#learn) organizes six chapters around classes, individuals, relationships, chained rules, contradictions, and applications. Learners can choose everyday or technical examples. Its Detective section asks for a prediction before showing a proof, with an optional SQL explanation. The conflicting-revenue case was completed in the hosted interface: the displayed trace identifies two class assignments and the disjointness rule that makes their combination inconsistent.

For the course wiki, the useful design is a short cycle: state a managerial question, expose the inputs and rules, ask for a prediction, and reveal each inference with its source. Keep a text and table representation beside the graph. An original implementation can run locally in a static page and export the student's definitions in a readable format. Points and badges are optional; the source review supplies no estimate of their learning effect.

## Domain Rules and Data Validation

An OWL domain or range declaration can infer a type from a relationship. A missing type declaration does not automatically invalidate the relationship. Under OWL's open-world semantics, an absent fact can remain unknown. SHACL supplies a separate framework for testing whether an RDF graph satisfies declared conditions. These distinctions are explained in the [W3C OWL Primer, §§2 and 4.6](https://www.w3.org/TR/owl2-primer/) and [SHACL specification, §§1 and 4](https://www.w3.org/TR/shacl/).

Consider an original marketing rule: the range of `placedBy` is `Customer`. Recording that an order was placed by account A classifies A as a Customer under that rule. The inference does not verify the transaction, establish that the account belongs to one person, or determine whether the person authorized advertising. Those questions require additional evidence and explicit definitions. A generated analysis should retain the transaction source, account identifier, time, and relevant permission record.

Use ordinary Python or SQL checks for required timestamps, unique keys, allowed units, and missing values in the introductory exercise. Introduce SHACL as a possible implementation when the data are represented in RDF. A complete OWL reasoner is unnecessary for teaching these distinctions.

## Assess the Definitions Behind a Contradiction

The site's introductory examples often attribute contradictions to incorrect records. In a course application, evaluate the records and the axioms together. Declaring `LoyalCustomer` and `PriceSensitiveCustomer` disjoint creates an inconsistency when a customer belongs to both. The business meaning of these categories provides no general reason for that disjointness. Correcting the category definition may be more appropriate than deleting a customer observation.

The revenue case is useful when the object is a metric definition with an explicit refund convention. A gross-revenue measure and a net-revenue measure can also have identical numerical values when refunds are zero. Numerical equality does not make the definitions identical. Store the definition, currency, period, unit, and refund treatment alongside the value.

For time-varying states, identify the observation's date. A subscription can be active in one period and canceled in another without contradiction. Attach a state to an account-period or state interval, rather than making an account permanently belong to incompatible categories.

## Claims, Graphs, and AI Retrieval

An ontology defines vocabulary and rules. A knowledge graph records entities and relationships using a representation that may employ an ontology. A taxonomy supplies a category hierarchy. A database schema specifies the structure of stored records. These objects can work together; none alone establishes the truth of a statement extracted from a document.

For earnings calls, preserve an object such as `Claim` with a speaker, company, call date, source passage, and stated time horizon. A link saying that an executive attributes a price increase to input costs should remain an attributed assertion. Turning it into an unqualified causal relationship changes the evidence.

[Microsoft's GraphRAG documentation](https://microsoft.github.io/graphrag/) describes a particular pipeline that extracts entities and relationships, builds communities, and produces summaries for retrieval. An OWL inference engine and that pipeline perform different tasks. The course can compare a small manually checked graph with text retrieval on the same questions, measuring source support, missing evidence, and cost. The presence of a graph is insufficient evidence of improved answer accuracy.

## Implementation and Reading Scope

The inspected [repository revision](https://github.com/mani-bellan/concept-playgrounds/tree/4fc52fd92f644e03e76880c5de16f0accb4770e7) is dated November 23, 2026. Its README, all six chapter definitions, and the complete small reasoner were read. Selected example definitions were inspected. The hosted overview, course menu, and conflicting-revenue Detective exercise were checked in the browser. The website's deployment commit was not exposed, so the hosted interface and pinned repository are recorded separately.

The [reasoner](https://github.com/mani-bellan/concept-playgrounds/blob/4fc52fd92f644e03e76880c5de16f0accb4770e7/ontology/src/ontology.js) applies subclass inheritance, domain, range, inverse, and transitive rules to a fixed point, then checks explicit disjoint class memberships. It preserves one derivation for each added fact. It implements an instructional subset of OWL: the code omits self-edges from transitive cycles and does not implement general OWL cardinality or datatype reasoning. Its Turtle exporter replaces non-alphanumeric characters with underscores; distinct names can therefore map to the same identifier. An original course implementation should use stable unique identifiers and test export separately.

No upstream source was installed or executed locally. The hosted exercise does not establish that every lesson, export, or browser interaction works. No repository-wide license was identified, so source files and lesson text are linked rather than redistributed. The proposed marketing examples are original course designs.
