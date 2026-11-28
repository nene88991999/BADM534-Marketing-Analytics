# Glossary of Terms

## A

**A/B Test.** An experiment comparing two assigned versions of an intervention. Random assignment supports a causal comparison when implementation, outcome measurement, attrition, and interference are handled consistently with the design. [M6 §6.3](modules/M06_Causal_Inference_and_Experiments.md#63-designing-an-experiment-around-the-decision).

**Accountability.** The obligation to answer for a decision and provide relevant reasons or records. Accountability can attach to a role even when personal blame for the resulting harm remains unresolved. [M9 §9.65.7](modules/M09_Marketing_Dialectics.md#9657-responsibility-for-the-artifact-and-its-uses).

**Accuracy.** The proportion of classified observations whose predicted labels match the reference labels. Its meaning depends on class prevalence, label quality, and the consequences of different errors. [M7 §7.5](modules/M07_Prediction_and_Machine_Learning.md#75-case-study-accuracy-can-conceal-a-useless-model).

**Adaptive Experiment.** An experiment whose assignment rule changes in response to accumulated observations. Valid inference and policy evaluation must account for the changing probabilities and the information used to choose them. [M8 §8.20](modules/M08_Current_Topics_and_Integrated_Decisions.md#820-ai-experimentation-and-personalized-pricing).

**Adstock.** A transformation summarizing current and past advertising exposure under an assumed persistence rule. Its decay parameter controls carryover, and its causal interpretation requires a design addressing the determinants of spending. [M8 §8.3](modules/M08_Current_Topics_and_Integrated_Decisions.md#83-marketing-mix-models-combine-carryover-and-saturation).

**Agency.** A person's capacity to form, revise, and act on purposes. Recorded purchases or continued engagement supply evidence about behavior; assessing agency also requires attention to understanding, alternatives, and authority to refuse. [M9 §9.7](modules/M09_Marketing_Dialectics.md#97-personalization-learning-and-the-ability-to-revise-a-goal); [M9 §9.44](modules/M09_Marketing_Dialectics.md#944-personalization-and-the-learners-authority).

**AI-Assisted Coding.** Developing or revising code with a language model or coding agent. A defensible workflow specifies the task, inspects inputs, implements small steps, and checks the resulting calculations and interpretations independently. [M1 §1.5](modules/M01_Marketing_Analytics_and_Python.md#15-ai-assisted-coding-as-a-sequence-of-verifiable-steps); [M1 §1.14](modules/M01_Marketing_Analytics_and_Python.md#114-specifications-independent-checks-and-retained-skills).

**Algorithmic Pricing.** Setting or recommending prices through an automated rule. Its economic and moral implications depend on the information shared, decisions delegated, customer alternatives, and comparison with feasible pricing arrangements. [M8 §8.28](modules/M08_Current_Topics_and_Integrated_Decisions.md#828-shared-pricing-systems-and-customer-choice).

**Annotation.** Assigning a label or interpretation to a document, passage, or observation. A useful annotation protocol defines the construct, unit, decision rules, and treatment of ambiguity before labels become evaluation targets. [M5 §5.6](modules/M05_Text_Social_and_Network_Analysis.md#56-human-and-llm-annotation).

**Anticipation.** A response that occurs before the recorded treatment date because an actor expects the intervention. Preparatory utility investment can create exposure before a data center opens, changing the interpretation of pre-treatment periods. [M6 §6.35](modules/M06_Causal_Inference_and_Experiments.md#635-institutional-exposure-and-the-meaning-of-an-untreated-utility); [M6 §6.41](modules/M06_Causal_Inference_and_Experiments.md#641-phantom-projects-and-the-meaning-of-a-control).

**Antinomy.** A conflict in which reason appears to support opposing conclusions about an unconditioned object beyond possible experience. In Kantian dialectic, this concerns reason's claims to knowledge; an ordinary empirical disagreement is not automatically an antinomy (Kant, 1781/1787). [M9 §9.2](modules/M09_Marketing_Dialectics.md#92-transcendental-dialectic-and-the-limits-of-reason).

**Area Under the ROC Curve (ROC AUC).** The probability that a randomly selected positive receives a higher score than a randomly selected negative, plus half the probability of a tie. It summarizes ranking across the two classes without specifying an action threshold. [M7 §7.6](modules/M07_Prediction_and_Machine_Learning.md#76-ranking-and-calibration-answer-different-questions).

**Argument.** A set of premises offered as reasons for a conclusion. An analytical recommendation needs an empirical account of the proposed action and a defended normative premise connecting that account to what ought to be done. [M1 §1.20](modules/M01_Marketing_Analytics_and_Python.md#120-a-recommendation-as-an-argument); [M9 §9.40](modules/M09_Marketing_Dialectics.md#940-logical-consequence-and-a-defensible-recommendation).

**Artifactual Object.** An object whose creation, identity, or persistence depends on human practices. A dataset can depend on recording rules and institutions while the people, events, and burdens it represents have independent conditions of existence and truth (Thomasson, 1999, 2003). [M9 §9.60](modules/M09_Marketing_Dialectics.md#960-the-ontology-of-a-dataset).

**Aspect Sentiment.** A judgment about a particular attribute, such as delivery or product quality, within a text. A document can express positive and negative views about different attributes, making a single overall label inadequate for some decisions. [M5 §5.4](modules/M05_Text_Social_and_Network_Analysis.md#54-sentiment-aspect-labels-and-topic-models).

**Assignment Unit.** The entity to which a treatment is allocated, such as a customer, store, or market. It may differ from the row in the analysis, and it helps determine the appropriate comparison and uncertainty calculation. [M6 §6.3](modules/M06_Causal_Inference_and_Experiments.md#63-designing-an-experiment-around-the-decision).

**Association.** A statistical relationship between observed quantities. An association can arise from a causal effect, common causes, selection, measurement, or their combination; its interpretation requires a stated design and comparison. [M3 §3.1](modules/M03_Regression.md#31-a-conditional-mean-and-a-regression-line); [M6 §6.2](modules/M06_Causal_Inference_and_Experiments.md#62-why-the-treated-untreated-difference-can-be-biased).

**Association Rule.** A conditional co-occurrence pattern among items, often summarized by support, confidence, and lift. A basket association can guide prediction or merchandising hypotheses while leaving the causal effect of a recommendation unresolved. [M7 §7.17](modules/M07_Prediction_and_Machine_Learning.md#717-mhealth-basket-associations-and-future-validation).

**Attrition.** Loss of observations or outcomes after units enter a study. When loss depends on treatment or outcomes, analyzing only retained units can change the population represented and distort the intended comparison. [M6 §6.6](modules/M06_Causal_Inference_and_Experiments.md#66-implementation-checks-that-protect-the-comparison).

**Autonomy.** The capacity and authority to direct action through one's own deliberation. In the Kantian discussion, autonomy concerns rational self-legislation; a marketing application also examines whether customers can understand, reconsider, and refuse a proposed course of action. [M9 §9.4](modules/M09_Marketing_Dialectics.md#94-respect-for-persons-and-commercial-exchange); [M9 §9.41](modules/M09_Marketing_Dialectics.md#941-phenomena-noumena-and-the-ends-of-analysis).

**Average Treatment Effect (ATE).** The mean difference between the outcomes that the target population would experience under two treatment conditions. Estimating it requires a design or assumptions that connect observed outcomes to the missing counterfactual outcomes. [M6 §6.1](modules/M06_Causal_Inference_and_Experiments.md#61-define-the-treatment-outcome-and-estimand).

## B

**Bad Control.** A variable whose inclusion in an adjustment set distorts the intended causal comparison. Conditioning on a mediator, collider, or treatment-affected variable can create bias or change the estimand, depending on the causal structure. [M3 §3.20](modules/M03_Regression.md#320-a-control-variable-needs-a-causal-role); [M6 §6.40](modules/M06_Causal_Inference_and_Experiments.md#640-treatment-affected-covariates-in-a-panel).

**Basal Metabolic Rate (BMR).** The energy required to sustain basic physiological functions under standardized resting conditions. Predicted BMR depends on the available physiological inputs and the population for which the prediction equation is appropriate. [M2 §2.11](modules/M02_Customer_Data_and_Visualization.md#211-mhealth-nutrition-knowledge-and-sample-restrictions).

**Baseline.** A specified reference for comparison, such as a pre-intervention outcome, simple forecasting model, or existing policy. The analyst should identify which meaning applies and hold the relevant comparison constant. [M7 §7.2](modules/M07_Prediction_and_Machine_Learning.md#72-baselines-loss-functions-and-regularization); [M6 §6.3](modules/M06_Causal_Inference_and_Experiments.md#63-designing-an-experiment-around-the-decision).

**Bayesian Inference.** Updating a prior distribution with a likelihood to obtain a posterior distribution over unknown quantities. Posterior conclusions depend on the sampling model, prior, observed information, and the relationship between the modeled quantity and the substantive claim. [M4 §4.31](modules/M04_Conjoint_Segmentation_and_CLV.md#431-released-retail-data-integrated-heterogeneity-and-competing-explanations); [M9 §9.57](modules/M09_Marketing_Dialectics.md#957-heterogeneity-and-the-interpretation-of-consumer-harm).

**Benevolence.** Concern for the well-being of others as a ground for conduct. In the Confucian applications, the quality of relationships and responsibility to customers constrain the pursuit of commercial advantage. [M9 §9.11.1](modules/M09_Marketing_Dialectics.md#9111-righteousness-and-profit).

**Bias.** The difference between an estimator's expected value and its target under a stated data-generating process. A low-bias estimator for one target can still answer the wrong substantive question or support an unjustified decision. [M3 §3.22](modules/M03_Regression.md#322-unbiased-estimation-and-the-consequences-of-error); [M9 §9.66](modules/M09_Marketing_Dialectics.md#966-statistical-virtues-and-ontological-laziness).

**Bias-Variance Tradeoff.** A comparison between systematic estimation error and sampling variability. Regularization may reduce expected prediction error by accepting bias in exchange for lower variance; its desirability depends on the target and loss being evaluated. [M7 §7.2](modules/M07_Prediction_and_Machine_Learning.md#72-baselines-loss-functions-and-regularization).

**Bootstrap.** A resampling method that approximates sampling uncertainty by repeatedly drawing from observed data. Resampling must preserve the dependence relevant to the design, such as repeated records belonging to the same customer or assignment cluster. [M3 §3.6](modules/M03_Regression.md#36-uncertainty-dependence-and-practical-importance).

**Burden of Justification.** The responsibility to provide adequate reasons for a claim or action. Its allocation depends on authority, access to evidence, exposure to harm, and feasible alternatives; a company's convenience does not settle what affected people must accept. [M9 §9.10](modules/M09_Marketing_Dialectics.md#910-self-interest-and-the-burden-of-justification); [M9 §9.54](modules/M09_Marketing_Dialectics.md#954-who-ought-to-bear-the-burden-of-producing-evidence).

## C

**Calibration.** Agreement between stated probabilities and observed event frequencies over a defined evaluation population. Calibration concerns probability quality; it does not by itself establish good ranking, equitable treatment, or a justified decision threshold. [M7 §7.6](modules/M07_Prediction_and_Machine_Learning.md#76-ranking-and-calibration-answer-different-questions).

**Candidate Set.** The alternatives eligible for ranking or recommendation at a particular decision. Evaluation depends on how this set is formed, which options are excluded, and what information was available when selection occurred. [M7 §7.10](modules/M07_Prediction_and_Machine_Learning.md#710-recommendation-models-and-the-candidate-set).

**Cannibalization.** Sales of one product or offer that replace sales of another product supplied by the same firm. Evaluating a launch requires the resulting change in total contribution, including displaced purchases. [M4 §4.3](modules/M04_Conjoint_Segmentation_and_CLV.md#43-case-study-a-new-bundle-can-cannibalize-existing-sales).

**Carryover.** The persistence of an intervention's influence across later periods. A marketing-mix model may represent advertising carryover through an adstock transformation whose parameters determine how past exposure enters current response. [M8 §8.3](modules/M08_Current_Topics_and_Integrated_Decisions.md#83-marketing-mix-models-combine-carryover-and-saturation).

**Categorical Imperative.** A principle of moral obligation whose authority does not depend on achieving a chosen contingent end. Its universal-law and humanity formulations examine the principle of action and the treatment of persons (Kant, 1785). [M9 §9.4](modules/M09_Marketing_Dialectics.md#94-respect-for-persons-and-commercial-exchange); [M9 §9.16](modules/M09_Marketing_Dialectics.md#916-a-kantian-critique-of-commercial-optimization).

**Causal Effect.** The difference in an outcome under specified alternative interventions for a defined unit or population. The effect must be distinguished from an observed difference between groups that may have experienced different selection and background conditions. [M6 §6.1](modules/M06_Causal_Inference_and_Experiments.md#61-define-the-treatment-outcome-and-estimand); [M6 §6.2](modules/M06_Causal_Inference_and_Experiments.md#62-why-the-treated-untreated-difference-can-be-biased).

**Causal Identification.** The connection between observable information and a causal target under stated assumptions. Identification addresses whether the target is determined in principle; sampling uncertainty concerns how accurately it is estimated from finite data. [M6 §6.7](modules/M06_Causal_Inference_and_Experiments.md#67-observational-adjustment-and-its-limits); [M9 §9.40.3](modules/M09_Marketing_Dialectics.md#9403-compatibility-identification-and-valuation).

**Causal Responsibility.** Contribution to producing an outcome. It is distinct from the duties of a role, the obligation to answer for conduct, moral blame, and the capacity to repair the resulting problem. [M9 §9.65.7](modules/M09_Marketing_Dialectics.md#9657-responsibility-for-the-artifact-and-its-uses).

**Censoring.** Incomplete observation of an event time. For a customer still active when observation ends, the duration is known to exceed the observed period, and treating the end of observation as the event would misstate the outcome. [M4 §4.13](modules/M04_Conjoint_Segmentation_and_CLV.md#413-mhealth-time-until-a-logging-gap).

**Choice Probability.** The probability that a customer selects an alternative from a specified set under a model and information state. Substitution patterns depend on the utility specification, alternatives, and distribution of unobserved components. [M4 §4.2](modules/M04_Conjoint_Segmentation_and_CLV.md#42-utility-choice-probabilities-and-willingness-to-pay).

**Cluster-Robust Standard Error.** An uncertainty calculation that permits dependence within specified clusters while relying on suitable independence or weak dependence across clusters. Cluster choice and the number of informative clusters matter for the approximation. [M3 §3.6](modules/M03_Regression.md#36-uncertainty-dependence-and-practical-importance); [M6 §6.30](modules/M06_Causal_Inference_and_Experiments.md#630-store-assignment-and-false-discoveries).

**Clustering.** Grouping observations according to a chosen representation and similarity criterion. A mathematically stable partition can still have little managerial meaning if the features, scaling, or resulting groups do not match the decision. [M4 §4.5](modules/M04_Conjoint_Segmentation_and_CLV.md#45-segmentation-begins-with-a-definition-of-similarity); [M4 §4.25](modules/M04_Conjoint_Segmentation_and_CLV.md#425-stable-segments-and-substantive-meaning).

**Cohort.** A group defined by a common entry event or other fixed rule, such as customers who first subscribed in a particular month. Cohort comparisons require consistent follow-up horizons and denominators. [M2 §2.4](modules/M02_Customer_Data_and_Visualization.md#24-cohorts-retention-and-customer-age).

**Collider.** A variable caused by two other variables in a causal structure. Conditioning on it can create an association between its causes, including a spurious path between treatment and outcome. [M3 §3.20](modules/M03_Regression.md#320-a-control-variable-needs-a-causal-role); [M3 §3.21](modules/M03_Regression.md#321-exact-examples-of-helpful-and-harmful-adjustment).

**Compatibility.** Consistency between a claim and the available evidence under stated assumptions. One compatible explanation does not establish that it is actual or that every other explanation has been excluded. [M9 §9.27.1](modules/M09_Marketing_Dialectics.md#9271-premises-consequences-and-counterexamples); [M9 §9.40.3](modules/M09_Marketing_Dialectics.md#9403-compatibility-identification-and-valuation).

**Conceptual Engineering.** The deliberate assessment or revision of concepts for a purpose. Defining harm, admissible evidence, or success can redistribute which concerns receive attention before a statistical calculation begins. [M9 §9.56](modules/M09_Marketing_Dialectics.md#956-evidentiary-standards-as-conceptual-engineering).

**Confidence Interval.** A set produced by a procedure with a specified long-run coverage rate under its assumptions. Its width and position describe uncertainty about the target; a wide interval around zero can leave economically important effects unresolved. [M3 §3.6](modules/M03_Regression.md#36-uncertainty-dependence-and-practical-importance); [M6 §6.47](modules/M06_Causal_Inference_and_Experiments.md#647-choosing-the-null-for-a-claim-about-harm).

**Conflict of Interest.** A situation in which a secondary interest can improperly influence judgment owed to another person or purpose. Its existence supplies a reason for safeguards and scrutiny without proving that a particular judgment was corrupted. [M9 §9.45](modules/M09_Marketing_Dialectics.md#945-conflicts-of-interest-and-the-analysts-judgment).

**Conformal Prediction.** A method that uses a calibration sample and nonconformity scores to construct prediction sets or intervals with coverage guarantees under specified conditions. Marginal coverage generally does not imply equal coverage for every customer subgroup. [M7 §7.24](modules/M07_Prediction_and_Machine_Learning.md#724-demand-intervals-and-the-distribution-of-forecast-errors); [M7 §7.25](modules/M07_Prediction_and_Machine_Learning.md#725-prediction-sets-and-customer-service-routing).

**Confounding.** A distortion of a causal comparison caused by common influences on treatment and outcome. Adjustment can address measured confounding under suitable assumptions, while predictive fit alone does not establish that the comparison is causal. [M6 §6.2](modules/M06_Causal_Inference_and_Experiments.md#62-why-the-treated-untreated-difference-can-be-biased); [M6 §6.7](modules/M06_Causal_Inference_and_Experiments.md#67-observational-adjustment-and-its-limits).

**Confucian Role Ethics.** An approach that evaluates conduct through relationships, responsibilities, and cultivated judgment. Evaluating a commercial role requires considering humaneness, appropriate conduct, and reciprocity alongside formal obligations. [M9 §9.11](modules/M09_Marketing_Dialectics.md#911-confucian-perspectives-on-marketing-conduct).

**Conjoint Analysis.** A method for learning preferences from evaluations or choices among profiles whose attributes vary by design. Design, task realism, identification, and the relationship between stated and actual choices determine the usefulness of the estimated tradeoffs. [M4 §4.1](modules/M04_Conjoint_Segmentation_and_CLV.md#41-product-design-requires-tradeoffs); [M4 §4.4](modules/M04_Conjoint_Segmentation_and_CLV.md#44-estimate-and-validate-preferences).

**Consent.** Authorization under conditions that support understanding, voluntariness, and a meaningful opportunity to refuse. A click, purchase, or continuing payment does not by itself establish that those conditions hold. [M9 §9.5](modules/M09_Marketing_Dialectics.md#95-worked-case-identical-renewal-different-customer-intent); [M9 §9.37](modules/M09_Marketing_Dialectics.md#937-mobile-targeting-and-authority-over-customer-information).

**Construct.** The concept an analysis seeks to represent, such as satisfaction, agency, or affordability. Its relationship to a recorded variable must be defended through definitions, measurement choices, and evidence relevant to the intended use. [M5 §5.1](modules/M05_Text_Social_and_Network_Analysis.md#51-define-the-construct-and-the-document); [M2 §2.32](modules/M02_Customer_Data_and_Visualization.md#232-defining-harm-before-choosing-its-measure).

**Construct Validity.** The adequacy of a measurement or operational procedure for representing its intended construct. A reliably recorded quantity can still be an inadequate measure of the customer interest named in the claim. [M2 §2.28](modules/M02_Customer_Data_and_Visualization.md#228-electricity-prices-household-bills-and-the-unit-of-harm); [M9 §9.68](modules/M09_Marketing_Dialectics.md#968-worked-assessments-of-the-missing-object).

**Consumer Harm Elasticity.** The proportional change in a specified consumer-harm measure relative to a proportional change in a specified statistical property. In the worked example, it is a conditional sensitivity calculation whose sign and interpretation depend on the model, baseline, and decision rule. [M6 §6.46](modules/M06_Causal_Inference_and_Experiments.md#646-greater-precision-and-fewer-detected-harms); [M9 §9.57](modules/M09_Marketing_Dialectics.md#957-heterogeneity-and-the-interpretation-of-consumer-harm).

**Consumer Surplus.** The difference between modeled willingness to pay and expenditure for the purchased quantity. Its welfare interpretation depends on the preference model, available alternatives, and treatment of constraints; it does not exhaust reasons concerning autonomy or fair treatment. [M4 §4.26](modules/M04_Conjoint_Segmentation_and_CLV.md#426-demand-information-pricing-and-consumer-surplus); [M9 §9.35](modules/M09_Marketing_Dialectics.md#935-identical-tested-demand-and-opposite-welfare-conclusions).

**Contestability.** An affected person's effective opportunity to question a classification, claim, or decision and obtain a response capable of changing it. Nominal access to a complaint form can coexist with an ineffective route for challenge. [M9 §9.62](modules/M09_Marketing_Dialectics.md#962-reasons-owed-to-the-people-represented); [M9 §9.65](modules/M09_Marketing_Dialectics.md#965-justifying-restricted-research-to-affected-people).

**Contextual Integrity.** An account of privacy that evaluates information flows by their social context, actors, attributes, and transmission principles. A restriction requires attention to the appropriate flow and protected person, not secrecy as an end in itself (Nissenbaum, 2004). [M9 §9.65.3](modules/M09_Marketing_Dialectics.md#9653-a-philosophical-argument-against-protective-secrecy).

**Contractualism.** An ethical approach that asks whether principles regulating conduct could be reasonably rejected by affected individuals. Justification depends on their reasons and burdens under feasible alternatives, rather than treating aggregate advantage as sufficient (Scanlon, 1998). [M9 §9.30](modules/M09_Marketing_Dialectics.md#930-what-a-company-ought-to-do); [M9 §9.65.8](modules/M09_Marketing_Dialectics.md#9658-maxims-of-data-production-and-disclosure).

**Contradiction in Conception.** A failure in universalization where the maxim undermines a practice or means that its own action presupposes (Kant, 1785). Seeking the credibility of observation while knowingly presenting invention as observation supplies an analogous research case. [M9 §9.65.8](modules/M09_Marketing_Dialectics.md#9658-maxims-of-data-production-and-disclosure).

**Contradiction in Willing.** A failure in universalization where an agent cannot consistently will the maxim as universal alongside ends necessarily implicated in rational agency. An unpopular outcome or a personal dislike alone does not establish this contradiction (Kant, 1785). [M9 §9.65.8](modules/M09_Marketing_Dialectics.md#9658-maxims-of-data-production-and-disclosure).

**Control Group.** Units used to represent the outcome that treated units would have experienced under the comparison condition. Absence of a recorded operating data center does not by itself establish absence of preparatory investment or other exposure. [M6 §6.8](modules/M06_Causal_Inference_and_Experiments.md#68-difference-in-differences-and-a-counterfactual-trend); [M6 §6.41](modules/M06_Causal_Inference_and_Experiments.md#641-phantom-projects-and-the-meaning-of-a-control).

**Cosine Similarity.** The normalized inner product of two nonzero vectors. It compares their directions in a chosen representation, so its substantive meaning depends on how that representation encodes the objects of interest. [M5 §5.3](modules/M05_Text_Social_and_Network_Analysis.md#53-embeddings-and-semantic-similarity).

**Counterexample.** A case in which an argument's premises hold while its proposed conclusion fails. It defeats the asserted entailment, although establishing which case describes the actual world remains an empirical question. [M9 §9.27.1](modules/M09_Marketing_Dialectics.md#9271-premises-consequences-and-counterexamples).

**Counterfactual.** The outcome or state that would obtain under a specified alternative to the observed action or condition. Its credibility depends on the design, assumptions, and institutional details supporting the alternative. [M6 §6.1](modules/M06_Causal_Inference_and_Experiments.md#61-define-the-treatment-outcome-and-estimand); [M9 §9.38](modules/M09_Marketing_Dialectics.md#938-pricing-evidence-in-a-us-antitrust-case).

**Coverage.** The proportion of relevant cases represented by data, or the probability that an interval contains its target. These uses require different denominators and should be distinguished whenever reporting evidence coverage or statistical coverage. [M2 §2.20](modules/M02_Customer_Data_and_Visualization.md#220-access-to-evidence-changes-the-review-sample); [M7 §7.24](modules/M07_Prediction_and_Machine_Learning.md#724-demand-intervals-and-the-distribution-of-forecast-errors).

**Cross-Fitting.** Estimating nuisance components on observations separate from those used in a subsequent estimating equation, often rotating across folds. This separation helps control overfitting effects under the estimator's additional assumptions. [M6 §6.23](modules/M06_Causal_Inference_and_Experiments.md#623-adjustment-for-selected-discount-intensity).

**Cross-Validation.** Evaluating a modeling procedure across held-out subsets of the available data. Splits must respect the deployment setting, and every learned preprocessing or tuning step must be kept separate from the corresponding validation observations. [M7 §7.4](modules/M07_Prediction_and_Machine_Learning.md#74-validation-cross-validation-and-leakage).

**Culpability.** The basis for moral blame, assessed through knowledge, intention, negligence, control, and reasonable alternatives. A defective dataset or retracted article does not alone establish which individual knowingly caused the defect. [M9 §9.65.7](modules/M09_Marketing_Dialectics.md#9657-responsibility-for-the-artifact-and-its-uses); [M9 §9.84](modules/M09_Marketing_Dialectics.md#984-misleading-research-replication-and-correction).

**CUPED.** A control-variate adjustment that uses pre-treatment information to reduce experimental outcome variance. Its justification requires preserving the treatment comparison and handling estimation of the adjustment consistently with the design. [M6 §6.15](modules/M06_Causal_Inference_and_Experiments.md#615-mhealth-prior-activity-and-experiment-precision).

**Customer Lifetime Value (CLV).** The discounted expected contribution from a customer relationship over a defined horizon, net of the costs included in the calculation. Retention, timing, margin, acquisition expense, and discounting determine its interpretation. [M4 §4.7](modules/M04_Conjoint_Segmentation_and_CLV.md#47-customer-lifetime-value-depends-on-timing-and-margin).

## D

**Data Dictionary.** Documentation of variables, units, allowable values, missing-value conventions, and observation units. It supports consistent use of a file but must be reconciled with the records and collection process. [M1 §1.8](modules/M01_Marketing_Analytics_and_Python.md#18-mhealth-from-food-entries-to-a-decision-table).

**Data Leakage.** Use of information during training or evaluation that would be unavailable at the intended prediction time or would improperly reveal evaluation outcomes. Leakage can produce strong reported performance that fails under actual deployment. [M7 §7.4](modules/M07_Prediction_and_Machine_Learning.md#74-validation-cross-validation-and-leakage).

**Data Lineage.** The documented path from source records through extracts, joins, transformations, and released outputs. Preserving lineage allows a critic to connect a reported quantity to the decisions that produced it. [M2 §2.30](modules/M02_Customer_Data_and_Visualization.md#230-data-have-a-production-history); [M9 §9.65.7](modules/M09_Marketing_Dialectics.md#9657-responsibility-for-the-artifact-and-its-uses).

**Data Provenance.** Information about a dataset's origin, collection, authorship, version, and processing history. Provenance helps assess what the records represent and which claims they can support. [M2 §2.30](modules/M02_Customer_Data_and_Visualization.md#230-data-have-a-production-history); [M2 §2.35](modules/M02_Customer_Data_and_Visualization.md#235-reproducing-a-result-and-assessing-its-records).

**Data-Generating Process.** The probabilistic or institutional account of how observations arise. A simulation specifies such a process, while an empirical analysis must justify how its model relates to actual selection, measurement, and behavior. [M3 §3.22](modules/M03_Regression.md#322-unbiased-estimation-and-the-consequences-of-error); [M6 §6.2](modules/M06_Causal_Inference_and_Experiments.md#62-why-the-treated-untreated-difference-can-be-biased).

**Decision Threshold.** The cutoff at which a score, probability, or evidential quantity triggers an action. A justified threshold connects uncertainty to the costs, benefits, and reasons associated with acting or withholding action. [M7 §7.7](modules/M07_Prediction_and_Machine_Learning.md#77-thresholds-should-reflect-the-decision); [M7 §7.48](modules/M07_Prediction_and_Machine_Learning.md#748-prediction-thresholds-and-consumer-consequences).

**Deduction.** Inference in which the conclusion follows necessarily from the premises. A valid deduction can still fail to establish a substantive conclusion when its premises are false or unsupported. [M9 §9.27.1](modules/M09_Marketing_Dialectics.md#9271-premises-consequences-and-counterexamples); [M9 §9.40.1](modules/M09_Marketing_Dialectics.md#9401-validity-soundness-and-evidential-support).

**Denominator.** The population, exposure, or total relative to which a rate or proportion is calculated. Changing the denominator can change the meaning of a comparison even when the numerator remains fixed. [M2 §2.1](modules/M02_Customer_Data_and_Visualization.md#21-define-the-population-before-the-metric); [M5 §5.14](modules/M05_Text_Social_and_Network_Analysis.md#514-earnings-calls-pricing-language-speaking-exposure-and-meaning).

**Deontology.** An approach to morality that gives duties and constraints on conduct a role independent of maximizing aggregate consequences. The Kantian applications examine principles and treatment of persons alongside the outcomes of marketing practices. [M9 §9.4](modules/M09_Marketing_Dialectics.md#94-respect-for-persons-and-commercial-exchange); [M9 §9.16](modules/M09_Marketing_Dialectics.md#916-a-kantian-critique-of-commercial-optimization).

**Derivative Moral Right.** A right whose justification rests on the interests or rights of others. A corporation may claim protection through the people it serves or represents, but the relevant interests and restriction still require a specific defense (Pasternak, 2017). [M9 §9.65.2](modules/M09_Marketing_Dialectics.md#9652-corporate-duties-and-human-protections).

**Descriptive Claim.** A statement about observed records or a specified population summary. Its support depends on measurement, selection, denominators, and the scope of observation; a descriptive comparison does not automatically identify an intervention's effect. [M1 §1.6](modules/M01_Marketing_Analytics_and_Python.md#16-interpreting-and-communicating-a-result); [M2 §2.1](modules/M02_Customer_Data_and_Visualization.md#21-define-the-population-before-the-metric).

**Development Set.** Observations used to choose models, prompts, hyperparameters, or analytical procedures. Repeated selection makes this set part of development and creates a need for independent final evaluation. [M7 §7.20](modules/M07_Prediction_and_Machine_Learning.md#720-repeated-selection-can-improve-a-score-without-improving-prediction); [M5 §5.15](modules/M05_Text_Social_and_Network_Analysis.md#515-repeated-prompt-revision-and-independent-text-evaluation).

**Difference-in-Differences (DiD).** A comparison of changes in outcomes across treated and comparison groups. A causal interpretation requires a justified counterfactual trend and appropriate handling of timing, anticipation, composition, and spillovers. [M6 §6.8](modules/M06_Causal_Inference_and_Experiments.md#68-difference-in-differences-and-a-counterfactual-trend); [M6 §6.27](modules/M06_Causal_Inference_and_Experiments.md#627-continuous-treatment-and-parallel-trends).

**Distribution Shift.** A change between the data distribution used to develop or evaluate a model and the distribution encountered later. Changes in customers, policies, measurement, or labels can invalidate earlier performance or coverage claims. [M7 §7.24](modules/M07_Prediction_and_Machine_Learning.md#724-demand-intervals-and-the-distribution-of-forecast-errors); [M8 §8.21](modules/M08_Current_Topics_and_Integrated_Decisions.md#821-prediction-intervals-when-demand-changes).

**Dose-Response Curve.** The expected outcome under different levels of a treatment, such as discount depth. A causal curve requires a defined population, adequate treatment support, and assumptions linking observed dose variation to interventions. [M6 §6.22](modules/M06_Causal_Inference_and_Experiments.md#622-discount-depth-and-the-causal-response-curve); [M6 §6.23](modules/M06_Causal_Inference_and_Experiments.md#623-adjustment-for-selected-discount-intensity).

**Double Machine Learning.** An estimation approach that combines nuisance-function learning with estimating equations designed to reduce sensitivity to nuisance errors, commonly using cross-fitting. Causal validity still depends on identification assumptions and suitable rates or regularity conditions. [M6 §6.23](modules/M06_Causal_Inference_and_Experiments.md#623-adjustment-for-selected-discount-intensity).

**Dynamic Pricing.** Prices that vary over time or market conditions. Whether a practice involves deception, discrimination, coordination, or justified adjustment depends on its actual conduct and institutional setting. [M9 §9.15](modules/M09_Marketing_Dialectics.md#915-pricing-policy-what-conduct-is-being-evaluated); [M8 §8.16](modules/M08_Current_Topics_and_Integrated_Decisions.md#816-pricing-communication-customer-outcomes-and-regulatory-evidence).

## E

**Ecological Inference.** Drawing conclusions about individuals from aggregate observations. Area averages can conceal differences in exposure, consumption, and costs, so a household interpretation requires additional evidence or assumptions. [M2 §2.28](modules/M02_Customer_Data_and_Visualization.md#228-electricity-prices-household-bills-and-the-unit-of-harm); [M3 §3.17](modules/M03_Regression.md#317-area-income-digital-usage-and-the-comparison-defined-by-controls).

**Economic Significance.** The magnitude of an effect relative to a substantive decision, burden, or benchmark. It is distinct from statistical significance and requires stated units, a meaningful comparison, and attention to uncertainty. [M6 §6.5](modules/M06_Causal_Inference_and_Experiments.md#65-power-precision-and-the-minimum-useful-effect); [M6 §6.32](modules/M06_Causal_Inference_and_Experiments.md#632-statistical-detection-and-a-profitable-campaign).

**Elasticity.** The proportional response of one quantity to a proportional change in another, holding the specified conditions fixed. Its substantive interpretation depends on the variables, comparison, and whether the relationship is descriptive, structural, or causal. [M3 §3.12](modules/M03_Regression.md#312-price-elasticity-when-prices-respond-to-demand).

**Embedding.** A numerical representation of an object, such as a text, in a vector space. Similarity in that space reflects the representation and training objective; it requires validation for the marketing construct and population of interest. [M5 §5.3](modules/M05_Text_Social_and_Network_Analysis.md#53-embeddings-and-semantic-similarity).

**Empiricism.** A family of views emphasizing experience or observation in knowledge. Critical assessment asks whether measurable regularities can settle questions of ontology or moral permission without further premises. [M9 §9.43](modules/M09_Marketing_Dialectics.md#943-philosophical-critiques-of-empiricism-and-reduction); [M9 §9.67](modules/M09_Marketing_Dialectics.md#967-philosophical-grounds-for-the-critique).

**Epistemic Fallacy.** The reduction of questions about what exists to questions about how it is known. The critique preserves a distinction between a real burden and the available means of measuring or identifying it (Bhaskar, 2007). [M9 §9.67.1](modules/M09_Marketing_Dialectics.md#9671-abstraction-and-the-object-represented).

**Epistemic Injustice.** A wrong affecting people in their capacity as knowers, including diminished credibility or inadequate shared resources for making their experience intelligible. Institutional prestige can affect whose account receives uptake in a public dispute. [M9 §9.32](modules/M09_Marketing_Dialectics.md#932-who-counts-as-a-stakeholder-and-why).

**Epistemic Norm.** A standard governing warranted belief or inquiry, such as attention to evidence, independent criticism, and reliable inference. Compliance with an epistemic standard leaves further questions about the permissible use of the resulting claim. [M9 §9.52](modules/M09_Marketing_Dialectics.md#952-truth-warrant-and-the-different-force-of-norms).

**Epistemology.** Inquiry into knowledge, justification, and the grounds of belief. In analytics, it asks what supports an interpretation and how evidence, assumptions, and criticism affect its warrant. [M9 §9.52](modules/M09_Marketing_Dialectics.md#952-truth-warrant-and-the-different-force-of-norms); [M9 §9.67](modules/M09_Marketing_Dialectics.md#967-philosophical-grounds-for-the-critique).

**Equivalence Test.** A test designed to assess whether an effect lies within a pre-specified interval of substantively negligible values. Failure to reject a zero-effect null does not substitute for demonstrating equivalence within those margins. [M6 §6.47](modules/M06_Causal_Inference_and_Experiments.md#647-choosing-the-null-for-a-claim-about-harm); [M9 §9.25](modules/M09_Marketing_Dialectics.md#925-evidence-for-a-small-burden).

**Equivocation.** A change in the meaning of a term within an argument that makes an inference appear stronger than it is. Moving from an average electricity price to a claim about household bills can conceal a change in the object being evaluated. [M9 §9.40.2](modules/M09_Marketing_Dialectics.md#9402-the-question-and-the-meaning-of-its-terms); [M2 §2.28](modules/M02_Customer_Data_and_Visualization.md#228-electricity-prices-household-bills-and-the-unit-of-harm).

**Estimand.** The quantity an analysis seeks to learn, defined through its population, outcome, treatment or comparison, and time horizon. A precise estimator can be unhelpful if its estimand differs from the question used to justify action. [M6 §6.1](modules/M06_Causal_Inference_and_Experiments.md#61-define-the-treatment-outcome-and-estimand); [M9 §9.66](modules/M09_Marketing_Dialectics.md#966-statistical-virtues-and-ontological-laziness).

**Estimator.** A rule for calculating an estimate from observed data. Its bias, variance, and other properties are defined relative to a target, sampling process, and assumptions. [M3 §3.1](modules/M03_Regression.md#31-a-conditional-mean-and-a-regression-line); [M3 §3.22](modules/M03_Regression.md#322-unbiased-estimation-and-the-consequences-of-error).

**Evidential Warrant.** The support that evidence and defensible premises provide for a claim. Warrant concerns the relationship between evidence and interpretation; the institutional approval of an output alone does not establish it. [M9 §9.52](modules/M09_Marketing_Dialectics.md#952-truth-warrant-and-the-different-force-of-norms).

**Exchangeability.** A symmetry under which the joint distribution is unchanged by permitted permutations of observations. It underlies standard conformal guarantees and must be assessed against time dependence, group structure, and changing policies. [M7 §7.24](modules/M07_Prediction_and_Machine_Learning.md#724-demand-intervals-and-the-distribution-of-forecast-errors).

**Exclusion Restriction.** The condition that an instrument affects the outcome only through the treatment channel relevant to the model. A strong first-stage relationship does not establish this condition. [M3 §3.12](modules/M03_Regression.md#312-price-elasticity-when-prices-respond-to-demand); [M6 §6.9](modules/M06_Causal_Inference_and_Experiments.md#69-other-designs-discontinuities-and-instruments).

**Expected Loss.** The probability-weighted consequence of errors or actions under a specified loss function. Choosing the loss function assigns importance to outcomes and affected parties, so optimization requires a defended objective. [M7 §7.7](modules/M07_Prediction_and_Machine_Learning.md#77-thresholds-should-reflect-the-decision); [M6 §6.44](modules/M06_Causal_Inference_and_Experiments.md#644-type-i-and-type-ii-errors-under-unequal-costs).

**Expression of Concern.** A formal journal notice identifying unresolved concerns about a published article. It differs from a retraction and does not establish that every result, author, or associated study is fraudulent. [M9 §9.84](modules/M09_Marketing_Dialectics.md#984-misleading-research-replication-and-correction).

**External Validity.** The credibility of extending a finding to a different population, setting, policy, or period. A well-identified effect in one study requires additional reasoning to support its use under changed conditions. [M6 §6.21](modules/M06_Causal_Inference_and_Experiments.md#621-experimental-evidence-and-ai-assisted-decisions); [M8 §8.18](modules/M08_Current_Topics_and_Integrated_Decisions.md#818-model-updates-and-the-decision-to-revisit-an-analysis).

## F

**False Discovery Rate.** The expected proportion of false rejections among rejected hypotheses, with the proportion defined as zero when there are no rejections. Control depends on the procedure and its assumptions about the tests. [M6 §6.30](modules/M06_Causal_Inference_and_Experiments.md#630-store-assignment-and-false-discoveries).

**False Negative.** A case in which a decision rule fails to flag a condition that is present. Its frequency and harm depend on the target condition, threshold, reference evidence, and consequences of withholding action. [M7 §7.5](modules/M07_Prediction_and_Machine_Learning.md#75-case-study-accuracy-can-conceal-a-useless-model); [M7 §7.48](modules/M07_Prediction_and_Machine_Learning.md#748-prediction-thresholds-and-consumer-consequences).

**False Positive.** A case in which a decision rule flags a condition that is absent. Its practical cost depends on the action triggered; an exploratory inquiry and a final penalty can impose different burdens. [M7 §7.48](modules/M07_Prediction_and_Machine_Learning.md#748-prediction-thresholds-and-consumer-consequences); [M6 §6.44](modules/M06_Causal_Inference_and_Experiments.md#644-type-i-and-type-ii-errors-under-unequal-costs).

**Feature.** An input supplied to a prediction or estimation procedure. Feature availability, construction, scaling, and timing affect validity, especially when preprocessing learns from data or a feature is affected by treatment. [M7 §7.1](modules/M07_Prediction_and_Machine_Learning.md#71-specify-the-forecast-origin-and-target); [M7 §7.4](modules/M07_Prediction_and_Machine_Learning.md#74-validation-cross-validation-and-leakage).

**Feedback Loop.** A process in which model-directed actions influence the observations used for subsequent learning. Recommendations shape exposure, so observed clicks can reflect both customer preferences and the policy that made items visible. [M8 §8.1](modules/M08_Current_Topics_and_Integrated_Decisions.md#81-recommendation-systems-learn-from-selected-exposure); [M9 §9.44](modules/M09_Marketing_Dialectics.md#944-personalization-and-the-learners-authority).

**Fixed Effects.** Parameters representing persistent differences across specified units or periods. Their inclusion changes the variation used to estimate a relationship and does not automatically remove time-varying confounding or treatment-induced selection. [M3 §3.7](modules/M03_Regression.md#37-diagnostics-and-panel-data).

**Forecast Origin.** The moment at which a prediction is made and the information set is fixed. Features, training labels, and evaluation splits must respect what could actually be known at that time. [M7 §7.1](modules/M07_Prediction_and_Machine_Learning.md#71-specify-the-forecast-origin-and-target); [M7 §7.30](modules/M07_Prediction_and_Machine_Learning.md#730-event-timing-and-information-at-the-alert).

**Free Will.** The philosophical question of agency and control relevant to a person's authorship of action and responsibility. Statistical predictability or randomness alone does not resolve that question. [M9 §9.41](modules/M09_Marketing_Dialectics.md#941-phenomena-noumena-and-the-ends-of-analysis).

## G

**Gamification.** Use of game-associated features, such as points, streaks, or challenges, within another activity. Evaluating it requires distinguishing beneficial goal support from burdens that arise when continued activity loses the user's endorsement. [M9 §9.70](modules/M09_Marketing_Dialectics.md#970-marketing-research-and-compulsive-online-engagement); [M9 §9.73](modules/M09_Marketing_Dialectics.md#973-whose-value-does-gamification-create).

**Generalized Propensity Score.** A representation of the conditional distribution or density of treatment intensity given covariates. Its role in a causal dose-response analysis depends on overlap, the assignment assumptions, and the treatment scale. [M6 §6.23](modules/M06_Causal_Inference_and_Experiments.md#623-adjustment-for-selected-discount-intensity); [M6 §6.24](modules/M06_Causal_Inference_and_Experiments.md#624-overlap-weight-concentration-and-missing-confounders).

**Goldberg Screen.** An assessment comparing reported energy intake with basal metabolic rate and an expected activity-related requirement under specified variability assumptions. Appropriate use depends on the instrument, observation period, population, and availability of relevant physiological information. [M2 §2.11](modules/M02_Customer_Data_and_Visualization.md#211-mhealth-nutrition-knowledge-and-sample-restrictions).

**Graph.** A representation of entities as nodes and specified relationships as edges. The meaning of an edge, the included population, and the direction or weight of a relation determine which substantive questions the graph can answer. [M5 §5.7](modules/M05_Text_Social_and_Network_Analysis.md#57-networks-connections-reach-and-brokerage); [M5 §5.25](modules/M05_Text_Social_and_Network_Analysis.md#525-attributed-claims-and-graph-relationships).

**Graph Coarsening.** Reducing a graph by grouping or aggregating nodes while seeking to preserve selected properties. A good compression score does not establish that customer access or predictive conclusions survive the transformation. [M5 §5.24](modules/M05_Text_Social_and_Network_Analysis.md#524-compressing-a-network-and-preserving-customer-access); [M7 §7.38](modules/M07_Prediction_and_Machine_Learning.md#738-network-compression-label-purity-and-predictive-evidence).

**Ground Truth.** The reference used to judge a prediction or label. In an empirical application, that reference has its own collection rules, uncertainty, and possible error; the label alone supplies no guarantee of truth. [M5 §5.20](modules/M05_Text_Social_and_Network_Analysis.md#520-evaluate-the-grader-and-justify-the-rubric); [M7 §7.26](modules/M07_Prediction_and_Machine_Learning.md#726-evaluation-coverage-and-the-costs-of-grading-errors).

## H

**Harm.** An adverse effect on a specified person's interests or standing. A defensible analysis identifies the affected person, burden, comparison, and timing before selecting a proxy or deciding what evidence would justify protection. [M2 §2.32](modules/M02_Customer_Data_and_Visualization.md#232-defining-harm-before-choosing-its-measure); [M9 §9.32](modules/M09_Marketing_Dialectics.md#932-who-counts-as-a-stakeholder-and-why).

**Hash.** A deterministic digest computed from a file's bytes. A matching cryptographic hash can verify that two copies are byte-identical; it does not establish the truth of the observations or the adequacy of their interpretation. [M2 §2.34](modules/M02_Customer_Data_and_Visualization.md#234-worked-example-retention-and-pending-cancellation); [M2 §2.35](modules/M02_Customer_Data_and_Visualization.md#235-reproducing-a-result-and-assessing-its-records).

**Heterogeneity.** Differences across customers, products, markets, or periods in characteristics, responses, or preferences. Modeling these differences can change fit, uncertainty, and estimated incidence, with no universal direction for the detection of harm. [M4 §4.30](modules/M04_Conjoint_Segmentation_and_CLV.md#430-heterogeneous-demand-market-power-and-consumer-interests); [M6 §6.46](modules/M06_Causal_Inference_and_Experiments.md#646-greater-precision-and-fewer-detected-harms).

**Hierarchy in a Statistical Model.** A structure in which unit-specific parameters are related through shared distributional parameters. It enables partial pooling and makes assumptions about similarity consequential for individual estimates. [M4 §4.31](modules/M04_Conjoint_Segmentation_and_CLV.md#431-released-retail-data-integrated-heterogeneity-and-competing-explanations); [M6 §6.26](modules/M06_Causal_Inference_and_Experiments.md#626-store-decisions-and-partial-pooling).

**Humanity Formulation.** The requirement to treat humanity, in oneself and others, always also as an end and never merely as a means. Its marketing applications examine deception, authority, and the person's capacity to judge and pursue ends (Kant, 1785). [M9 §9.4](modules/M09_Marketing_Dialectics.md#94-respect-for-persons-and-commercial-exchange); [M9 §9.65.8](modules/M09_Marketing_Dialectics.md#9658-maxims-of-data-production-and-disclosure).

**Hyperparameter.** A choice governing a learning procedure, such as regularization strength or tree depth. It should be selected using training or development information while preserving an independent basis for final evaluation. [M7 §7.2](modules/M07_Prediction_and_Machine_Learning.md#72-baselines-loss-functions-and-regularization); [M7 §7.4](modules/M07_Prediction_and_Machine_Learning.md#74-validation-cross-validation-and-leakage).

## I

**Identification.** Whether a target is uniquely determined by the information and assumptions available. Observationally equivalent explanations can leave a target unidentified even with unlimited data from the same observation process. [M9 §9.40.3](modules/M09_Marketing_Dialectics.md#9403-compatibility-identification-and-valuation); [M6 §6.38](modules/M06_Causal_Inference_and_Experiments.md#638-equal-historical-fit-and-different-price-effects).

**Inductive Risk.** The risk of error when evidence supports an inference without determining its truth with certainty. The consequences of accepting or rejecting a claim can matter for evidential standards and decisions about action. [M9 §9.52](modules/M09_Marketing_Dialectics.md#952-truth-warrant-and-the-different-force-of-norms); [M9 §9.58](modules/M09_Marketing_Dialectics.md#958-a-reasonable-principle-for-acting-under-uncertainty).

**Information Set.** The facts, signals, records, and tools available to an actor at a specified time. Respecting that boundary is necessary when evaluating forecasts, experiments, agent behavior, or the reasonableness of a past decision. [M1 §1.17](modules/M01_Marketing_Analytics_and_Python.md#117-information-tools-and-a-verified-analysis); [M7 §7.44](modules/M07_Prediction_and_Machine_Learning.md#744-available-information-and-observed-answers).

**Instrumental Rationality.** Choosing effective means to a given end. A profitable or statistically efficient action can satisfy this criterion while leaving the worthiness of the end and reasons owed to others unresolved. [M9 §9.30](modules/M09_Marketing_Dialectics.md#930-what-a-company-ought-to-do); [M9 §9.41.4](modules/M09_Marketing_Dialectics.md#9414-deliberate-about-ends-before-optimizing-means).

**Instrumental Variable.** A source of treatment variation used to isolate a causal comparison under relevance, exclusion, and other design-specific assumptions. The resulting effect depends on the population and variation identified by those assumptions. [M3 §3.12](modules/M03_Regression.md#312-price-elasticity-when-prices-respond-to-demand); [M6 §6.9](modules/M06_Causal_Inference_and_Experiments.md#69-other-designs-discontinuities-and-instruments).

**Integration over Heterogeneity.** Averaging over a modeled distribution of differing preferences or response parameters when calculating a likelihood, prediction, or welfare quantity. The result inherits the specification, distributional assumptions, and definition of the target. [M4 §4.31](modules/M04_Conjoint_Segmentation_and_CLV.md#431-released-retail-data-integrated-heterogeneity-and-competing-explanations); [M9 §9.57](modules/M09_Marketing_Dialectics.md#957-heterogeneity-and-the-interpretation-of-consumer-harm).

**Intent-to-Treat Effect.** The effect of assignment to an intervention, regardless of subsequent compliance or uptake. It answers a policy question about offering or assigning the treatment under the implementation studied. [M6 §6.4](modules/M06_Causal_Inference_and_Experiments.md#64-case-study-estimate-an-email-assignment-effect).

**Interaction.** A specification in which the relationship between one variable and an outcome depends on another variable. Interpreting the model requires the relevant combination of coefficients and the support of the interacting variables. [M3 §3.5](modules/M03_Regression.md#35-interactions-describe-how-a-relationship-changes).

**Interference.** A situation in which one unit's outcome depends on another unit's treatment. It can undermine a comparison that treats customers, stores, or utilities as isolated and requires an exposure definition matched to the mechanism. [M6 §6.3](modules/M06_Causal_Inference_and_Experiments.md#63-designing-an-experiment-around-the-decision); [M6 §6.35](modules/M06_Causal_Inference_and_Experiments.md#635-institutional-exposure-and-the-meaning-of-an-untreated-utility).

**Internal Validity.** The credibility of the study's inference for the comparison and population it actually studies. Assignment, measurement, attrition, and analysis choices determine this credibility; broad external applicability is a separate question. [M6 §6.3](modules/M06_Causal_Inference_and_Experiments.md#63-designing-an-experiment-around-the-decision); [M6 §6.6](modules/M06_Causal_Inference_and_Experiments.md#66-implementation-checks-that-protect-the-comparison).

**Inverse Power.** Reasoning from a test's power properties and nonrejection to bounds or statements about effects still compatible with the result. It requires a specified test and assumptions; substituting the observed estimate for a meaningful alternative does not establish no harm. [M6 §6.34](modules/M06_Causal_Inference_and_Experiments.md#634-inverse-power-and-the-scope-of-nonrejection).

## J

**Join Cardinality.** The relationship between key occurrences in two tables, such as one-to-one or one-to-many. Unexpected many-to-many matches can duplicate records and change totals without producing a software error. [M1 §1.2](modules/M01_Marketing_Analytics_and_Python.md#12-the-unit-of-observation-determines-the-calculation); [M2 §2.2](modules/M02_Customer_Data_and_Visualization.md#22-build-a-customer-table-without-losing-customers).

**Justification.** Reasons adequate to support a belief, claim, or action. Empirical support for a response estimate and moral permission to use it answer different questions, each requiring premises suited to its conclusion. [M9 §9.3](modules/M09_Marketing_Dialectics.md#93-a-critical-examination-of-marketing-claims); [M9 §9.30](modules/M09_Marketing_Dialectics.md#930-what-a-company-ought-to-do).

## K

**K-Means.** A clustering procedure that seeks centers minimizing within-group squared distances. Feature scaling, the number of centers, initialization, and the geometry of the representation affect the resulting partition. [M4 §4.5](modules/M04_Conjoint_Segmentation_and_CLV.md#45-segmentation-begins-with-a-definition-of-similarity); [M4 §4.18](modules/M04_Conjoint_Segmentation_and_CLV.md#418-clustering-cost-and-the-meaning-of-a-segment).

**Known to Be the Never Known.** An expression for a principled limit on theoretical knowledge, developed through Kantian noumena. It is distinct from a presently unmeasured empirical quantity and does not license factual assertions without evidence. [M9 §9.41.5](modules/M09_Marketing_Dialectics.md#9415-the-known-to-be-the-never-known).

## L

**Label Shift.** A change in the prevalence of outcome classes across populations or periods while class-conditional feature distributions remain stable. Precision can change with prevalence even when class-conditional error rates remain fixed. [M5 §5.5](modules/M05_Text_Social_and_Network_Analysis.md#55-case-study-a-complaint-detector-under-changing-prevalence).

**Leakage.** See **Data Leakage**. [M7 §7.4](modules/M07_Prediction_and_Machine_Learning.md#74-validation-cross-validation-and-leakage).

**Learning Objective.** The quantity a training or adaptation procedure seeks to improve. Selecting the objective defines which responses count as success and requires justification when the resulting behavior affects people. [M9 §9.44](modules/M09_Marketing_Dialectics.md#944-personalization-and-the-learners-authority); [M7 §7.47](modules/M07_Prediction_and_Machine_Learning.md#747-a-predictable-response-and-a-defensible-objective).

**Legal Personhood.** Recognition of an entity as a bearer of rights or duties within a legal system. It is distinct from biological humanity, moral agency, and the grounds for moral protection. [M9 §9.65.2](modules/M09_Marketing_Dialectics.md#9652-corporate-duties-and-human-protections).

**Likelihood.** The probability or density of observed data viewed as a function of model parameters. It organizes evidence within the specified model and does not establish the adequacy of that model for a broader interpretation. [M4 §4.31](modules/M04_Conjoint_Segmentation_and_CLV.md#431-released-retail-data-integrated-heterogeneity-and-competing-explanations).

**LLM-as-Judge.** Use of a language model to score or label other outputs. Its judgments require validation against the intended rubric, error costs, stability across versions, and independence from the procedure being evaluated. [M5 §5.20](modules/M05_Text_Social_and_Network_Analysis.md#520-evaluate-the-grader-and-justify-the-rubric); [M7 §7.26](modules/M07_Prediction_and_Machine_Learning.md#726-evaluation-coverage-and-the-costs-of-grading-errors).

**Logical Validity.** A property of an argument in which the conclusion must follow if its premises are true. Validity concerns the inferential structure; the truth and evidential support of the premises require separate assessment. [M9 §9.27](modules/M09_Marketing_Dialectics.md#927-logical-assessment-of-an-empirical-argument); [M9 §9.40.1](modules/M09_Marketing_Dialectics.md#9401-validity-soundness-and-evidential-support).

**Logistic Regression.** A model that relates covariates to the log odds of a binary outcome. Its probability predictions are nonlinear in the covariates, and causal interpretations require additional design or identification assumptions. [M7 §7.3](modules/M07_Prediction_and_Machine_Learning.md#73-logistic-regression-trees-and-ensembles).

**Loss Function.** A rule assigning a cost to a prediction error or decision outcome. Its choice determines which mistakes the procedure prioritizes and may omit consumer burdens that matter to the decision. [M7 §7.2](modules/M07_Prediction_and_Machine_Learning.md#72-baselines-loss-functions-and-regularization); [M7 §7.7](modules/M07_Prediction_and_Machine_Learning.md#77-thresholds-should-reflect-the-decision).

## M

**Many Hands, Problem of.** The difficulty of allocating responsibility when many actors contribute to an outcome while knowledge and authority are distributed among them. Identifiable duties and records of decisions help prevent diffusion of accountability (Nissenbaum, 1996). [M9 §9.65.7](modules/M09_Marketing_Dialectics.md#9657-responsibility-for-the-artifact-and-its-uses).

**Marginal Effect.** The change in a modeled outcome associated with a small change in one input at specified values of other inputs. In nonlinear models, it can differ across observations and from the reported coefficient. [M3 §3.14](modules/M03_Regression.md#314-a-linear-coefficient-and-a-nonlinear-decision).

**Marginal Return.** The additional contribution generated by the next unit of spending or effort. Allocation decisions compare marginal returns under the relevant constraints, rather than assuming that the highest historical average return deserves the next dollar. [M8 §8.4](modules/M08_Current_Topics_and_Integrated_Decisions.md#84-case-study-allocate-the-next-dollar-using-marginal-returns).

**Market Power.** The ability to profitably sustain prices or other terms above a relevant competitive benchmark. Assessing it requires attention to substitution, entry, constraints, and the conduct at issue, alongside estimated demand. [M4 §4.30](modules/M04_Conjoint_Segmentation_and_CLV.md#430-heterogeneous-demand-market-power-and-consumer-interests); [M9 §9.38](modules/M09_Marketing_Dialectics.md#938-pricing-evidence-in-a-us-antitrust-case).

**Marketing Dialectics.** Critical examination of the premises connecting commercial results, claims about customers, and recommendations. This application draws on philosophical dialectic and ethical justification while preserving the distinction from a technical Kantian antinomy. [M9 §9.2](modules/M09_Marketing_Dialectics.md#92-transcendental-dialectic-and-the-limits-of-reason); [M9 §9.3](modules/M09_Marketing_Dialectics.md#93-a-critical-examination-of-marketing-claims).

**Marketing-Mix Model.** A model relating marketing activity and other covariates to an outcome over time or across units. Carryover, saturation, confounding, and the chosen outcome affect the meaning of budget recommendations. [M8 §8.3](modules/M08_Current_Topics_and_Integrated_Decisions.md#83-marketing-mix-models-combine-carryover-and-saturation).

**Maxim.** A subjective principle of action stated through its circumstance, action, and end. Moral assessment requires a faithful account of the operative principle, including the purpose of a restriction or assurance (Kant, 1785). [M9 §9.65.8](modules/M09_Marketing_Dialectics.md#9658-maxims-of-data-production-and-disclosure).

**Mean Absolute Error (MAE).** The average absolute difference between predictions and observed outcomes over a specified sample. It preserves the outcome's units and weights errors linearly, so evaluation still requires a sample and loss appropriate to the decision. [M7 §7.2](modules/M07_Prediction_and_Machine_Learning.md#72-baselines-loss-functions-and-regularization).

**Measurement.** The process of representing a defined attribute through observations and rules. Accuracy in recording a variable leaves a further question about whether that variable represents the substantive object named in a claim. [M2 §2.28](modules/M02_Customer_Data_and_Visualization.md#228-electricity-prices-household-bills-and-the-unit-of-harm); [M9 §9.60](modules/M09_Marketing_Dialectics.md#960-the-ontology-of-a-dataset).

**Measurement Error.** A discrepancy between a recorded measure and the quantity it is intended to represent. Its consequences depend on how the error relates to treatment, outcomes, covariates, and selection. [M2 §2.16](modules/M02_Customer_Data_and_Visualization.md#216-mcdonalds-measuring-ice-cream-availability); [M9 §9.68](modules/M09_Marketing_Dialectics.md#968-worked-assessments-of-the-missing-object).

**Mediator.** A variable on a causal pathway from treatment to outcome. Adjusting for it can remove part of the total effect and requires additional assumptions if the target is a direct effect. [M3 §3.20](modules/M03_Regression.md#320-a-control-variable-needs-a-causal-role); [M6 §6.40](modules/M06_Causal_Inference_and_Experiments.md#640-treatment-affected-covariates-in-a-panel).

**Minimum Detectable Effect (MDE).** The effect magnitude associated with a chosen power under a specified design, significance level, and alternative. It is a design quantity, and it need not equal the smallest effect that matters economically. [M6 §6.5](modules/M06_Causal_Inference_and_Experiments.md#65-power-precision-and-the-minimum-useful-effect); [M6 §6.32](modules/M06_Causal_Inference_and_Experiments.md#632-statistical-detection-and-a-profitable-campaign).

**Missingness.** Absence of a record or value that the analysis would otherwise use. Missing observations can represent unrecorded activity, unavailable documents, or loss to follow-up; treating them as zeros requires substantive justification. [M2 §2.2](modules/M02_Customer_Data_and_Visualization.md#22-build-a-customer-table-without-losing-customers); [M2 §2.10](modules/M02_Customer_Data_and_Visualization.md#210-mhealth-recorded-variety-and-missing-days).

**Modality.** The status of a claim as possible, necessary, or actual. Showing that a model permits a reassuring explanation does not establish that the explanation occurred, and identifying a possible burden does not establish its realized magnitude. [M9 §9.40.3](modules/M09_Marketing_Dialectics.md#9403-compatibility-identification-and-valuation).

**Moral Agency.** The capacity of an actor to bear moral obligations and answer for choices. Arguments that an organization can bear duties do not by themselves establish that it has all the moral protections of a human person. [M9 §9.65.2](modules/M09_Marketing_Dialectics.md#9652-corporate-duties-and-human-protections).

**Moral Standing.** The status of having interests or claims that count directly in moral evaluation. It is distinct from legal personhood and from the capacity to make morally responsible choices. [M9 §9.65.2](modules/M09_Marketing_Dialectics.md#9652-corporate-duties-and-human-protections).

**Multiple Testing.** Examining several hypotheses or outcomes within a research process. Interpreting selected significant findings requires attention to the family of comparisons, selection rules, and the error criterion being controlled. [M6 §6.30](modules/M06_Causal_Inference_and_Experiments.md#630-store-assignment-and-false-discoveries).

## N

**Network Centrality.** A measure of a node's position or importance in a specified graph. Degree, brokerage, and path-based measures answer different questions; a high score does not automatically establish influence on purchasing. [M5 §5.7](modules/M05_Text_Social_and_Network_Analysis.md#57-networks-connections-reach-and-brokerage).

**Non-Disclosure Agreement (NDA).** An agreement restricting access to or disclosure of information. Its evidential and moral significance depends on the actual terms governing selection, analysis, publication, preservation, and independent challenge. [M9 §9.63](modules/M09_Marketing_Dialectics.md#963-research-under-confidentiality-agreements); [M9 §9.65.5](modules/M09_Marketing_Dialectics.md#9655-worked-case-confidentiality-and-corporate-accountability).

**Noninferiority Test.** A test asking whether an outcome is no worse than a reference by more than a specified margin. The direction, units, margin, and assumptions must match the practical assurance being offered. [M6 §6.47](modules/M06_Causal_Inference_and_Experiments.md#647-choosing-the-null-for-a-claim-about-harm).

**Nonrejection.** A test outcome that does not meet the rule for rejecting its null hypothesis. Its substantive meaning depends on uncertainty and the effects the procedure could detect or exclude; it does not alone establish absence or negligibility. [M6 §6.33](modules/M06_Causal_Inference_and_Experiments.md#633-testing-electricity-price-interpretations-against-the-reported-tables); [M6 §6.47](modules/M06_Causal_Inference_and_Experiments.md#647-choosing-the-null-for-a-claim-about-harm).

**Norm.** A standard concerning belief, conduct, or institutional practice. Distinguishing epistemic, moral, legal, and professional norms prevents success under one standard from being treated as sufficient under all the others. [M9 §9.52](modules/M09_Marketing_Dialectics.md#952-truth-warrant-and-the-different-force-of-norms).

**Normalized Discounted Cumulative Gain (NDCG).** A ranking measure comparing position-discounted relevance with the best ordering under the same relevance labels. The cutoff, gain scale, candidate set, and label availability determine the comparison. [M7 §7.11](modules/M07_Prediction_and_Machine_Learning.md#711-ranking-metrics-depend-on-position-and-available-labels).

**Normative Premise.** A premise about what ought to be done, permitted, or valued. It supplies a necessary part of an argument that moves from a descriptive or causal finding to a recommendation. [M9 §9.30](modules/M09_Marketing_Dialectics.md#930-what-a-company-ought-to-do); [M9 §9.40.5](modules/M09_Marketing_Dialectics.md#9405-from-a-conditional-result-to-an-ought-conclusion).

**Noumenon.** An object considered apart from the conditions of sensible intuition. In its negative Kantian use, it marks a limit on theoretical cognition; it is not simply an unmeasured variable awaiting a better dataset (Kant, 1781/1787). [M9 §9.41](modules/M09_Marketing_Dialectics.md#941-phenomena-noumena-and-the-ends-of-analysis).

**Null Hypothesis.** The parameter restriction or class of states against which a statistical procedure evaluates evidence. A zero-effect null and a null containing harmful effects pose different inferential questions. [M6 §6.47](modules/M06_Causal_Inference_and_Experiments.md#647-choosing-the-null-for-a-claim-about-harm).

## O

**Observation Unit.** The entity or event represented by one analytical record. A food entry, customer-day, utility-year, and household bill describe different objects, even when each becomes a row in a table. [M1 §1.2](modules/M01_Marketing_Analytics_and_Python.md#12-the-unit-of-observation-determines-the-calculation); [M2 §2.28](modules/M02_Customer_Data_and_Visualization.md#228-electricity-prices-household-bills-and-the-unit-of-harm).

**Observational Equivalence.** A situation in which different mechanisms or parameter configurations produce the same available observations. Additional data, assumptions, or a different design are needed to distinguish their substantive implications. [M6 §6.38](modules/M06_Causal_Inference_and_Experiments.md#638-equal-historical-fit-and-different-price-effects); [M9 §9.35](modules/M09_Marketing_Dialectics.md#935-identical-tested-demand-and-opposite-welfare-conclusions).

**Off-Policy Evaluation.** Estimating the value of a policy using observations collected under another policy. Validity depends on information about exposure or assignment, support for the proposed actions, and assumptions linking recorded outcomes to the target policy. [M6 §6.11](modules/M06_Causal_Inference_and_Experiments.md#611-ai-assisted-workflow-and-practice); [M8 §8.1](modules/M08_Current_Topics_and_Integrated_Decisions.md#81-recommendation-systems-learn-from-selected-exposure).

**Omitted-Variable Bias.** A difference between a regression coefficient and its intended target caused by leaving out a relevant variable correlated with included regressors. The interpretation depends on the model and the target of the coefficient. [M3 §3.2](modules/M03_Regression.md#32-multiple-regression-and-the-comparison-it-uses); [M3 §3.3](modules/M03_Regression.md#33-case-study-attractive-markets-and-apparent-competitive-benefits).

**Ontological Adequacy.** The defensibility of an analysis's account of the entities, interests, and relationships named in its substantive claim. Better statistical performance for a chosen variable need not improve that account. [M9 §9.42](modules/M09_Marketing_Dialectics.md#942-a-spectrum-of-ontological-adequacy); [M9 §9.66](modules/M09_Marketing_Dialectics.md#966-statistical-virtues-and-ontological-laziness).

**Ontological Laziness.** Treating a convenient representation as an adequate account of the relevant reality without defending the connection. A substantive criticism identifies the omitted relation and explains how it could change the interpretation or decision. [M9 §9.66](modules/M09_Marketing_Dialectics.md#966-statistical-virtues-and-ontological-laziness).

**Ontology.** Inquiry into what exists and the kinds of entities and relationships involved. In analytics, it asks what a customer, outcome, burden, or data object is before a convenient field is treated as its complete representation. [M9 §9.19](modules/M09_Marketing_Dialectics.md#919-definitions-evidence-and-permission); [M9 §9.60](modules/M09_Marketing_Dialectics.md#960-the-ontology-of-a-dataset).

**Operationalization.** The rules translating a construct into a recorded variable or analytical procedure. Counting completed renewals operationalizes a billing status; interpreting it as voluntary continuation requires further evidence. [M2 §2.25](modules/M02_Customer_Data_and_Visualization.md#225-cancellation-requests-and-recorded-completion); [M9 §9.61](modules/M09_Marketing_Dialectics.md#961-what-the-artifact-makes-visible).

**Opportunity Cost.** The value of the best feasible alternative forgone by a decision. It depends on the alternatives available to the relevant actor and should not be confused with an observed expenditure alone. [M4 §4.16](modules/M04_Conjoint_Segmentation_and_CLV.md#416-ai-services-buyer-burden-and-the-outside-option); [M8 §8.4](modules/M08_Current_Topics_and_Integrated_Decisions.md#84-case-study-allocate-the-next-dollar-using-marginal-returns).

**Ordinary Least Squares (OLS).** An estimator choosing coefficients to minimize the sum of squared residuals in a linear regression. Causal, predictive, and descriptive uses require different interpretations and supporting assumptions. [M3 §3.1](modules/M03_Regression.md#31-a-conditional-mean-and-a-regression-line).

**Ought.** A claim about what an actor should do. Its defense requires reasons and normative premises alongside empirical evidence about the feasible actions and their consequences. [M9 §9.30](modules/M09_Marketing_Dialectics.md#930-what-a-company-ought-to-do); [M9 §9.40.5](modules/M09_Marketing_Dialectics.md#9405-from-a-conditional-result-to-an-ought-conclusion).

**Outcome.** The quantity evaluated after or in relation to an action. Its definition specifies the observation unit, units, timing, and population, and determines which consequences enter the analysis. [M6 §6.1](modules/M06_Causal_Inference_and_Experiments.md#61-define-the-treatment-outcome-and-estimand); [M2 §2.32](modules/M02_Customer_Data_and_Visualization.md#232-defining-harm-before-choosing-its-measure).

**Outside Option.** The alternative available if a customer declines the focal offer. Access, switching costs, essential needs, and information can make this option materially different across customers. [M4 §4.16](modules/M04_Conjoint_Segmentation_and_CLV.md#416-ai-services-buyer-burden-and-the-outside-option); [M9 §9.22](modules/M09_Marketing_Dialectics.md#922-pricing-authority-and-customer-alternatives).

**Overfitting.** Adapting a model or decision process to idiosyncrasies of the development data so that reported fit exceeds performance on independent cases. Repeated prompt revision can create the same problem as repeated model tuning. [M7 §7.4](modules/M07_Prediction_and_Machine_Learning.md#74-validation-cross-validation-and-leakage); [M5 §5.15](modules/M05_Text_Social_and_Network_Analysis.md#515-repeated-prompt-revision-and-independent-text-evaluation).

**Overlap.** Availability of treatment or action variation across the covariate values relevant to a causal or policy comparison. Weak overlap can make estimates depend heavily on a few observations or on extrapolation. [M6 §6.24](modules/M06_Causal_Inference_and_Experiments.md#624-overlap-weight-concentration-and-missing-confounders).

## P

**P-Value.** The probability, under the null hypothesis and test assumptions, of a statistic at least as incompatible with the null as the observed statistic according to the test's ordering. It is not the probability that the null is true. [M3 §3.19](modules/M03_Regression.md#319-p-values-across-repeated-marketing-experiments); [M6 §6.33](modules/M06_Causal_Inference_and_Experiments.md#633-testing-electricity-price-interpretations-against-the-reported-tables).

**Panel Data.** Repeated observations on the same units over time. Their analysis must account for dependence, changing composition, timing, and the distinction between differences across units and changes within units. [M3 §3.7](modules/M03_Regression.md#37-diagnostics-and-panel-data); [M2 §2.22](modules/M02_Customer_Data_and_Visualization.md#222-customer-differences-and-changes-within-customers).

**Parallel Trends.** A condition that treated and comparison groups would have followed the specified common trend in the absence of treatment. Similar observed pre-treatment trends may inform its plausibility but cannot prove the unobserved counterfactual. [M6 §6.8](modules/M06_Causal_Inference_and_Experiments.md#68-difference-in-differences-and-a-counterfactual-trend); [M6 §6.27](modules/M06_Causal_Inference_and_Experiments.md#627-continuous-treatment-and-parallel-trends).

**Partial Identification.** Learning a set of values consistent with the available evidence and assumptions when a unique value is not determined. Its usefulness depends on the decision and the consequences associated with the remaining possibilities. [M9 §9.40.3](modules/M09_Marketing_Dialectics.md#9403-compatibility-identification-and-valuation); [M6 §6.45](modules/M06_Causal_Inference_and_Experiments.md#645-evidence-for-action-before-precise-identification).

**Partial Pooling.** Estimating unit-specific quantities while sharing information through a common model. It can reduce variance and pull estimates toward a group distribution, with consequences that depend on the degree of pooling and substantive heterogeneity. [M6 §6.26](modules/M06_Causal_Inference_and_Experiments.md#626-store-decisions-and-partial-pooling); [M6 §6.46](modules/M06_Causal_Inference_and_Experiments.md#646-greater-precision-and-fewer-detected-harms).

**Personalization.** Adapting an offer, price, message, or ranking to information about a person. Evaluating it requires attention to the objective, customer alternatives, distribution of burdens, and authority to revise or reject the resulting treatment. [M9 §9.7](modules/M09_Marketing_Dialectics.md#97-personalization-learning-and-the-ability-to-revise-a-goal); [M8 §8.20](modules/M08_Current_Topics_and_Integrated_Decisions.md#820-ai-experimentation-and-personalized-pricing).

**Phantom Data Center.** A proposed or anticipated project that does not become an operating facility in the relevant period. Preparatory expenditure can precede failure or withdrawal, so operating-facility data can miss economically relevant exposure. [M6 §6.35](modules/M06_Causal_Inference_and_Experiments.md#635-institutional-exposure-and-the-meaning-of-an-untreated-utility); [M6 §6.41](modules/M06_Causal_Inference_and_Experiments.md#641-phantom-projects-and-the-meaning-of-a-control).

**Phenomenon.** An object as it appears under the conditions of experience. The Kantian discussion distinguishes empirical inquiry into appearances from claims to theoretical knowledge of things considered independently of those conditions. [M9 §9.41](modules/M09_Marketing_Dialectics.md#941-phenomena-noumena-and-the-ends-of-analysis).

**Physical Activity Level (PAL).** A measure of total energy expenditure relative to basal metabolic rate over a defined period. An assumed PAL in a dietary screen should be distinguished from an individually measured value. [M2 §2.11](modules/M02_Customer_Data_and_Visualization.md#211-mhealth-nutrition-knowledge-and-sample-restrictions).

**Policy Value.** The expected outcome under a specified rule for choosing actions. Its interpretation depends on the target population, reward definition, information, and assumptions supporting evaluation of that rule. [M6 §6.11](modules/M06_Causal_Inference_and_Experiments.md#611-ai-assisted-workflow-and-practice); [M8 §8.1](modules/M08_Current_Topics_and_Integrated_Decisions.md#81-recommendation-systems-learn-from-selected-exposure).

**Post-Treatment Variable.** A variable determined after treatment and potentially affected by it. Conditioning on such a variable can block part of the effect, induce selection, or change the population being compared. [M3 §3.20](modules/M03_Regression.md#320-a-control-variable-needs-a-causal-role); [M6 §6.40](modules/M06_Causal_Inference_and_Experiments.md#640-treatment-affected-covariates-in-a-panel).

**Posterior Distribution.** The distribution over unknown quantities obtained by combining a prior with the likelihood of observed data. It quantifies uncertainty conditional on the chosen model and prior. [M4 §4.31](modules/M04_Conjoint_Segmentation_and_CLV.md#431-released-retail-data-integrated-heterogeneity-and-competing-explanations); [M9 §9.57](modules/M09_Marketing_Dialectics.md#957-heterogeneity-and-the-interpretation-of-consumer-harm).

**Power.** The probability of rejecting a null hypothesis under a specified alternative and design. Power is relative to an effect and test; a statement that a study is well powered needs a substantively relevant alternative. [M6 §6.5](modules/M06_Causal_Inference_and_Experiments.md#65-power-precision-and-the-minimum-useful-effect); [M6 §6.34](modules/M06_Causal_Inference_and_Experiments.md#634-inverse-power-and-the-scope-of-nonrejection).

**Precision.** In estimation, the concentration of an estimator's sampling distribution, often summarized by its standard error. In classification, precision is the share of predicted positives that are reference positives. The two meanings use different denominators and answer different questions. [M3 §3.6](modules/M03_Regression.md#36-uncertainty-dependence-and-practical-importance); [M5 §5.5](modules/M05_Text_Social_and_Network_Analysis.md#55-case-study-a-complaint-detector-under-changing-prevalence).

**Prediction Interval.** A range intended to cover a future outcome or another specified predictive target. It includes variation relevant to that target and differs from uncertainty about an estimated mean or parameter. [M7 §7.24](modules/M07_Prediction_and_Machine_Learning.md#724-demand-intervals-and-the-distribution-of-forecast-errors).

**Premise.** A proposition offered in support of a conclusion. A useful assessment identifies whether it is definitional, empirical, theoretical, or normative, and examines the evidence or reasons needed to defend it. [M9 §9.27](modules/M09_Marketing_Dialectics.md#927-logical-assessment-of-an-empirical-argument); [M9 §9.40](modules/M09_Marketing_Dialectics.md#940-logical-consequence-and-a-defensible-recommendation).

**Price Discrimination.** Charging different prices across customers or transactions beyond differences explained by the relevant cost comparison. Its economic, legal, and moral evaluation depends on the conduct, setting, alternatives, and distribution of gains and burdens. [M9 §9.15](modules/M09_Marketing_Dialectics.md#915-pricing-policy-what-conduct-is-being-evaluated); [M9 §9.38](modules/M09_Marketing_Dialectics.md#938-pricing-evidence-in-a-us-antitrust-case).

**Prior Distribution.** A distribution representing assumptions or information about unknown quantities before updating with the specified data. Its influence should be evaluated where evidence is weak or pooling affects consequential individual conclusions. [M4 §4.31](modules/M04_Conjoint_Segmentation_and_CLV.md#431-released-retail-data-integrated-heterogeneity-and-competing-explanations); [M9 §9.57](modules/M09_Marketing_Dialectics.md#957-heterogeneity-and-the-interpretation-of-consumer-harm).

**Privacy.** Protection of people's interests in the collection, use, and disclosure of information about them. A corporation's commercial confidentiality requires its own justification and is not automatically equivalent to a person's privacy claim. [M9 §9.65.2](modules/M09_Marketing_Dialectics.md#9652-corporate-duties-and-human-protections); [M9 §9.65.3](modules/M09_Marketing_Dialectics.md#9653-a-philosophical-argument-against-protective-secrecy).

**Propensity Score.** The probability of treatment conditional on specified pre-treatment covariates. It can support adjustment under appropriate assignment assumptions and overlap, while balance on observed covariates leaves unobserved confounding unresolved. [M6 §6.7](modules/M06_Causal_Inference_and_Experiments.md#67-observational-adjustment-and-its-limits).

**Proxy.** A recorded variable used to represent another construct or quantity. Its convenience or predictive association does not establish that it preserves the meaning of the claim or the interests relevant to the decision. [M2 §2.28](modules/M02_Customer_Data_and_Visualization.md#228-electricity-prices-household-bills-and-the-unit-of-harm); [M9 §9.68](modules/M09_Marketing_Dialectics.md#968-worked-assessments-of-the-missing-object).

**Publication Bias.** Selection into the public research record associated with findings or their perceived publishability. Accurate calculations within published studies do not by themselves repair the resulting distortion in the visible evidence. [M9 §9.53](modules/M09_Marketing_Dialectics.md#953-undone-science-and-the-distribution-of-evidence); [M9 §9.63.3](modules/M09_Marketing_Dialectics.md#9633-selection-before-and-after-estimation).

## Q

**Qualitative Evidence.** Interpretive evidence from documents, statements, observations, or other contextual records. Credible use preserves provenance, sampling, exact meaning, contrary cases, and the distinction between an actor's stated account and independently established conduct. [M5 §5.27](modules/M05_Text_Social_and_Network_Analysis.md#527-utility-disclosures-as-qualitative-evidence); [M6 §6.36](modules/M06_Causal_Inference_and_Experiments.md#636-qualitative-mechanisms-and-a-causal-comparison).

## R

**Random Assignment.** Allocation of treatment using a chance mechanism with known or controlled probabilities. It supports comparable groups in expectation, while finite-sample imbalance, noncompliance, missing outcomes, and interference still require assessment. [M6 §6.3](modules/M06_Causal_Inference_and_Experiments.md#63-designing-an-experiment-around-the-decision); [M6 §6.6](modules/M06_Causal_Inference_and_Experiments.md#66-implementation-checks-that-protect-the-comparison).

**Random Seed.** An initialization controlling a pseudorandom generator's sequence. Recording it supports reproduction within a specified environment, while exact agreement can also depend on libraries, algorithms, ordering, and parallel execution. [M1 §1.3](modules/M01_Marketing_Analytics_and_Python.md#13-python-objects-and-reproducible-calculations); [M6 §6.13](modules/M06_Causal_Inference_and_Experiments.md#613-mhealth-planning-a-randomized-suggestion-test).

**Randomization Inference.** Inference based on the distribution of a statistic over assignments permitted by the experimental design, often under a sharp null. Its validity rests on the assignment mechanism and the tested hypothesis. [M6 §6.15](modules/M06_Causal_Inference_and_Experiments.md#615-mhealth-prior-activity-and-experiment-precision); [M6 §6.30](modules/M06_Causal_Inference_and_Experiments.md#630-store-assignment-and-false-discoveries).

**Ranking.** Ordering alternatives according to a score or rule. Ranking quality differs from calibrated probability, forecasted quantities, and consumer welfare, each of which requires its own target and evaluation. [M7 §7.6](modules/M07_Prediction_and_Machine_Learning.md#76-ranking-and-calibration-answer-different-questions); [M7 §7.23](modules/M07_Prediction_and_Machine_Learning.md#723-the-same-ranking-can-produce-different-demand-forecasts).

**Reasonable Rejection.** An objection to a general principle grounded in an affected person's reasons, burdens, and feasible alternatives. It is a standard of interpersonal justification, not a count of disapproval or a rule that every preference must prevail (Scanlon, 1998). [M9 §9.30](modules/M09_Marketing_Dialectics.md#930-what-a-company-ought-to-do); [M9 §9.65.8](modules/M09_Marketing_Dialectics.md#9658-maxims-of-data-production-and-disclosure).

**Reasonableness.** The acceptability of reasons and conduct in light of relevant persons, burdens, and alternatives. Efficient pursuit of a firm's chosen goal can leave reasonableness unresolved when others bear consequences they could reasonably reject. [M9 §9.30](modules/M09_Marketing_Dialectics.md#930-what-a-company-ought-to-do); [M9 §9.58](modules/M09_Marketing_Dialectics.md#958-a-reasonable-principle-for-acting-under-uncertainty).

**Recall.** The share of reference-positive cases identified as positive by a classifier. Improving recall can increase false positives, so the operating point requires attention to both the evaluation population and the decisions triggered. [M5 §5.5](modules/M05_Text_Social_and_Network_Analysis.md#55-case-study-a-complaint-detector-under-changing-prevalence); [M7 §7.5](modules/M07_Prediction_and_Machine_Learning.md#75-case-study-accuracy-can-conceal-a-useless-model).

**Receiver Operating Characteristic (ROC) Curve.** A comparison of true-positive and false-positive rates as a binary-score threshold varies. It describes classification tradeoffs but leaves action costs, class prevalence, and a justified deployment threshold to be specified. [M7 §7.6](modules/M07_Prediction_and_Machine_Learning.md#76-ranking-and-calibration-answer-different-questions).

**Recency, Frequency, and Monetary Value (RFM).** Customer summaries of time since a recorded transaction, transaction frequency, and recorded expenditure over defined windows. Their construction requires a common reference date and consistent treatment of missing activity and observation length. [M2 §2.13](modules/M02_Customer_Data_and_Visualization.md#213-mhealth-recency-and-frequency-at-a-fixed-date).

**Reciprocity.** Examination of one's treatment of others from their position. In the Confucian application, it motivates attention to customers' actual resources and purposes, rather than assuming that the manager's own tolerance defines acceptable treatment. [M9 §9.11.3](modules/M09_Marketing_Dialectics.md#9113-remonstrance-reciprocity-and-learning).

**Rectification of Names.** A Confucian concern with the relationship among descriptions, social roles, and appropriate conduct. Calling a process customer care or cancellation carries expectations about what the service should actually accomplish. [M9 §9.11.2](modules/M09_Marketing_Dialectics.md#9112-trustworthiness-and-the-responsibilities-of-a-role); [M9 §9.19](modules/M09_Marketing_Dialectics.md#919-definitions-evidence-and-permission).

**Regression Discontinuity (RD).** A design comparing outcomes near a treatment-assignment threshold. A causal interpretation requires conditions about continuity, sorting, and treatment implementation and typically concerns units near that cutoff. [M6 §6.9](modules/M06_Causal_Inference_and_Experiments.md#69-other-designs-discontinuities-and-instruments).

**Regularization.** A restriction or penalty that limits model complexity or shrinks fitted parameters. It can improve out-of-sample performance while changing bias, variance, and the behavior of estimates for particular groups. [M7 §7.2](modules/M07_Prediction_and_Machine_Learning.md#72-baselines-loss-functions-and-regularization).

**Remedial Responsibility.** A duty to help correct harm, repair an unreliable public claim, or change the process producing the problem. It can follow from capacity and institutional connection even when personal culpability remains unresolved. [M9 §9.65.7](modules/M09_Marketing_Dialectics.md#9657-responsibility-for-the-artifact-and-its-uses); [M9 §9.84.4](modules/M09_Marketing_Dialectics.md#9844-the-harm-and-the-duty-to-correct).

**Remonstrance.** Reasoned, truthful challenge offered within a relationship of service or authority. Its organizational application requires an effective opportunity to raise objections and have them considered, including objections to a profitable practice. [M9 §9.11.3](modules/M09_Marketing_Dialectics.md#9113-remonstrance-reciprocity-and-learning).

**Replication.** Using newly collected data to examine the same scientific question. Its design and target must be stated, and a failure to replicate does not by itself establish fabrication in the earlier study. [M9 §9.84.1](modules/M09_Marketing_Dialectics.md#9841-three-questions-about-a-research-claim).

**Reproducibility.** Obtaining consistent computational results using the same data, code, and analytical procedure. It supports checking calculations while leaving separate questions about source integrity, identification, and moral justification. [M2 §2.35](modules/M02_Customer_Data_and_Visualization.md#235-reproducing-a-result-and-assessing-its-records); [M9 §9.84.1](modules/M09_Marketing_Dialectics.md#9841-three-questions-about-a-research-claim).

**Research Integrity.** Responsibilities supporting trustworthy production, interpretation, preservation, and correction of research. A reliable public record requires incentives and institutions that permit independent scrutiny as well as accurate computation. [M9 §9.84](modules/M09_Marketing_Dialectics.md#984-misleading-research-replication-and-correction).

**Residual.** The difference between an observed outcome and its fitted value. A residual can contain unexplained variation, measurement error, or omitted mechanisms; its label does not identify a substantive cause. [M3 §3.1](modules/M03_Regression.md#31-a-conditional-mean-and-a-regression-line); [M8 §8.31](modules/M08_Current_Topics_and_Integrated_Decisions.md#831-hbs-reassurance-and-misleading-research-communication).

**Responsibility.** An allocation of causal contribution, role duties, accountability, blame, or repair. These meanings should be distinguished because control over a data artifact and authority over its use can lie with different actors. [M9 §9.65.7](modules/M09_Marketing_Dialectics.md#9657-responsibility-for-the-artifact-and-its-uses).

**Retention.** Continued observed participation or subscription under a specified rule and horizon. A retained account can coexist with an unresolved cancellation request, so interpreting retention as voluntary loyalty requires additional evidence. [M2 §2.4](modules/M02_Customer_Data_and_Visualization.md#24-cohorts-retention-and-customer-age); [M2 §2.34](modules/M02_Customer_Data_and_Visualization.md#234-worked-example-retention-and-pending-cancellation).

**Retraction.** A formal withdrawal of reliance on a published article because of stated reliability or other publication concerns. The notice's grounds determine its scope; retraction alone does not identify which person knowingly caused a defect. [M9 §9.84](modules/M09_Marketing_Dialectics.md#984-misleading-research-replication-and-correction).

**Righteousness.** Judging conduct through what is appropriate or morally required, including constraints on the pursuit of gain. In the Confucian discussion, profit alone leaves the justification of means and relationships unresolved. [M9 §9.11.1](modules/M09_Marketing_Dialectics.md#9111-righteousness-and-profit).

**Ritual Propriety (Li).** Patterned social conduct associated with cultivation and appropriate relationships in Confucian thought. Its role extends beyond formal compliance, and the term should be distinguished from the separately written Chinese word for profit also romanized as li. [M9 §9.11.4](modules/M09_Marketing_Dialectics.md#9114-moral-beginnings-and-cultivated-conduct).

**Role Responsibility.** Duties attached to an actor's position and authority, such as preserving source records or correcting a public statement. Performance is assessed against what the role required and what the person could reasonably know and do. [M9 §9.65.7](modules/M09_Marketing_Dialectics.md#9657-responsibility-for-the-artifact-and-its-uses).

**Root Mean Squared Error (RMSE).** The square root of the average squared prediction error over a specified sample. It has the outcome's units and gives larger errors more influence than mean absolute error. [M7 §7.2](modules/M07_Prediction_and_Machine_Learning.md#72-baselines-loss-functions-and-regularization).

## S

**Sample Selection.** The process determining which units or observations enter an analysis. Selection can change representation, create associations, or remove important exposures, even when the retained observations are measured accurately. [M2 §2.18](modules/M02_Customer_Data_and_Visualization.md#218-sample-restrictions-and-customer-representation); [M6 §6.42](modules/M06_Causal_Inference_and_Experiments.md#642-thoughtful-design-before-convenient-data).

**Saturation.** A decline in the additional response generated by further exposure or spending. Estimating a saturation curve requires sufficient support and a defensible interpretation of the relationship between spending and response. [M8 §8.3](modules/M08_Current_Topics_and_Integrated_Decisions.md#83-marketing-mix-models-combine-carryover-and-saturation).

**Sensitivity Analysis.** Examining how a conclusion changes when specified assumptions, inputs, or modeling choices vary. A useful exercise identifies the changed object, plausible range, and implication for the decision. [M6 §6.24](modules/M06_Causal_Inference_and_Experiments.md#624-overlap-weight-concentration-and-missing-confounders); [M6 §6.50](modules/M06_Causal_Inference_and_Experiments.md#650-bias-missing-outcomes-and-the-scope-of-reassurance).

**Sentiment Analysis.** Classifying or scoring evaluative language in a defined text unit. Performance depends on context, reference labels, prevalence, and whether the sentiment construct fits the managerial question. [M5 §5.4](modules/M05_Text_Social_and_Network_Analysis.md#54-sentiment-aspect-labels-and-topic-models); [M5 §5.5](modules/M05_Text_Social_and_Network_Analysis.md#55-case-study-a-complaint-detector-under-changing-prevalence).

**Shrinkage.** Movement of an estimate toward a reference value or shared distribution through a penalty or statistical model. Its consequences depend on the target and heterogeneity; smaller variance need not preserve detection of every subgroup burden. [M6 §6.46](modules/M06_Causal_Inference_and_Experiments.md#646-greater-precision-and-fewer-detected-harms); [M9 §9.57](modules/M09_Marketing_Dialectics.md#957-heterogeneity-and-the-interpretation-of-consumer-harm).

**Soundness.** The property of an argument that is logically valid and has true premises. In an empirical assessment, the analyst must also explain the evidence supporting those premises and the scope of their interpretation. [M9 §9.40.1](modules/M09_Marketing_Dialectics.md#9401-validity-soundness-and-evidential-support).

**Spillover.** An effect of one unit's treatment on another unit's outcome. Spillovers can expose nominal controls or alter the population relevant to an experiment, requiring a design that represents the transmission mechanism. [M6 §6.3](modules/M06_Causal_Inference_and_Experiments.md#63-designing-an-experiment-around-the-decision); [M6 §6.35](modules/M06_Causal_Inference_and_Experiments.md#635-institutional-exposure-and-the-meaning-of-an-untreated-utility).

**Stakeholder.** A person or group with interests, claims, or exposure relevant to a decision. Moral standing does not depend solely on the person's bargaining power, profitability, or ability to attract institutional attention. [M9 §9.32](modules/M09_Marketing_Dialectics.md#932-who-counts-as-a-stakeholder-and-why).

**Standard Error.** An estimate of the sampling variability of an estimator under a specified design or model. It differs from the spread of individual outcomes and must reflect the relevant dependence structure. [M3 §3.6](modules/M03_Regression.md#36-uncertainty-dependence-and-practical-importance).

**Statistical Significance.** A test result meeting a specified rejection threshold under the test's assumptions. It concerns compatibility with the tested null, while effect magnitude, decision value, and moral permission require further assessment. [M3 §3.19](modules/M03_Regression.md#319-p-values-across-repeated-marketing-experiments); [M6 §6.33](modules/M06_Causal_Inference_and_Experiments.md#633-testing-electricity-price-interpretations-against-the-reported-tables).

**Statistical Unbiasedness.** The property that an estimator's expectation equals its target under the assumed process. It does not establish that the target captures the relevant consumer burden or that the associated decision rule is justified. [M3 §3.22](modules/M03_Regression.md#322-unbiased-estimation-and-the-consequences-of-error); [M9 §9.66](modules/M09_Marketing_Dialectics.md#966-statistical-virtues-and-ontological-laziness).

**Structural Model.** A model linking observed behavior to an explicit account of preferences, constraints, technology, or strategic interaction. Counterfactual conclusions depend on the identification and stability of the structure under the proposed change. [M4 §4.30](modules/M04_Conjoint_Segmentation_and_CLV.md#430-heterogeneous-demand-market-power-and-consumer-interests); [M6 §6.38](modules/M06_Causal_Inference_and_Experiments.md#638-equal-historical-fit-and-different-price-effects).

**Substantive Interpretation.** An account of what an analytical finding means for the people, institutions, or decision under study. It connects the statistical object to the claimed mechanism or burden through explicit, supported premises. [M1 §1.6](modules/M01_Marketing_Analytics_and_Python.md#16-interpreting-and-communicating-a-result); [M9 §9.68](modules/M09_Marketing_Dialectics.md#968-worked-assessments-of-the-missing-object).

**Support.** The values or situations represented by a distribution or dataset. Claims about treatments, prices, or customer types outside that support require extrapolation or additional evidence. [M6 §6.24](modules/M06_Causal_Inference_and_Experiments.md#624-overlap-weight-concentration-and-missing-confounders); [M4 §4.26](modules/M04_Conjoint_Segmentation_and_CLV.md#426-demand-information-pricing-and-consumer-surplus).

**Survival Function.** The probability that a time-to-event outcome exceeds a specified duration. Its interpretation requires a defined event, origin, observation horizon, and treatment of censoring. [M4 §4.13](modules/M04_Conjoint_Segmentation_and_CLV.md#413-mhealth-time-until-a-logging-gap).

**Synthetic Data.** Records generated through a specified construction or model. They can verify calculations and explore consequences of assumptions, while any claim about actual behavior requires validation against appropriate empirical evidence. [M4 §4.23](modules/M04_Conjoint_Segmentation_and_CLV.md#423-synthetic-consumers-and-product-concept-screening); [M7 §7.36](modules/M07_Prediction_and_Machine_Learning.md#736-validation-of-synthetic-consumer-panels).

## T

**Target Population.** The set of units to which an analytical conclusion is intended to apply. The observed sample and available labels may represent only part of that population. [M2 §2.1](modules/M02_Customer_Data_and_Visualization.md#21-define-the-population-before-the-metric); [M6 §6.1](modules/M06_Causal_Inference_and_Experiments.md#61-define-the-treatment-outcome-and-estimand).

**Test Set.** Observations reserved for final evaluation after development choices are fixed. Its independence and relevance to deployment matter more than its label; repeated examination can turn it into development information. [M7 §7.4](modules/M07_Prediction_and_Machine_Learning.md#74-validation-cross-validation-and-leakage); [M7 §7.20](modules/M07_Prediction_and_Machine_Learning.md#720-repeated-selection-can-improve-a-score-without-improving-prediction).

**Testimony.** Information offered through another person's or institution's account. Its evidential force depends on competence, access, incentives, and opportunities for challenge, rather than institutional prestige alone. [M9 §9.32](modules/M09_Marketing_Dialectics.md#932-who-counts-as-a-stakeholder-and-why); [M9 §9.65.8](modules/M09_Marketing_Dialectics.md#9658-maxims-of-data-production-and-disclosure).

**TF-IDF.** A text representation combining term frequency within a document with a weight based on rarity across documents. The corpus, document unit, preprocessing, and denominator shape the resulting representation. [M5 §5.2](modules/M05_Text_Social_and_Network_Analysis.md#52-representing-language-with-counts-and-weights).

**Time Split.** An evaluation design that trains on earlier information and evaluates on later observations. It should also respect label availability, forecast horizons, customer recurrence, and preprocessing boundaries. [M7 §7.4](modules/M07_Prediction_and_Machine_Learning.md#74-validation-cross-validation-and-leakage); [M7 §7.18](modules/M07_Prediction_and_Machine_Learning.md#718-mcdonalds-forecasting-availability-with-missing-future-labels).

**Topic Model.** A model organizing patterns of word occurrence into latent topics. Interpreting a topic requires examining its documents and terms; a statistical component does not automatically correspond to a meaningful customer motive. [M5 §5.4](modules/M05_Text_Social_and_Network_Analysis.md#54-sentiment-aspect-labels-and-topic-models); [M5 §5.12](modules/M05_Text_Social_and_Network_Analysis.md#512-mhealth-text-topics-and-their-denominators).

**Training Set.** Observations used to fit model parameters and learned transformations. Keeping training operations separate from held-out outcomes is necessary for an honest evaluation of performance on new cases. [M7 §7.4](modules/M07_Prediction_and_Machine_Learning.md#74-validation-cross-validation-and-leakage).

**Treatment.** The intervention, exposure, or assignment whose effect is being evaluated. A recorded opening date, a proposed project, and preparatory infrastructure investment define different treatments and possible causal comparisons. [M6 §6.1](modules/M06_Causal_Inference_and_Experiments.md#61-define-the-treatment-outcome-and-estimand); [M6 §6.35](modules/M06_Causal_Inference_and_Experiments.md#635-institutional-exposure-and-the-meaning-of-an-untreated-utility).

**Trustworthiness.** Conduct that warrants another person's reliance on one's representations or performance of a role. The relevant judgment concerns what is said and done, including whether the organization responds faithfully to the customer's expressed purpose. [M9 §9.11.2](modules/M09_Marketing_Dialectics.md#9112-trustworthiness-and-the-responsibilities-of-a-role).

**Truth.** Whether a claim holds about its subject under the relevant conditions. The creation of a dataset or institutional acceptance of an interpretation does not make every represented claim true. [M9 §9.52](modules/M09_Marketing_Dialectics.md#952-truth-warrant-and-the-different-force-of-norms); [M9 §9.60.3](modules/M09_Marketing_Dialectics.md#9603-created-objects-and-independent-truth-conditions).

**Type I Error.** Rejecting a null hypothesis when it is true. Its practical meaning depends on how the null is defined and what action follows rejection. [M6 §6.44](modules/M06_Causal_Inference_and_Experiments.md#644-type-i-and-type-ii-errors-under-unequal-costs); [M6 §6.47](modules/M06_Causal_Inference_and_Experiments.md#647-choosing-the-null-for-a-claim-about-harm).

**Type II Error.** Failing to reject a null hypothesis under a specified alternative where it is false. Its probability depends on that alternative, and its societal cost depends on the resulting action or inaction. [M6 §6.44](modules/M06_Causal_Inference_and_Experiments.md#644-type-i-and-type-ii-errors-under-unequal-costs); [M6 §6.47](modules/M06_Causal_Inference_and_Experiments.md#647-choosing-the-null-for-a-claim-about-harm).

## U

**Undone Science.** Research that remains unperformed or underdeveloped despite potential relevance to affected people. The distribution of questions and data can reflect institutions and incentives; establishing a particular omission's cause requires evidence. [M9 §9.53](modules/M09_Marketing_Dialectics.md#953-undone-science-and-the-distribution-of-evidence).

**Unit Test.** A check of a small program behavior against a defined expected result. Hand-checkable cases and deliberate counterexamples can expose errors that a plausible aggregate result would conceal. [M1 §1.5](modules/M01_Marketing_Analytics_and_Python.md#15-ai-assisted-coding-as-a-sequence-of-verifiable-steps); [M7 §7.46](modules/M07_Prediction_and_Machine_Learning.md#746-evaluate-a-checker-with-deliberately-incorrect-programs).

**Universalization.** Evaluating whether a maxim can be conceived and willed as a universal law. It tests the principle's coherence and relation to rational agency, rather than replacing moral reasoning with a popularity survey (Kant, 1785). [M9 §9.65.8](modules/M09_Marketing_Dialectics.md#9658-maxims-of-data-production-and-disclosure).

**Utility.** A representation of preferences within a specified choice model. Its normalization and interpretation depend on the model, and an estimated utility function does not by itself establish every morally relevant interest of the person. [M4 §4.2](modules/M04_Conjoint_Segmentation_and_CLV.md#42-utility-choice-probabilities-and-willingness-to-pay); [M9 §9.34](modules/M09_Marketing_Dialectics.md#934-a-customer-type-and-a-persons-reasons).

## V

**Validation.** Evaluation of whether a measure, model, procedure, or interpretation performs adequately for a stated purpose. The relevant evidence changes with the object being validated and the use for which it is proposed. [M7 §7.4](modules/M07_Prediction_and_Machine_Learning.md#74-validation-cross-validation-and-leakage); [M2 §2.32](modules/M02_Customer_Data_and_Visualization.md#232-defining-harm-before-choosing-its-measure).

**Variable.** A recorded or modeled attribute that takes values across units or states. Its name, units, timing, missingness, and construction determine the information it can supply. [M1 §1.1](modules/M01_Marketing_Analytics_and_Python.md#11-from-a-marketing-question-to-an-analytical-object); [M2 §2.30](modules/M02_Customer_Data_and_Visualization.md#230-data-have-a-production-history).

**Variance.** The expected squared deviation of a quantity from its mean. Outcome variance describes dispersion among outcomes, while sampling variance describes variation in an estimator across repeated samples or assignments. [M3 §3.6](modules/M03_Regression.md#36-uncertainty-dependence-and-practical-importance); [M6 §6.5](modules/M06_Causal_Inference_and_Experiments.md#65-power-precision-and-the-minimum-useful-effect).

**Vibe Coding.** An informal label for developing software through conversational instructions to an AI system. Explicit specifications, inspection, small changes, and independent checks make the resulting code and claims assessable. [M1 §1.5](modules/M01_Marketing_Analytics_and_Python.md#15-ai-assisted-coding-as-a-sequence-of-verifiable-steps); [M1 §1.14](modules/M01_Marketing_Analytics_and_Python.md#114-specifications-independent-checks-and-retained-skills).

## W

**Warrant.** See **Evidential Warrant**. [M9 §9.52](modules/M09_Marketing_Dialectics.md#952-truth-warrant-and-the-different-force-of-norms).

**Willingness to Pay.** The maximum payment consistent with choosing an option under specified preferences, resources, and alternatives. Its interpretation is affected by income and constraints and does not measure every morally relevant reason concerning the exchange. [M4 §4.2](modules/M04_Conjoint_Segmentation_and_CLV.md#42-utility-choice-probabilities-and-willingness-to-pay); [M9 §9.77](modules/M09_Marketing_Dialectics.md#977-willingness-to-pay-and-equal-moral-standing).
