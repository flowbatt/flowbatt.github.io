// Current concise page copy, grounded in the accepted camera-ready paper.
// Source passages, abridgments, and retained full-text exports are documented
// in scripts/PAPER_CONTENT.md. The table and its complete notes are unchanged.

export const tldr = "We introduce FlowBatt, a use-inspired conditional generative framework that adapts flow matching to probabilistic battery degradation modeling.";

export const overview = "Accurate degradation prediction is challenging, as battery aging emerges from complex and heterogeneous interactions among cycling behavior, operating conditions, and cell chemistry. FlowBatt adapts flow matching to model full state of health (SOH) trajectories as probabilistic degradation processes conditioned on early-cycle capacity data. By generating multiple plausible trajectories, it provides empirical prediction intervals for battery degradation modeling. We evaluate FlowBatt on five public benchmark settings spanning diverse chemistries and aging conditions, comparing it with supervised and diffusion-based trajectory models under shared data splits. The framework brings together trajectory forecasting, uncertainty estimation, and degradation-curve synthesis in a single conditional generative model.";

export const methodology = "The capacity matrix is a cycle-by-voltage array of baseline-subtracted discharge-capacity curves. A CNN encodes this early-life input into a conditioning vector that is combined with a time embedding to modulate a compact diffusion transformer (DiT). Flow matching trains the network to predict a continuous-time vector field; integrating this field transports Gaussian noise into SOH trajectories.";

// Camera-ready CNN encoder description and appendix Grad-CAM analysis.
// These are scalar-RUL CNN diagnostics, motivating the FlowBatt encoder.
export const xaiDiscussion = "Grad-CAM analysis of CNNs trained for RUL prediction reveals initialization-sensitive behavior, including blank attribution maps for some test cells. We replace ReLU activations with LeakyReLU activations to obtain a more robust XAI-guided CNN encoder for FlowBatt.";

export const xaiCaption = "Capacity matrices and Grad-CAM maps for the 42 MATR-1 test batteries, reproduced from the paper in the same order across panels. Grad-CAM colors show relative attribution within each cell; their magnitudes are not directly comparable across cells or models.";

export const resultsIntro = "We compare full SOH trajectory predictions across five benchmark settings using shared data splits. RMSE is computed over the degradation curve up to the end-of-life (EOL) point, padding the remainder of the sequence with the final observed value. Results are reported as the mean RMSE across all test samples, in percentage units. Random forest (RF) [51], MLP [51], and BatLiNet [52] are adapted for trajectory-wise SOH prediction.";

export const resultsFindings = "FlowBatt achieves the lowest mean trajectory-wise SOH RMSE on all five datasets. DiffBatt improves upon the Transformer on all five datasets and achieves the second-best results across the benchmark, indicating that diffusion-based generative modeling already provides a strong improvement over purely supervised trajectory prediction.";

// Camera-ready Section 3.2 and Figure 4; condensed without changing the findings.
export const rulDiscussion = "RUL is computed from each predicted SOH trajectory as the cycle index at which it reaches the end-of-life threshold. FlowBatt remains highly competitive on this downstream task, despite being designed primarily for full trajectory modeling. It achieves the best result on HUST and ranks among the top three by RMSE across all five benchmark settings. The spread of RUL estimates from ten generated trajectories quantifies predictive variability; larger prediction errors generally tend to coincide with higher variability.";

export const rulCaption = "Predicted versus reference RUL for all test cells; the diagonal marks perfect agreement. Color shows the standard deviation across ten generated trajectories per cell, with a separate scale for each dataset. End-of-life thresholds are 80% SOH, except 90% for MIX-20.";

// Camera-ready conclusions: contribution, final benchmark result, empirical intervals,
// and synthesis finding; omit the synthesis sentence's numerical-gain clause.
export const closingConclusion = "FlowBatt learns full SOH trajectories conditioned on early-cycle capacity data, providing a trajectory-level representation of battery aging and a unified model for forecasting, uncertainty estimation, and synthesis. Across all five benchmark datasets, FlowBatt obtains the best trajectory-wise SOH prediction results. Since the model generates multiple plausible degradation trajectories for the same early-life input, it also provides empirical prediction intervals that capture predictive uncertainty. The synthesis experiments further show that FlowBatt-generated SOH trajectories can improve downstream RUL modeling.";

// Retained as paper provenance; omitted from the displayed page at the author's request.
export const closingLimitations = "Empirical prediction intervals show more pronounced undercoverage on MATR-2 and HUST. The model conditions only on capacity matrices from fixed 20- or 100-cycle windows, without direct temperature, current-profile, charging-protocol, environmental, or cooling inputs. The fixed benchmark splits do not establish generalization to unseen chemistries or cycling protocols. FlowBatt also does not explicitly enforce electrochemical, thermal, or conservation constraints.";

// Verbatim broader-impact sentences followed by the final camera-ready outlook sentence.
export const closingOutlook = "Our work on probabilistic battery degradation prediction has positive societal implications by supporting the transition to sustainable energy technologies. Accurate SOH forecasting and uncertainty quantification can optimize battery usage, extend lifespans, and improve the reliability of electric vehicles and stationary storage systems, thereby reducing electronic waste and resource consumption. Scaling this framework to broader battery datasets may also provide a path toward more general foundation models for battery health prediction.";

// Accepted camera-ready acknowledgments; rendered as small footer text after email.
export const acknowledgments = "This research was conducted within the Research Training Group CircularLIB, supported by the Ministry of Science and Culture of Lower Saxony with funds from the program zukunft.niedersachsen of the Volkswagen Foundation (MWK | ZN3678). This work was also supported by the Lower Saxony Digital Science Support Space (DS³) project as part of Hochschule.digital Niedersachsen, funded by zukunft.niedersachsen. We would like to thank the anonymous reviewers who contributed to the improvement of our manuscript with their valuable suggestions and comments.";

// Historical full-text exports retained for provenance, not current page copy.
// Revision markup resolves to the final branch: revdd -> second argument.
// screenshotTldr preserves the original wording restored in tldr; laySummary is historical.
// Numeric citations and cross-references retain camera-ready numbering.

export const screenshotTldr = "We introduce FlowBatt, a use-inspired conditional generative framework that adapts flow matching to probabilistic battery degradation modeling.";

export const laySummary = "Batteries power our phones and electric cars, but how long they will keep working well is difficult to predict. Waiting for batteries to wear out also makes testing slow and costly. We developed FlowBatt, a generative AI model that learns from battery tests. Using measurements from a battery's early use, it predicts how its ability to store energy may change as it ages. Rather than giving a single prediction or only estimating lifespan, it generates several possible aging paths to explore how the future might vary. Across five sets of publicly available battery data, FlowBatt predicted changes over time more accurately than the other methods we compared. This approach could help accelerate battery testing and support the design of longer-lasting, more sustainable energy systems.";

export const abstract = "Battery degradation remains a central challenge in the development and broad application of sustainable energy technologies. Accurate degradation prediction is challenging, as battery aging emerges from complex and heterogeneous interactions among cycling behavior, operating conditions, and cell chemistry. Existing machine-learning approaches typically focus on deterministic end-of-life predictions or modeling degradation curves within fixed chemistry settings, leaving probabilistic state of health (SOH) trajectory modeling across heterogeneous chemistries underexplored. We introduce FlowBatt, a use-inspired conditional generative framework that adapts flow matching with a diffusion transformer (DiT) backbone to battery degradation trajectory modeling. FlowBatt models full SOH trajectories as probabilistic degradation processes conditioned on early-cycle capacity data. To strengthen this conditioning pathway, we use explainable AI analysis to diagnose and improve the encoder that maps early-cycle capacity matrices into conditioning vectors. We evaluate FlowBatt on five public benchmark settings spanning diverse chemistries and aging conditions, comparing it with supervised and diffusion-based trajectory models as well as established baselines for remaining useful life (RUL) prediction under shared data splits. FlowBatt achieves the best trajectory-wise SOH prediction performance on all five datasets, with errors below 2.5%, and delivers competitive RUL prediction performance. By generating multiple plausible trajectories, FlowBatt provides empirical prediction intervals for battery degradation modeling. These results indicate that flow-matching-based trajectory modeling is a promising framework for probabilistic battery health prediction.";

export const sohResults = [
  "In practical applications, estimating a battery's SOH requires assessing the current discharge capacity under standardized conditions using reference performance tests and historical cycling data. However, the discrepancy between real-world battery usage and these standardized conditions poses significant challenges in obtaining precise ground-truth labels, which complicates accurate SOH prediction. Consequently, establishing robust and reproducible benchmark settings for SOH prediction remains an ongoing effort within the research community.",
  "In this work, we primarily evaluate SOH prediction in a trajectory-wise setting. In this setting, the models predict the full SOH trajectory, and the RMSE is computed over the degradation curve up to the EOL point, padding the remainder of the sequence with the final observed value. Results are then reported as the mean RMSE across all test samples. Since SOH is expressed as a percentage of the nominal capacity, the RMSE is also reported in percentage units. Further details on the experimental setup and error metrics are provided in appendix A.5.",
  "Most established RUL baselines predict a scalar and require adaptation to produce full SOH trajectories. We include MLP as a standard neural baseline and RF for its best reported RUL performance on BatteryML's largest dataset, MIX [51], together with BatLiNet [52], a state-of-the-art RUL predictor. These three baselines are adapted for trajectory-wise SOH prediction. For RUL, we retain the broader set of direct scalar predictors.",
  "The trajectory-wise SOH results are reported in table 1. This setting directly evaluates the models on their ability to forecast full degradation trajectories and is therefore the most representative evaluation for FlowBatt. The supervised Transformer baseline provides a useful point of comparison, achieving reasonable performance on some datasets such as MATR-1 (1.09±0.07) and MIX-20 (1.42±0.10), but showing noticeably higher errors on more challenging datasets such as HUST (3.18±0.16). DiffBatt improves upon the Transformer on all five datasets and achieves the second-best results across the benchmark, indicating that diffusion-based generative modeling already provides a strong improvement over purely supervised trajectory prediction.",
  "FlowBatt achieves the lowest mean trajectory-wise SOH RMSE on all five datasets. In particular, it reaches an RMSE of 0.87±0.02 on MATR-1, 1.77±0.04 on MATR-2, 2.10±0.12 on HUST, and 0.88±0.03 on the heterogeneous MIX-20 dataset. These results indicate that flow matching provides a reliable and scalable approach for SOH trajectory forecasting across diverse battery chemistries and operating conditions. FlowBatt also provides a unified generative framework for full-trajectory prediction, uncertainty quantification, and synthesis. Overall, the trajectory-wise results confirm that FlowBatt is particularly strong when the task requires modeling the temporal evolution of degradation rather than only isolated SOH targets."
] as const;

export const conclusions = [
  "Battery degradation remains a major challenge for reliable and sustainable energy-storage systems. In this work, we introduced FlowBatt, a use-inspired adaptation of flow matching with a diffusion transformer backbone for probabilistic battery degradation trajectory modeling. Rather than predicting only an endpoint such as RUL, FlowBatt learns full SOH trajectories conditioned on early-cycle capacity data, providing a trajectory-level representation of battery aging and a unified model for forecasting, uncertainty estimation, and synthesis. Across all five benchmark datasets, FlowBatt obtains the best trajectory-wise SOH prediction results. Since the model generates multiple plausible degradation trajectories for the same early-life input, it also provides empirical prediction intervals that capture predictive uncertainty. In the downstream RUL task, RUL values derived from FlowBatt trajectories remain competitive with specialized RUL baselines, including BatLiNet [52], and rank among the top methods across all evaluated datasets. The synthesis experiments further show that FlowBatt-generated SOH trajectories can improve downstream RUL modeling, reducing random-forest RMSE and MAPE on MATR-1 by approximately 26% and 19%, respectively.",
  "Limitations. Prediction remains challenging on MATR-2 and HUST, as reflected in higher RUL errors than on MATR-1 and more pronounced undercoverage of the empirical prediction intervals. The model conditions only on capacity matrices from fixed 20- or 100-cycle windows, without direct temperature, current-profile, charging-protocol, environmental, or cooling inputs. The fixed benchmark splits do not establish generalization to unseen chemistries or cycling protocols. FlowBatt also does not explicitly enforce electrochemical, thermal, or conservation constraints."
] as const;

export const outlook = [
  "Outlook. These results support flow matching as a promising framework for probabilistic battery degradation modeling. Future work should improve uncertainty calibration, especially under distribution shifts across chemistries and cycling protocols; incorporate additional operating and environmental variables; and connect generative trajectory models more closely with physics-based constraints and descriptions of battery aging. Generalization should be assessed by holding out entire chemistries or cycling protocols. Future work should include controlled evaluation of conditioning-history length and explore encoder architectures capable of processing variable-length cycle sequences. Scaling this framework to broader battery datasets may also provide a path toward more general foundation models for battery health prediction."
] as const;

// Current Table 1 data and complete caption/notes, unchanged by abridgment.
export const sohTable = {
  "columns": [
    "MATR-1",
    "MATR-2",
    "HUST",
    "MIX-20",
    "MIX-100"
  ],
  "rows": [
    {
      "method": "BatLiNet",
      "values": [
        "1.86 ± 0.06",
        "3.62 ± 0.24",
        "2.87 ± 0.23",
        "2.04 ± 0.06",
        "2.34 ± 0.22"
      ],
      "emphasis": "none"
    },
    {
      "method": "RF",
      "values": [
        "2.01 ± 0.04",
        "2.50 ± 0.01",
        "3.57 ± 0.03",
        "3.42 ± 0.02",
        "5.45 ± 0.04"
      ],
      "emphasis": "none"
    },
    {
      "method": "MLP",
      "values": [
        "1.97 ± 0.11",
        "3.06 ± 0.17",
        "4.11 ± 0.13",
        "2.23 ± 0.09",
        "3.13 ± 0.14"
      ],
      "emphasis": "none"
    },
    {
      "method": "Transformer (ours)",
      "values": [
        "1.09 ± 0.07",
        "2.25 ± 0.22",
        "3.18 ± 0.16",
        "1.42 ± 0.10",
        "1.76 ± 0.06"
      ],
      "emphasis": "none"
    },
    {
      "method": "DiffBatt (ours)",
      "values": [
        "0.92 ± 0.04",
        "1.85 ± 0.03",
        "2.44 ± 0.14",
        "1.15 ± 0.08",
        "1.71 ± 0.09"
      ],
      "emphasis": "second"
    },
    {
      "method": "FlowBatt (ours)",
      "values": [
        "0.87 ± 0.02",
        "1.77 ± 0.04",
        "2.10 ± 0.12",
        "0.88 ± 0.03",
        "1.41 ± 0.02"
      ],
      "emphasis": "best"
    }
  ],
  "caption": "Trajectory-wise SOH prediction results reported as mean RMSE (%) over the predicted degradation trajectories.",
  "notes": [
    "The ± values denote standard deviations of RMSE across ten generative draws from one trained checkpoint for FlowBatt and DiffBatt, and across ten training initializations for the other models.",
    "Best results are shown in bold and second-best results are underlined.",
    "This table evaluates full-trajectory SOH prediction.",
    "RMSE is computed over the predicted degradation trajectories up to EOL and therefore measures a different task from the cycle-wise SOH setting reported in appendix A.5.3."
  ]
} as const;

export const paperReferences = [
  {
    "number": 51,
    "key": "Zhang2023BatteryML:AnDegradation",
    "title": "BatteryML: An open-source platform for machine learning on battery degradation.",
    "href": "https://arxiv.org/abs/2310.14714"
  },
  {
    "number": 52,
    "key": "Zhang2025",
    "title": "Battery lifetime prediction across diverse ageing conditions with inter-cell deep learning.",
    "href": "https://doi.org/10.1038/s42256-024-00972-x"
  }
] as const;
