---
Domain: "01"
Subdomain:
  - General
Date: 2024-04-20
tags: [Sufentanyl, Manual-infusions, TIVA, TCI]
Date modified: Friday, October 4th 2024, 4:57:11 pm
---

# Indications

### Patient

- Malignant hyperthermia history, susceptibility, or risk
- Muscular dystrophy, core myopathy, or neuromuscular disease
- Previous history of PONV or motion sickness
- Risk or previous history of emergence delirium
- History of acute or chronic reactive airways
- Fear of facemask
- Minimization of allergy risk

### Surgical

- Airway surgery or shared airway procedures
- Requirement for evoked potential monitoring, e.g., scoliosis surgery
- Neurosurgical procedures
- Middle ear surgery
- Procedures with high PONV risk, e.g., strabismus, T&A

### Procedural

- Remote site anaesthesia, e.g., MRI
- Muscle biopsy for neuromuscular diagnosis

# General

- The mean difference between estimated and measured concentrations is usually less than 25%, but if the patient differs from the population in which the model was developed, the difference may be considerably greater.
- TCI pumps can be a useful tool for titrating a propofol infusion to effect (clinical effect or the desired effect on the EEG as measured by a pEEG monitor), but the predicted propofol concentration cannot be assumed to be accurate.
- Lack of evidence on whether it is better to use total body weight or another scalar such as adjusted body weight when using a TCI pump with these models in the obese. When using TIVA in the obese, titration to clinical effect and pEEG monitoring is recommended. Schnider <35 BMI (women); <42 BMI (Men).
- The drug concentration achieved should be sufficient to produce loss of consciousness and prevent movement in response to noxious stimulus. There is no plasma or effect-site concentration that is appropriate for all patients.
- The brain concentration required cannot be predicted in advance, but observation of the patient’s response during induction of anaesthesia can give an indication of the approximate propofol concentration that is likely to be required for maintenance.
- Administration of opioids, benzodiazepines, ketamine, α2-adrenoceptor agonists, magnesium, and nitrous oxide result in a marked reduction in the required brain propofol concentration. Remifentanil reduces propofol concentration by 50%.

## Ideal Drug Properties for TCI

1. Predictable plasma concentration according to a known pharmacokinetic model.
2. Predictable link between pharmacokinetic and pharmacodynamic properties.
3. No active metabolites.
4. Fast onset.
5. Fast elimination.
6. Stable in a plastic syringe.

## Pharmacokinetics

- **Volume of Distribution (Vd)**
  - Apparent volume in which the drug is distributed.
  - Vd = dose/concentration of drug.
  - As the volume of distribution increases, so does the half-life.
  - Its value depends on whether it is calculated at time zero (after a bolus, Vc) or at steady state after an infusion (Vss).
- **Clearance**
  - Volume of plasma (Vp) from which the drug is eliminated per unit time.
  - Clearance = Elimination × Vp.
  - As clearance increases, the half-life reduces.
  - Clearance also describes how quickly the drug moves between compartments. The drug is initially distributed into the central compartment before distribution to peripheral compartments.
- **Loading Dose/Bolus Dose**
  - If the initial volume of distribution (Vc) and the desired concentration for therapeutic effect (Cp) are known, it is possible to calculate the loading dose to achieve that concentration.
  - Loading dose = Cp × Vc.
  - It can also be used to calculate the bolus dose required to rapidly increase the concentration during a continuous infusion:
	- Bolus dose = (Cnew–Cactual) × Vc.
- **The Rate of Infusion to Maintain Steady State**
  - The rate of infusion to maintain steady state = Cp × Clearance.
  - Simple infusion regimens do not achieve a steady-state plasma concentration until at least five multiples of the elimination half-life. The desired concentration can be achieved more quickly if a bolus dose is followed by an infusion rate.

### Pharmacokinetics of Target Controlled Infusions

- Pharmacokinetic models attempt to describe the relationship between dose and plasma concentration with respect to time. These models predict the blood concentration profile of a drug after a bolus dose or after an infusion of varying duration.
- These models are derived from measuring arterial or venous plasma concentrations after a bolus or infusion in a group of volunteers, using standardized statistical approaches and computer software models.
- Mathematical models generate pharmacokinetic parameters such as volume of distribution and clearance. These can be used to calculate the loading dose and rate of infusion necessary to maintain a steady-state plasma concentration at equilibrium.
- **Traditional Model (Roberts)**
  - Traditional practice involved calculating the infusion regimen for propofol by the Roberts method. A 1.5 mg/kg loading dose is followed by an infusion of 10 mg/kg/hour that is reduced to rates of 8 and 6 mg/kg/hr at ten-minute intervals.
- **Computer-Controlled Pharmacokinetic Models**
  - Using a pharmacokinetic model, a computer continuously calculates the patient’s expected drug concentration and administers a BET regimen, adjusting pump infusion rates, typically at 10-second intervals. Models are derived from previously performed population pharmacokinetic studies.
  - The TCI pumps have three superimposed infusions: one at a constant rate to replace drug elimination and two exponentially decreasing infusions to match drug removed from the central compartment to other peripheral compartments of distribution.
- **Difference Between Plasma Site and Effect Site TCI**
  - Plasma site targeting stabilizes the plasma drug concentration by initially overshooting, then allowing for distribution from the central to peripheral compartments (undershooting), then infusing at a slower rate to balance the washout caused by elimination from and redistribution back into the central compartment.
  - Effect site targeting takes ke0 into account and manipulates the plasma concentration accordingly, with a positive concentration gradient for effect site increase, and negative for decrease, without overshooting or undershooting.
- **How the Pump Maintains Constant Infusion**
  - Increase: The infuser gives a bolus to fill up the central compartment and then stops. Thereafter, the infusion is recommenced at a lower rate to counteract the washout, determined by the interplay between intercompartmental redistribution back into the central compartment, and elimination.
  - Decrease: The infuser stops until elimination and redistribution decrease the plasma concentration to the desired level, then restarts the infusion at a rate that matches elimination without ignoring redistribution.

# Routine Practice

## Propofol

- **Models**
  - **Marsh**:
	- Does not include age in calculation, but cannot use in <16 years.
	- Central compartment volume calculated as 15.9 L, delivering a much larger bolus.
  - **Schnider**:
	- Requires age, height, and total body weight to be input for programming.
	- The pump calculates the lean body mass for that patient and doses and infusion rates accordingly.
	- Central compartment volume calculated as 4.27 L.
- **Induction**: Propofol target concentrations of 4–6 µg/ml. Loss of consciousness generally at 5–6 µg/ml and at 4–5 µg/ml in premedicated patients. Can be up to 8 µg/ml in young fit un-premedicated adults.
  - Slower induction starting at 1 µg/ml then incrementally increasing by 0.5 µg/ml.
	- Useful for older, frail, or unwell patients.
	- Makes it easier for the anaesthetist to observe the estimated effect-site concentration at which the patient stops responding to stimuli.
	- Clinical calibration of the individual patient’s response to propofol is recommended.
- **Maintenance**: 3–6 µg/ml (without opioids), 2.5–4.0 µg/ml (with opioids).
- **Waking from Anaesthesia**: Blood concentration of around 1–2 µg/ml.

### Propofol and Remifentanil
**These targets must be increased or decreased depending on individual patient response and/or processed EEG data.**

#### Suggested Effect-Site Concentrations for TIVA

|Age (yr)|Spontaneous Breathing||IPPV||
|---|---|---|---|---|
||Propofol (µg ml⁻¹)|Remifentanil (ng ml⁻¹)|Propofol (µg ml⁻¹)|Remifentanil (ng ml⁻¹)|
|<50|4-6|1-3|3-4|5-8|
|>50|2-4|1-2|2-3|3-6|

## Remifentanil
- TCI remifentanil is administered with propofol, target remifentanil concentrations of 2–8 ng.ml. May require concentrations up to 15 ng/ml for stimulating procedures
	- A remifentanil infusion of 0.25-0.5 mcg/kg/min in 70kg, 170cm, 40 yr old man produces a blood concentration of around 6ng/ml after 25 minutes.
- Induction
	- 4-7ng.ml
- Spontaneous ventilation is uncommon with concentrations > 1.5 ng.ml in adults
### Remifentanil (Ultiva) Dosage

#### TIVA Dosage (µg/kg/min)

- 0.05: Sedation/Awakening
- 0.10: Perioperatively, light pain
- 0.20: Surgical anaesthesia
- 0.25: Intubation
- 0.35: Strong pain stimuli
- 0.50: Deep anaesthesia
- 0.80: Very deep anaesthesia

#### TCI Dosage (ng/ml)

- 1.3: Sedation/Awakening
- 2.0: Perioperatively, light pain
- 3.0: Surgical anaesthesia
- 6.0: Intubation
- 7.5: Strong pain stimuli
- 10.0: Deep anaesthesia
- 12.0: Very deep anaesthesia
- 15.0: Very deep anaesthesia

## Sufentanyl

Analgesia: 0.03-0.15 Apnea: >0.15. Titrate Ce: 0.2-0.3

### Sufentanil Dosage (ng/ml)

- Intubation: 0.3-0.4
- LMA: 0.2
- Thorax: 0.5-0.7
- Laparoscopy: 0.4-0.6
- Abdomen: 0.3-0.6
- Soft tissues: 0.1-0.3
- Extubation: 0.15
- Sedation: 0.05-0.15

**Preparation**

- Sufenta Gepts: effect site
- Concentration: 5 µg/ml
- 250 µg amp dilute to 50 ml
- Set on induction: 0.5 ng/ml = 20 µg bolus
- After induction, reduce to a set of 0.2 ng/ml = 20 µg per hour target
- Set decrement concentration to 0.08 ng/ml
## Alfentanyl
### Alfentanil (Rapifen) Dosage

#### TIVA Dosage (µg/kg/min)

- 0.10: Sedation
- 0.15: Light pain
- 0.20: Laryngeal mask
- 0.35: Moderate pain
- 0.50: Surgical anaesthesia
- 0.70: Intubation
- 1.0: Strong pain
- 2.0: Deep anaesthesia

#### TCI Dosage (ng/ml)

- 20: Sedation
- 30: Light pain
- 40: Laryngeal mask
- 50: Moderate pain
- 60: Surgical anaesthesia
- 70: Intubation
- 80: Strong pain
- 90: Deep anaesthesia
## Manual Infusions

### Anesthesia

|Drug|Loading Dose (µg/kg)|Maintenance Infusion (µg/kg/min)|Maintenance Infusion (µg/kg/h)|
|---|---|---|---|
|Alfentanil|50-150|0.5-3|30-90|
|Fentanyl|5-15|0.03-0.1|1.8-6.0|
|Sufentanil|0.5-5|0.01-0.05|0.6-3.0|
|Remifentanil|0.5-1.0|0.1-0.4|6-24|
|Ketamine|1500-2500|25-75|1500-4500|
|Propofol|1000-2000|50-150|3-9|
|Midazolam|50-150|0.25-1.5|15-90|

### Sedation or Analgesia

| Drug         | Loading Dose (µg/kg) | Maintenance Infusion (µg/kg/min) | Maintenance Infusion (µg/kg/h) |
| ------------ | -------------------- | -------------------------------- | ------------------------------ |
| Alfentanil   | 10-25                | 0.25-1                           | 15-60                          |
| Fentanyl     | 1-3                  | 0.01-0.03                        | 0.6-1.8                        |
| Sufentanil   | 0.1-0.5              | 0.005-0.01                       | 0.3-0.6                        |
| Remifentanil | †                    | 0.025-0.1                        | 1.5-6                          |
| Ketamine     | 500-1000             | 10-20                            | 600-1200                       |
| Propofol     | 250-1000             | 10-50                            | 600-3000                       |
| Midazolam    | 25-100               | 0.25-1                           | 15-60                          |

### Notes on Infusion Protocols

#### General Guidelines
- **After the loading dose**, an initially high infusion rate to account for redistribution should be used. This rate should then be titrated to the lowest infusion rate that will maintain adequate anesthesia or sedation.
- When using opiates as part of a nitrous-narcotic technique or for cardiac anesthesia, the dosing scheme listed under anesthesia is used.
- When the opiate is combined as part of balanced anesthesia, dosing listed for analgesia is needed.

#### Remifentanil Specific Note
- **For analgesia or during sedation**, an initial loading dose of remifentanil should not be given because its very rapid onset may result in apnea or muscle rigidity.
# Practical Aspects of TCI/TIVA

## Common Causes of Accidental Awareness During TIVA
- Failure to deliver the intended dose of the drug
- Poor understanding of the underlying pharmacological principles

## Drug Concentrations, Pumps, Models, and Syringes

### Safety Aspects
- **Drug Concentrations**
  - Stock only one concentration of a drug.
  - Dilute to a single standard concentration.
- **TCI Pumps**
  - Adequate numbers of TCI pumps should be available.
  - Use a single model of TCI pump, containing a locally approved set of pharmacokinetic models.
  - Program infusion pumps with the brand of syringe used.
- **Syringes**
  - Use a single brand of syringe within a department.
  - Syringes should have Luer-lock connectors to reduce the risk of accidental disconnection.
- **Alarms**
  - Pumps for both TCI infusions and fixed-rate infusions should have audible alarms enabled by default.
  - Alarms should include high pressure, stopped infusion, empty syringe, disconnection from the mains electricity supply, and low battery.
  - Some pumps also have an alarm for a drop in pressure, which may permit some disconnections to be detected.
- **Infusion Rate**
  - Infusion pumps that automatically decrease the infusion rate to a low ‘keep vein open’ (KVO) rate when the syringe is nearly empty should not be used for infusions of propofol or remifentanil.
- **Visual Indicators**
  - There should be a visual display to indicate that the infusion is in progress.
- **Mixing Drugs**
  - Mixing propofol and remifentanil in a single syringe is not recommended.
  - Hypnotic and analgesic components of the anaesthetic can cause issues such as rapid infusion at induction, resulting in an excessive dose of remifentanil.
  - Remifentanil and propofol undergo separation and layering when mixed in a syringe, resulting in varying remifentanil concentrations in different regions of the syringe.

## Drug Infusion Administration Sets and i.v. Cannulae

- **Connections and Valves**
  - Use Luer-lock connectors at each end to reduce the risk of accidental disconnection.
  - Use an antisyphon valve on the drug delivery line(s) to prevent uncontrolled infusion from a damaged syringe.
- **Multiple Infusions**
  - When more than one infusion is given through a single i.v. cannula, an anti-reflux valve should be present to prevent backward flow of drug up the infusion tubing.
  - Join drug and fluid lines as close to the patient as possible to minimize dead space in which a drug may accumulate rather than entering the vein.
- **Minimizing Leakage**
  - Aim for as few potential sites for leakage as possible, ideally a continuous line from syringe to cannula without additional connections or three-way taps.
- **Visibility and Security**
  - Secure and make visible the i.v. line whenever practical.
  - Inspect the cannula site immediately if the patient’s response to the infused drug(s) appears less than expected.

## Preparation for TIVA

- **Charging and Power**
  - Ensure the pumps are charged before use and are mains powered where possible.
- **Programming**
  - Program pumps only after placing a syringe containing the drug to be infused in the pump.
  - Label syringes with the drug name and concentration only when the intended drug is drawn up.

## Conduct of TIVA

- **Pre-Infusion Checks**
  - Check drugs to be administered, the programming of the pump, the infusion set, and the IVI cannula before starting TIVA.
- **Neuromuscular Blocking Drugs**
  - Administer these drugs only after confirming loss of consciousness.
- **Observing Infusion Rate**
  - The anaesthetist should observe the infusion rate (ml/hour or mg/kg/h).
- **Pump Shutdowns**
  - If a TCI pump shuts down due to a depleted battery or malfunction, do not restart using the previous target concentration. Restart in manual mode and program an infusion rate similar to that being delivered at the time of failure.
- **Flushing Devices**
  - Flush all vascular access devices used for TIVA with at least twice the dead space volume at the end of the procedure to prevent potent anaesthetic drugs from being accidentally administered postoperatively.

## Consent for Anaesthesia
- Specific formal consent for the use of TIVA per se is not routinely required.

## Monitoring the Patient During TIVA

- **pEEG Monitor**
  - Recommended when a neuromuscular blocking drug is used with TIVA.
  - Should be commenced prior to the block and continued until full recovery from the effects of the neuromuscular blockade has been confirmed by monitoring with a nerve stimulator.

## TIVA in Particular Circumstances

- **Rapid Sequence Induction**
  - Set an initial high target concentration to deliver the induction ‘bolus’ dose of propofol as a rapid infusion, then reduce the target concentration once the desired dose is administered.
  - Co-administration of other drugs with a rapid onset such as remifentanil or alfentanil can reduce the time to loss of consciousness.
- **Switching from Inhalational Anaesthesia to TIVA**
  - Ensure an adequate brain concentration of the IV anaesthetic agent as the concentration of volatile anaesthetic agent falls.
  - Use a TCI pump and increase the target concentration as the end-tidal concentration of the volatile anaesthetic agent falls.
  - Use processed EEG monitoring when switching from an inhaled anaesthetic agent to TIVA in a patient who has received a neuromuscular blocking drug.
- **TIVA in MRI**
  - Not all pumps are MRI compatible. Specific safety issues include:
	1. i.v. cannula site not visible.
	2. High suspicion for problems with infusions; check cannula site, infusion tubing, and connections between scanning sequences.
	3. Pump alarms may not be audible in the scanning room.
	4. Use a single, long infusion line rather than multiple shorter lines to prevent leakages and resistance.
	5. Ensure an appropriate combination of infusion lines, pump(s), and pump settings to prevent infusion stoppage due to high-pressure alarms.
	6. Processed EEG monitoring during MRI is impractical as currently available monitors are not MRI compatible.
- **Remifentanil and Propofol Combination**
  - Start propofol first to produce a faster induction. Starting remifentanil infusion prior to propofol may cause the patient to stop breathing before losing consciousness, requiring caution in those with difficult airways.

## Checklist for Setting Up TCI Systems

1. Use only dedicated pharmacokinetic TCI pumps.
2. Ensure training in the use of the chosen pump and pharmacokinetic model.
3. Ensure the pumps have been serviced in the past 12 months.
4. Ensure the pumps are plugged into the mains.
5. Ensure the batteries are charged.
6. Ensure correct drug dilutions are entered correctly into the pump.
7. Ensure correct syringe type and size data are entered and syringes are mounted correctly.
8. Ensure the pump is programmed for the drug actually attached to it.
9. Ensure low and high infusion pressure alarms are set.
10. Ensure correct patient data are entered.
11. Consider if the targets set are appropriate to the patient’s age and ASA status.
12. Determine a plan B if the pump(s) fail.

## Recommendations for Preventing Technical Problems with TIVA

1. Complete the TCI system checklist.
2. Affix the i.v. cannula firmly to the patient’s skin.
3. Keep the site of TIVA infusion visible to detect disconnection, leakage, or a 'tissued' cannula.
4. Use only a dedicated twoor three-way TIVA set:
	- Anti-siphon valves on drug administration lines
	- Non-return valve on any i.v. fluid line
	- Minimal dead space distal to the point of agent and/or i.v. fluid mixing
5. Use only Luer lock syringes for administering drugs.
6. Do not label the remifentanil syringe until the drug has been added to the diluent.
7. Always check the infusion site if a pump alarms.
8. Flush TIVA drugs from the dead space of a three-way administration set before connection to the patient cannula and out of the cannula at the end of the case.

## Safe Practice Summary

1. Training and competence of all anaesthetists in TIVA delivery.
2. TCI recommended when GA is maintained by propofol infusion.
3. Patient-specific starting target concentrations based on co-administered drugs and clinical situation.
4. Standardized concentrations of propofol ampoules and remifentanil dilution within an anaesthetic department.
5. Infusion set: Luer lock, anti-reflux valves, minimize dead space, specific sets if possible.
6. Insert syringe first, then program the pump.
7. Visibility of the IV cannula/CVC throughout anaesthesia.
8. pEEG familiarity with principles, interpretation, and limitations.
9. pEEG use when NMB is used with TIVA.
10. Same standards of practice and monitoring outside OT when using TIVA, as for in theatre.

## Obesity
- Schnider model >35 BMI not validated. Use adjusted body weight.
- Use depth of anaesthesia monitoring.
- Eleveld model can be used for propofol and remifentanil across a full range of weights.

## Paediatric TIVA

### Advantages
- Rapid equilibration between plasma and effect site (KEO).
- Rapid onset of action independent from alveolar ventilation.
- Improved quality of emergence (reduced delirium).
- Reduced environmental pollution.
- Reduced PONV.
- Choice for children at

 risk of MH.

- Less interference with evoked potential monitoring.

### Disadvantages
- Risk of bacterial contamination.
- Pain on injection.
- Risk of Prise, lactic/metabolic acidosis.
- Need for IV access and sophisticated infusion pumps.
- No reliable point of care monitoring (BIS has interindividual variability) = risk of awareness.
- Prolonged context-sensitive half-life in children.
- Plastic waste.

# Links
- [[Sedation]]
- [[Day case surgery]]
- [[Awareness]]
- [[Paediatric Total Intravenous Anaesthesia (TIVA)]]
- [[Practical Protocols and recipes]]

---

---
**References:**

1. Anderson, B. J. and Houghton, J. (2019). Total intravenous anesthesia and target-controlled infusion. A Practice of Anesthesia for Infants and Children, 177-198.e3. https://doi.org/10.1016/b978-0-323-42974-0.00008-2
2. Nimmo, A. F., Absalom, A., Bagshaw, O., Biswas, A., Cook, T., Costello, A., … & Wiles, M. D. (2018). Guidelines for the safe practice of total intravenous anaesthesia (tiva). Anaesthesia, 74(2), 211-224. https://doi.org/10.1111/anae.14428
**Summary or mindmap:**

---------------------------------------------------------------------------------------------


---

**Copyright**
© 2022 Francois Uys. All Rights Reserved.
