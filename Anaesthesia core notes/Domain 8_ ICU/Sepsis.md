---
Domain: "08"
Subdomain:
  - ICU
Date: 2024-07-04
tags: [SOFA, qSOFA, Sepsis, Septic-shock]
Date modified: Friday, October 4th 2024, 5:00:12 pm
---

# Introduction
- Hospital mortality rates for patients with sepsis are estimated to be as high as 35.3%.

## History
### 1991 Consensus Conference (“Sepsis-1”)
- Sepsis was defined as resulting from the host's response (SIRS) to infection, introducing MODS and proposed definitions for infection and its sequelae.
- The idea behind the definition of SIRS was to provide a practical approach usable in both clinical and research settings, as there was no uniform definition of sepsis prior.
- The Kaukonen study demonstrated that SIRS criteria lack both specificity and sensitivity for diagnosing severe sepsis.
- **Sensitivity:** The ability of a test to recognize true positives.
- **Specificity:** The number of true negatives correctly identified.
- **SIRS Criteria:**
  - Temperature >38°C or <36°C
  - Heart rate >90 beats/min
  - Respiratory rate >20/min or PaCO2 <32 mmHg (4.3 kPa)
  - White blood cell count >12000/mm³ or <4000/mm³ (or 10% immature neutrophils (bands))

### 1996
- The CARS, MARS, SIRS, and CHAOS proposal reflected on the pathobiology of sepsis.

### 2001 Task Force (“Sepsis-2”)
- Recognized limitations with the 1991 definitions, expanded the list of diagnostic criteria but did not offer alternatives due to the lack of supporting evidence. Introduced the concept of PIRO.

### 2001 & 2012
- **Surviving Sepsis Campaign Guidelines:**
  - Introduced therapeutic targets for the treatment of septic shock.
  - Distinction made between definitions and therapeutic targets.
  - **Septic induced hypotension defined as:**
	- sBP <90 mmHg, or MAP <70 mmHg, or a decrease in sBP >40 mmHg (or less than 2 SD below normal for age) in the absence of other causes of hypotension.
	- **Therapeutic target:** MAP threshold ≥65 mmHg.

### 2016
- 3rd international consensus definition for sepsis and septic shock (Sepsis-3).

## Sepsis-2 Vs Sepsis-3

### Sepsis-2
- **Publication Year:** 2001
- **Mechanism (Pathophysiology):** Physiological inflammatory response (SIRS) to infection.
- **Spectrum:** SIRS → sepsis → severe sepsis → septic shock → MODS.
- **Predictive Validity for In-Hospital Mortality (Area under the curve, p<0.001):** 0.64 (95% CI, 0.62–0.66).
- **Sensitivity/Specificity:**
  - ↑ Sensitivity
  - ↓ Specificity
- **Definition of Septic Shock:** Acute circulatory failure characterized by persistent arterial hypotension unexplained by other causes.
- **Practical Considerations:** Three of four SIRS criteria obtainable at bedside without the need for laboratory testing.

### Sepsis-3
- **Publication Year:** 2016
- **Mechanism (Pathophysiology):** Dysregulated immune response to infection.
- **Spectrum:** Sepsis → septic shock.
- **Predictive Validity for In-Hospital Mortality (Area under the curve, p<0.001):** 0.74 (95% CI, 0.73–0.76).
- **Sensitivity/Specificity:**
  - ↓ Sensitivity
  - ↑ Specificity
- **Definition of Septic Shock:** Subset of sepsis in which underlying circulatory and cellular metabolic abnormalities are profound enough to substantially increase mortality.
- **Practical Considerations:** Multiple laboratory test results required to calculate SOFA score; qSOFA can be used as a substitute prior to test availability.

## Definition
### Sepsis
- **Definition:** Life-threatening organ dysfunction caused by a dysregulated host response to infection.
- **Organ Dysfunction:** An increase in the total SOFA score of ≥2 points, associated with a mortality of >10%.
- Baseline SOFA score assumed to be 0 unless pre-existing organ dysfunction prior to infection onset is known.
- **Clinical Criteria:** Suspected or documented infection and an acute increase of ≥2 SOFA points (SOFA score as a proxy for organ dysfunction).

### Septic Shock
- **Definition:** A subset of sepsis with profound circulatory, cellular, and metabolic abnormalities associated with a higher risk of mortality than sepsis alone.
- **Clinical Identification:**
  - Need for vasopressors to maintain a MAP ≥65 mmHg.
  - Serum lactate level >2 mmol/L in the absence of hypovolemia.
  - Associated with an in-hospital mortality of >40%.
- **Sepsis-3 Criteria for Septic Shock:**
  - Fluid-resistant hypotension.
  - Need for vasopressors.
  - Hyperlactatemia >2 mmol/L.
- **Surviving Sepsis Campaign Guidelines Database:**
  - Presence of all three criteria (and a lactate of >4 mmol/L) is associated with an in-hospital mortality rate of 49.7%.
  - If a serum lactate of >2 mmol/L is used (as in Sepsis-3), the mortality rate is 42.3%.
# ICU Scoring Systems

## Overview
- **Outcome Prediction Models:** APACHE I-IV (Applied Physiology and Chronic Health Evaluation), SAPS II (Simplified Acute Physiology Score)
- **Organ Dysfunction Scores:** LODS (Logistic Organ Dysfunction System), MODS (Multi Organ Dysfunction Score), SOFA (Sepsis-related Organ Failure Assessment Score)
- **Severity Assessment Scores Based on Workload:** TISS (Therapeutic Intervention Scoring System), NAS (Nursing Activities Score)

## SOFA (Sepsis-related Organ Failure Assessment)

- **Purpose:** Describes the sequence of complications in critically ill patients rather than predicting outcomes.
- **Use:** Frequently used daily in critically ill patients to chart progress.
- **Components:** 6 organ systems (neurologic, cardiovascular, respiratory, coagulation, renal, hepatic; no score for gastrointestinal dysfunction) scored from 0 to 4 based on dysfunction severity.
- **Total Score Range:** 0 to 24, determined by the worst value in each 24-hour period.

### SOFA Scoring Table

|SOFA Score|1|2|3|4|
|---|---|---|---|---|
|**Respiration:** PaO₂/FiO₂ (mmHg)|<400|<300|<200 with respiratory support|<100 with respiratory support|
|**Coagulation:** Platelets x10³/mm³|<150|<100|<50|<20|
|**Liver:** Bilirubin (µmol/L)|20–32|33–101|102–204|>204|
|**Cardiovascular:** Hypotension|MAP<70mmHg|Dopamine ≤5, or dobutamine (any dose)|Dopamine >5, or adrenaline or noradrenaline ≤0.1|Dopamine >15, or adrenaline or noradrenaline >0.1|
|**Central Nervous System:** Glasgow Coma Score|13–14|10–12|6–9|<6|
|**Renal:** Creatinine (µmol/L) or urine output|110–170|171–299|300–440 or <500ml/day|>440 or <200ml/day|

_Adrenergic agents administered for at least 1h (doses in µg/kg/min)._

## qSOFA (Quick SOFA)

- **Premise:** Identifies sepsis among patients with suspected or confirmed infection to recognize those at increased risk of dying from infection.
- **Variables:**
  - Respiratory rate ≥22 breaths/min
  - Glasgow Coma Scale ≤13
  - Systolic Blood Pressure ≤100 mmHg
- **Scoring:** 1 point per variable; total score range 0-3.

### Predictive Ability
- **Exclusion of Serum Lactate:** Did not meet statistical thresholds for inclusion and did not improve qSOFA's predictive ability.
- **Comparison to Other Scoring Systems:** Better at predicting in-hospital mortality for patients with suspected infection not yet admitted to ICU.
- **Mortality Risks Based on qSOFA Score:**
  - 1 criterion: 2-3% risk of death
  - 2 criteria: 8% risk of death
  - 3 criteria: >20% risk of death

### Clinical Application
- **In-ICU Patients:** Use SOFA score for predicting in-hospital mortality.
- **Non-ICU Patients:** Use qSOFA for patients suspected of infection to predict sepsis risk and mortality. Do not withhold sepsis treatment even if qSOFA criteria are not met.

### Flow Diagram of qSOFA

1. **Patient with Suspected Infection**
   - If qSOFA less than 2:
	 - **Sepsis Still Suspected?**
	   - **Yes:** Monitor clinical condition; re-evaluate for possible sepsis if clinically indicated.
	   - **No:** Assess for evidence of organ dysfunction.
 - If SOFA ≥2:
		Sepsis
			Despite adequate fluid resuscitation:
			 1. Vasopressors required to maintain MAP ≥65 mm Hg.
			 2. Serum lactate level >2 mmol/L.
			 **Yes:** Septic shock.
				**No:** Monitor clinical condition; revaluate for possible sepsis if clinically indicated.
# Pathophysiology of Septic Shock

## Overview

Septic shock represents the culmination of severe sepsis, characterized by an overwhelming immune response to infection, leading to widespread inflammation, tissue damage, and organ failure.

Sure, I will create a mind map to summarize the information you provided.

![](Pasted%20image%2020240805122616.png)

[View or edit this diagram in Whimsical.](https://whimsical.com/sepsis-pathophysiology-VjBgjTF1p1PkccWZFFBG5Q?ref=chatgpt)

## Pathophysiology of Sepsis-Induced Myocardial Dysfunction

1. **Normal Cardiac Cycle:**
   - Left ventricular (LV) pressure-volume diagram shows contraction starting at the end of diastole. The aortic valve opens when ventricular pressure exceeds aortic pressure, leading to ejection.

2. **Sepsis-Induced Myocardial Dysfunction:**
   - **Early Phase:** Decreased contractility with a low ESPVR slope and low stroke volume (SV) before volume resuscitation.
   - **Compensatory Mechanisms:**
	 - Restored stroke volume through hyperdynamic septic shock with elevated SV.
	 - Decreased afterload allows further ejection to a smaller end-systolic volume.
	 - Increased end-diastolic volume (EDV) due to volume resuscitation.
	 - Increased diastolic compliance shifts the end-diastolic pressure-volume relationship.
	 - Infused catecholamines may increase contractility, shifting the ESPVR up and to the left.

# Treatment of Septic Shock
## Golden Hour
1. **Measure Lactate Level:** Follow serial measurements if initial level >2 mmol/L.
2. **Obtain Blood Cultures:** Prior to administering antibiotics.
3. **Administer Broad Spectrum Antibiotics**
4. **Rapid Administration of Crystalloid:** 30 mL/kg for hypotension or lactate ≥4 mmol/L.
5. **Start Vasopressors:** If patient is hypotensive during or after fluid resuscitation to maintain a MAP ≥65 mm Hg.
![](Pasted%20image%2020240705170902.png)

[View or edit this diagram in Whimsical.](https://whimsical.com/1-hour-bundle-D2t43SD9PxwefjvP7Ew7Ar?ref=chatgpt)

## Care Bundle

### Antibiotics
- **Early Administration:** Critical for improving patient outcomes.

### Fluids
- **Initial Administration:** Several liters, including:
  - Colloids
  - Crystalloids
  - Starches
  - High chloride solutions

### Vasopressors
- **Timing:** Administered 1–6 hours after onset.
- **Types:**
  - Norepinephrine
  - Epinephrine
  - Vasopressin
  - Dopamine
  - Phenylephrine

### Other Supportive Therapies
- Enteral Feeding
- Insulin Therapy
- Deep Sedation
- Molecular Targeted Therapies
- Lung Protective Ventilation
- Urinary Catheter
### Adjuvants

1. **Steroids:** Hydrocortisone 200 mg IV daily for persistent circulatory failure despite adequate fluid resuscitation and vasopressors. Reduces mortality (Annane 2015).
2. **Glycaemic Control:** Initiate management at >10 mmol/L to maintain <10 mmol/L.
3. **Anticoagulants:** Thrombomodulin use in sepsis with DIC is well established in Japan.
4. **Vitamin C / Thiamine:** No multicentre RCTs support their use.
5. **Blood Purification Techniques:** Endotoxin removal via haemoperfusion; the EUPHRATES trial terminated early due to failure to achieve the primary endpoint.
6. **IV Immunoglobulin:** Not recommended.

### Use of Lactate to Guide Resuscitation
- **Lactate as a Marker:** Reflects disease severity, but also occurs under other conditions (e.g., hepatic dysfunction, accelerated glycolysis, impaired aerobic respiration).
- **Sensitivity vs. Specificity:** Sensitive but not specific.
- **Lactate Levels:** Associated with worse outcomes; serves as an objective surrogate for tissue perfusion.
- **Lactate-Guided Resuscitation:** Significant reduction in mortality compared to resuscitation without lactate monitoring.

### Targeting MAP of 65 mmHg
- **MAP:** Driving pressure of tissue perfusion.
- **Autoregulation:** Perfusion of critical organs protected by autoregulation, but below a threshold MAP, perfusion depends on arterial pressure.

### Procalcitonin (PCT)
- **Use:** Suggest using PCT to limit or discontinue antibiotic therapy. Elevations can be seen in uninfected patients, especially those with renal disease. Elevated PCT alone is insufficient to determine antibiotic initiation.
## Approach to Timing of Surgery

- **Ongoing Hemorrhage:** Immediate surgery.
- **Septic Shock:** Within 3 hours.
- **Sepsis with Organ Dysfunction:** Within 6 hours.
- **Sepsis without Organ Dysfunction:** Within 18 hours.
# Surviving Sepsis Campaign: Best Practices

![](Pasted%20image%2020240705170026.png)

[View or edit this diagram in Whimsical.](https://whimsical.com/generated-board-PF9BzAoQFKGAasU65YcomK?ref=chatgpt)

## A. Initial Resuscitation
1. Sepsis and septic shock are medical emergencies, and we recommend that treatment and resuscitation begin immediately (BPS).
2. We recommend that, in the resuscitation from sepsis-induced hypoperfusion, at least 30 mL/kg of IV crystalloid fluid be given within the first 3 hours (strong recommendation, low quality of evidence).
3. We recommend that, following initial fluid resuscitation, additional fluids be guided by frequent reassessment of hemodynamic status (BPS).
   - Remarks: Reassessment should include a thorough clinical examination and evaluation of available physiologic variables (heart rate, blood pressure, arterial oxygen saturation, respiratory rate, temperature, urine output, and others), as well as other noninvasive or invasive monitoring, as available.
4. We recommend further hemodynamic assessment (such as assessing cardiac function) to determine the type of shock if the clinical examination does not lead to a clear diagnosis (BPS).
5. We suggest that dynamic over static variables be used to predict fluid responsiveness, where available (weak recommendation, low quality of evidence).
6. We recommend an initial target mean arterial pressure of 65 mm Hg in patients with septic shock requiring vasopressors (strong recommendation, moderate quality of evidence).
7. We suggest guiding resuscitation to normalize lactate in patients with elevated lactate levels as a marker of tissue hypoperfusion (weak recommendation, low quality of evidence).

## B. Screening for Sepsis and Performance Improvement
1. We recommend that hospitals and hospital systems have a performance improvement program for sepsis, including sepsis screening for acutely ill, high-risk patients (BPS).

## C. Diagnosis
1. We recommend that appropriate routine microbiologic cultures (including blood) be obtained before starting antimicrobial therapy in patients with suspected sepsis or septic shock if doing so results in no substantial delay in the start of antimicrobials (BPS).
   - Remarks: Appropriate routine microbiologic cultures always include at least two sets of blood cultures (aerobic and anaerobic).

## D. Antimicrobial Therapy
1. We recommend that administration of IV antimicrobials should be initiated as soon as possible after recognition and within one hour for both sepsis and septic shock (strong recommendation, moderate quality of evidence).
2. We recommend empiric broad-spectrum therapy with one or more antimicrobials for patients presenting with sepsis or septic shock to cover all likely pathogens (including bacterial and potentially fungal or viral coverage) (strong recommendation, moderate quality of evidence).
3. We recommend that empiric antimicrobial therapy be narrowed once pathogen identification and sensitivities are established and/or adequate clinical improvement is noted (BPS).
4. We recommend against sustained systemic antimicrobial prophylaxis in patients with severe inflammatory states of noninfectious origin (e.g., severe pancreatitis, burn injury) (BPS).
5. We recommend that dosing strategies of antimicrobials be optimized based on accepted pharmacokinetic/pharmacodynamic principles and specific drug properties in patients with sepsis or septic shock (BPS).
6. We suggest empiric combination therapy (using at least two antibiotics of different antimicrobial classes) aimed at the most likely bacterial pathogen(s) for the initial management of septic shock (weak recommendation, low quality of evidence).
   - Remarks: Readers should review Table 6 for definitions of empiric, targeted/definitive, broad-spectrum, combination, and multidrug therapy before reading this section.
7. We suggest that combination therapy not be routinely used for ongoing treatment of most other serious infections, including bacteremia and sepsis without shock (weak recommendation, low quality of evidence).
   - Remarks: This does not preclude the use of multidrug therapy to broaden antimicrobial activity.
8. We recommend against combination therapy for the routine treatment of neutropenic sepsis/bacteremia (strong recommendation, moderate quality of evidence).
   - Remarks: This does not preclude the use of multidrug therapy to broaden antimicrobial activity.
9. If combination therapy is used for septic shock, we recommend de-escalation with discontinuation of combination therapy within the first few days in response to clinical improvement and/or evidence of infection resolution. This applies to both targeted (for culture-positive infections) and empiric (for culture-negative infections) combination therapy (BPS).
10. We suggest that an antimicrobial treatment duration of 7 to 10 days is adequate for most serious infections associated with sepsis and septic shock (weak recommendation, low quality of evidence).
11. We suggest that longer courses are appropriate in patients who have a slow clinical response, undrainable foci of infection, bacteremia with Staphylococcus aureus, some fungal and viral infections, or immunologic deficiencies, including neutropenia (weak recommendation, low quality of evidence).
12. We suggest that shorter courses are appropriate in some patients, particularly those with rapid clinical resolution following effective source control of intra-abdominal or urinary sepsis and those with anatomically uncomplicated pyelonephritis (weak recommendation, low quality of evidence).
13. We recommend daily assessment for de-escalation of antimicrobial therapy in patients with sepsis and septic shock (BPS).
14. We suggest that measurement of procalcitonin levels can be used to support shortening the duration of antimicrobial therapy in sepsis patients (weak recommendation, low quality of evidence).
15. We suggest that procalcitonin levels can be used to support the discontinuation of empiric antibiotics in patients who initially appeared to have sepsis but subsequently have limited clinical evidence of infection (weak recommendation, low quality of evidence).

## E. Source Control
1. We recommend that a specific anatomic diagnosis of infection requiring emergent source control should be identified or excluded as rapidly as possible in patients with sepsis or septic shock, and that any required source control intervention should be implemented as soon as medically and logistically practical after the diagnosis is made (BPS).
2. We recommend prompt removal of intravascular access devices that are a possible source of sepsis or septic shock after other vascular access has been established (BPS).

## F. Fluid Therapy
1. We recommend that a fluid challenge technique be applied where fluid administration is continued as long as hemodynamic factors continue to improve (BPS).
2. We recommend crystalloids as the fluid of choice for initial resuscitation and subsequent intravascular volume replacement in patients with sepsis and septic shock (strong recommendation, moderate quality of evidence).
3. We suggest using either balanced crystalloids or saline for fluid resuscitation of patients with sepsis or septic shock (weak recommendation, low quality of evidence).
4. We suggest using albumin in addition to crystalloids for initial resuscitation and subsequent intravascular volume replacement in patients with sepsis and septic shock when patients require substantial amounts of crystalloids (weak recommendation, low quality of evidence).
5. We recommend against using hydroxyethyl starches for intravascular volume replacement in patients with sepsis or septic shock (strong recommendation, high quality of evidence).
6. We suggest using crystalloids over gelatins when resuscitating patients with sepsis or septic shock (weak recommendation, low quality of evidence).

## G. Vasoactive Medications
1. We recommend norepinephrine as the first-choice vasopressor (strong recommendation, moderate quality of evidence).
2. We suggest adding either vasopressin (up to 0.03 U/min) (weak recommendation, moderate quality of evidence) or epinephrine (weak recommendation, low quality of evidence) to norepinephrine with the intent of raising mean arterial pressure to target, or adding vasopressin (up to 0.03 U/min) (weak recommendation, moderate quality of evidence) to decrease norepinephrine dosage.
3. We suggest using dopamine as an alternative vasopressor agent to norepinephrine only in highly selected patients (e.g., patients with low risk of tachyarrhythmias and absolute or relative bradycardia) (weak recommendation, low quality of evidence).
4. We recommend against using low-dose dopamine for renal protection (strong recommendation, high quality of evidence).
5. We suggest using dobutamine in patients who show evidence of persistent hypoperfusion despite adequate fluid loading and the use of vasopressor agents (weak recommendation, low quality of evidence).
6. We suggest that all patients requiring vasopressors have an arterial catheter placed as soon as practical if resources are available (weak recommendation, very low quality of evidence).

## H. Corticosteroids
1. We suggest against using IV hydrocortisone to treat septic shock patients if adequate fluid resuscitation and vasopressor therapy are able to restore hemodynamic stability. If this is not achievable, we suggest IV hydrocortisone at a dose of 200 mg per day (weak recommendation, low quality of evidence).

## I. Blood Products
1. We recommend that RBC transfusion occur only when hemoglobin concentration decreases to < 7.0 g/dL in adults in the absence of extenuating circumstances, such as myocardial ischemia, severe hypoxemia, or acute hemorrhage (strong recommendation, high quality of evidence).
2. We recommend against the use of erythropoietin for treatment of anemia associated with sepsis (strong recommendation, moderate quality of evidence).
3. We suggest against the use of fresh frozen plasma to correct clotting abnormalities in the absence of bleeding or planned invasive procedures (weak recommendation, very low quality of evidence).
4. We suggest prophylactic platelet transfusion when counts are < 10,000/mm³ (10 × 10⁹/L) in the absence of apparent bleeding and when counts are < 20,000/mm³ (20 × 10⁹/L) if the patient has a significant risk of bleeding. Higher platelet counts (≥ 50,000/mm³ [50 × 10⁹/L]) are advised for active bleeding, surgery, or invasive procedures (weak recommendation, very low quality of evidence).

## J. Immunoglobulins
1. We suggest against the use of IV immunoglobulins in patients with sepsis or septic shock (weak recommendation, low quality of evidence).

## K. Blood Purification
1. We make no recommendation regarding the use of blood purification techniques.

## L. Anticoagulants
1. We recommend against the use of antithrombin for the treatment of sepsis and septic shock (strong recommendation, moderate quality of evidence).
2. We make no recommendation regarding the use of thrombomodulin or heparin for the treatment of sepsis or septic shock.

## M. Mechanical Ventilation
1. We recommend using a target tidal volume of 6 mL/kg predicted body weight compared with 12 mL/kg in adult patients with sepsis-induced acute respiratory distress syndrome (ARDS) (strong recommendation, high quality of evidence).
2. We recommend using an upper limit goal for plateau pressures of 30 cm H₂O over higher plateau pressures in adult patients with sepsis-induced severe ARDS (strong recommendation, moderate quality of evidence).
3. We suggest using higher positive end-expiratory pressure (PEEP) over lower PEEP in adult patients with sepsis-induced moderate to severe ARDS (weak recommendation, moderate quality of evidence).
4. We suggest using recruitment maneuvers in adult patients with sepsis-induced, severe ARDS (weak recommendation, moderate quality of evidence).
5. We recommend using prone over supine position in adult patients with sepsis-induced ARDS and a PaO₂/FiO₂ ratio < 150 (strong recommendation, moderate quality of evidence).
6. We recommend against using high-frequency oscillatory ventilation in adult patients with sepsis-induced ARDS (strong recommendation, moderate quality of evidence).
7. We make no recommendation regarding the use of noninvasive ventilation for patients with sepsis-induced ARDS.
8. We suggest using neuromuscular blocking agents for ≤ 48 hours in adult patients with sepsis-induced ARDS and a PaO₂/FiO₂ ratio < 150 mm Hg (weak recommendation, moderate quality of evidence).
9. We recommend a conservative fluid strategy for patients with established sepsis-induced ARDS who do not have evidence of tissue hypoperfusion (strong recommendation, moderate quality of evidence).
10. We recommend against the use of β-2 agonists for the treatment of patients with sepsis-induced ARDS without bronchospasm (strong recommendation, moderate quality of evidence).
11. We recommend against the routine use of the pulmonary artery catheter for patients with sepsis-induced ARDS (strong recommendation, high quality of evidence).
12. We suggest using lower tidal volumes over higher tidal volumes in adult patients with sepsis-induced respiratory failure without ARDS (weak recommendation, low quality of evidence).
13. We recommend that mechanically ventilated sepsis patients be maintained with the head of the bed elevated between 30 and 45 degrees to limit aspiration risk and to prevent the development of ventilator-associated pneumonia (strong recommendation, low quality of evidence).
14. We recommend using spontaneous breathing trials in mechanically ventilated patients with sepsis who are ready for weaning (strong recommendation, high quality of evidence).
15. We recommend using a weaning protocol in mechanically ventilated patients with sepsis-induced respiratory failure who can tolerate weaning (strong recommendation, moderate quality of evidence).

## N. Sedation and Analgesia
1. We recommend that continuous or intermittent sedation be minimized in mechanically ventilated sepsis patients, targeting specific titration end points (BPS).

## O. Glucose Control
1. We recommend a protocolized approach to blood glucose management in ICU patients with sepsis, commencing insulin dosing when two consecutive blood glucose levels are > 180 mg/dL. This approach should target an upper blood glucose level ≤ 180 mg/dL rather than an upper target blood glucose level ≤ 110 mg/dL (strong recommendation, high quality of evidence).
2. We recommend that blood glucose levels be monitored every 1 to 2 hours until glucose levels and insulin infusion rates are stable, then every 4 hours thereafter in patients receiving insulin infusions (BPS).
3. We recommend that glucose levels obtained with point-of-care testing of capillary blood be interpreted with caution because such measurements may not accurately estimate arterial blood or plasma glucose values (BPS).
4. We suggest the use of arterial blood rather than capillary blood for point-of-care testing using glucose meters if patients have arterial catheters (weak recommendation, low quality of evidence).

## P. Renal Replacement Therapy
1. We suggest that either continuous or intermittent renal replacement therapy (RRT) be used in patients with sepsis and acute kidney injury (weak recommendation, moderate quality of evidence).
2. We suggest using continuous therapies to facilitate management of fluid balance in hemodynamically unstable septic patients (weak recommendation, low quality of evidence).
3. We suggest against the use of RRT in patients with sepsis and acute kidney injury for increase in creatinine or oliguria without other definitive indications for dialysis (weak recommendation, low quality of evidence).

## Q. Bicarbonate Therapy
1. We suggest against the use of sodium bicarbonate therapy to improve hemodynamics or to reduce vasopressor requirements in patients with hypoperfusion-induced lactic acidemia with pH ≥ 7.15 (weak recommendation, moderate quality of evidence).

## R. Venous Thromboembolism Prophylaxis
1. We recommend pharmacologic prophylaxis (unfractionated heparin [UFH] or low-molecular-weight heparin [LMWH]) against venous thromboembolism (VTE) in the absence of contraindications to the use of these agents (strong recommendation, high quality of evidence).
2. We recommend using LMWH rather than UFH for VTE prophylaxis in the absence of contraindications to the use of LMWH (strong recommendation, moderate quality of evidence).
3. We suggest combining pharmacologic VTE prophylaxis and mechanical prophylaxis, whenever possible (weak recommendation, low quality of evidence).
4. We suggest mechanical VTE prophylaxis when pharmacologic VTE is contraindicated (weak recommendation, low quality of evidence).

## S. Stress Ulcer Prophylaxis
1. We recommend that stress ulcer prophylaxis be given to patients with sepsis or septic shock who have risk factors for gastrointestinal (GI) bleeding (strong recommendation, low quality of evidence).
2. We suggest using either proton pump inhibitors or histamine-2 receptor antagonists when stress ulcer prophylaxis is indicated (weak recommendation, low quality of evidence).
3. We recommend against stress ulcer prophylaxis in patients without risk factors for GI bleeding (BPS).

## T. Nutrition
1. We recommend against the administration of early parenteral nutrition alone or parenteral nutrition in combination with enteral feedings (but rather initiate early enteral nutrition) in critically ill patients with sepsis or septic shock who can be fed enterally (strong recommendation, moderate quality of evidence).
2. We recommend against the administration of parenteral nutrition alone or in combination with enteral feeds (but rather to initiate IV glucose and advance enteral feeds as tolerated) over the first 7 days in critically ill patients with sepsis or septic shock for whom early enteral feeding is not feasible (strong recommendation, moderate quality of evidence).
3. We suggest the early initiation of enteral feeding rather than a complete fast or only IV glucose in critically ill patients with sepsis or septic shock who can be fed enterally (weak recommendation, low quality of evidence).
4. We suggest either early trophic/hypocaloric or early full enteral feeding in critically ill patients with sepsis or septic shock; if trophic/hypocaloric feeding is the initial strategy, then feeds should be advanced according to patient tolerance (weak recommendation, moderate quality of evidence).
5. We recommend against the use of omega-3 fatty acids as an immune supplement in critically ill patients with sepsis or septic shock (strong recommendation, high quality of evidence).
6. We suggest against routinely monitoring gastric residual volumes in critically ill patients with sepsis or septic shock (weak recommendation, low quality of evidence). However, we suggest measurement of gastric residuals in patients with feeding intolerance or who are considered to be at high risk of aspiration (weak recommendation, very low quality of evidence).
   - Remarks: This recommendation refers to nonsurgical critically ill patients with sepsis or septic shock.
7. We suggest the use of prokinetic agents in critically ill patients with sepsis or septic shock and feeding intolerance (weak recommendation, low quality of evidence).
8. We suggest placement of post-pyloric feeding tubes in critically ill patients with sepsis or septic shock with feeding intolerance or who are considered to be at high risk of aspiration (weak recommendation, low quality of evidence).
9. We recommend against the use of IV selenium to treat sepsis and septic shock (strong recommendation, moderate quality of evidence).
10. We suggest against the use of arginine to treat sepsis and septic shock (weak recommendation, low quality of evidence).
11. We recommend against the use of glutamine to treat sepsis and septic shock (strong recommendation, moderate quality of evidence).
12. We make no recommendation about the use of carnitine for sepsis and septic shock.

## U. Setting Goals of Care
1. We recommend that goals of care and prognosis be discussed with patients and families (BPS).
2. We recommend that goals of care be incorporated into treatment and end-of-life care planning, utilizing palliative care principles where appropriate (strong recommendation, moderate quality of evidence).
3. We suggest that goals of care be addressed as early as feasible, but no later than within 72 hours of ICU admission (weak recommendation, low quality of evidence).

# Links
- [[Resus end targets in shock]]
- [[Polytrauma and haemorrhagic shock]]
- [[Maternal sepsis]]
- [[Inotropes]]
- [[Infection and antibiotics]]
- [[ARDS]]

---

---
**References:**  

1. Wise, R., Bishop, D., Joynt, G., & Rodseth, R. (2018). Perioperative ARDS and lung injury: for anaesthesia and beyond. _Southern African Journal of Anaesthesia and Analgesia_, _24_(2), 32–39. https://doi.org/10.1080/22201181.2018.1449463
2. Walley, Keith R.. Sepsis-induced myocardial dysfunction. Current Opinion in Critical Care 24(4):p 292-299, August 2018. | DOI: 10.1097/MCC.0000000000000507  
3. Carsetti A, Vitali E, Pesaresi L, Antolini R, Casarotta E, Damiani E, Adrario E, Donati A. Anesthetic management of patients with sepsis/septic shock. Front Med (Lausanne). 2023 Mar 23;10:1150124. doi: 10.3389/fmed.2023.1150124. PMID: 37035341; PMCID: PMC10076637.
4. Yuki K, Murakami N. Sepsis pathophysiology and anesthetic consideration. Cardiovasc Hematol Disord Drug Targets. 2015;15(1):57-69. doi: 10.2174/1871529x15666150108114810. PMID: 25567335; PMCID: PMC4704087.
5. Nunnally, M. (2016). Sepsis for the anaesthetist. British Journal of Anaesthesia, 117, iii44-iii51. https://doi.org/10.1093/bja/aew333
6. Part II Anaesthesia Refresher Course–2016 University of Cape Town. Sepsis stuff What’s new? Dr Jenna Piercy
7. The Calgary Guide to Understanding Disease. (2024). Retrieved June 5, 2024, from https://calgaryguide.ucalgary.ca/
8. FRCA Mind Maps. (2024). Retrieved June 5, 2024, from https://www.frcamindmaps.org/
9. Anesthesia Considerations. (2024). Retrieved June 5, 2024, from https://www.anesthesiaconsiderations.com/
10. ICU One Pager. (2024). Retrieved June 5, 2024, from [https://onepagericu.com/](https://onepagericu.com/)
**Summary or mindmap:**
[Scoring](https://frcamindmaps.org/mindmaps/itu/scoringonitu/scoringonitu.html)

---------------------------------------------------------------------------------------------
