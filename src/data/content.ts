// Author metadata from the paper; resource URLs supplied by the authors.
export const authors = [
  { name: 'Hamidreza Eivazi', affiliation: '1', corresponding: true },
  { name: 'Eslam Sharaawy', affiliation: '2' },
  { name: 'Stefan Wittek', affiliation: '2' },
  { name: 'André Hebenbrock', affiliation: '3' },
  { name: 'Raphael Ginster', affiliation: '4' },
  { name: 'Steffen Blömeke', affiliation: '5' },
];

export const affiliations = [
  'Division Data-Driven Modeling of Mechanical Systems, Institute of Applied Mechanics, TU Braunschweig',
  'Institute for Software and Systems Engineering, Clausthal University of Technology',
  'Institute of Chemical and Electrochemical Process Engineering, Clausthal University of Technology',
  'Institute of Automotive Management and Industrial Production, TU Braunschweig',
  'Institute of Machine Tools and Production Technology, TU Braunschweig',
];

export const resources = {
  paper: 'https://arxiv.org/abs/2611.03150',
  code: 'https://github.com/HamidrezaEiv/FlowBatt',
  models: 'https://github.com/HamidrezaEiv/FlowBatt/tree/main/checkpoints',
};

export const citation = `@inproceedings{eivazi2026flowbatt,
  title     = {{FlowBatt}: Flow Matching for Probabilistic Battery Degradation Prediction},
  author    = {Eivazi, Hamidreza and Sharaawy, Eslam and Wittek, Stefan and Hebenbrock, André and Ginster, Raphael and Blömeke, Steffen},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  keywords  = {flow matching, battery degradation, state of health, remaining useful life, generative models},
  month     = dec,
  year      = {2026},
  url       = {https://arxiv.org/abs/2611.03150}
}`;
