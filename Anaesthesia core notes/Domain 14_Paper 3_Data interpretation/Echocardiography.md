---
Domain: "14"
Subdomain:
  - Data-interpretation
Date: 2024-07-10
tags: [ECHO, TOE]
Date modified: Friday, October 4th 2024, 4:56:22 pm
---

# Introduction to Ultrasound

## Definition of Ultrasound
- **Ultrasound (US)** is the vibration of sound at a frequency above the threshold of human hearing. Ultrasound is defined as any frequency greater than 20,000 Hz. Medical ultrasound typically operates at frequencies of 1,000,000 Hz (1 Megahertz) or greater.
- Ultrasound probes or transducers are designed with a specific frequency, known as the **bandwidth**, typically ranging between 2 Megahertz and 10 Megahertz. For instance, probes used for general abdominal imaging operate at 2.5-3.5 MHz, whereas those for superficial imaging use 5.0-10 MHz.

## Image Generation
- Ultrasound images are traditionally created using the **Piezoelectric Effect**. This involves the vibration of a piezoelectric crystal at the tip of the transducer, generating ultrasonic frequencies that create ultrasound waves.
  - Piezoelectric crystals are delicate and costly, with replacements costing thousands of dollars.
- The ultrasonic waves penetrate the body's soft tissues and reflect back to the transducer. These returning waves are converted into ultrasound images displayed on a screen.
- Understanding the physics of waves is fundamental to grasping how ultrasound images are formed, how ultrasound artifacts occur, and how to use advanced ultrasound applications such as Doppler.

**Note:** Some newer handheld ultrasound devices utilize silicon chips instead of the traditional piezoelectric effect to create images. However, the principles of wave physics remain applicable.
![](Pasted%20image%2020240224143121.png)
## Does Echo Influence Survival Outcome

- Echo improves diagnostic accuracy but is not associated with improved survival or shorter hospital stay.
## Physics
### Frequency and Wavelengths

- **Frequency**: The number of sound wave cycles per second.
- **Wavelength**: The length or distance of a single cycle of a wave.
- **Equation**: Frequency = Speed of sound wave / Wavelength
	- As wavelength increases, frequency decreases (and vice versa).
	- Shorter wavelength = Higher frequency
	- Longer wavelength = Lower frequency

#### Impact of Frequency on Ultrasound Imaging

- **High-Frequency Probes**:
	- Emit shorter wavelengths
	- Provide better resolution
	- Have decreased penetration
- **Low-Frequency Probes**:
	- Emit longer wavelengths
	- Provide deeper penetration
	- Have lower resolution

#### Types of Probes and Their Characteristics

- **Phased Array Probe**: Great penetration, moderate resolution
- **Curvilinear Probe**: Good penetration, good resolution
- **Linear Probe**: Poor penetration, excellent resolution

![](Pasted%20image%2020240224141347.png)

![](Pasted%20image%2020240224141421.png)

### Acoustic Impedance

- **Definition**: Acoustic impedance (Z) is the resistance to ultrasound propagation as it passes through a tissue.
- **Equation**: Impedance = Density x Propagation Speed of Sound Wave
- **Dependence**: Acoustic impedance is dependent on the tissue density and the speed of sound through that tissue.
- **Effect**: As tissue density increases, the impedance (resistance) increases as well.

### Reflection of Ultrasound Waves

- **Mechanism**: Reflection occurs when ultrasound waves encounter the interface of two tissues with significantly different impedance values.
- **Proportion**: The proportion of reflected ultrasound waves is proportional to the difference in impedance between the two tissues.
- **Example**: Bone and air appear as bright lines on ultrasound due to the large impedance difference from soft tissue, causing almost all ultrasound waves to reflect back.
	- **Impedance Values**: Air (0.0004), Bone (12), Soft tissue (1.6).

### Refraction of Ultrasound Waves

- **Mechanism**: Refraction occurs when ultrasound waves encounter tissues with slightly different impedance values.
- **Effect**: The speed of the ultrasound waves changes, causing a change in direction (refraction).
- **Dependence**: The degree of refraction depends on the angle of incidence and the change in speed in the second medium.
- **Example**: Refraction is seen at the rounded interfaces between fluid-filled structures and adjacent soft tissues, causing edge artifacts such as black lines from the edges of structures like the gallbladder, cysts, vessels, and bladder.

## Attenuation–Absorption

- **Definition**: Attenuation is the loss and absorption of ultrasound energy as it passes through a medium.
- **Effect**: Describes how rapidly a medium reduces the intensity of an ultrasound wave.
- **High Attenuation Mediums**: Air and bone have the highest attenuation.
- **Dependence**: Unlike impedance, attenuation is not solely dependent on the density of the material.
![](Pasted%20image%2020240224143146.png)
## Doppler Effect

- **Definition**: The Doppler Effect (or Doppler Shift) evaluates movement either towards or away from the ultrasound probe/transducer. Commonly used to detect blood movement, but can also evaluate tissue and muscle movement.

### Doppler Shift Equation

- **Equation**: Doppler Shift = (2 x Velocity of blood x Transducer frequency x cos θ) / Propagation speed
	- **θ**: Angle of Insonation (angle of incidence between the ultrasound beam and the direction of flow).
- **Dependence**: The Doppler shift is primarily related to:
	1. The velocity of the blood cells.
	2. The angle of insonation.
- **Technique**: For accurate Doppler measurements, ensure the movement is parallel to the ultrasound probe (0 degrees). Angles above 25-30 degrees will significantly underestimate measurements. At 90 degrees, the Doppler will read no flow due to the cosine of 90 degrees being 0.

**Note**: While using the velocity of blood as an example, the same principles apply when measuring muscle movement using tissue Doppler.
![](Pasted%20image%2020240224141711.png)

## Artifacts in Ultrasound

### Mirror Image Artifact
- **Description**: Occurs when ultrasound waves encounter a highly reflective surface adjacent to air.
- **Common Instances**: Pleural-diaphragm interface causing the appearance of “liver” or “spleen” inside the lung; pleural-pericardium interface during cardiac ultrasound.

### Acoustic Shadowing Artifact
- **Description**: Occurs when ultrasound waves encounter a structure with a high attenuation coefficient.
- **Common Instances**: Bones, ribs, and gallstones.

### Posterior Acoustic Enhancement
- **Description**: The opposite of acoustic shadowing; occurs when ultrasound waves pass through a structure with significantly low attenuation, such as blood or fluid-filled structures.
- **Common Instances**: Bladder, gallbladder, cysts, vessels, ocular ultrasound.

### Edge Shadowing Artifact
- **Description**: Caused by refraction; ultrasound waves are deflected from their original path when they encounter curved and smooth-walled structures.
- **Common Instances**: Vessel walls, gallbladder, cystic structures, testicle, aorta.

### Reverberation Artifact
- **Description**: In the presence of highly reflective surfaces, echoes may reflect back and forth between the reflective surface and the ultrasound probe, causing multiple echoes on the screen.
- **Example**: Highly reflective pleural line causing "A-lines" in normal lung ultrasound.

### Comet Tail Artifact
- **Description**: A form of reverberation artifact where two reflective surfaces are closely spaced, making it difficult to distinguish between each reflected echo.
- **Characteristic**: Dissipates with depth and has a triangular, tapered shape.
- **Common Instance**: Arising from a needle tip.

### Ring Down Artifact
- **Description**: Previously thought to be a type of comet tail artifact. Distinct in that echoes do not dissipate with depth and form bright echogenic lines going to the bottom of the screen.
- **Common Instance**: Seen as "B-lines" in lung ultrasound, indicating interstitial edema.
- **Theory**: Caused by ultrasound waves reflecting infinitely in a tetrahedron of air bubbles.

### Side Lobe Artifact
- **Description**: Occurs when an off-axis side lobe beam encounters a structure, creating a duplicate structure on the screen but in a different area.
- **Common Instance**: Appears as a moving structure in the left atrium, but actually a side lobe artifact from the mitral valve leaflet.
- **Significance**: Important to confirm multiple views to differentiate between artifact and pathology, such as clots or foreign bodies.
## Probes

![](Pasted%20image%2020240224142232.png)

### Probe Movement
- Only do one movement at a time. 1mm of movement of probe on patient is 2cm on screen
![](Pasted%20image%2020240224142308.png)
## Modes of Ultrasound

### B-Mode (Brightness Mode) or 2D Mode

- **Description**: Creates a two-dimensional (2D) greyscale image and is the most commonly used mode in ultrasound.
- **Importance**: Mastering B-mode is crucial for proficiency in point-of-care ultrasound (POCUS). All other modes rely on obtaining a good B-mode image.
- **Access**:
	- "B" button on GE machines.
	- "2D" button on Sonosite and Philips machines.
- **Tip**: Reset settings to B-mode/2D by pressing the corresponding button.

### M-Mode (Motion Mode)

- **Description**: Displays motion versus time along a chosen line from a B-mode image. Motion is on the Y-axis, and time is on the X-axis.
- **Applications**:
	- Evaluating E point septal separation in cardiac scanning.
	- Calculating fetal heart rate in obstetrics.
	- Assessing lung sliding to rule out pneumothorax.
- **Mechanism**: M-mode takes a "slice" of the B-mode image along the cursor line and translates it over time, showing the relative motion of structures.

### Pulse Wave (PW) Doppler Mode

![](Pasted%20image%2020240224142548.png)

- **Description**: Measures the velocity of blood flow at a single point using a sample gate.
- **Limitation**: Maximum speed detectable is limited by the Nyquist Limit; aliasing occurs if this limit is exceeded. Not suitable for high-velocity applications (>200 cm/s).
- **Applications**: Measuring cardiac output (LVOT VTI) and diastolic dysfunction.

### Continuous Wave (CW) Doppler Mode

- **Description**: Measures all points along the cursor line and can detect very high velocities (>1000 cm/s). It does not alias.
- **Application**: Optimal for measuring high-velocity flow, such as valvular stenosis and regurgitation.
- **Mechanism**: Measures the maximum velocity of flow detected along the cursor line but cannot specify the exact location of the velocity.

### Tissue Doppler Imaging (TDI) Mode

- **Description**: A form of Pulse Wave Doppler designed to measure slower speeds of tissue/muscle movement (1 cm/s–20 cm/s).
- **Access**: Usually involves pressing a "TDI" button/knob while in Pulse Wave Doppler mode.
- **Principle**: Applies the same principles as Pulse Wave Doppler but for slower tissue movement rather than faster blood flow.

# Basics of Operation

## Positioning

Stand on the left side of the patient with the probe in the right hand. The patient should be in the left lateral position with the arm above the head.

## Probe Marker Orientation

Locate the marker on the screen. With echocardiography, the marker is on the right side and corresponds to the marker on the cardiac probe.

## Probe Movement

You can slide, rotate, rock (parallel to probe marker—rock the foot), or tilt (perpendicular to probe marker—tilt the tail) the transducer. Attempt to perform only one movement at a time. Note that 1 mm of movement of the probe on the patient equates to 2 cm on the screen.

## Optimising the Image

- **Depth:** A centimetre scale is seen on the side of the screen indicating the depth of tissue being scanned. Adjust the depth to ensure the entire structure being evaluated or the area of interest is visible on the screen.
- **Gain:** Adjust the intensity of returning echoes shown on the screen. Increasing the gain will brighten the display, while decreasing the gain will darken it.
- **Time Gain Compensation:** Adjusts the gain at varying depths using multiple slider levers.
- **Focus Point:** Define the area you want to focus on.

### Basic Mode (B-Mode) and Motion Mode (M-Mode)
- Gain (Brightness)
- Depth
- Time gain compensation
- Frequency (use higher frequency for more superficial structures, usually 2-4 MHz)
- Focus point
- I-beam (compounding—smooths the picture)
- Grey map (choose the grey scale)
- Zoom (enhances the view, especially useful for M-mode)

### Doppler (Pulse Wave Doppler - PW)
- If the indicator is green, it is active, and you can move it.
- Adjust sample volume (size measured). The sample volume should never be less than the diameter of the vessel and never more than 2/3 of the diameter.
- Steer: Change the direction of measurement.
- Quick angle: Change to 60 degrees and maintain steer.
- Use finite angle adjustment for further angle adjustments.
- I-touch: Automatically adjusts scale and baseline.
- Can invert the image and adjust the baseline.
- Adjust the scale to fit the entire waveform.
- Duplex: Simultaneous live imaging and Doppler.
- Sweep speed: Adjusts the number of waves.

### Color Doppler
- **BART mnemonic: Blue AWAY, Red TOWARDS.**
- Adjust the size and steer the box.
- Gain will adjust color.
- Utilizes pulsed wave Doppler and the Doppler equation to generate colors.
- Aliasing: Blood velocity moving faster than the analyzing frequency shift, leading to misinterpretation.
- Best interpreted when the box is placed inline with blood flow. Aim for cos=0 degrees (cos0=1). If not inline, the angle of observation (cos) will increase and underestimate the velocity of blood flow.
- A larger box will decrease the frame rate, so keep the box as small as possible while including all the areas you want to assess.

![](Pasted%20image%2020240224141833.png)

# CARDIAC and Fluid Responsiveness

![](Pasted%20image%2020240224142803.png)

Patient position: Attempt in Left lateral position or place pillow beneath right shoulder. Might require patient to hold breath for more adequate view.

![](Pasted%20image%2020240224143233.png)

![](Pasted%20image%2020240224143304.png)

![](Pasted%20image%2020240224145433.png)

## Views

![](Pasted%20image%2020240224143358.png)

### General
**Position:** Ideally in left lateral decubitus with left arm above head.  
**4 views:** PLAX, PSAX, A4C, S4C with IVC  
**3 positions:**
- Left parasternal 2-4 ICS
- Apex in MAL
- Sub xiphoid

**Clockwise orientation and probe marker positioning:**
1. 10 o’ clock (right shoulder)
2. 1-2 o’ clock (left shoulder)
3. 3 o’ clock (left side)
4. 12 o’ clock (head)

### Parasternal Long Axis (PLAX)
**How to obtain view:**
- Probe footprint at 2-4 ICS LSB.
- Marker aimed at right shoulder.
- Depth at 10-16.
- Start as close to the sternum as possible and move downwards.

**Criteria for adequate image:**
- Ensure descending aorta in line with marker on screen.
- Apex not visualised.
- MV in middle of screen.
- IV septum and posterior wall should be horizontal.
- Cups of AV valve visualised and symmetric.

**Obtaining RV inflow from PLAX:**
- Tilt footprint downwards (look down).

**Obtaining RV outflow from PLAX:**
- Tilt footprint upwards (look up).

**Rules of thumb:**
- Effusion: Look for descending thoracic aorta to differentiate between pericardial/pleural fluid.
- RV = Aortic Root = LA (1:1:1).
- VL:RV = 2:1.
- MV: Anterior leaflet touching IV septum. AV: Good opening/closing. Thickness.
- LV: Good contractility, muscle should thicken by 50% and move toward cavity during systole.

**Approach:**
- Pericardial effusion.
- RV size.
- LA size.
- LV size.
- LV contractility.
- MV leaflet approximates the septum.
- MV morphology and movement normal.
- AV morphology and movement normal.

### Short Axis (PSAX)
**How to obtain view:**
- Start from PLAX with mitral valve at the center of the screen.
- Rotate 60-90 degrees clockwise toward the left shoulder to obtain PSAX at the level of the MV.
- Probe marker between left sternal notch and MCL.

**Criteria for adequate image:**
- Should be able to visualise all 6 walls and circular.

**Tips and tricks:**
- Tilt tail of probe towards right shoulder to visualise lower levels and away from right shoulder to visualise higher levels.
- May need to go one ICS higher and more lateral.

**4 different views depending on level:**
- Aortic valve (RV inflow/Outflow view). Start from PLAX when aortic valve is in the centre of the screen. “Mercedes sign”. Measurement of AV using PISA.
- Mitral valve. Start from PLAX when mitral valve is in the centre of the screen. Tilt tail away from right shoulder to find the aortic valve.
- Papillary muscle/Apex. Tilt tail towards right shoulder. Move 1 ICS down to assist view. Teicholtz measurement possible.
- Pulmonary artery view: At aortic valve level. Tilt tail away from right shoulder and increase clockwise rotation. May need to go 1 ICS up and more lateral.

**Approach:**
- Assess overall ventricular movement and function.
- LV: Good equal kinetic movement. At papillary level place finger in the center of LV and see if all chambers contract towards it.
- RV: If larger than the left, investigate.
- IVS: Should contract equally. If it bulges, look for RV overload.
- MV and AV: Motion and thickness.

![](Pasted%20image%2020240224143933.png)

### Apical 4 Chamber (A4C)
**How to obtain view:**
- Palpate the maximal apex beat for probe placement, usually in 4-6 ICS between MCL-AXL.
- Probe marker at 03-05 o'clock position (left).
- Start just medial of the target and “window shop” superiorly and inferiorly.

**Criteria for adequate image:**
- All four chambers with IV valves should be visible (Tricuspid valve displaced more towards apex in relation to the mitral valve).
- Septum should be vertical, and the LV apex in the centre of the screen.

**Tips and tricks:**
- To centre the apex, slide the transducer more laterally or medially.
- To straighten the septum, tilt the tail of the probe laterally or medially.

**3 different views:**
1. **Apical 5 Chamber:** From A4C, tilt the tail down. May need to slide laterally or medially.
2. **Apical 2 Chamber:** From A4C with LV in the centre, rotate 30-60 degrees counter-clockwise (no RV should be seen). Marker towards patient’s axilla.
3. **Apical 3 Chamber:** From A2C, continue to rotate counter-clockwise (marker to the right shoulder).

### Subcostal
**How to obtain view:**
- 1-2 cm below the xiphoid process right to the midline.
- Probe to left flank (02 o'clock position).

**Tips and tricks:**
- To see the IVC, bring RA to the centre and rotate counterclockwise 60-90 degrees towards the patient's head.

### RV Outflow Tract
**How to obtain view:**
- From PLAX, tilt the tail downwards and rotate 30-45 degrees clockwise.
- May need to move 1 ICS higher.

### RV Inflow
**How to obtain view:**
- From PLAX, tilt the tail toward the right shoulder.

### IVC
**How to obtain view:**
- From subcostal, tilt the probe toward the right atrium and rotate 60-90 degrees toward the head.

**Criteria for adequate image:**
- The hepatic vein will enter the IVC at a 90-degree angle just after the RA.
- RA/IVJ should be visible.

### Probe Marker Orientation (if Marker on Left Side of screen)
- **Subcostal:** Towards you.
- **Long Axis:** Left hip 2 ICS LSB.
- **Short Axis:** Left shoulder 2 ICS LSB.
- **Apex:** Towards you 5th ICS.
## FOCUS/FATE Examination

![](Pasted%20image%2020240224145734.png)

![](Pasted%20image%2020240224145800.png)

![](Pasted%20image%2020240224145831.png)

![](Pasted%20image%2020240224145903.png)

### Parasternal Long Axis (PLAX)

#### Binary Questions

- Is the heart and valves moving well?
- Are the chamber sizes proportional?
- Is there an effusion?
- What is the systolic function?

#### Qualitative Assessment

- **RV:** RV = Aortic Root = LA (1:1:1); LV:RV= 2:1
- **AV:** Good opening/closing; assess for thickness.
- **LA:** Should not be much larger than the Aortic root.
- **Aortic Root:** Measure just beyond sinuses from interior to interior wall; >4cm needs investigation.
- **MV:** Anterior leaflet should touch the IV septum; assess thickness and motion.
- **RV:** Assess size and contractility.
- **LV:** Good contractility; muscle should thicken by 50% and move toward cavity during systole. Assess thickness and size (if less, could indicate hypokinesis, dyskinesis, or akinesis).
- **Effusion:** Look for the descending thoracic aorta to differentiate between pericardial and pleural fluid.
- **Aortic Root Size:** Ensure measurement accuracy for potential pathological investigation.

#### Quantitative Assessment

- **EF (Systolic), EPSS, LVOT**
- **LV Diameter:** Measure in diastole just anterior to MV leaflets. Measure from beyond septal muscle up to posterior wall muscle.
- **Septum:** Normal < 1.2cm; Severe > 2cm.
- **LVD:** Normal < 6cm; Severe > 6.5cm.
- **FS (Fractional Shortening):** (LVEdV - LVEsV) / LVEdV x 100; Normal > 25%; Severe < 15%.
#### LV EF (systolic function)

![](Pasted%20image%2020240224144545.png)

### LV Systolic Function Assessment

**How to assess:**

1. **M-mode through the thickest part of the LV** (where MV leaflet ends). Ensure the MV is not seen in M-mode.
2. **Press Measure. Teicholz method:** Systole is narrow, diastole is wide.
3. **Measure IVSd** (IV septum in diastole); **LVIDd** (left ventricular internal diameter in diastole); **LVPWd** (left ventricular posterior wall in diastole). Repeat systolic measurements.
4. The calculation will automatically be done based on the end-diastolic and systolic volume. EF, SV, and FS will be provided.
5. **Add HR on the first and third systolic peak** to determine CO.
6. **Measure width diastole and systole** and do the calculation.

**Maths:** (LVEDV - LVESV) / LVEDV

**Findings:**

- Normal > 55%
- Severe < 35%

**Mitral Annular Plane Systolic Excursion (MAPSE):**

- **How:** M-mode through lateral and medial mitral annulus. Measure from peak to trough.

### Ejection Fraction Using End Point Septal Separation (EPSS)

**Binary Question:** Is the systolic function adequate?

**How to assess:**

- **Measure EPSS:** M-mode through tip mitral valve leaflets

**Findings:**

- Normal: 7mm
- HFrEF: > 10mm

_Note: Do not use with mitral stenosis or aortic regurgitation._

##### Using MAPSE

![](Pasted%20image%2020240224150154.png)

#### Cardiac Output

![](Pasted%20image%2020240224150052.png)

### LVOT

**How to measure:**

- Click on "Measure" and select AV diameter.
- Manually measure LVOT diameter.
### Short Axis (PSAX)

#### Binary Questions

- Is the heart contracting well?
- Are the chamber sizes proportional?
- Is the IVS bulging into the LV?

### Qualitative Assessment

- Assess overall ventricular movement and function.
- **LV:** Good equal kinetic movement. At the papillary level, place a finger in the center of the LV and see if all chambers contract towards it.
- **RV:** If larger than the left, investigate.
- **IVS:** Should contract equally. If it bulges, then RV overload.
- **MV and AV:** Assess motion and thickness.

### Quantitative Assessment

- **EF (systolic) through papillary muscle view.**

### Apical 4 Chamber (A4C)

#### Binary Questions

- Is the heart and valves moving well?
- Are the chamber sizes proportional?
- Is there an effusion?
- What is the LV diastolic function?
- What is the RV function?
- Is the patient fluid responsive?

### Qualitative Assessment

- **LV:** General function, contractility, size.
- **Valves:** Assess opening and closing.
- **RV:** Important view for function.
- **Normal RV:** 1/3 LV 2/3

### Quantitative Assessment

- **LV Diastolic function, RV Function (TAPSE, Systolic excursion). MAPSE. Stroke volume/fluid responsiveness VTI (in 5 chamber view). Simpson’s method for systolic function.**

### Simpson’s Method (A4C)

**Binary Question:** What is the ejection fraction?

**How to assess:**

1. Freeze image when heart is at its widest and select "Measure SimP (A4C)."
2. Select "Trace" and manually trace the internal diameter.
3. Repeat measurement at its narrowest portion.

### LV Diastolic Function

**Binary Question:** Is there diastolic dysfunction?

**How to assess:**

- **Measure Mitral inflow via Doppler flow (PW) wave** at tips of mitral valve when open and assess diastolic inflow.
- PW is a form of spectral Doppler. The pulse (E/A wave) represents the velocity (y-axis) and time (x-axis). If above the line (positive), blood is moving towards the probe; if below the line, blood is moving away from the probe. The Doppler equation is used to determine velocity (Doppler shift).

**Wave Components:**

- **E-wave:** Early ventricular filling.
- **A-wave:** Atrial contraction.
- **S-wave (negative deflection):** Mitral valve annulus moving away from probe during systole.

**Findings:**

- **Normal:** E > A
- **Impaired relaxation:** A > E
- **Pseudo normal:** E > A (increased LA pressure)
- **Restrictive filling/Diastolic failure:** E/A ratio > 2:1

**Differentiate between pseudo normal and normal:**

- **Tissue Doppler to determine E’ wave:** Place Doppler at septal mitral annulus (where the mitral valve inserts into the septum). Will see negative deflection. E’ wave < 7cm is abnormal.
- **Is the filling or atrial pressure elevated?** e/E’ < 8 (normal); > 15 (abnormal).
- 8-15: if there is CHF, then elevated.
![](Pasted%20image%2020240224140937.png)
![](Pasted%20image%2020240224145410.png)
### RV Function

#### Binary Question

- Is the RV dysfunctional?

**Assessment Methods:**

**Tricuspid Annular Plane Systolic Excursion (TAPSE):**

- **How:** Find the tricuspid annulus on the RV lateral side. Use M-mode. Measure the highest and lowest point of the wave.
- **Findings:**
	- > 16-20mm = normal
	- <16mm = diminished RV function

**Systolic Excursion:**

- **How:** Similar to TAPSE, but add Doppler to the lateral side of the right ventricle (closer to the apex than with TAPSE). Observe the positive deflection (S-wave).
- **Findings:**
	- S-wave > 10cm: normal RV function
![](Pasted%20image%2020240224145305.png)
### Right Heart Strain

#### Parasternal Long Axis (PLAX)

- **Compare LA/Aorta and RV:** Should be 1:1:1. **RV will be enlarged** in strain.

#### Parasternal Short Axis (PSAX)

- **LV Shape:** Should have a round LV. **Septum bulges into LV**, causing a **"D shaped" LV** in strain.

#### Subxiphoid

- **LV Ratio:** LV should be 2/3 of the heart.

#### Apical 4 Chamber (A4C)

- **Chamber Size:** LV should be bigger than RV.
- **McConnell’s Sign:** Apical dipping of RV indicative of acute strain.

#### Dilated IVC

- Indication of right heart strain.

### Stroke Volume/Fluid Responsiveness

#### Binary Question

- Will the patient’s stroke volume increase with fluid?

#### Stroke Volume Calculation

- **Formula:** Stroke volume = LVOT X VTI
- **How to measure:**
	- Measure LVOT in PLAX.
	- In the 5-chamber apical view, place Doppler over the aortic valve outflow. Ensure Doppler line is aligned with LVOT.
	- Calculate VTI by measuring the downward deflection.

**Normal VTI:** 18-22 cm

#### Fluid Responsiveness

- **Method:** Measure VTI before and after a fluid bolus of 200ml or passive leg raise.
- **Findings:**
	- > 15% increase in VTI after fluid bolus indicates fluid responsiveness

_Notes:_

- LVOT: Left ventricular outflow tract diameter
- VTI: Velocity time integral
- Not accurate in arrhythmias

### Subcostal View

#### Qualitative Assessment

- **Pericardial Effusion**
- **RV Size, Thickness, and Function**

#### Quantitative Assessment

- **RV Wall Thickness:** Normal <5mm

### IVC

#### Binary Question

- Should I give fluids?

#### Qualitative Assessment

- **IVC Appearance:** Assess if the IVC looks massive or small and if it is collapsing.

#### Quantitative Assessment

- **How to measure:**
	- Pause the screen while observing the IVC after inspiration (expansion) and after expiration (collapse).
	- Calculate: (Expansion - Collapse) / Expansion

**Findings:**

- **Ventilated Patients:** 16-18% change indicates fluid need.
- **Spontaneous Breathing:** 50% change indicates fluid need.
- **IVC Diameter:** Less than 2 cm indicates volume requirement.

_Notes:_

- Do not use M-mode.
- Measure 2 cm from the RA-IVC junction, just past the hepatic vein.
![](Pasted%20image%2020240224144046.png)
## Valvulopathies
### General Assessment

#### Assessing Leaflet Morphology and Motion

1. **Morphology:** Examine the structure and appearance of the valve leaflets.
2. **Motion:** Evaluate the movement of the valve leaflets during the cardiac cycle.

#### Color Doppler Assessment

1. **Place color Doppler over the valve and preceding chamber:**
	
	- Assess for turbulence prior to the valve during antegrade flow.
	- Evaluate color before and after the valve during retrograde regurgitation.
2. **Techniques:**
	
	- Slow the clip down and freeze to more accurately assess the flow patterns.
	- Look for associated findings when lesions are suspected.
	- The vena contracta indicates the size of the regurgitant orifice.

#### Overcoming Aliasing

1. **Increase the frequency transmitted:**
	
	- Use higher frequency settings to improve resolution and reduce aliasing.
2. **Increase the angle of insonation:**
	
	- Adjust the probe angle to optimize the Doppler signal and reduce aliasing artifacts.
3. **Reduce sampling depth:**
	
	- Decrease the depth of the sample volume to minimize aliasing.
4. **Adjust Doppler velocity scale:**
	
	- Increase the velocity scale to accommodate higher flow velocities.
5. **Baseline shift:**
	
	- Adjust the baseline to better visualize flow patterns and reduce aliasing.
### Aortic Valve
#### Aortic Stenosis

High Niquest limit (60). Sweep speed of 50-100. at least 3 beats

Use multiple views: Suprasternal, subcostal, A5C etc

Long axis (120 ME): Measure LVOT diameter in midsystole(cusp insertion-inner edge to inner edge)

Short axis (40-60 ME): Morphology and CFD

A5C/(Transgastric 120-140):

	CWD through AV for AVmax and gradient 

	PWD through LVOT for calculation of SV and AVA 

Late peaking waveform of AV max suggestive of severe AS

##### Aortic Sclerosis

AVmax ,<2.5/sec

##### Severe
- Vmax: >4.0m/s
- Gradient: >40mmHg
- VA: <1.0cm2
#### Aortic Regurgitation

High Niquest limit (60). Sweep speed of 50-100. at least 3 beats

Use multiple views: Suprasternal, subcostal, A5C etc

Visual: Large, dense central CWD and large convergence zone suggestive of higher grade severity

Regurgitant jet width:

	Jet diameter/LVOT diameter. >65% suggestive of severe AR 

Pressure half time

	Severe AR Pressure half time of <200m/sec (only accurate in severe AR, could be inaccurate with mod AR)

Holodiastolic flow reversal in descending aorta with end diastolic velocity of 20cm/sec (correlates with regurgitant fraction of >40%)

Vena contracta

	Smallest flow diameter of regurgitant jet

	VC of >6mm is severe 

Regurgitant volume

	VTI from CWD of regurgitant jet or calculate the difference from SVLVOTSVMitral valve 

### Mitral Valve
#### Mitral Stenosis

Quantitative (all severe):

	Mean gradient of > 10mmHg 

	Planimetry for valve area: <1.0cm2 

	Pressure half time: >220m/sec

	SPAP: >50mmhg 

Qualitative:

# Lung Ultrasound

![](Pasted%20image%2020240224140817.png)

#### Signs

- **A-lines:**
	
	- Appearance: Horizontal lines seen inside the space, representing reverberations of the pleural line.
	- Characteristics: Motionless and parallel to the pleural line.
- **B-lines (Comet Tails):**
	
	- Appearance: Hyperechoic reverberation artefacts.
	- Characteristics: Vertical, start at the pleural line, span the entire depth of the image, move with normal respiration, and erase the appearance of A-lines.
- **Lung Sliding (Marching Ants):**
	
	- Appearance: Pleurae sliding over each other.
	- Characteristics: The artefact caused by this phenomenon can be appreciated as lung sliding.
- **Lung Pulse:**
	
	- Appearance: Movement of the pleural line.
	- Characteristics: Vertical movement in synchrony with the cardiac rhythm.
- **Lung Point:**
	
	- Description: If there is an absence of lung sliding and a B-line pattern in the anterior chest, moving the probe laterally to the dependent part of the lung may identify this point where normal sliding of the lung is replaced by the pneumothorax.

#### Pneumothorax

- **Where:** 2nd ICS, MCL
- **Probe:** Linear
- **Probe Direction:** Superior

**Findings:**

- **No Lung Sliding:** Absence of the pleurae sliding over each other.
- **Lung Point:** The end of the pneumothorax, do not confuse with the diaphragm.
- **No B-lines:** Absence of B-lines in the affected area.
- **Stratosphere/Barcode Sign in M-mode:** Normal M-mode appearance is an ocean with a beach; the barcode sign indicates pneumothorax.
![](Pasted%20image%2020240224143726.png)
![](Pasted%20image%2020240224143748.png)
### Pleural Effusion

#### Where

- **Location:** Midaxillary line (MAL) around the 5th ICS

#### Probe

- **Type:** Curved
- **Direction:** Superior

#### Findings

- **Spine Sign:** Visualization of vertebral spines, which can also indicate pneumonia if the appearance resembles a mass.
- **Mirror Sign:** Absence of the reflection below the diaphragm.

**Rule of Thumb:** Any effusion >4 cm usually measures >1000 mL.

#### Approach

1. **Hypoechoic Fluid Around Lung Base:**
	- **Spine Sign:** Yes
2. **Quad Sign:** Yes
3. **Sinusoid Sign Seen on M-mode:** Yes
![](Pasted%20image%2020240224143810.png)
### Pneumonia

#### Where

- **Location:** Different chest zones

#### Probe

- **Type:** Cardiac
- **Direction:** Superior

#### Findings

- **Air Bronchograms:**
	- Appearance: White dots.
	- Characteristics:
		- Static: Seen in atelectasis.
		- Dynamic: Pathognomonic for pneumonia.
- **Fluid Bronchograms:**
	- Appearance: Resembles tram tracks.
- **Hepatization:**
	- Description: Lung tissue appears similar to liver tissue.
- **B-lines:**
	- Appearance: Hyperechoic reverberation artefacts.
- **Pleural Effusions:**
	- Description: Presence of fluid in the pleural space.
- **Subpleural Consolidation:**
	- Description: Consolidation located just beneath the pleura.
# VEXUS

![](Pasted%20image%2020240224145200.png)

![](Pasted%20image%2020240224145218.png)

# Links
- [[Transoesophageal ultrasound (TOE)]]
- [[Electrocardiogram (ECG)]]
- [[Cardiac physiology]]

---

---
**References:**

1. Raj, T. D. (2017). Data interpretation in anesthesia.. https://doi.org/10.1007/978-3-319-55862-2
2. Paulus WJ, Tschöpe C, Sanderson JE, Rusconi C, Flachskampf FA, Rademakers FE, Marino P, Smiseth OA, De Keulenaer G, Leite-Moreira AF, Borbély A, Edes I, Handoko ML, Heymans S, Pezzali N, Pieske B, Dickstein K, Fraser AG, Brutsaert DL. How to diagnose diastolic heart failure: a consensus statement on the diagnosis of heart failure with normal left ventricular ejection fraction by the Heart Failure and Echocardiography Associations of the European Society of Cardiology. Eur Heart J 2007;28:2539–50
3. Jensen MB, Sloth E, Larsen KM, Schmidt MB. Transthoracic echocardiography for cardiopulmonary monitoring in intensive care. Eur J Anaesthesiol 2004;21:700–7 3. Frederiksen CA, Juhl-Olsen P, Larsen UT, Nielsen DG, Eika B, Sloth E. New pocket echocardiography device is interchangeable with high-end portable system when performed by experienced examiners. Acta Anaesthesiol Scand 2010;54:1217–23
4. Jakobsen CJ, Torp P, Sloth E. Perioperative feasibility of imaging the heart and pleura in patients with aortic stenosis undergoing aortic valve replacement. Eur J Anaesthesiol 2007;24:589–95
5. Frederiksen CA, Knudsen L, Juhl-Olsen P, Sloth E. Focusassessed transthoracic echocardiography in the sitting position: two life-saving cases. Acta Anaesthesiol Scand 2011;55:126–9
6. Canty DJ, Royse CF, Kilpatrick D, Bowman L, Royse AG. The impact of focused transthoracic echocardiography in the preoperative clinic. Anaesthesia 2012;67:618–25
7. Canty DJ, Royse CF, Kilpatrick D, Williams DL, Royse AG. The impact of pre-operative focused transthoracic echocardiography in emergency non-cardiac surgery patients with known or risk of cardiac disease. Anaesthesia 2012;67:714–20
**Summary or mindmap:**

---------------------------------------------------------------------------------------------
