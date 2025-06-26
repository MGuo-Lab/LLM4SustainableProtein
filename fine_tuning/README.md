## Read Me - Fine Tuning Task - LLM4SustainableProtein

This folder of the LLM4SustainableProtein repository contains scripts for the fine-tuning task described in [our research on RAG-based multi-agent AI](https://doi.org/10.48550/arXiv.2506.20598), for aiding in sustainable protein production research.

The following scripts and data files are included:

| File Name                        | Description                                 |
|----------------------------------|---------------------------------------------|
| `README.md`                      | Project overview and documentation          |
| `pdf_text_extraction.py`         | Script to extract and refine text from a PDF file  |
| `example_paper_vaswani_2017.pdf` | Example open-access paper PDF file*         |
| `gpt_queries.py`                 | Script to query a GPT model with prompts, via OpenAI API |
| `gpt_fine_tuning.py`             | Script to fine-tune GPT model, via the OpenAI API      |
| `prompts_table.tsv`              | Tablular data of prompts for fine-tuning**  |
| `SBERT_cosine_similarity.py`     | Script for calculating text cosine similarity, using pre-trained transformers. |

*One example open-access paper has been provided, for the text extraction script to use - Vaswani et al. (2017).

**Due to potential legal constraints of the text content of scientific literature used in the study, all potentially sensitive content has been redacted from the `prompts_table.tsv` data file provided. Please see the supplementary materials of [Piercy et al. (2023)](https://doi.org/10.1039/D2GC03095K), if you wish to obtain the same literature for your own work.

Please cite [our original research](https://doi.org/10.48550/arXiv.2506.20598), if using any of these scripts.
