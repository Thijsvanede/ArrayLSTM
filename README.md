# ArrayLSTM
This code was implemented as part of the IEEE S&P [DeepCASE](https://vm-thijs.ewi.utwente.nl/static/homepage/papers/deepcase.pdf) [1] paper.
We provide a Pytorch implementation of [Recurrent Memory Array Structures](https://arxiv.org/abs/1607.03085) by Kamil M Rocki.
We ask people to [cite](#References) both works when using the software for academic research papers.

## Introduction
The following report introduces ideas augmenting standard Long Short Term Memory (LSTM) architecture with multiple memory cells per hidden unit in order to improve its generalization capabilities.
It considers both deterministic and stochastic variants of memory operation.
It is shown that the nondeterministic Array-LSTM approach improves state-of-the-art performance on character level text prediction achieving 1.402 BPC on enwik8 dataset.
Furthermore, this report estabilishes baseline neural-based results of 1.12 BPC and 1.19 BPC for enwik9 and enwik10 datasets respectively.

## Documentation
We provide an extensive documentation including installation instructions and reference at [arraylstm.readthedocs.io](https://arraylstm.readthedocs.io/en/latest)

## References
[1] `van Ede, T., Aghakhani, H., Spahn, N., Bortolameotti, R., Cova, M., Continella, A., van Steen, M., Peter, A., Kruegel, C. & Vigna, G. (2022, May). DeepCASE: Semi-Supervised Contextual Analysis of Security Events. In 2022 Proceedings of the IEEE Symposium on Security and Privacy (S&P). IEEE.`

[2] `Rocki, K.M. (2016). Recurrent memory array structures. In arXiv preprint arXiv:1607.03085.`


### Bibtex
```
@inproceedings{vanede2020deepcase,
  title={{DeepCASE: Semi-Supervised Contextual Analysis of Security Events}},
  author={van Ede, Thijs and Aghakhani, Hojjat and Spahn, Noah and Bortolameotti, Riccardo and Cova, Marco and Continella, Andrea and van Steen, Maarten and Peter, Andreas and Kruegel, Christopher and Vigna, Giovanni},
  booktitle={Proceedings of the IEEE Symposium on Security and Privacy (S&P)},
  year={2022},
  organization={IEEE}
}
```

```
@article{rocki2016recurrent,
  title={Recurrent memory array structures},
  author={Rocki, Kamil},
  journal={arXiv preprint arXiv:1607.03085},
  year={2016}
}

```
