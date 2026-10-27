# <img src="img/heart-beat.svg" width="30"><img src="img/heart-beat.svg" width="30"><img src="img/heart-beat.svg" width="30"> Awesome Foundation Models for Biosignals [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](https://github.com/guxiao0822/awesome-biosignal-foundation-model/pulls)


Biosignals like ECG, EEG, and PPG capture the body's physiological and behavioural "languages", but analyzing them at scale requires dedicated approaches. Foundation models, which have transformed NLP and computer vision, are now emerging for biosignal analysis, promising to unlock patterns across vast amounts of sensor readings.

This curated list covers **foundation models (FMs), datasets, and tools for biosignals** based on our comprehensive survey of the field.

> **📚 Survey Paper**: [Foundation Models for Biosignals: A Survey](https://www.techrxiv.org/users/953631/articles/1322825/master/file/data/25_BFM_Survey/25_BFM_Survey.pdf?inline=true#scrollbar=1&toolbar=1&statusbar=1&navpanes=1%23&page=1.00&gsr=0) - A comprehensive review of foundation model development and applications for biosignals.


## 🗺️ Landscape of Biosignal Foundation Models
![Three Directions Overview](img/Overview.png)
**timeline marked by the first online date of each work*

The field of biosignal foundation models can be organized into three converging directions:
1. **Pretraining Biosignal FMs from Scratch**: Pretraining dedicated foundation models on large biosignal corpora
2. **Adapting Time Series FMs to Biosignals**: Repurposing general time series foundation models to biosignal tasks
3. **Leveraging LLMs for Biosignals**: Leverage (multi-modal) large language models for biosignal analysis

### 📈 Papers in this list by year
![Papers by year](img/papers_by_year.png)
*Counts papers in the three direction sections, each paper counted once; auto-generated from this README with `python scripts/plot_paper_stats.py`.*

## 📌 Table of Contents

- [🗺️ Landscape](#-landscape-of-biosignal-foundation-models)
- [📚 Surveys & Reviews](#-surveys--reviews)
- [🔬 Datasets & Benchmarks & Tools](#-datasets--benchmarks--tools)
  - [Large-Scale Training Datasets](#large-scale-training-datasets)
  - [Evaluation Benchmarks](#evaluation-benchmarks)
  - [Preprocessing Toolboxes and Packages](#preprocessing-toolboxes-and-packages)
- [🏗️ Pretraining Biosignal Foundation Models from Scratch](#-pretraining-biosignal-foundation-models-from-scratch)
- [🔄 Adapting Time Series Foundation Models to Biosignals](#-adapting-time-series-foundation-models-to-biosignals)
- [🤖 Leveraging Large Language Models for Biosignal Analysis](#-leveraging-large-language-models-for-biosignal-analysis)
- [‼️ Open Challenges](#-open-challenges)
- [🤝 Contributing](#-contributing)

## 📚 Surveys & Reviews

- **[NPJ Digital Medicine, 2026]** Review of open foundation models and datasets for ECG and PPG waveforms [[paper]](https://doi.org/10.1038/s41746-026-03101-7)
- **[National Science Review, 2026]** EEG-FM-Compass: progress, benchmarking and future directions for EEG foundation models [[paper]](https://doi.org/10.1093/nsr/nwag466)
- **[ACM IMWUT, 2026]** Foundation Models Defining A New Era In Sensor-based Human Activity Recognition: A Survey And Outlook [[paper]](https://doi.org/10.1145/3810230)
- **[NPJ Digital Medicine, 2026]** A perspective on federated foundation models in biomedical sensing and imaging [[paper]](https://doi.org/10.1038/s41746-026-03164-6)
- **[ACM Computing Surveys, 2026]** Data-Centric Foundation Models in Computational Healthcare: A Survey [[paper]](https://doi.org/10.1145/3800677)
- **[ICML, 2026]** Position: Beyond Prediction: Toward Verifiable Physiological Waveform Reasoning with Foundation Models and Agentic LLMs [[paper]](https://openreview.net/forum?id=cgpU6fhUXx)
- **[IEEE TPAMI, 2025]** Foundation models defining a new era in vision: a survey and outlook [[paper]](https://arxiv.org/abs/2307.13721)
- **[ACM SIGKDD, 2024]** Foundation models for time series analysis: a tutorial and survey [[paper]](https://arxiv.org/abs/2403.14735)
- **[Arxiv, 2024]** A survey of time series foundation models: generalizing time series representation with large language mode [[paper]](https://arxiv.org/abs/2405.02358)
- **[Arxiv, 2024]** Biomedical foundation model: a survey [[paper]](https://arxiv.org/abs/2503.02104)
- **[Arxiv, 2024]** Deep time series models: a comprehensive survey and benchmark [[paper]](https://arxiv.org/abs/2407.13278)
- **[Arxiv, 2024]** Foundation models for video understanding: a survey [[paper]](https://arxiv.org/abs/2405.03770)
- **[IJCAI, 2024]** Large language models for time series: a survey [[paper]](https://arxiv.org/abs/2402.01801)

## 🔬 Datasets & Benchmarks & Tools
<img src="img/Data%20Perspective.png" alt="Illustration of representative biosignals" width="500"/>


- `ECG` - Electrocardiography (heart electrical activity)
- `EEG` - Electroencephalography (brain electrical activity)  
- `PPG` - Photoplethysmography (blood volume changes)
- `IMU` - Inertial Measurement Unit (motion sensors)
- `EMG` - Electromyography (muscle electrical activity)
- `ABP` - Arterial Blood Pressure
- `PCG` - Phonocardiography (heart sounds)
- `Resp` - Respiration/Respiratory signals (breathing patterns)
- `BCG` - Ballistocardiography (body motion from cardiac ejection)

### Large-Scale Training Datasets

| Dataset | Modality | # Individuals | # Duration (hr) | Link |
|---------|----------|-------------|---------------|------|
| **UKBiobank** | `ECG` `PPG` `IMU` `Health Metrics` | - | - | [[dataset]](https://www.ukbiobank.ac.uk/) |
| **MC-MED** | `ECG` `PPG` `Resp` `Vital Signs` | 70K | - | [[dataset]](https://physionet.org/content/mc-med/1.0.0/) |
| **MIMIC-III-WDB** | `ECG` `PPG` `ABP` `Resp` `Vital Signs` | 30K | 3M | [[dataset]](https://physionet.org/content/mimic3wdb/1.0/) |
| **MIMIC-III-Ext-PPG** | `PPG` `ECG` `ABP` `Resp` | 6K | 53K | [[dataset]](https://physionet.org/content/mimic-iii-ext-ppg/) |
| **VitalDB** | `ECG` `PPG` `ABP` `Resp` `Vital Signs` | 6K | - | [[dataset]](https://vitaldb.net/dataset/) |
| **VitalDB Arrhythmia** | `ECG` | 482 | 204 | [[dataset]](https://doi.org/10.1038/s41597-026-07076-8) |
| **PulseDB** | `ECG` `PPG` `ABP` | 5K | 50M | [[dataset]](https://github.com/pulselabteam/PulseDB) |
| **MESA** | `ECG` `PPG` `EEG` | 2K | - | [[dataset]](https://www.sleepdata.org/datasets/mesa) |
| **VTaC** | `ECG` `PPG` `ABP` | 2K | - | [[dataset]](https://physionet.org/content/vtac/) |
| **CODE** | `ECG` | 2M | - | [[dataset]](https://figshare.scilifelab.se/articles/dataset/CODE_dataset/15169716) |
| **MIMIC-IV-ECG** | `ECG` | 160K | 2K | [[dataset]](https://physionet.org/content/mimic-iv-ecg/1.0/) |
| **PhysioNet2020** | `ECG` | 40K | 90 | [[dataset]](https://physionet.org/content/challenge-2020/1.0.2/) |
| **MEETI** | `ECG` `Text` | - | - | [[dataset]](https://doi.org/10.1038/s41597-026-06796-1) |
| **Pediatric Normal ECG** | `ECG` | - | - | [[dataset]](https://doi.org/10.1038/s41597-026-08301-0) |
| **eICU** | `Vital Signs` | 139K | - | [[dataset]](https://eicu-crd.mit.edu/) |
| **HiRID** | `Vital Signs` | 34K | - | [[dataset]](https://physionet.org/content/hirid/) |
| **OpenMHC** | `Health Metrics` | 12K | 60M | [[dataset]](https://arxiv.org/abs/2607.16235) |
| **UCSF-PPG** | `PPG` | 21K | 600K | [[dataset]](https://tison.ucsf.edu/ppg-diabetes) |
| **Multi-site Wearable PPG** | `PPG` `IMU` | - | 350 | [[dataset]](https://github.com/jiayimaggieshao/wearable-ppg-dataset) |
| **TUEG** | `EEG` | 15K | 27K | [[dataset]](https://isip.piconepress.com/projects/tuh_eeg/) |
| **HBN-EEG** | `EEG` | 3K | 3K | [[dataset]](https://neuromechanist.github.io/data/hbn/) |
| **MOABB** | `EEG` | >1K | - | [[dataset]](https://moabb.neurotechx.com/) |
| **SEED Series** | `EEG` `Gaze Metrics` | - | - | [[dataset]](https://bcmi.sjtu.edu.cn/home/seed) |
| **ROAMM** | `EEG` `Gaze Metrics` | 44 | 50 | [[dataset]](https://openneuro.org/datasets/ds007629) |
| **emg2pose** | `EMG` | 193 | 370 | [[dataset]](https://github.com/facebookresearch/emg2pose) |
| **emg2qwerty** | `EMG` | 108 | 346 | [[dataset]](https://github.com/facebookresearch/emg2qwerty) |
| **HUNT4** | `IMU` | 35K | - | [[dataset]](https://github.com/ntnu-ai-lab/SelfPAB) |
| **Capture24** | `IMU` | 151 | 4K | [[dataset]](https://github.com/OxWearables/capture24) |
| **Ego4D** | `IMU` `Audio` `Gaze Metrics` | 923 | 4K | [[dataset]](https://ego4d-data.org/) |
| **COVID-19 Sounds** | `Audio` | 36K | 552 | [[dataset]](https://www.covid-19-sounds.org/en/blog/neurips_dataset.html) |

### Evaluation Benchmarks

- **PhysioNet Challenges**: Annual international competitions providing standardized evaluation frameworks for various biosignal analysis tasks including ECG interpretation, sleep staging, and arrhythmia detection [[benchmark]](https://physionet.org/challenge/)

- **MOABB** (Mother of All BCI Benchmarks): Comprehensive benchmarking framework for EEG-based brain-computer interface algorithms with standardized pipelines and evaluation protocols [[benchmark]](https://moabb.neurotechx.com/)

- **ECG FM Reality Check** (ICLR 2026): Benchmarks 8 ECG foundation models on 26 clinical tasks from 12 public datasets [[benchmark]](https://github.com/AI4HealthUOL/ecg-fm-benchmarking) [[paper]](https://openreview.net/forum?id=xXRqWpt3Xr)

- **Are EEG Foundation Models Worth It?** (ICLR 2026): Compares EEG foundation models with traditional decoders across BCI tasks under six evaluation protocols [[paper]](https://openreview.net/forum?id=5Xwm8e6vbh)

- **EEG-FM-Bench** (ICML 2026): Systematic evaluation and diagnostic analysis of EEG foundation models over 14 datasets and 10 paradigms [[benchmark]](https://github.com/xw1216/EEG-FM-Bench) [[paper]](https://arxiv.org/abs/2508.17742)

- **SleepBench** (ICML 2026): Open sleep foundation model benchmark built on 166.5K hours of PSG from 9 public sources [[benchmark]](https://github.com/yang-ai-lab/OSF-Open-Sleep-FM) [[paper]](https://openreview.net/forum?id=rlVGCyjqnt)

- **HEARTS** (ICML 2026): Benchmarks LLM reasoning on health time series across 20 signal modalities and 110 tasks [[benchmark]](https://yang-ai-lab.github.io/HEARTS/) [[paper]](https://arxiv.org/abs/2603.06638)

- **SzCORE** (ICML 2026): Seizure detection generalization benchmark of 28 algorithms on 4,360 hours of held-out EEG [[benchmark]](https://epilepsybenchmarks.com/) [[paper]](https://openreview.net/forum?id=3vhn9kVVY5)

### Preprocessing Toolboxes and Packages

| Toolbox/Package  | Modality | Link |
|------------------|----------|------|
| **MNE-Python**   | `EEG`| [[tool]](https://mne.tools/stable/) |
| **NeuroKit**     | `ECG` `PPG` `Resp` `EMG` | [[tool]](https://github.com/neuropsychology/NeuroKit) |
| **HeartPy**      | `ECG` `PPG` | [[tool]](https://python-heart-rate-analysis-toolkit.readthedocs.io/en/latest/) |
| **pyHRV**        | `ECG` `PPG` | [[tool]](https://pyhrv.readthedocs.io/en/latest/) |
| **BIOBSS**       | `ECG` `PPG` `IMU` | [[tool]](https://github.com/obss/BIOBSS) |
| **BioSPPy**      | `ECG` `PPG` `EEG` `Resp` `EMG` `PCG` | [[tool]](https://github.com/scientisst/BioSPPy) |
| **PyPhysio**     | `ECG` `PPG` `IMU` | [[tool]](https://gitlab.com/a.bizzego/pyphysio) |
| **EEGLAB**       | `EEG` | [[tool]](https://eeglab.org/) |
| **Vital-Sqi**    | `ECG` `PPG` | [[tool]](https://github.com/meta00/vital_sqi) |
| **PhysioKit**    | `PPG` `Resp` | [[tool]](https://github.com/PhysiologicAILab/PhysioKit) |
| **PPGFeat**      | `PPG` | [[tool]](https://github.com/saadsur/PPGFeat) |
| **WFDB Toolbox** | `ECG` `PPG` `EEG` `Resp` `ABP` `EMG` | [[tool]](https://physionet.org/content/wfdb-matlab/0.10.0/) |
| **PyPPG**        | `PPG` | [[tool]](https://pyppg.readthedocs.io/) |
| **braindecode**  | `EEG` `MEG` | [[tool]](https://braindecode.org/) |
| **EEGEmoLib**    | `EEG` | [[tool]](https://doi.org/10.1093/nsr/nwag460) |
## 🏗️ Pretraining Biosignal Foundation Models from Scratch
<!-- Badge Definitions -->
[ECG]: <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/>
[EEG]: <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/>
[EOG]: <img src="https://img.shields.io/badge/EOG-pink" alt="EOG" height="16"/>
[PPG]: <img src="https://img.shields.io/badge/PPG-purple" alt="PPG" height="16"/>
[IMU]: <img src="https://img.shields.io/badge/IMU-orange" alt="IMU" height="16"/>
[EMG]: <img src="https://img.shields.io/badge/EMG-green" alt="EMG" height="16"/>
[MEG]: <img src="https://img.shields.io/badge/MEG-darkblue" alt="MEG" height="16"/>
[Resp]: <img src="https://img.shields.io/badge/Resp-yellow" alt="Resp" height="16"/>
[Health-metrics]: <img src="https://img.shields.io/badge/Health--metrics-lightblue" alt="Health-metrics" height="16"/>
[iEEG]: <img src="https://img.shields.io/badge/iEEG-steelblue" alt="iEEG" height="16"/>
[BCG]: <img src="https://img.shields.io/badge/BCG-crimson" alt="BCG" height="16"/>

*Building dedicated foundation models using large biosignal corpora*
- **[Nature Communications, 2026]** A unified time-frequency foundation model for sleep decoding <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> <img src="https://img.shields.io/badge/EMG-green" alt="EMG" height="16"/> <img src="https://img.shields.io/badge/EOG-pink" alt="EOG" height="16"/> [[paper]](https://www.nature.com/articles/s41467-025-67970-4)[[code]](https://github.com/LordXX505/SleepGPT)
- **[Nature, 2026]** A foundation model for continuous glucose monitoring data <img src="https://img.shields.io/badge/Health--metrics-lightblue" alt="Health-metrics" height="16"/> [[paper]](https://www.nature.com/articles/s41586-025-09925-9)[[code]](https://github.com/Guylu/GluFormer)
- **[Nature, 2026]** Insulin resistance prediction from wearables and routine blood biomarkers <img src="https://img.shields.io/badge/Health--metrics-lightblue" alt="Health-metrics" height="16"/> [[paper]](https://www.nature.com/articles/s41586-026-10179-2)[[code]](https://github.com/Google-Health/consumer-health-research/tree/main/insulin_resistance_prediction)
- **[Nature Machine Intelligence, 2026]** Cardiac health assessment across scenarios and devices using a multimodal foundation model pretrained on data from 1.7 million individuals. <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> <img src="https://img.shields.io/badge/PPG-purple" alt="PPG" height="16"/> [[paper]](https://www.nature.com/articles/s42256-026-01180-5)[[code]](https://github.com/guxiao0822/Cardiac-Sensing-FM)
- **[Nature Medicine, 2026]** A multimodal sleep foundation model for disease prediction <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/>  <img src="https://img.shields.io/badge/Resp-yellow" alt="Resp" height="16"/> <img src="https://img.shields.io/badge/EMG-green" alt="EMG" height="16"/>[[paper]](https://www.nature.com/articles/s41591-025-04133-4) [[code]](https://github.com/zou-group/sleepfm-clinical)
- **[Lancet Digital Health, 2026]** Development and external validation of a contrastive learning foundation model for ECG-based prediction of cardiovascular diseases and outcomes <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://doi.org/10.1016/j.landig.2026.101092)
- **[Lancet Digital Health, 2026]** Toward unified and comprehensive automated electroencephalogram interpretation: a multicentre development and validation of an electroencephalogram foundation model <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://doi.org/10.1016/j.landig.2026.101039)
- **[Nature Communications, 2026]** A self-supervised electrocardiogram foundation model for empowering cardiovascular disease prediction and genetic factor discovery <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://www.nature.com/articles/s41467-026-72436-2)[[code]](https://github.com/biomed-AI/ECG-LFM)
- **[European Heart Journal, 2026]** Foundation models for electrocardiogram interpretation: clinical implications <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://doi.org/10.1093/eurheartj/ehaf1119)[[code]](https://github.com/HeartWise-AI/DeepECG_Docker)
- **[European Heart Journal - Digital Health, 2026]** Wearable-Echo-FM: an ECG echo foundation model for 1-lead electrocardiography <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://academic.oup.com/ehjdh/article/7/4/ztag049/8541415)[[code]](https://github.com/CarDS-Yale/Wearable-Echo-FM)
- **[NPJ Digital Medicine, 2026]** Sleep EEG foundation models reveal within-stage microstructure that improves health screening beyond traditional stages <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://www.nature.com/articles/s41746-026-02970-2)
- **[NPJ Digital Medicine, 2026]** BenchECG and xECG: a benchmark and baseline for ECG foundation models <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://www.nature.com/articles/s41746-026-03196-y) [[code]](https://github.com/dlaskalab/bench-xecg/)
- **[IEEE TBME, 2026]** TinyMyo: a Tiny Foundation Model for Flexible EMG Signal Processing at the Edge <img src="https://img.shields.io/badge/EMG-green" alt="EMG" height="16"/> [[paper]](https://arxiv.org/abs/2512.15729)[[code]](https://github.com/pulp-bio/BioFoundation)
- **[IEEE TBME, 2026]** FEMBA on the Edge: Physiologically-Aware Pre-Training, Quantization, and Deployment of a Bidirectional Mamba EEG Foundation Model on an Ultra-Low Power Microcontroller <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://doi.org/10.1109/TBME.2026.3683482)
- **[IEEE JBHI, 2026]** SingLEM: Single-Channel Large EEG Model <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://doi.org/10.1109/JBHI.2026.3732223)[[code]](https://github.com/ttlabtuat/SingLEM)
- **[IEEE JBHI, 2026]** A Foundation Model for Wearable Movement Data in Mental Health Research <img src="https://img.shields.io/badge/IMU-orange" alt="IMU" height="16"/> [[paper]](https://arxiv.org/abs/2411.15240)[[code]](https://github.com/njacobsonlab/Pretrained-Actigraphy-Transformer/)
- **[Journal of Neural Engineering, 2026]** A pretrained foundation model for headache disorders based on magnetoencephalography <img src="https://img.shields.io/badge/MEG-darkblue" alt="MEG" height="16"/> [[paper]](https://doi.org/10.1088/1741-2552/ae2805)
- **[NeurIPS, 2026]** Next-Token Prediction Enables Scalable Learning of Sleep Physiology <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> <img src="https://img.shields.io/badge/Resp-yellow" alt="Resp" height="16"/> [[paper]](https://openreview.net/forum?id=pXVvnchQzY)
- **[NeurIPS, 2026]** Inertia-1: An Open Exploration of Wearable Motion Foundation Models <img src="https://img.shields.io/badge/IMU-orange" alt="IMU" height="16"/> [[paper]](https://arxiv.org/abs/2607.06617)
- **[NeurIPS, 2026]** GlucoFM: A Dual-Stream Foundation Model for Continuous Glucose Monitoring <img src="https://img.shields.io/badge/Health--metrics-lightblue" alt="Health-metrics" height="16"/> [[paper]](https://openreview.net/forum?id=SxWZ7KJ3KP)
- **[NeurIPS, 2026]** NeuroRVQ: Multi-Scale Biosignal Tokenization for Generative Foundation Models <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> <img src="https://img.shields.io/badge/EMG-green" alt="EMG" height="16"/> [[paper]](https://arxiv.org/abs/2510.13068)
- **[NeurIPS, 2026]** VCR: Learning Valid Contextual Representation for Incomplete Wearable Signals <img src="https://img.shields.io/badge/Health--metrics-lightblue" alt="Health-metrics" height="16"/> [[paper]](https://openreview.net/forum?id=5BWCy21RFh)
- **[NeurIPS, 2026]** NeuroNTP - A Generalizable Multimodal Foundation Model for Epilepsy <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://openreview.net/forum?id=seM8LkgKy6)
- **[NeurIPS, 2026]** CLEF: EEG Foundation Models for Learning Clinical Semantics <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://openreview.net/forum?id=wMcJWB6pBK)
- **[NeurIPS, 2026]** B[FM]²: Brain Foundation Model via Flow Matching with SplitUNet <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://openreview.net/forum?id=zdfQqwhwe7)
- **[NeurIPS, 2026]** EEG-X: Toward Device-Agnostic and Noise-Robust Foundation Models for EEG <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://openreview.net/forum?id=UHwOAjPtEg)
- **[NeurIPS, 2026]** MAGE: Towards Generalizable Multi-timescale EEG Representations <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://openreview.net/forum?id=cBtjuprKBt)
- **[NeurIPS, 2026]** MENDR: Manifold-Embedded Neural Data Representations for Channel-Agnostic EEG Foundation Modeling <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://openreview.net/forum?id=pf1CbF5JeQ)
- **[NeurIPS, 2026]** SPERA: Spherical Prior EEG Foundation Model with Geometry- and Frequency-Aware Latent Prediction <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://openreview.net/forum?id=71zbNNbFKV)
- **[NeurIPS, 2026]** Vibe-Spike: An Energy-Preserving EEG Foundation Model Through the Landscape of Neural Coherence <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://openreview.net/forum?id=C1hqOzVwCn)
- **[NeurIPS, 2026]** Process-conditioned Pretraining with Topographic Spatial Retrieval for Large EEG Models <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://openreview.net/forum?id=wrHWTrf4Uv)
- **[NeurIPS, 2026]** LEAF: Language-EEG Aligned Foundation Model for Brain-Computer Interfaces <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://openreview.net/forum?id=Ao4vGWr7BX)
- **[NeurIPS, 2026]** BrainCoT: A Multi-Task Zero-Shot Brain Signal Foundation Model with Neurometric-Anchored Chain-of-Thought Reasoning <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://openreview.net/forum?id=4EYWJe33bO)
- **[NeurIPS, 2026]** Brain-OF: An Omnifunctional Foundation Model for fMRI, EEG and MEG <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> <img src="https://img.shields.io/badge/MEG-darkblue" alt="MEG" height="16"/> [[paper]](https://openreview.net/forum?id=54rAPNnSej)
- **[ICML, 2026]** OSF: On Pre-training and Scaling of Sleep Foundation Models <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> <img src="https://img.shields.io/badge/Resp-yellow" alt="Resp" height="16"/> [[paper]](https://openreview.net/forum?id=rlVGCyjqnt)[[code]](https://github.com/yang-ai-lab/OSF-Open-Sleep-FM)
- **[ICML, 2026]** SleepMaMi: A Universal Sleep Foundation Model for Integrating Macro- and Micro-structures <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> <img src="https://img.shields.io/badge/Resp-yellow" alt="Resp" height="16"/> [[paper]](https://openreview.net/forum?id=e9hvlHlUas)[[code]](https://github.com/KeondoPark/SleepMaMi)
- **[ICML, 2026]** A robust PPG foundation model using multimodal physiological supervision <img src="https://img.shields.io/badge/PPG-purple" alt="PPG" height="16"/> [[paper]](https://openreview.net/forum?id=JF4045xnhl)
- **[ICML, 2026]** SIGMA-PPG: Statistical-prior Informed Generative Masking Architecture for PPG Foundation Model <img src="https://img.shields.io/badge/PPG-purple" alt="PPG" height="16"/> [[paper]](https://openreview.net/forum?id=PKgGsbORt9)[[code]](https://github.com/ZonghengGuo/SigmaPPG)
- **[ICML, 2026]** Physiology-Aware Masked Cross-Modal Reconstruction for Biosignal Representation Learning* <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> <img src="https://img.shields.io/badge/PPG-purple" alt="PPG" height="16"/> [[code]](https://github.com/hzhou3/xMAE)
- **[ICML, 2026]** Bio-Inspired Self-Supervised Learning for Wrist-worn Accelerometer Data* <img src="https://img.shields.io/badge/IMU-orange" alt="IMU" height="16"/> [[paper]](https://arxiv.org/abs/2603.10961)[[code]](https://github.com/Prithvitarale/biopm)
- **[ICML, 2026]** MEG-XL: Data-Efficient Brain-to-Text via Long-Context Pre-Training <img src="https://img.shields.io/badge/MEG-darkblue" alt="MEG" height="16"/> [[paper]](https://openreview.net/forum?id=cefix4VmhS)[[code]](https://github.com/neural-processing-lab/MEG-XL)
- **[ICML, 2026]** NeuroCLUS: A Foundation Model with Functional Clustering for Intracranial Neural Decoding <img src="https://img.shields.io/badge/iEEG-steelblue" alt="iEEG" height="16"/> [[paper]](https://openreview.net/forum?id=pFweJM4Uw8)
- **[ICML, 2026]** PATCHCODE: Discrete Latent Predictive Learning for EEG Foundation Model <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://openreview.net/forum?id=NWcZ5vualM)[[code]](https://github.com/kierenyyu/Patchcode)
- **[ICML, 2026]** KAST-BAR: Knowledge-Anchored Semantically-Dynamic Topology Brain Autoregressive Modeling for Universal Neural Interpretation <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://openreview.net/forum?id=Ee4j4zMir5)[[code]](https://github.com/KAST-BAR/KAST-BAR)
- **[ICLR, 2026]** sleep2vec: Unified Cross-Modal Alignment for Heterogeneous Nocturnal Biosignals <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> <img src="https://img.shields.io/badge/EOG-pink" alt="EOG" height="16"/> <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://openreview.net/forum?id=DDXhRN66eV)
- **[ICLR, 2026]** HiMAE: Hierarchical Masked Autoencoders Discover Resolution-Specific Structure in Wearable Time Series <img src="https://img.shields.io/badge/PPG-purple" alt="PPG" height="16"/> [[paper]](https://arxiv.org/abs/2510.25785)
- **[ICLR, 2026]** CodeBrain: Bridging Decoupled Tokenizer and Multi-Scale Architecture for EEG Foundation Model <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://openreview.net/forum?id=msJgEkjwh5)[[code]](https://github.com/jingyingma01/CodeBrain)
- **[ICLR, 2026]** Uni-NTFM: A Unified Foundation Model for EEG Signal Representation Learning <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://openreview.net/forum?id=oUMiuYHW21)
- **[ICLR, 2026]** ECHO: Toward Contextual Seq2Seq Paradigms in Large EEG Models <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://openreview.net/forum?id=ClLQ6cLkoR)[[code]](https://github.com/wythedee/ECHO)
- **[IJCAI, 2026]** DNA-PPG: A Foundation Model for Photoplethysmography via Dual Neighborhood Alignment <img src="https://img.shields.io/badge/PPG-purple" alt="PPG" height="16"/> [[paper]](https://www.ijcai.org/proceedings/2026/777)
- **[IJCAI, 2026]** SPOTR: Spatio-temporal Pooling One-Token Reconstruction for Universal Physiological Signal Self-supervised Learning* <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> <img src="https://img.shields.io/badge/PPG-purple" alt="PPG" height="16"/> [[paper]](https://www.ijcai.org/proceedings/2026/612)
- **[KDD, 2026]** CAP: Towards PPG Universal Representation Learning with Patient-level Supervision <img src="https://img.shields.io/badge/PPG-purple" alt="PPG" height="16"/> [[paper]](https://arxiv.org/abs/2606.15284)[[code]](https://github.com/gody123gody/CAP)
- **[AAAI, 2026]** Tracing the Heart's Pathways: ECG Representation Learning from a Cardiac Conduction Perspective* <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://ojs.aaai.org/index.php/AAAI/article/view/37057)
- **[AAAI, 2026]** BraSTORM: A Dual-Branch Self-Supervised Framework for EEG Representation Learning via Input-Level Spatio-Temporal Decomposition* <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://ojs.aaai.org/index.php/AAAI/article/view/38838)
- **[EMNLP, 2026]** FOCAL: Fine-Grained Optimal-Transport-Driven Contrastive Alignment of Language and ECGs with Waveform Enhancement <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://aclanthology.org/2026.emnlp-main.1244/)
- **[MICCAI, 2026]** Echo2ECG: Enhancing ECG Representations with Cardiac Morphology from Multi-View Echos* <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://arxiv.org/abs/2603.08505)[[code]](https://github.com/michelleespranita/Echo2ECG)
- **[MICCAI, 2026]** LEGEND: A Language-Aligned EEG Foundation Model with Flow Matching Latent Denoising <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://papers.miccai.org/miccai-2026/0579-Paper3568.html)[[code]](https://github.com/5GYYYYY/LEGEND)
- **[MICCAI, 2026]** Subject- and Task-Aware EEG Foundation Model <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://papers.miccai.org/miccai-2026/1006-Paper2756.html)[[code]](https://github.com/SionAn/MICCAI2026STEM)
- **[MICCAI, 2026]** GTRE: A Physiological-Semantic Foundation Model for Generalizable EEG Analysis via Preference-Guided Alignment <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://papers.miccai.org/miccai-2026/0437-Paper6477.html)[[code]](https://github.com/AZFAR176/GTRE-)
- **[Arxiv, 2026]** Towards a General Intelligence and Interface for Wearable Health Data <img src="https://img.shields.io/badge/PPG-purple" alt="PPG" height="16"/> <img src="https://img.shields.io/badge/IMU-orange" alt="IMU" height="16"/> <img src="https://img.shields.io/badge/Health--metrics-lightblue" alt="Health-metrics" height="16"/> [[paper]](https://arxiv.org/abs/2605.22759)
- **[Arxiv, 2026]** BCG-FM: A Foundation Model for Ambient Cardiac Health Sensing <img src="https://img.shields.io/badge/BCG-crimson" alt="BCG" height="16"/> [[paper]](https://arxiv.org/abs/2606.07692)
- **[Arxiv, 2025]** CLEF: Clinically-Guided Contrastive Learning for Electrocardiogram Foundation Models <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://www.arxiv.org/abs/2512.02180) [[code]](https://github.com/Nokia-Bell-Labs/ecg-foundation-model)
- **[NEJM AI, 2025]** An Electrocardiogram Foundation Model Built on over 10 Million Recordings with External Evaluation across Multiple Domains <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://www.ovid.com/journals/neai/abstract/10.1056/aioa2401033~an-electrocardiogram-foundation-model-built-on-over-10?redirectionsource=fulltextview) [[code]](https://github.com/PKUDigitalHealth/ECGFounder)
- **[JAMIA Open, 2025]** ECG-FM: An Open Electrocardiogram Foundation Model <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://academic.oup.com/jamiaopen/article/8/5/ooaf122/8287827) [[code]](https://github.com/bowang-lab/ECG-FM/)
- **[Arxiv, 2025]** ProtoECGNet: Case-Based Interpretable Deep Learning for Multi-Label ECG Classification with Contrastive Learning <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://arxiv.org/abs/2504.08713) [[code]](https://github.com/bbj-lab/protoecgnet)
- **[Arxiv, 2025]** OpenECG: Benchmarking ECG Foundation Models with Public 1.2 Million Records <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://arxiv.org/abs/2503.00711)
- **[NeurIPS, 2025]** SensorLM: Learning the Language of Wearable Sensors <img src="https://img.shields.io/badge/Health--metrics-lightblue" alt="Health-metrics" height="16"/> [[paper]](https://arxiv.org/abs/2506.09108)
- **[NeurIPS, 2025]** PhysioWave: A Multi-Scale Wavelet-Transformer for Physiological Signal Representation <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> <img src="https://img.shields.io/badge/EMG-green" alt="EMG" height="16"/> [[paper]](https://arxiv.org/abs/2506.10351) [[code]](https://github.com/ForeverBlue816/PhysioWave) 
- **[NeurIPS, 2025]** BrainOmni: A Brain Foundation Model for Unified EEG and MEG Signals <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> <img src="https://img.shields.io/badge/MEG-darkblue" alt="MEG" height="16"/> [[paper]](https://arxiv.org/abs/2505.18185) [[code]](https://github.com/OpenTSLab/BrainOmni) 
- **[NeurIPS, 2025]** NeurIPT: Foundation Model for Neural Interfaces <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://arxiv.org/abs/2510.16548) [[code]](https://github.com/ZzzitaoFang/NeurIPT) 
- **[NeurIPS, 2025]** LUNA: Efficient and Topology-Agnostic Foundation Model for EEG Signal Analysis <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://arxiv.org/abs/2510.22257) [[code]](https://github.com/pulp-bio/biofoundation) 
- **[ICML, 2025]** EEG-Language Pretraining for Highly Label-Efficient Clinical Phenotyping <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://openreview.net/pdf?id=yaI2ZYFmeD) [[code]](https://github.com/SamGijsen/ELM) 
- **[ICML, 2025]** From Token to Rhythm: A Multi-Scale Approach for ECG-Language Pretraining <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://openreview.net/forum?id=fUjkoGUre0) [[code]](https://github.com/HKU-MedAI/MELP)
- **[ICML, 2025]** Boosting Masked ECG-Text Auto-Encoders as Discriminative Learners <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://openreview.net/pdf?id=mM65b81LdM) [[code]]( https://github.com/manhph2211/D-BETA)
- **[ICML, 2025]** Beyond Sensor Data: Foundation Models of Behavioral Data from Wearables Improve Health Predictions <img src="https://img.shields.io/badge/Health--metrics-lightblue" alt="Health-metrics"  height="16"/> [[paper]](https://openreview.net/forum?id=DtVVltU1ak) 
- **[Nature, 2025]** A generic noninvasive neuromotor interface for human-computer interaction <img src="https://img.shields.io/badge/EMG-green" alt="EMG" height="16"/> [[paper]](https://www.nature.com/articles/s41586-025-09255-w) [[code]](https://github.com/facebookresearch/generic-neuromotor-interface)
- **[UbiComp, 2025]** Pulse-PPG: An Open-Source Field-Trained PPG Foundation Model for Wearable Applications Across Lab and Field Settings <img src="https://img.shields.io/badge/PPG-purple" alt="PPG" height="16"/> [[paper]](https://arxiv.org/abs/2502.01108) [[code]](https://github.com/maxxu05/pulseppg)
- **[ICLR, 2025]** CBraMod: A Criss-Cross Brain Foundation Model for EEG Decoding <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://arxiv.org/abs/2412.07236) [[code]](https://github.com/wjq-learning/CBraMod)
- **[ICLR, 2025]** Reading Your Heart: Learning ECG Words and Sentences via Pre-training ECG Language Model* <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://arxiv.org/abs/2502.10707) [[code]](https://github.com/PKUDigitalHealth/HeartLang)
- **[ICLR, 2025]** NeuroLM: A Universal Multi-task Foundation Model for Bridging the Gap between Language and EEG Signals <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://openreview.net/pdf?id=Io9yFt7XH7) [[code]](https://github.com/935963004/NeuroLM)
- **[ICLR, 2025]** PaPaGei: Open Foundation Models for Optical Physiological Signals <img src="https://img.shields.io/badge/PPG-purple" alt="PPG" height="16"/> [[paper]](https://arxiv.org/abs/2410.20542) [[code]](https://github.com/nokia-bell-labs/papagei-foundation-model)
- **[ICLR, 2025]** RelCon: Relative Contrastive Learning for a Motion Foundation Model for Wearable Data <img src="https://img.shields.io/badge/IMU-orange" alt="IMU" height="16"/> [[paper]](https://openreview.net/pdf?id=k2uUeLCrQq) [[code]](https://github.com/maxxu05/relcon)
- **[SPI Health Data Science, 2025]** ECG-LM: Understanding Electrocardiogram with a Large Language Model <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://spj.science.org/doi/10.34133/hds.0221)
- **[NPJ Digital Medicine, 2024]** Self-supervised learning for human activity recognition using 700,000 person-days of wearable data <img src="https://img.shields.io/badge/IMU-orange" alt="IMU" height="16"/> [[paper]](https://www.nature.com/articles/s41746-024-01062-3) [[code]](https://github.com/OxWearables/ssl-wearables)
- **[NPJ Cardiovascular Health, 2024]** Foundation models for cardiovascular disease detection via biosignals from digital stethoscopes <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> <img src="https://img.shields.io/badge/PCG-lightblue" alt="PCG" height="16"/> [[paper]](https://www.nature.com/articles/s44325-024-00027-5.pdf)
- **[Cell Reports Medicine, 2024]** Foundation model of ECG diagnosis: Diagnostics and explanations of any form and rhythm on ECG <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://www.cell.com/cell-reports-medicine/pdfExtended/S2666-3791(24)00646-3)
- **[NeurIPS, 2024]** Towards Open Respiratory Acoustic Foundation Models: Pretraining and Benchmarking <img src="https://img.shields.io/badge/Respiratory-lightblue" alt="Respiratory" height="16"/> [[paper]](https://arxiv.org/pdf/2406.16148) [[code]](https://github.com/evelyn0414/OPERA)
- **[ICLR, 2024]** Large-scale Training of Foundation Models for Wearable Biosignals <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> <img src="https://img.shields.io/badge/PPG-purple" alt="PPG" height="16"/> [[paper]](https://arxiv.org/abs/2312.05409)
- **[ICLR, 2024]** Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://arxiv.org/abs/2405.18765) [[code]](https://github.com/935963004/LaBraM)
- **[AAAI Spring Symposium, 2024]** EEGFormer: Towards Transferable and Interpretable Large-Scale EEG Foundation Model <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://arxiv.org/abs/2401.10278)
- **[IEEE ISBI, 2024]** Neuro-GPT: Towards A Foundation Model for EEG <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://arxiv.org/pdf/2311.03764) [[code]](https://github.com/wenhui0206/NeuroGPT)
- **[Applied Intelligence, 2024]** SelfPAB: large-scale pre-training on accelerometer data for human activity recognition* <img src="https://img.shields.io/badge/IMU-orange" alt="IMU" height="16"/> [[paper]](https://link.springer.com/article/10.1007/s10489-024-05322-3) [[code]](https://github.com/ntnu-ai-lab/SelfPAB)
- **[Physiological Measurement, 2024]** Siamquality: a convnet-based foundation model for photoplethysmography signals <img src="https://img.shields.io/badge/PPG-purple" alt="PPG" height="16"/> [[paper]](https://iopscience.iop.org/article/10.1088/1361-6579/ad6747/meta) [[code]](https://github.com/chengding0713/SiamQuality)
- **[Arxiv, 2024]** AnyECG: Foundational Models for Multitask Cardiac Analysis in Real-World Settings <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://arxiv.org/abs/2411.17711)
- **[Arxiv, 2024]** Self-Supervised Pre-Training with Joint-Embedding Predictive Architecture Boosts ECG Classification Performance <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://arxiv.org/abs/2410.13867) [[code]](https://github.com/kweimann/ECG-JEPA)
- **[Arxiv, 2024]** BrainWave: A Brain Signal Foundation Model for Clinical Applications <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://arxiv.org/abs/2402.10251) [[code]](https://github.com/yzz673/Brant-2)
- **[Arxiv, 2024]** Foundation Models for ECG: Leveraging Hybrid Self-Supervised Learning for Advanced Cardiac Diagnostics <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://arxiv.org/pdf/2407.07110)
- **[Arxiv, 2024]** Scaling Wearable Foundation Models <img src="https://img.shields.io/badge/Health--metrics-lightblue" alt="Health-metrics" height="16"/> [[paper]](https://arxiv.org/pdf/2410.13638)
- **[Arxiv, 2024]** Wearable Accelerometer Foundation Models for Health via Knowledge Distillation <img src="https://img.shields.io/badge/PPG-purple" alt="PPG" height="16"/> <img src="https://img.shields.io/badge/IMU-orange" alt="IMU" height="16"/> [[paper]](https://arxiv.org/abs/2412.11276)
- **[Arxiv, 2024]** Toward Foundation Model for Multivariate Wearable Sensing of Physiological Signals <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> <img src="https://img.shields.io/badge/PPG-purple" alt="PPG" height="16"/> <img src="https://img.shields.io/badge/IMU-orange" alt="IMU" height="16"/> <img src="https://img.shields.io/badge/EMG-green" alt="EMG" height="16"/> [[paper]](https://arxiv.org/abs/2412.09758) [[code]](https://github.com/Mobile-Sensing-and-UbiComp-Laboratory/NormWear)
- **[NPJ Digital Medicine, 2023]** A foundational vision transformer improves diagnostic performance for electrocardiograms <img src="https://img.shields.io/badge/ECG-red" alt="ECG" height="16"/> [[paper]](https://www.nature.com/articles/s41746-023-00840-9) [[code]](https://github.com/akhilvaid/HeartBEiT)
- **[NeurIPS, 2023]** Brant: Foundation Model for Intracranial Neural Signal <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://proceedings.neurips.cc/paper_files/paper/2023/file/535915d26859036410b0533804cee788-Paper-Conference.pdf) [[code]](https://zju-brainnet.github.io/Brant.github.io/)
- **[NeurIPS, 2023]** Learning Topology-Agnostic EEG Representations with Geometry-Aware Modeling* <img src="https://img.shields.io/badge/EEG-blue" alt="EEG" height="16"/> [[paper]](https://openreview.net/pdf?id=hiOUySN0ub) [[code]](https://seqml.github.io/MMM/)

*\*Self-supervised approaches not explicitly claimed as foundation models*

## 🔄 Adapting Time Series Foundation Models to Biosignals

*Repurposing general time series foundation models for biomedical-domain-specific tasks*

<img src="img/Tasks%20perspective.png" alt="Tasks Perspective" width="500"/>

<details>
<summary><strong>📊 Mainstream Time Series Foundation Models</strong> (Click to expand)</summary>

| Model | Venue | Year | Dataset Scale | Model Size | Tasks | Paper | Code |
|-------|-------|------|---------------|------------|-------|-------|------|
| **Kairos** | NeurIPS | 2026 | 300B | 10 / 23 / 50M | `F` | [[paper]](https://arxiv.org/abs/2509.25826) | [[code]](https://github.com/foundation-model-research/Kairos) |
| **TiRex-2** | NeurIPS | 2026 | - | 38M | `F` | [[paper]](https://arxiv.org/abs/2607.01204) | [[code]](https://github.com/NX-AI/tirex-2) |
| **TempoPFN** | NeurIPS | 2026 | - | 38M | `F` | [[paper]](https://arxiv.org/abs/2510.25502) | [[code]](https://github.com/automl/TempoPFN) |
| **HORAI** | NeurIPS | 2026 | 1B | - | `F` `D` | [[paper]](https://arxiv.org/abs/2602.05646) | - |
| **FLAME** | NeurIPS | 2026 | - | 2 / 6 / 10M | `F` | [[paper]](https://arxiv.org/abs/2512.14253) | [[code]](https://github.com/decisionintelligence/FLAME) |
| **Mantis** | ICML | 2026 | 2M | 8M | `C` | [[paper]](https://arxiv.org/abs/2502.15637) | [[code]](https://github.com/vfeofanov/mantis) |
| **Olivia** | ICML | 2026 | - | - | `F` | [[paper]](https://arxiv.org/abs/2605.17340) | [[code]](https://github.com/TSTS13/Olivia) |
| **Aurora** | ICLR | 2026 | 1B | - | `F` | [[paper]](https://arxiv.org/abs/2509.22295) | [[code]](https://github.com/decisionintelligence/Aurora) |
| **Time-MoE** | ICLR | 2025 | 309B | 2.4B | `F` | [[paper]](https://arxiv.org/abs/2401.04182) | [[code]](https://github.com/Time-MoE/Time-MoE) |
| **Timer-XL** | ICLR | 2025 | - | - | `F` | [[paper]](https://arxiv.org/abs/2410.04803) | [[code]](https://github.com/thuml/Large-Time-Series-Model) |
| **ChatTime** | AAAI | 2025 | 1M | 350M | `F` | [[paper]](https://arxiv.org/abs/2412.11376) | [[code]](https://github.com/ForestsKing/ChatTime) |
| **TimePFN** | AAAI | 2025 | 1.5M | - | `F` | [[paper]](https://arxiv.org/abs/2502.16294) | [[code]](https://github.com/egetaga/TimePFN) |
| **TTM** | NeurIPS | 2024 | 1B | 5M | `F` | [[paper]](https://arxiv.org/abs/2401.03955) | [[code]](https://github.com/ibm-granite/granite-tsfm/tree/main/tsfm_public/models/tinytimemixer) |
| **Time-FFM** | NeurIPS | 2024 | - | - | `F` | [[paper]](https://arxiv.org/abs/2405.14252) | [[code]](https://github.com/yuppielqx/Time-FFM) |
| **UniTS** | NeurIPS | 2024 | - | 8M | `F` `D` `I` | [[paper]](https://arxiv.org/abs/2403.00131) | [[code]](https://github.com/mims-harvard/UniTS) |
| **Moirai-MOE** | NeurIPS Workshop | 2024 | - | 11M-86M | `F` | [[paper]](https://arxiv.org/abs/2410.10469) | [[code]](https://github.com/SalesforceAIResearch/uni2ts) |
| **Moirai** | ICML | 2024 | 27B | 14 / 91 / 311M | `F` | [[paper]](https://arxiv.org/abs/2402.02592) | [[code]](https://github.com/salesforceairesearch/uni2ts) |
| **MOMENT** | ICML | 2024 | 1B | 385M | `F` `C` `D` `I` | [[paper]](https://arxiv.org/abs/2402.03885) | [[code]](https://github.com/moment-timeseries-foundation-model/moment) |
| **TimesFM** | ICML | 2024 | 100B | 200M | `F` | [[paper]](https://arxiv.org/abs/2310.10688) | [[code]](https://github.com/google-research/timesfm) |
| **Timer** | ICML | 2024 | 28B | 67M | `F` `D` `I` | [[paper]](https://arxiv.org/abs/2402.02368) | [[code]](https://github.com/thuml/Large-Time-Series-Model) |
| **DAM** | ICLR | 2024 | - | - | `F` `I` | [[paper]](https://arxiv.org/abs/2407.17880) | - |
| **Chronos** | TMLR | 2024 | 84B | 20 / 46 / 200 / 710M | `F` | [[paper]](https://arxiv.org/abs/2403.07815) | [[code]](https://github.com/amazon-science/chronos-forecasting) |
| **GTT** | ACM CIKM | 2024 | 2B | 7 / 19 / 57M | `F` | [[paper]](https://dl.acm.org/doi/10.1145/3627673.3679931) | [[code]](https://github.com/cfeng783/GTT) |
| **Mamba4Cast** | - | 2024 | - | 27M | `F` | [[paper]](https://arxiv.org/abs/2410.09385) | [[code]](https://github.com/automl/Mamba4Cast) |
| **TimeRAF** | - | 2024 | 320M | - | `F` | [[paper]](https://arxiv.org/abs/2412.20810) | - |
| **TSMamba** | - | 2024 | - | - | `F` | [[paper]](https://arxiv.org/abs/2411.02941) | - |
| **TimeDiT** | - | 2024 | 5B | 33 / 120 / 460 / 680M | `F` `D` | [[paper]](https://arxiv.org/abs/2409.02322) | -|
| **ViTime** | - | 2024 | - | 74 / 95M | `F` | [[paper]](https://arxiv.org/abs/2407.07311) | [[code]](https://github.com/IkeYang/ViTime) |
| **Lag-Llama** | - | 2023 | 360M | 200M | `F` | [[paper]](https://arxiv.org/abs/2310.08278) | [[code]](https://github.com/time-series-foundation-models/lag-llama) |
| **TimeGPT-1** | - | 2023 | 100B | - | `F` `D` | [[paper]](https://arxiv.org/abs/2310.03589) | [[code]](https://github.com/Nixtla/nixtla) |

***Task Legend:** `F` = Forecasting, `C` = Classification, `D` = Anomaly Detection, `I` = Data Imputation*

</details>

**TSFM adaptation**
---
- **[ICML, 2026]** EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation and Diagnostic Analyses of EEG Foundation Models [[paper]](https://arxiv.org/abs/2508.17742) [[code]](https://github.com/xw1216/EEG-FM-Bench) - *Benchmarked general TSFMs **Mantis and MOMENT** against EEG foundation models under frozen, full fine-tuning and LoRA adaptation*
- **[ICML, 2026]** Position: Time-Series Foundation Models Require Explicit Domain-Level Benchmarks [[paper]](https://proceedings.mlr.press/v306/syed26a.html) - *Evaluated 7 TSFMs across 6 domains including healthcare, showing pooled leaderboards hide domain-level failures*
- **[ML4H, 2025]** STAMP: Spatial-Temporal Adapter with Multi-Head Pooling [[paper]](https://proceedings.mlr.press/v297/shook26a.html) [[code]](https://github.com/autonlab/STAMP) - *Lightweight spatial-temporal adapter on frozen **MOMENT, Chronos and TSPulse** embeddings for clinical EEG*
- **[ICML, 2025]** Efficient Personalized Adaptation for Physiological Signal Foundation Model [[paper]](https://openreview.net/pdf?id=55ysNwbOTI) - *Applied diffusion to generate LoRA weights for adaptation of FMs*
- **[ICLR, 2025]** PaPaGei: Open Foundation Models for Optical Physiological Signals [[paper]](https://arxiv.org/abs/2410.20542) [[code]](https://github.com/nokia-bell-labs/papagei-foundation-model) - *Benchmarked against **Chronos and MOMENT** for PPG analysis, demonstrated transferable features from general time series FMs*
- **[ML4H, 2024]** Are time series foundation models ready for vital sign forecasting in healthcare? [[paper]](https://proceedings.mlr.press/v259/gu25a.html) - *Adapted **Lag-LLaMA, TimesFM, MOMENT, Moirai, Chronos** for vital sign forecasting using feature extraction approach*
- **[ICMI, 2024]** Low-rank adaptation of time series foundational models for out-of-domain modality forecasting [[paper]](https://arxiv.org/abs/2405.10216) - *LoRA techniques applied to **Moirai and Chronos** for cross-domain biosignal adaptation*
- **[Arxiv, 2024]** Beyond LoRA: Exploring Efficient Fine-Tuning Techniques for Time Series Foundational Models [[paper]](https://arxiv.org/abs/2409.11302) - *Applied LoRA, QLoRA, and other PEFT techniques to **Lag-LLaMA** for biomedical time series adaptation*
- **[Arxiv, 2024]** Generalized Prompt Tuning: Adapting frozen univariate time series foundation models for multivariate healthcare time series [[paper]](https://arxiv.org/abs/2411.12824) [[code]](https://github.com/Ilovecodingforever/Gen-P-Tuning) - *Gen-P-Tuning module for adapting **univariate time series FMs** (MOMENT) to multivariate clinical data*
- **[Arxiv, 2024]** Repurposing Foundation Model for Generalizable Medical Time Series Classification [[paper]](https://arxiv.org/abs/2410.03794) - *FORMED method repurposing **TimesFM** to classification tasks with post-processing modules*

**Other related works**
---
- **[CHIL, 2026]** A Multi-dimensional Framework for Evaluating Generalization in EEG Foundation Models [[paper]](https://proceedings.mlr.press/v333/kommineni26a.html)
- **[MLHC, 2026]** Test-Time Adaptation for EEG Foundation Models: A Systematic Study under Real-World Distribution Shifts [[paper]](https://arxiv.org/abs/2604.16926)
- **[ICML, 2025]** H-Tuning: Toward Low-Cost and Efficient ECG-based Cardiovascular Disease Detection with Pre-Trained Models [[paper]](https://openreview.net/pdf?id=RLu1QIPiVr) [[code]](https://github.com/KAZABANA/H-Tuning)
- **[ICML, 2025]** Pre-Training Graph Contrastive Masked Autoencoders are Strong Distillers for EEG [[paper]](https://openreview.net/pdf?id=YKfJFTiRz8) [[code]](https://github.com/weixinxu666/EEG_DisGCMAE)

## 🤖 Leveraging Large Language Models for Biosignal Analysis

*Using (multi-modal) LLMs for biosignal analysis and interpretation*

<img src="img/LLM%20for%20biosignals.png" alt="LLM for Biosignals" width="500"/>

<!-- Define macros -->
[backbone]: https://img.shields.io/badge/🔧-Backbone-orange
[knowledge]: https://img.shields.io/badge/💡-Knowledge-blue
[fusion]: https://img.shields.io/badge/🔗-Fusion-purple
[agent]: https://img.shields.io/badge/🤖-Agent-lightgreen

Four functional roles of LLMs: ![tool][backbone] ![tool][knowledge] ![tool][fusion] ![tool][agent]
- **[Nature Communications, 2026]** Transforming wearable data into personal health insights using large language model agents <img src="https://img.shields.io/badge/🤖-Agent-lightgreen" height="16" style="vertical-align: text-bottom;"> [[paper]](https://www.nature.com/articles/s41467-025-67922-y)[[code]](https://github.com/yahskapar/personal-health-insights-agent) - *An LLM agent for analyzing wearable daily statistics tables and tables of discrete activity events*
- **[ICML, 2026]** ECG-R1: Protocol-Guided and Modality-Agnostic MLLM for Reliable ECG Interpretation <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://arxiv.org/abs/2602.04279)[[code]](https://github.com/PKUDigitalHealth/ECG-R1) - *Reasoning ECG MLLM taking ECG signals and/or images, trained with protocol-guided data and RL rewards*
- **[ICML, 2026]** OpenTSLM: Time-Series Language Models for Reasoning over Multivariate Medical Text- and Time-Series Data <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://proceedings.mlr.press/v306/langer26a.html)[[code]](https://github.com/OpenTSLM/OpenTSLM) - *Time series as a native LLM modality with chain-of-thought reasoning for sleep staging, HAR and ECG-QA*
- **[ICML, 2026]** SleepLM: Natural-Language Intelligence for Human Sleep <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://proceedings.mlr.press/v306/xu26at.html)[[code]](https://github.com/yang-ai-lab/SleepLM) - *Sleep-language foundation model trained on >100K hours of PSG paired with text*
- **[ICML, 2026]** HEARTS: Benchmarking LLM Reasoning on Health Time Series <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🤖-Agent-lightgreen" height="16" style="vertical-align: text-bottom;"> [[paper]](https://arxiv.org/abs/2603.06638) - *Benchmark of 110 tasks across 20 signal modalities, showing LLMs lag specialized models*
- **[ICLR, 2026]** CerebraGloss: Instruction-Tuning a Large Vision-Language Model for Fine-Grained Clinical EEG Interpretation <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://openreview.net/forum?id=Xi1jkajWi9)[[code]](https://github.com/iewug/CerebraGloss) - *Vision-language model instruction-tuned on EEG plots for clinical EEG interpretation*
- **[NeurIPS, 2026]** Neural Signals Generate Clinical Notes in the Wild <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://arxiv.org/abs/2601.22197)[[code]](https://github.com/Jathurshan0330/CELM) - *Couples EEG foundation models with LLMs to generate clinical EEG reports from long recordings*
- **[AAAI, 2026]** EEG Agent: A Unified Framework for Automated EEG Analysis Using Large Language Models <img src="https://img.shields.io/badge/🤖-Agent-lightgreen" height="16" style="vertical-align: text-bottom;"> [[paper]](https://doi.org/10.1609/aaai.v40i21.38867)[[code]](https://github.com/rebootingLine/EEGAgent) - *LLM agent that plans and schedules EEG tools for preprocessing, feature extraction and event detection*
- **[AAAI, 2026]** anyECG-chat: A Generalist ECG-MLLM for Flexible ECG Input and Multi-Task Understanding <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://doi.org/10.1609/aaai.v40i1.37024) - *ECG MLLM handling variable-length, reduced-lead and multiple ECGs for report generation and QA*
- **[ACL, 2026]** Is EEG-to-Text Feasible in Real-World Scenarios? An In-Depth Analysis Using a Neuropsychology-Inspired Benchmark <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://aclanthology.org/2026.acl-long.61/)[[code]](https://github.com/baoyudu/COFETT) - *Benchmark evaluating EEG-to-text decoding without teacher forcing*
- **[MICCAI, 2026]** EmERGE: A Multimodal LLM-Based Evidence-Mediated ECG Report Generation and Evaluation Approach <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://papers.miccai.org/miccai-2026/0342-Paper4833.html)[[code]](https://github.com/hustselab511/EmERGE) - *ECG report generation conditioned on extracted ECG evidence*
- **[MICCAI, 2026]** LEGEND: A Language-Aligned EEG Foundation Model with Flow Matching Latent Denoising <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://papers.miccai.org/miccai-2026/0579-Paper3568.html)[[code]](https://github.com/5GYYYYY/LEGEND) - *EEG-language alignment framing EEG decoding as instruction-based answer generation*
- **[MICCAI, 2026]** MSS-Net: Learning Hierarchical Multi-scale and Multimodal Representations for Complex Cardiac Disease Classification <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> [[paper]](https://papers.miccai.org/miccai-2026/0678-Paper4140.html)[[code]](https://github.com/origami-one/MSS-Net) - *Clinical text descriptions fused with ECG features as auxiliary supervision*
- **[IEEE JBHI, 2026]** EEG-VLM: A Hierarchical Vision-Language Model with Multi-Level Feature Alignment and Visually Enhanced Language-Guided Reasoning for EEG Image-Based Sleep Stage Prediction <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://doi.org/10.1109/jbhi.2026.3685511) - *LLaVA-style VLM with chain-of-thought reasoning for interpretable sleep staging*
- **[NPJ Digital Medicine, 2026]** Teaching multimodal LLMs to comprehend 12-lead electrocardiographic images <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://www.nature.com/articles/s41746-026-02551-3) [[code]](https://aimedlab.github.io/PULSE/) - *Multimodal ECG analysis using image plots with vision-language model integration*
- **[MLHC, 2026]** ELF: A Family of Encoder-Free ECG-Language Models <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> [[paper]](https://proceedings.mlr.press/v340/han26a.html)[[code]](https://github.com/ELM-Research/ECG-Language-Models) - *Encoder-free ECG-language models competitive with encoder-based ones*
- **[ACM IMWUT, 2026]** DeepFeature: LLM-Empowered Context-aware Feature Generation for Wearable Biosignals <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🤖-Agent-lightgreen" height="16" style="vertical-align: text-bottom;"> [[paper]](https://arxiv.org/abs/2512.08379) - *LLM generates, refines and verifies feature extraction code for wearable biosignals*
- **[Nature Medicine, 2025]** A personal health large language model for sleep and fitness coaching <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🤖-Agent-lightgreen" height="16" style="vertical-align: text-bottom;"> [[paper]](https://www.nature.com/articles/s41591-025-03888-0) - *Personal health LLM agent using activity measures as text input for personalized health insights*
- **[NeurIPS, 2025]** GEM: Empowering MLLM for Grounded ECG Understanding with Time Series and Images <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> [[paper]](https://arxiv.org/pdf/2503.06073) [[code]](https://github.com/lanxiang1017/GEM) - *Convert ECG to images and feature vectors for multi-modal LLM understanding*
- **[ICML, 2025]** EEG-Language Pretraining for Highly Label-Efficient Clinical Phenotyping <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> [[paper]](https://openreview.net/pdf?id=yaI2ZYFmeD) [[code]](https://github.com/SamGijsen/ELM)- *EEG-Modal-LLM alignment for knowledge integration*
- **[ICML, 2025]** Boosting Masked ECG-Text Auto-Encoders as Discriminative Learners <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> [[paper]](https://openreview.net/pdf?id=mM65b81LdM) [[code]]( https://github.com/manhph2211/D-BETA) - *ECG-text-report integration via contrastive masked autoencoding*
- **[IEEE TBD, 2025]** Large Language Model-informed ECG Dual Attention Network for Heart Failure Risk Prediction <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> [[paper]](https://arxiv.org/abs/2403.10581) - *Heart failure risk prediction using LLM-informed dual attention network with ECG time sequences*
- **[SPI Health Data Science, 2025]** ECG-LM: Understanding Electrocardiogram with a Large Language Model <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🤖-Agent-lightgreen" height="16" style="vertical-align: text-bottom;"> [[paper]](https://spj.science.org/doi/10.34133/hds.0221) - *Comprehensive ECG understanding using LLMs with signal analysis, text integration, and conversational capabilities*
- **[Arxiv, 2025]** EEG Emotion Copilot: Optimizing Lightweight LLMs for Emotional EEG Interpretation with Assisted Medical Record Generation <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://arxiv.org/pdf/2410.00166) [[code]](https://github.com/NZWANG/EEG_Emotion_Copilot) - *EEG emotion recognition with LLM backbone and multimodal fusion for personalized emotion analysis*
- **[Findings of ACL, 2025]** MEIT: Multi-Modal Electrocardiogram Instruction Tuning on Large Language Models for Report Generation <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> [[paper]](https://aclanthology.org/2025.findings-acl.749/) [[code]](https://github.com/AIoT-MLSys-Lab/MEIT) - *ECG report generation using multimodal instruction tuning with time sequences*
- **[Arxiv, 2025]** LLaSA: A Multimodal LLM for Human Activity Analysis Through Wearable and Smartphone Sensors <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://arxiv.org/pdf/2406.14498) [[code]](https://github.com/BASHLab/LLaSA) - *Multimodal LLM for human activity analysis using IMU data and natural language*
- **[Cell Reports Medicine, 2024]** FoundationmodelofECGdiagnosis:Diagnosticsand explanations of any form and rhythm on ECG <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://www.cell.com/cell-reports-medicine/pdfExtended/S2666-3791(24)00646-3) [[code]](https://github.com/control-spiderman/ECGFM-KED) - *Foundation ECG diagnosis model with comprehensive LLM integration across all functional roles*
- **[ICML, 2024]** Zero-Shot ECG Classification with Multimodal Learning and Test-time Clinical Knowledge ncement <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> [[paper]](https://arxiv.org/abs/2403.06659) [[code]](https://github.com/cheliu-computation/MERL-ICML2024) - *ECG diagnosis using LLMs with retrieval-augmented generation and knowledge integration*
- **[ICLR, 2024]** BELT-2: Bootstrapping EEG-to-Language Representation Alignment for Multi-task Brain Decoding <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://arxiv.org/pdf/2409.00121) [[code]](https://anonymous.4open.science/r/BELT-2-0048) - *EEG-to-language alignment using transformer backbone with multimodal integration*
- **[TMLR, 2024]** ECG Semantic Integrator (ESI): A Foundation ECG Model Pretrained with LLM-nced Cardiological Text <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> [[paper]](https://arxiv.org/abs/2405.19366) [[code]](https://github.com/comp-well-org/ESI) - *Foundation ECG model pretrained with LLM-nced cardiological text for semantic integration*
- **[CHIL, 2024]** Health-LLM: Large Language Models for Health Prediction via Wearable Sensor Data <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> [[paper]](https://arxiv.org/abs/2401.06866) [[code]](https://github.com/mitmedialab/Health-LLM) - *Health prediction using LLMs with activity measures as text input*
- **[ACM IMWUT, 2024]** Sensor2Text: Enabling Natural Language Interactions for Daily Activity Tracking Using Wearable Sensors <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://dl.acm.org/doi/abs/10.1145/3699747) - *Natural language interactions for activity tracking using wearable sensor data with multimodal fusion*
- **[IEEE CSCAIoT, 2024]** Are You Being Tracked? Discover the Power of Zero-Shot Trajectory Tracing with LLMs! <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://arxiv.org/abs/2403.06201) - *Multi-object tracking using LLMs with IMU text sequences and knowledge integration*
- **[IEEE FMSys, 2024]** HARGPT: Are LLMs Zero-Shot Human Activity Recognizers? <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> [[paper]](https://arxiv.org/pdf/2403.02727 ) [[code]](https://github.com/aiot-lab/HARGPT) - *Zero-shot human activity recognition using LLMs with IMU time sequence data*
- **[IEEE TNSRE, 2024]** Integrating Large Language Model, EEG, and Eye-Tracking for Word-Level Neural State Classification in Reading Comprehension <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> [[paper]](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10636286) - *Word-level neural state classification using EEG time sequences with LLM knowledge integration*
- **[IEEE BHI, 2024]** PhysioLLM: Supporting Personalized Health Insights with Wearables and Large Language Models <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🤖-Agent-lightgreen" height="16" style="vertical-align: text-bottom;"> [[paper]](https://arxiv.org/pdf/2406.19283) - *Personalized health insights using LLMs with activity measures and knowledge integration*
- **[Arxiv, 2024]** Conversational Health Agents: A Personalized LLM-Powered Agent Framework <img src="https://img.shields.io/badge/🤖-Agent-lightgreen" height="16" style="vertical-align: text-bottom;"> [[paper]](https://arxiv.org/abs/2310.02374) [[code]](https://github.com/Institute4FutureHealth/CHA) - *Conversational health agent using activity measures as text for personalized health interactions*
- **[Arxiv, 2024]** ECG-Chat: A Large ECG-Language Model for Cardiac Disease Diagnosis <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://arxiv.org/abs/2408.08849) [[code]](https://github.com/YubaoZhao/ECG-Chat) - *Large ECG-language model combining signal analysis and time sequences for conversational diagnosis*
- **[ACL, 2024]** Enhancing EEG-to-Text Decoding through Transferable Representations from Pre-trained Contrastive EEG-Text Masked Autoencoder <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://aclanthology.org/2024.acl-long.393) [[code]](https://github.com/JackieWang9811/CET-MAE) - *EEG-to-text generation using feature sequences with LLM knowledge*
- **[EMNLP, 2023]** Can Brain Signals Reveal Inner Alignment with Human Languages? <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://aclanthology.org/2023.findings-emnlp.120.pdf) [[code]](https://github.com/Jielin-Qiu/EEG_Language_Alignment) - *EEG analysis using LoRA-enhanced LLMs with multimodal fusion capabilities*
- **[ACM ISWC, 2023]** IMUGPT 2.0: Language-Based Cross Modality Transfer for Sensor-Based Human Activity Recognition <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> [[paper]](https://dl.acm.org/doi/10.1145/3678545) [[code]](https://github.com/ZikangLeng/IMUGPT) - *IMU signal analysis using generative transformer architecture for activity recognition*
- **[MIDL, 2023]** Frozen Language Model Helps ECG Zero-Shot Learning <img src="https://img.shields.io/badge/💡-Knowledge-blue" height="16" style="vertical-align: text-bottom;"> [[paper]](https://proceedings.mlr.press/v227/li24a.html) - *ECG zero-shot learning using frozen language models for knowledge enhancement*
- **[AAAI, 2022]** Open Vocabulary Electroencephalography-To-Text Decoding and Zero-shot Sentiment Classification <img src="https://img.shields.io/badge/🔧-Backbone-orange" height="16" style="vertical-align: text-bottom;"> <img src="https://img.shields.io/badge/🔗-Fusion-purple" height="16" style="vertical-align: text-bottom;"> [[paper]](https://arxiv.org/abs/2112.02690) [[code]](https://github.com/MikeWangWZHL/EEG-To-Text) - *EEG-to-text decoding using BART backbone with sentiment classification capabilities*

## ‼️ Open Challenges
Based on our survey, key challenges include:
- **Standardization**: Harmonizing datasets from diverse sources and acquisition protocols
- **Interpretability**: Making foundation models clinically interpretable and trustworthy
- **Efficiency**: Deploying large models in resource-constrained healthcare environments
- **Benchmarking**: Establishing comprehensive evaluation frameworks for clinical relevance
- **Security & Safety**: Protecting sensitive biosignal data from privacy breaches and ensuring model robustness against adversarial attacks in clinical settings

## 🤝 Contributing

<a href="https://github.com/guxiao0822/awesome-biosignal-foundation-model">
  <img src="https://contrib.rocks/image?repo=guxiao0822/awesome-biosignal-foundation-model" />
</a>

We welcome contributions! Please:
- Follow the format: `**[Venue Year]** Title [[paper]](link) [[code]](link)`
- Focus on foundation models for biosignals (not general ML papers)
- Ensure papers fit one of the three main directions
- Open an issue or submit a PR

**Citation**: If you find this repository useful, please cite our survey:
```bibtex
@article{gu2025bfm,
  title={Foundation Models for Biosignals: A Survey},
  author = {Gu, Xiao and Shu, Yuxuan and Han, Jinpei and Liu, Yuxuan and Liu, Zhangdaihong and Anibal, James and Sangha, Veer and Phillips, Edward and Segal, Bradley and Liu, Yuxuan and Yuan, Hang and Liu, Fenglin and Branson, Kim and Schwab, Patrick and Belgrave, Danielle and Clifton, Lei and Spathis, Dimitris and Lampos, Vasileios and Faisal, A. Aldo and Clifton, David A.}
  year={2025},
  publisher={TechRxiv}
}
