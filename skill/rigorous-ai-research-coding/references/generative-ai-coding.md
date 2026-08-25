# Generative-AI Coding

## Instrument every model call

Record when permitted:

- provider, model identifier, version or access date;
- system and user prompts or prompt hashes;
- decoding parameters, seed support, tools, response format, and context construction;
- raw output or immutable output hash, latency, token usage, cost, retry count, and terminal error.

Treat closed-model behavior as time-dependent when exact versioning is unavailable. Never store credentials.

## Evaluation integrity

- Separate prompt development and evaluator development from protected evaluation.
- Preserve all tried prompts, exemplars, thresholds, retrieval settings, and checkpoints.
- Use repeated samples when decoding or service behavior is stochastic.
- Audit benchmark contamination, answer leakage, duplicated items, and template leakage.
- Distinguish task quality, safety, calibration, latency, cost, and robustness rather than collapsing them without justification.

## LLM judges

- Version the judge model, prompt, rubric, ordering, and parsing code.
- Randomize or counterbalance response order when position bias is possible.
- Calibrate against blinded human judgments on an appropriate sample.
- Report agreement and disagreement patterns; a judge score is a measurement, not ground truth.

## RAG and agents

- Version corpus, chunking, embeddings, index, retrieval settings, tools, and stopping rules.
- Evaluate retrieval and generation separately, then end-to-end.
- Prevent answer-bearing fields or future information from entering the retriever.
- Bound loops, tool calls, retries, time, and spending; log trajectories and terminal states.
- Classify failures by retrieval, reasoning, tool use, execution, grounding, and evaluation.

## Evidence basis

- Liang et al., *Holistic Evaluation of Language Models*, TMLR, 2023.
- Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*, NeurIPS Datasets and Benchmarks, 2023.
- Deng et al., *Reproducibility in Large Language Models*, 2023.
- Gebru et al., *Datasheets for Datasets*, Communications of the ACM, 2021.
- Mitchell et al., *Model Cards for Model Reporting*, FAT*, 2019.
