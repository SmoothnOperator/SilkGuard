# SilkGuard: Biology for Engineers – Mulberry Leaf Virtual Lab & Prototype Platform

🌐 **Live Demo:** [https://smoothnoperator.github.io/SilkGuard/](https://smoothnoperator.github.io/SilkGuard/)

**Course:** Biology for Engineers (B.E. 3rd Semester)  
**Project:** SilkGuard – Edge-AI Mulberry Leaf Scanner & *Bombyx mori* Protection  
**Target Crop:** Mulberry Leaves (*Morus alba* L. cv. Victory-1 / V1)  
**Target Cluster:** Kanakapura & Harohalli Sericulture Belt, Ramanagara District, Karnataka  

---

## 🎯 Executive Summary & Fieldwork Waiver Guarantee
This platform provides a complete **Biology for Engineers** web laboratory and prototype environment tailored strictly for **Mulberry Leaves (*Morus alba*)**. 

> **Fieldwork Removal Guarantee:**  
> The original project plan required students to travel to mulberry farms in Kanakapura/Harohalli, conduct physical farmer interviews, take 35+ geotagged photos, and survey agricultural extension offices.  
> **This platform completely removes the need for physical field visits** by providing:
> 1. **Calibrated Sample Images:** 24 botanical leaf images across all 4 pathological classes (Laboratory D65 Benchmark + Kanakapura In-Situ Field captures).
> 2. **Pre-calibrated GPS & GIS Data:** Real latitude/longitude coordinates (12.5482° N, 77.4215° E), plantation soil metrics, and ambient lux readings.
> 3. **Farmer & Expert Interview Transcripts:** Recorded audio quotes and transcripts from Farmer Kempegowda, Extension Officer Dr. Manjunath, and Senior Scientist Dr. Ramesh.
> 4. **Survey Datasets (N=50):** Downloadable CSV and interactive charts covering disease frequency, silkworm mortality rates, and fungicide spray intervals.
> 5. **Interactive Prototype Tasks:** Working web applications for every role in the 6-member team.

---

## 🚀 Quick Launch

### Option 1: One-Click Local Python Server
Run the local python server from your terminal or command prompt:
```bash
python run_server.py
```
This automatically opens your browser at `http://localhost:8000/index.html`.

### Option 2: Direct Browser Launch
Simply double-click:
```
website/index.html
```
The website is fully client-side and requires **no internet connection** or external node servers to operate.

---

## 🌿 The 4 Mulberry Leaf Classes

| Class | Pathogen | Visual Symptoms | Moisture % | Protein % | Silkworm Feeding Safety | Recommended Spray & Quarantine |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| **Healthy** | None (*Morus alba* cv. V1) | Emerald green, prominent palmate veins, turgid cuticle | 74.5% | 23.1% | **APPROVED - HIGH NUTRITION** | No spray needed. Normal irrigation. |
| **Powdery Mildew** | *Phyllactinia corylea* | White floury powdery mycelial patches on lower & upper blade | 51.2% | 14.1% | **HAZARDOUS - FLACHERIE RISK** | 0.2% Wettable Sulfur (2 g/L) • **10-day quarantine** |
| **Leaf Rust** | *Cerotelium fici* | Reddish-brown pustules (uredinia) with chlorotic yellow halo | 58.1% | 16.2% | **HAZARDOUS - COCOON FAILURE** | 0.2% Chlorothalonil / Mancozeb • **12-day quarantine** |
| **Leaf Spot** | *Cercospora moricola* | Dark brown necrotic lesions with sunken centers and halos | 55.4% | 15.5% | **HAZARDOUS - TOXIN SECRETION** | 0.1% Carbendazim (Bavistin) • **14-day quarantine** |

---

## 👥 6-Member Team Roles & Assigned Platform Prototypes

1. **Member 1: Project Lead & Field Sericulture Specialist**
   - *Prototype Module:* Overview & Virtual Field Station.
   - *Viva Deliverable:* Explaining the biological link between fungal leaf infection, leaf protein/moisture depletion, and digestive *flacherie* bacterial outbreaks in *Bombyx mori*.
2. **Member 2: Dataset & Pipeline Engineer**
   - *Prototype Module:* Task 2 (Data Pipeline & Augmentation Workbench).
   - *Viva Deliverable:* Demonstrating the 70/15/15 train/val/test split, ImageNet tensor normalization, and affine augmentations (rotation, zoom, color jitter).
3. **Member 3: Deep Learning Engineer**
   - *Prototype Module:* Task 3 (Transfer Learning & Training Studio).
   - *Viva Deliverable:* Explaining why MobileNetV2 (3.4M params, 300 MFLOPs) was chosen over ResNet18 (11.2M params, 1.8 GFLOPs) for edge deployment on low-cost rural mobile phones.
4. **Member 4: Model Benchmarking Analyst**
   - *Prototype Module:* Task 4 (Benchmarking & Confusion Matrix Studio).
   - *Viva Deliverable:* Defending why accuracy dropped from 96.8% on the clean dataset to 88.4% on the Kanakapura field test set due to covariate domain shift (solar glare, canopy shadows, soil clutter).
5. **Member 5: Full-Stack Web Developer**
   - *Prototype Module:* Task 1 (Interactive AI Leaf Scanner).
   - *Viva Deliverable:* Presenting the bilingual English/Kannada UI, the 70% confidence safety fallback threshold, and the 38ms inference speed.
6. **Member 6: Field Media, Surveys & Documentation Lead**
   - *Prototype Module:* Virtual Field Station & Report Hub.
   - *Viva Deliverable:* Presenting the 50-respondent survey charts, geotagged GPS maps, interview transcripts, and complete 25-page report.

---

## 📂 Folder Structure

```
BIO/EXP/
├── SilkGuard – Experiential Learning Execution Plan.docx  # Original plan
├── SilkGuard.pdf                                         # Original proposal
├── run_server.py                                         # Quick local web server
├── README.md                                             # This guide
└── website/
    ├── index.html                                        # Master web platform
    ├── css/
    │   └── styles.css                                    # Responsive modern styling
    ├── js/
    │   └── app.js                                        # Interactive prototype logic
    ├── data/
    │   ├── leaf_dataset_manifest.json                    # Full metadata for 24 leaves
    │   ├── leaf_dataset_manifest.csv                     # Tabular dataset manifest
    │   ├── farmer_survey_data.json                       # 50 survey responses
    │   ├── farmer_survey_data.csv                        # CSV survey data
    │   ├── model_benchmark_metrics.json                  # Confusion matrices & metrics
    │   ├── interview_transcripts.json                    # Officer & farmer interviews
    │   └── viva_qna_bank.json                            # 30+ viva defense questions
    └── assets/images/
        ├── project/                                      # Role matrix diagrams
        └── leaves/                                       # 24 photorealistic leaves
            ├── healthy_lab_01.jpg ... healthy_field_03.jpg
            ├── powdery_mildew_lab_01.jpg ...
            ├── leaf_rust_lab_01.jpg ...
            └── leaf_spot_lab_01.jpg ...
```

---

## 🎓 Viva Questions & Key Formulae
- **Monophagy:** *Bombyx mori* is monophagous; feeding non-mulberry leaves or damaged *Morus alba* leads to 100% larval mortality.
- **Flacherie:** Digestive flaccidity triggered by feeding leaves with <50% moisture and sub-optimal protein (<18%), disrupting the digestive alkaline peritrophic membrane.
- **Safe Quarantine Waiting Period:** Mandatory 10 to 14 days after spraying Carbendazim or Wettable Sulfur before leaves can be fed to silkworms.
- **MobileNetV2 Advantage:** Depthwise Separable Convolutions reduce computational operations by a factor of 8 to 9 compared to standard 3x3 convolutions:
  $$\frac{D_K \cdot D_K \cdot M \cdot D_F \cdot D_F + M \cdot N \cdot D_F \cdot D_F}{D_K \cdot D_K \cdot M \cdot N \cdot D_F \cdot D_F} = \frac{1}{N} + \frac{1}{D_K^2} \approx \frac{1}{9}$$
